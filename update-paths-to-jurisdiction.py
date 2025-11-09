#!/usr/bin/env python3
"""
Update all Python scripts to use the new jurisdiction-based directory structure.

Changes:
  ../i8n/NL-*.json -> ../i8n/netherlands/NL-*.json
  i8n/NL-*.json -> i8n/netherlands/NL-*.json
"""

import re
from pathlib import Path

def update_file(filepath):
    """Update file paths in a Python file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Update all NL-* file references to netherlands/ subdirectory
    # Pattern 1: ../i8n/NL-*.json -> ../i8n/netherlands/NL-*.json
    content = re.sub(
        r"(['\"])(\.\./i8n/)(NL-[^'\"]*\.json)(['\"])",
        r"\1\2netherlands/\3\4",
        content
    )

    # Pattern 2: i8n/NL-*.json -> i8n/netherlands/NL-*.json
    content = re.sub(
        r"(['\"])(i8n/)(NL-[^'\"]*\.json)(['\"])",
        r"\1\2netherlands/\3\4",
        content
    )

    # Pattern 3: ../i8n/incomplete-translations-report.json
    content = re.sub(
        r"(['\"])(\.\./i8n/)(incomplete-translations-report\.json)(['\"])",
        r"\1\2netherlands/\3\4",
        content
    )

    # Pattern 4: i8n/incomplete-translations-report.json
    content = re.sub(
        r"(['\"])(i8n/)(incomplete-translations-report\.json)(['\"])",
        r"\1\2netherlands/\3\4",
        content
    )

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """Update all Python scripts"""
    print("=" * 70)
    print("UPDATING PYTHON SCRIPTS FOR JURISDICTION-BASED STRUCTURE")
    print("=" * 70)

    # Find all Python files
    python_files = []

    # Root directory Python files
    for py_file in Path('.').glob('*.py'):
        if py_file.name != 'update-paths-to-jurisdiction.py':  # Skip this script
            python_files.append(py_file)

    # Import directory Python files
    for py_file in Path('import').glob('*.py'):
        python_files.append(py_file)

    print(f"\n📂 Found {len(python_files)} Python files to update\n")

    updated_count = 0
    for py_file in sorted(python_files):
        if update_file(py_file):
            print(f"  ✓ Updated: {py_file}")
            updated_count += 1
        else:
            print(f"  - Skipped: {py_file} (no changes needed)")

    print(f"\n📊 Summary:")
    print(f"  Total files checked: {len(python_files)}")
    print(f"  Files updated: {updated_count}")
    print(f"  Files unchanged: {len(python_files) - updated_count}")

    print("\n✅ Update complete!")
    print("\nChanges made:")
    print("  '../i8n/NL-*.json' -> '../i8n/netherlands/NL-*.json'")
    print("  'i8n/NL-*.json' -> 'i8n/netherlands/NL-*.json'")
    print("  'incomplete-translations-report.json' -> 'netherlands/incomplete-translations-report.json'")

if __name__ == '__main__':
    main()
