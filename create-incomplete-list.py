#!/usr/bin/env python3
"""
Create a separate file with ONLY incomplete translations for manual completion.

This extracts all sentences marked as incomplete and creates a simple format
for easy manual translation.
"""

import json
from pathlib import Path


def create_incomplete_list():
    """Create list of incomplete translations"""

    input_file = Path('legal-data/netherlands/legislation/civil-procedure/NL-EN-civil-procedure-sentences-all.json')
    output_file = Path('legal-data/netherlands/legislation/civil-procedure/INCOMPLETE-TRANSLATIONS.json')

    print("=" * 70)
    print("CREATING INCOMPLETE TRANSLATIONS LIST")
    print("=" * 70)

    # Load all sentences
    print(f"\n📂 Loading {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        all_sentences = json.load(f)

    print(f"  ✓ Loaded {len(all_sentences)} sentences")

    # Filter incomplete
    incomplete = [s for s in all_sentences if s.get('incomplete', False)]
    print(f"  ✓ Found {len(incomplete)} incomplete translations")

    # Create simplified format for manual work
    simplified = []
    for sent in incomplete:
        simplified.append({
            'id': sent['id'],
            'nl': sent['nl'],
            'en': sent['en'],  # Current (often copy of Dutch)
            'en-translated': '',  # USER FILLS THIS IN
            'reason': sent.get('incomplete-reason', ''),
            'document': sent.get('document', ''),
            'notes': ''  # USER CAN ADD NOTES
        })

    # Save simplified version
    print(f"\n💾 Saving to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(simplified, f, ensure_ascii=False, indent=2)

    file_size = output_file.stat().st_size / 1024
    print(f"  ✓ Saved {len(simplified)} incomplete entries")
    print(f"  ✓ File size: {file_size:.1f} KB")

    # Breakdown by reason
    print("\n📊 Breakdown by Reason:")
    reasons = {}
    for s in incomplete:
        reason = s.get('incomplete-reason', 'Unknown')
        reasons[reason] = reasons.get(reason, 0) + 1

    for reason, count in sorted(reasons.items(), key=lambda x: x[1], reverse=True):
        print(f"  • {reason}: {count}")

    # Breakdown by document
    print("\n📚 By Document:")
    docs = {}
    for s in incomplete:
        doc = s.get('document', 'Unknown')
        docs[doc] = docs.get(doc, 0) + 1

    for doc, count in sorted(docs.items()):
        print(f"  • {doc}: {count}")

    print("\n" + "=" * 70)
    print("USAGE INSTRUCTIONS")
    print("=" * 70)
    print("\n1. Open INCOMPLETE-TRANSLATIONS.json")
    print("2. For each entry:")
    print("   - Read the 'nl' (Dutch) text")
    print("   - Add English translation in 'en-translated' field")
    print("   - Optionally add notes")
    print("3. Save the file")
    print("4. Run: python apply-manual-translations.py")
    print("   (This will merge your translations back into the main file)")
    print("\n✅ List created!")


if __name__ == '__main__':
    create_incomplete_list()
