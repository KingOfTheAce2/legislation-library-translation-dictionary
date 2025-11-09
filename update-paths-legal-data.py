#!/usr/bin/env python3
"""
Update all file paths from i8n/ structure to legal-data/ structure with subfolders.

Changes:
  i8n/netherlands/NL-*.json -> legal-data/netherlands/dictionaries/NL-*.json (dictionaries)
  i8n/netherlands/NL-EN-civil-procedure-*.json -> legal-data/netherlands/legislation/civil-procedure/NL-EN-civil-procedure-*.json
  i8n/netherlands/NL-EN-example-sentences.json -> legal-data/netherlands/legislation/civil-procedure/NL-EN-example-sentences.json
  i8n/netherlands/incomplete-translations-report.json -> legal-data/netherlands/reports/incomplete-translations-report.json
"""

import re
from pathlib import Path

# Mapping of old paths to new paths
PATH_MAPPINGS = [
    # Dictionaries
    (r'i8n/netherlands/NL-legal-dictionary\.json', 'legal-data/netherlands/dictionaries/NL-legal-dictionary.json'),
    (r'i8n/netherlands/NL-EN-legal-dictionary\.json', 'legal-data/netherlands/dictionaries/NL-EN-legal-dictionary.json'),
    (r'i8n/netherlands/NL-EN-legal-glossary\.json', 'legal-data/netherlands/dictionaries/NL-EN-legal-glossary.json'),
    (r'i8n/netherlands/NL-FR-legal-glossary\.json', 'legal-data/netherlands/dictionaries/NL-FR-legal-glossary.json'),
    (r'i8n/netherlands/NL-DE-legal-glossary\.json', 'legal-data/netherlands/dictionaries/NL-DE-legal-glossary.json'),
    (r'i8n/netherlands/NL-ES-legal-glossary\.json', 'legal-data/netherlands/dictionaries/NL-ES-legal-glossary.json'),
    (r'i8n/netherlands/NL-EN-legislation-extracted-terms\.json', 'legal-data/netherlands/dictionaries/NL-EN-legislation-extracted-terms.json'),
    (r'i8n/netherlands/NL-EN-legislation-glossary-additions\.json', 'legal-data/netherlands/dictionaries/NL-EN-legislation-glossary-additions.json'),

    # Civil Procedure
    (r'i8n/netherlands/NL-EN-civil-procedure-all\.json', 'legal-data/netherlands/legislation/civil-procedure/NL-EN-civil-procedure-all.json'),
    (r'i8n/netherlands/NL-EN-civil-procedure-all-BACKUP\.json', 'legal-data/netherlands/legislation/civil-procedure/NL-EN-civil-procedure-all-BACKUP.json'),
    (r'i8n/netherlands/NL-EN-civil-procedure-book1\.json', 'legal-data/netherlands/legislation/civil-procedure/NL-EN-civil-procedure-book1.json'),
    (r'i8n/netherlands/NL-EN-civil-procedure-book2-3\.json', 'legal-data/netherlands/legislation/civil-procedure/NL-EN-civil-procedure-book2-3.json'),
    (r'i8n/netherlands/NL-EN-civil-procedure-book4\.json', 'legal-data/netherlands/legislation/civil-procedure/NL-EN-civil-procedure-book4.json'),
    (r'i8n/netherlands/NL-EN-example-sentences\.json', 'legal-data/netherlands/legislation/civil-procedure/NL-EN-example-sentences.json'),

    # Reports
    (r'i8n/netherlands/incomplete-translations-report\.json', 'legal-data/netherlands/reports/incomplete-translations-report.json'),
]

def update_file(filepath):
    """Update file paths in a file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Apply all path mappings
    for old_pattern, new_path in PATH_MAPPINGS:
        # Handle both relative paths (../) and absolute paths
        content = re.sub(
            rf"(\.\./)?{old_pattern}",
            lambda m: f"{m.group(1) or ''}{new_path}",
            content
        )

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """Update all files"""
    print("=" * 70)
    print("UPDATING PATHS: i8n/ → legal-data/ WITH SUBFOLDERS")
    print("=" * 70)

    # Find all Python files
    python_files = []

    # Root directory Python files
    for py_file in Path('.').glob('*.py'):
        if py_file.name not in ['update-paths-to-jurisdiction.py', 'update-paths-legal-data.py']:
            python_files.append(py_file)

    # Import directory Python files
    for py_file in Path('import').glob('*.py'):
        python_files.append(py_file)

    # HTML files
    html_files = list(Path('.').glob('*.html'))

    all_files = python_files + html_files

    print(f"\n📂 Found {len(all_files)} files to update")
    print(f"   - {len(python_files)} Python files")
    print(f"   - {len(html_files)} HTML files")
    print()

    updated_count = 0
    for file_path in sorted(all_files):
        if update_file(file_path):
            print(f"  ✓ Updated: {file_path}")
            updated_count += 1
        else:
            print(f"  - Skipped: {file_path} (no changes needed)")

    print(f"\n📊 Summary:")
    print(f"  Total files checked: {len(all_files)}")
    print(f"  Files updated: {updated_count}")
    print(f"  Files unchanged: {len(all_files) - updated_count}")

    print("\n✅ Update complete!")
    print("\nChanges made:")
    print("  i8n/netherlands/[dictionaries] → legal-data/netherlands/dictionaries/")
    print("  i8n/netherlands/[civil-procedure] → legal-data/netherlands/legislation/civil-procedure/")
    print("  i8n/netherlands/[reports] → legal-data/netherlands/reports/")

if __name__ == '__main__':
    main()
