#!/usr/bin/env python3
"""
Apply manual translations from INCOMPLETE-TRANSLATIONS.json back to the main file.

This script:
1. Reads INCOMPLETE-TRANSLATIONS.json (with user's manual translations)
2. Updates NL-EN-civil-procedure-sentences-all.json
3. Marks completed translations as incomplete=false
4. Generates a report
"""

import json
from pathlib import Path


def apply_manual_translations():
    """Apply manual translations"""

    incomplete_file = Path('legal-data/netherlands/legislation/civil-procedure/INCOMPLETE-TRANSLATIONS.json')
    main_file = Path('legal-data/netherlands/legislation/civil-procedure/NL-EN-civil-procedure-sentences-all.json')
    backup_file = Path('legal-data/netherlands/legislation/civil-procedure/NL-EN-civil-procedure-sentences-all.BACKUP.json')

    print("=" * 70)
    print("APPLYING MANUAL TRANSLATIONS")
    print("=" * 70)

    # Load files
    print(f"\n📂 Loading {incomplete_file}...")
    with open(incomplete_file, 'r', encoding='utf-8') as f:
        incomplete_data = json.load(f)
    print(f"  ✓ Loaded {len(incomplete_data)} incomplete entries")

    print(f"\n📂 Loading {main_file}...")
    with open(main_file, 'r', encoding='utf-8') as f:
        main_data = json.load(f)
    print(f"  ✓ Loaded {len(main_data)} total sentences")

    # Create backup
    print(f"\n💾 Creating backup at {backup_file}...")
    with open(backup_file, 'w', encoding='utf-8') as f:
        json.dump(main_data, f, ensure_ascii=False, indent=2)
    print(f"  ✓ Backup created")

    # Create lookup for manual translations
    manual_translations = {}
    for entry in incomplete_data:
        if entry.get('en-translated', '').strip():
            manual_translations[entry['id']] = entry['en-translated'].strip()

    print(f"\n🔍 Found {len(manual_translations)} manual translations to apply")

    if len(manual_translations) == 0:
        print("\n⚠️  No manual translations found!")
        print("   Make sure you filled in 'en-translated' fields in INCOMPLETE-TRANSLATIONS.json")
        return

    # Apply translations
    updated_count = 0
    for sentence in main_data:
        if sentence['id'] in manual_translations:
            old_en = sentence['en']
            new_en = manual_translations[sentence['id']]

            sentence['en'] = new_en
            sentence['incomplete'] = False
            sentence['incomplete-reason'] = None

            updated_count += 1

            if updated_count <= 5:  # Show first 5 examples
                print(f"\n  Updated {sentence['id']}:")
                print(f"    OLD: {old_en[:80]}...")
                print(f"    NEW: {new_en[:80]}...")

    print(f"\n✅ Updated {updated_count} translations")

    # Save updated main file
    print(f"\n💾 Saving updated file to {main_file}...")
    with open(main_file, 'w', encoding='utf-8') as f:
        json.dump(main_data, f, ensure_ascii=False, indent=2)

    # Generate report
    total_sentences = len(main_data)
    still_incomplete = sum(1 for s in main_data if s.get('incomplete', False))
    completed = total_sentences - still_incomplete

    print("\n" + "=" * 70)
    print("UPDATE REPORT")
    print("=" * 70)
    print(f"\nTotal sentences: {total_sentences}")
    print(f"Completed: {completed} ({completed/total_sentences*100:.1f}%)")
    print(f"Still incomplete: {still_incomplete} ({still_incomplete/total_sentences*100:.1f}%)")
    print(f"Translations applied: {updated_count}")

    if still_incomplete > 0:
        print(f"\n⚠️  {still_incomplete} translations still need work")
        print("   Run create-incomplete-list.py again to generate updated list")
    else:
        print("\n🎉 All translations complete!")

    print("\n✅ Done!")


if __name__ == '__main__':
    apply_manual_translations()
