#!/usr/bin/env python3
"""
Re-import all books from sentence-level TMX files to fix incomplete translations
"""
import xml.etree.ElementTree as ET
import json
import sys

def parse_tmx(filename, book_name):
    """Parse TMX file and extract translation units"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        translations = []
        incomplete_count = 0

        # Find all translation units
        for tu in root.findall('.//{*}tu'):
            tuid = tu.get('tuid', '')

            nl_text = None
            en_text = None

            # Find Dutch and English variants
            for tuv in tu.findall('{*}tuv'):
                lang = tuv.get('{http://www.w3.org/XML/1998/namespace}lang', '')
                seg = tuv.find('{*}seg')

                if seg is not None and seg.text:
                    if lang == 'nl':
                        nl_text = seg.text.strip()
                    elif lang == 'en-gb':
                        en_text = seg.text.strip()

            # Only add if we have both translations
            if nl_text and en_text:
                # Check for incomplete translations (known patterns)
                if (en_text.endswith(' apply') or
                    en_text.endswith(' applicable') or
                    len(en_text) < len(nl_text) * 0.3):  # English much shorter than Dutch
                    incomplete_count += 1
                    print(f"  Warning - possible incomplete translation (TUID {tuid}):")
                    print(f"    NL: {nl_text[:100]}...")
                    print(f"    EN: {en_text[:100]}...")

                translations.append({
                    'tuid': tuid,
                    'source': nl_text,
                    'target': en_text,
                    'lang-source': 'nl-nl',
                    'lang-target': 'en-gb',
                    'author': 'Burrough/Machon/Oranje/Frakes/Visser',
                    'license': 'CC BY 4.0',
                    'sme-reviewed': True,
                    'premium': False,
                    'type': 'legislation',
                    'document': f'Wetboek van Burgerlijke Rechtsvordering - {book_name}'
                })

        if incomplete_count > 0:
            print(f"  Found {incomplete_count} potentially incomplete translations")

        return translations
    except ET.ParseError as e:
        print(f"Error parsing TMX file: {e}", file=sys.stderr)
        return []

def main():
    print("=" * 70)
    print("RE-IMPORTING FROM SENTENCE-LEVEL TMX FILES")
    print("=" * 70)

    # Define files to import
    files = [
        {
            'file': 'Book 1 sentenced.tmx',
            'book': 'Book 1',
            'output': '../i8n/NL-EN-civil-procedure-book1.json'
        },
        {
            'file': 'book 2-3 (sentence).tmx',
            'book': 'Books 2-3',
            'output': '../i8n/NL-EN-civil-procedure-book2-3.json'
        },
        {
            'file': 'book 4 (sentence level).tmx',
            'book': 'Book 4',
            'output': '../i8n/NL-EN-civil-procedure-book4.json'
        }
    ]

    all_translations = []
    total_count = 0

    for file_info in files:
        print(f"\nProcessing {file_info['file']}...")
        translations = parse_tmx(file_info['file'], file_info['book'])

        if translations:
            # Save individual book file
            with open(file_info['output'], 'w', encoding='utf-8') as f:
                json.dump(translations, f, ensure_ascii=False, indent=2)

            print(f"  ✓ Saved {len(translations)} segments to {file_info['output']}")
            all_translations.extend(translations)
            total_count += len(translations)
        else:
            print(f"  ✗ No translations found in {file_info['file']}")

    # Create combined file
    if all_translations:
        combined_output = '../i8n/NL-EN-civil-procedure-all.json'
        with open(combined_output, 'w', encoding='utf-8') as f:
            json.dump(all_translations, f, ensure_ascii=False, indent=2)

        print(f"\n{'=' * 70}")
        print(f"✓ COMPLETE - Combined file created")
        print(f"  Total segments: {total_count}")
        print(f"  Output: {combined_output}")
        print(f"{'=' * 70}")

        # Show breakdown
        print("\nBreakdown by book:")
        for file_info in files:
            count = sum(1 for t in all_translations if t['document'].endswith(file_info['book']))
            print(f"  {file_info['book']:20s}: {count:5,} segments")

    else:
        print("\n✗ ERROR - No translations imported!")

if __name__ == '__main__':
    main()
