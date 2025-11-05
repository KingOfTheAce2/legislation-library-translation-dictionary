#!/usr/bin/env python3
"""
Extract text from DOCX files and fix incomplete translations
"""
import json
import zipfile
import xml.etree.ElementTree as ET
import re
from pathlib import Path

def extract_text_from_docx(docx_path):
    """Extract all text from a DOCX file"""
    paragraphs = []

    try:
        with zipfile.ZipFile(docx_path, 'r') as docx:
            # Read the main document XML
            xml_content = docx.read('word/document.xml')
            tree = ET.fromstring(xml_content)

            # Define namespace
            ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

            # Extract all paragraphs
            for para in tree.findall('.//w:p', ns):
                texts = []
                for text in para.findall('.//w:t', ns):
                    if text.text:
                        texts.append(text.text)

                if texts:
                    paragraph_text = ''.join(texts)
                    if paragraph_text.strip():
                        paragraphs.append(paragraph_text.strip())

    except Exception as e:
        print(f"Error extracting from {docx_path}: {e}")
        return []

    return paragraphs

def normalize_text(text):
    """Normalize text for comparison"""
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove special characters that might differ
    text = text.replace('\u00a0', ' ')  # Non-breaking space
    text = text.replace('\u2019', "'")  # Smart quote
    text = text.replace('\u201c', '"')
    text = text.replace('\u201d', '"')
    text = text.replace('\u2013', '-')  # En dash
    text = text.replace('\u2014', '-')  # Em dash
    return text.strip()

def find_best_match(incomplete_en, en_paragraphs, min_overlap=20):
    """Find best matching paragraph from DOCX"""
    incomplete_norm = normalize_text(incomplete_en)

    # If incomplete ends with ... or (, remove it
    search_text = incomplete_norm.rstrip('.(').rstrip('...')

    best_match = None
    best_score = 0

    for para in en_paragraphs:
        para_norm = normalize_text(para)

        # Check if incomplete text is a prefix of this paragraph
        if para_norm.startswith(search_text):
            score = len(search_text)
            if score > best_score and score >= min_overlap:
                best_score = score
                best_match = para

    return best_match

def fix_mutatis_mutandis(en_text):
    """Add 'mutatis mutandis' to apply clauses"""
    patterns = [
        (r'^(Articles? [\d\(\),\s]+(?:and|to|inclusive)+[\d\(\),\s]*)\s+apply\s*\.{0,3}$',
         r'\1 apply mutatis mutandis.'),
        (r'^(Article [\d\(\)]+)\s+applies\s*\.{0,3}$',
         r'\1 applies mutatis mutandis.'),
        (r'^(The .+?)\s+apply\s*\.{0,3}$',
         r'\1 apply mutatis mutandis.')
    ]

    for pattern, replacement in patterns:
        match = re.match(pattern, en_text.strip(), re.IGNORECASE)
        if match:
            return re.sub(pattern, replacement, en_text.strip(), flags=re.IGNORECASE)

    return en_text

def main():
    print("=" * 80)
    print("EXTRACTING DOCX AND FIXING INCOMPLETE TRANSLATIONS")
    print("=" * 80)

    # Load incomplete translations report
    report_file = '../i8n/incomplete-translations-report.json'
    print(f"\nLoading incomplete translations report...")

    with open(report_file, 'r', encoding='utf-8') as f:
        incomplete_items = json.load(f)

    print(f"Found {len(incomplete_items)} incomplete translations")

    # Extract DOCX files
    docx_files = {
        'Book 1': 'EN Book 1.docx',
        'Book 4': 'EN Book 4.docx'
    }

    docx_paragraphs = {}

    for book, filename in docx_files.items():
        print(f"\nExtracting {filename}...")
        paragraphs = extract_text_from_docx(filename)
        docx_paragraphs[book] = paragraphs
        print(f"  Extracted {len(paragraphs)} paragraphs")

    # Load all legislation files
    legislation_files = {
        'Book 1': '../i8n/NL-EN-civil-procedure-book1.json',
        'Books 2-3': '../i8n/NL-EN-civil-procedure-book2-3.json',
        'Book 4': '../i8n/NL-EN-civil-procedure-book4.json'
    }

    all_data = {}
    for book, filepath in legislation_files.items():
        with open(filepath, 'r', encoding='utf-8') as f:
            all_data[book] = json.load(f)

    # Fix incomplete translations
    print(f"\n{'=' * 80}")
    print("FIXING TRANSLATIONS")
    print(f"{'=' * 80}\n")

    fixed_count = 0
    mutatis_count = 0
    not_found_count = 0

    for item in incomplete_items:
        tuid = item['tuid']
        nl_text = item['nl']
        old_en = item['en']
        reason = item['reason']
        doc = item['document']

        # Determine which book
        book_key = None
        if 'Book 1' in doc:
            book_key = 'Book 1'
        elif 'Books 2-3' in doc:
            book_key = 'Books 2-3'
        elif 'Book 4' in doc:
            book_key = 'Book 4'

        if not book_key or book_key not in all_data:
            continue

        # Find the entry in the data
        data = all_data[book_key]
        entry_index = None

        for idx, entry in enumerate(data):
            if entry.get('tuid') == tuid:
                entry_index = idx
                break

        if entry_index is None:
            continue

        # Try to fix
        new_en = None
        fix_type = None

        # Strategy 1: For mutatis mutandis clauses, add the phrase
        if 'Mutatis mutandis' in reason or 'apply' in old_en.lower():
            new_en = fix_mutatis_mutandis(old_en)
            if new_en != old_en:
                fix_type = "Added 'mutatis mutandis'"
                mutatis_count += 1

        # Strategy 2: Try to find in DOCX (Book 1 and 4 only)
        if not new_en or new_en == old_en:
            if book_key in docx_paragraphs:
                matched = find_best_match(old_en, docx_paragraphs[book_key])
                if matched:
                    new_en = matched
                    fix_type = "Matched from DOCX"
                    fixed_count += 1

        # Apply fix if found
        if new_en and new_en != old_en:
            data[entry_index]['target'] = new_en
            print(f"[OK] Fixed TUID {tuid} ({fix_type})")
            print(f"  OLD: {old_en[:100]}...")
            print(f"  NEW: {new_en[:100]}...")
            print()
        else:
            not_found_count += 1

    # Save fixed files
    print(f"\n{'=' * 80}")
    print("SAVING FIXED FILES")
    print(f"{'=' * 80}\n")

    for book, filepath in legislation_files.items():
        if book in all_data:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(all_data[book], f, ensure_ascii=False, indent=2)
            print(f"[OK] Saved {filepath}")

    # Create combined file
    combined = []
    for book in ['Book 1', 'Books 2-3', 'Book 4']:
        if book in all_data:
            combined.extend(all_data[book])

    combined_file = '../i8n/NL-EN-civil-procedure-all.json'
    with open(combined_file, 'w', encoding='utf-8') as f:
        json.dump(combined, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved {combined_file}")

    # Summary
    print(f"\n{'=' * 80}")
    print("SUMMARY")
    print(f"{'=' * 80}")
    print(f"Total incomplete items:        {len(incomplete_items)}")
    print(f"Fixed with mutatis mutandis:   {mutatis_count}")
    print(f"Fixed from DOCX:               {fixed_count}")
    print(f"Still incomplete:              {not_found_count}")
    print(f"Total fixed:                   {mutatis_count + fixed_count}")
    print(f"{'=' * 80}\n")

if __name__ == '__main__':
    main()
