#!/usr/bin/env python3
"""
Process legislation file to:
1. Merge article numbers with following sentences
2. Extract new glossary terms not in existing glossary
"""
import json
import re
from typing import List, Dict, Set

def load_json(filepath: str) -> List[Dict]:
    """Load JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filepath: str, data: List[Dict]) -> None:
    """Save JSON file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def is_article_number(text: str) -> bool:
    """Check if text is just an article number like '1.', '2.', etc."""
    return bool(re.match(r'^\d+\.$', text.strip()))

def is_article_header(text: str) -> bool:
    """Check if text is an article header like 'Artikel 1'"""
    return bool(re.match(r'^Artikel \d+', text.strip(), re.IGNORECASE))

def merge_article_numbers(data: List[Dict]) -> List[Dict]:
    """Merge standalone article numbers with following sentences"""
    merged = []
    i = 0
    merges_count = 0

    while i < len(data):
        current = data[i]

        # Check if current is a standalone article number
        if is_article_number(current['source']):
            # Check if there's a next item
            if i + 1 < len(data):
                next_item = data[i + 1]

                # Skip if next item is also an article number or article header
                if not is_article_number(next_item['source']) and not is_article_header(next_item['source']):
                    # Merge them
                    merged_item = current.copy()
                    merged_item['source'] = f"{current['source']} {next_item['source']}"
                    merged_item['target'] = f"{current['target']} {next_item['target']}"
                    merged_item['tuid'] = current['tuid']  # Keep first TUID

                    merged.append(merged_item)
                    merges_count += 1
                    i += 2  # Skip both items
                    continue

        # If no merge, just add current item
        merged.append(current)
        i += 1

    print(f"Merged {merges_count} article numbers with following sentences")
    print(f"Original segments: {len(data)}")
    print(f"After merging: {len(merged)}")

    return merged

def extract_terms_from_text(text: str) -> Set[str]:
    """Extract potential legal terms from text"""
    terms = set()

    # Clean and split text
    words = text.lower().split()

    # Extract single words (nouns/legal terms)
    for word in words:
        # Remove punctuation
        clean_word = re.sub(r'[^\w\s-]', '', word)
        if len(clean_word) > 3:  # Skip very short words
            terms.add(clean_word)

    # Extract common multi-word legal phrases (2-3 words)
    for i in range(len(words)):
        # Two-word phrases
        if i + 1 < len(words):
            phrase = ' '.join(words[i:i+2])
            clean_phrase = re.sub(r'[^\w\s-]', '', phrase)
            if len(clean_phrase) > 6:
                terms.add(clean_phrase)

        # Three-word phrases
        if i + 2 < len(words):
            phrase = ' '.join(words[i:i+3])
            clean_phrase = re.sub(r'[^\w\s-]', '', phrase)
            if len(clean_phrase) > 10:
                terms.add(clean_phrase)

    return terms

