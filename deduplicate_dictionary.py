#!/usr/bin/env python3
"""
Deduplication script for unified-dictionary.json
Merges duplicate translations from "Civil Procedure Glossary" and "Legal Glossary"
into a single unified "Legal Glossary" entry.
"""

import json
import sys
from typing import List, Dict, Any

def deduplicate_translations(translations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Deduplicate translations by merging entries with same translation text
    but different source-type labels (Civil Procedure Glossary vs Legal Glossary)
    """
    # Group translations by (translation, lang, source, license, sme-reviewed, context, definition)
    translation_groups = {}

    for trans in translations:
        # Create a key based on the actual translation content
        key = (
            trans['translation'],
            trans['lang'],
            trans.get('definition'),
            trans.get('source', ''),
            trans.get('license', ''),
            trans.get('sme-reviewed', False),
            trans.get('context')
        )

        if key not in translation_groups:
            translation_groups[key] = []
        translation_groups[key].append(trans)

    # Merge duplicates
    deduplicated = []
    for key, group in translation_groups.items():
        if len(group) == 1:
            # No duplicates
            deduplicated.append(group[0])
        else:
            # Found duplicates - check if they're from Civil Procedure Glossary and Legal Glossary
            source_types = [t.get('source-type', '') for t in group]

            # If duplicates are from different glossary types, merge them
            if any('Glossary' in st for st in source_types):
                # Create merged entry with unified "Legal Glossary" label
                merged = group[0].copy()
                merged['source-type'] = 'Legal Glossary'
                deduplicated.append(merged)
                print(f"  Merged duplicate: {merged['translation']} ({merged['lang']}) - {len(group)} sources")
            else:
                # Keep all if they're legitimately different translations
                deduplicated.extend(group)

    return deduplicated

def main():
    print("🔧 Deduplicating unified-dictionary.json...")
    print()

    # Load unified dictionary
    try:
        with open('unified-dictionary.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("❌ Error: unified-dictionary.json not found")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing JSON: {e}")
        sys.exit(1)

    print(f"📚 Loaded {len(data)} terms")
    print()

    # Track statistics
    total_translations_before = sum(len(term['translations']) for term in data)
    terms_with_duplicates = 0

    # Process each term
    for term in data:
        original_count = len(term['translations'])
        term['translations'] = deduplicate_translations(term['translations'])
        new_count = len(term['translations'])

        if new_count < original_count:
            terms_with_duplicates += 1
            print(f"📝 {term['term']}: {original_count} → {new_count} translations")

    total_translations_after = sum(len(term['translations']) for term in data)

    print()
    print("📊 Deduplication Statistics:")
    print(f"  Terms with duplicates: {terms_with_duplicates}")
    print(f"  Total translations before: {total_translations_before}")
    print(f"  Total translations after: {total_translations_after}")
    print(f"  Removed duplicates: {total_translations_before - total_translations_after}")
    print()

    # Write deduplicated data
    output_file = 'unified-dictionary.json'
    print(f"💾 Writing deduplicated data to {output_file}...")

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("✅ Deduplication complete!")

if __name__ == '__main__':
    main()
