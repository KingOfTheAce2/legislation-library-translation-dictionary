#!/usr/bin/env python3
"""
Import FR-FR dictionary into unified dictionary structure
"""

import json
from pathlib import Path

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filepath, data):
    """Save JSON file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def import_fr_dictionary():
    """Import FR-FR dictionary into unified structure"""
    print("=" * 70)
    print("IMPORTING FR-FR DICTIONARY")
    print("=" * 70)

    # Load FR-FR dictionary
    fr_dict_path = Path('import/FR-FR-dictionary.json')
    print(f"\n📂 Loading {fr_dict_path}...")
    fr_entries = load_json(fr_dict_path)
    print(f"  ✓ Loaded {len(fr_entries)} French terms")

    # Load existing unified dictionary
    unified_path = Path('unified-dictionary.json')
    print(f"\n📂 Loading {unified_path}...")
    unified_dict = load_json(unified_path)
    print(f"  ✓ Loaded {len(unified_dict)} existing terms")

    # Find the highest ID number
    max_id = 0
    for entry in unified_dict:
        id_num = int(entry['id'].split('_')[1])
        max_id = max(max_id, id_num)

    print(f"\n🔢 Starting from ID: term_{str(max_id + 1).zfill(5)}")

    # Create a lookup for existing terms
    existing_terms = {entry['term'].lower().strip(): entry for entry in unified_dict}

    # Process FR-FR entries
    added_count = 0
    updated_count = 0

    print("\n🔨 Processing French terms...")
    for fr_entry in fr_entries:
        source_term = fr_entry.get('source', '').strip()
        if not source_term:
            continue

        # Convert boolean fields
        sme_reviewed = fr_entry.get('sme-reviewed')
        if isinstance(sme_reviewed, str):
            sme_reviewed = sme_reviewed.upper() == 'TRUE'

        premium = fr_entry.get('premium')
        if isinstance(premium, str):
            premium = premium.upper() == 'TRUE'

        # Create translation object (FR-FR definition)
        translation = {
            'translation': source_term,  # Same as source for FR-FR
            'lang': 'fr-fr',
            'definition': fr_entry.get('lang-source-dict'),
            'source': fr_entry.get('author', 'Unknown'),
            'source-type': 'French Legal Dictionary',
            'license': fr_entry.get('license', 'Unknown'),
            'sme-reviewed': bool(sme_reviewed),
            'context': None
        }

        # Check if term already exists
        term_key = source_term.lower().strip()
        if term_key in existing_terms:
            # Add to existing term
            existing_terms[term_key]['translations'].append(translation)
            updated_count += 1
        else:
            # Create new term entry
            max_id += 1
            new_entry = {
                'id': f"term_{str(max_id).zfill(5)}",
                'term': source_term,
                'lang': fr_entry.get('lang-source', 'fr-fr'),
                'translations': [translation],
                'examples': [],
                'metadata': {}
            }
            unified_dict.append(new_entry)
            existing_terms[term_key] = new_entry
            added_count += 1

    print(f"  ✓ Added {added_count} new French terms")
    print(f"  ✓ Updated {updated_count} existing terms with French definitions")

    # Sort by term
    unified_dict.sort(key=lambda x: x['term'].lower())

    # Save updated unified dictionary
    print(f"\n💾 Saving updated dictionary to {unified_path}...")
    save_json(unified_path, unified_dict)

    # Calculate statistics
    total_terms = len(unified_dict)
    total_translations = sum(len(t['translations']) for t in unified_dict)
    fr_terms = sum(1 for t in unified_dict if t['lang'] == 'fr-fr')

    print(f"\n📊 Final Statistics:")
    print(f"  Total terms: {total_terms}")
    print(f"  Total translations: {total_translations}")
    print(f"  French terms: {fr_terms}")

    # Calculate file size
    file_size = unified_path.stat().st_size
    file_size_mb = file_size / (1024 * 1024)
    print(f"  File size: {file_size_mb:.2f} MB")

    print("\n✅ Import complete!")

    return unified_dict

if __name__ == '__main__':
    import_fr_dictionary()