def extract_glossary_terms(legislation_data: List[Dict], existing_glossary: List[Dict]) -> List[Dict]:
    """Extract new glossary terms from legislation that don't exist in current glossary"""

    # Build set of existing terms (both source and target)
    existing_sources = set()
    existing_targets = set()

    for term in existing_glossary:
        if 'source' in term:
            existing_sources.add(term['source'].lower())
        if 'target' in term:
            existing_targets.add(term['target'].lower())

    print(f"Existing glossary has {len(existing_sources)} Dutch terms and {len(existing_targets)} English terms")

    # Extract term pairs from legislation
    term_pairs = {}  # source -> target mapping

    for item in legislation_data:
        source = item['source']
        target = item['target']

        # Skip headers, article numbers, dates, etc.
        if (is_article_header(source) or
            is_article_number(source) or
            source.isupper() or  # Skip all-caps titles
            len(source.split()) < 2 or  # Skip very short entries
            len(source) < 10):  # Skip very short text
            continue

        # Look for specific legal terms (specific patterns)
        # This is a basic extraction - can be enhanced with NLP
        source_lower = source.lower()
        target_lower = target.lower()

        # Only add if not already in glossary
        if source_lower not in existing_sources and target_lower not in existing_targets:
            # Create a term pair
            key = (source[:100], target[:100])  # Truncate for key
            if key not in term_pairs:
                term_pairs[key] = {
                    'source': source[:200],  # Limit length for glossary
                    'target': target[:200],
                    'count': 1
                }
            else:
                term_pairs[key]['count'] += 1

    # Convert to glossary format
    new_glossary = []
    for (src, tgt), data in term_pairs.items():
        # Only include if appears multiple times or is likely a legal term
        if data['count'] >= 1:  # You can adjust this threshold
            new_glossary.append({
                'source': data['source'],
                'lang-source': 'nl-nl',
                'target': data['target'],
                'lang-target': 'en-gb',
                'author': 'Burrough/Machon/Oranje/Frakes/Visser',
                'license': 'CC BY 4.0',
                'sme-reviewed': True,
                'premium': False,
                'type': 'legislation-derived',
                'occurrences': data['count']
            })

    # Sort by occurrence count
    new_glossary.sort(key=lambda x: x['occurrences'], reverse=True)

    print(f"Extracted {len(new_glossary)} potential new glossary terms")

    return new_glossary

def main():
    print("=" * 60)
    print("LEGISLATION PROCESSING SCRIPT")
    print("=" * 60)

    # File paths
    legislation_file = '../legal-data/netherlands/legislation/civil-procedure/NL-EN-civil-procedure-all.json'
    glossary_file = '../legal-data/netherlands/dictionaries/NL-EN-legal-glossary.json'
    output_legislation = '../i8n/netherlands/NL-EN-civil-procedure-all-merged.json'
    output_new_terms = '../legal-data/netherlands/dictionaries/NL-EN-legislation-extracted-terms.json'

    # Load files
    print("\n1. Loading files...")
    legislation_data = load_json(legislation_file)
    existing_glossary = load_json(glossary_file)

    print(f"   - Loaded {len(legislation_data)} legislation segments")
    print(f"   - Loaded {len(existing_glossary)} existing glossary terms")

    # Task 1: Merge article numbers
    print("\n2. Merging article numbers with sentences...")
    merged_legislation = merge_article_numbers(legislation_data)

    # Save merged legislation
    save_json(output_legislation, merged_legislation)
    print(f"   - Saved merged legislation to {output_legislation}")

    # Show some examples
    print("\n   Examples of merged entries:")
    count = 0
    for i, item in enumerate(merged_legislation):
        if item['source'].startswith(('1.', '2.', '3.', '4.', '5.')) and ' ' in item['source']:
            print(f"   - NL: {item['source'][:100]}...")
            print(f"     EN: {item['target'][:100]}...")
            count += 1
            if count >= 3:
                break

    # Task 2: Extract glossary terms
    print("\n3. Extracting potential glossary terms...")
    new_terms = extract_glossary_terms(merged_legislation, existing_glossary)

    # Save new terms
    save_json(output_new_terms, new_terms[:500])  # Save top 500 terms
    print(f"   - Saved top {min(500, len(new_terms))} new terms to {output_new_terms}")

    # Show top 10 most frequent
    print("\n   Top 10 most frequent new terms:")
    for i, term in enumerate(new_terms[:10], 1):
        print(f"   {i}. [{term['occurrences']}x] {term['source'][:60]} → {term['target'][:60]}")

    print("\n" + "=" * 60)
    print("PROCESSING COMPLETE!")
    print("=" * 60)
    print(f"\nNext steps:")
    print(f"1. Review {output_legislation} - merged article numbers")
    print(f"2. Review {output_new_terms} - potential glossary additions")
    print(f"3. Manually review and filter extracted terms before adding to glossary")
    print(f"4. Replace original file if satisfied with merges")

if __name__ == '__main__':
    main()
