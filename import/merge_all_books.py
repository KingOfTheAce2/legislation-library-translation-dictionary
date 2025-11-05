#!/usr/bin/env python3
"""
Merge all books into a single combined JSON file for easier browsing
"""
import json

def main():
    # Load all books
    book1_file = '../i8n/NL-EN-civil-procedure-book1.json'
    book2_3_file = '../i8n/NL-EN-civil-procedure-book2-3.json'
    book4_file = '../i8n/NL-EN-civil-procedure-book4.json'

    all_translations = []

    # Load Book 1
    with open(book1_file, 'r', encoding='utf-8') as f:
        book1 = json.load(f)
        all_translations.extend(book1)
        print(f"Loaded {len(book1)} translations from Book 1")

    # Load Books 2-3
    with open(book2_3_file, 'r', encoding='utf-8') as f:
        book2_3 = json.load(f)
        all_translations.extend(book2_3)
        print(f"Loaded {len(book2_3)} translations from Books 2-3")

    # Load Book 4
    with open(book4_file, 'r', encoding='utf-8') as f:
        book4 = json.load(f)
        all_translations.extend(book4)
        print(f"Loaded {len(book4)} translations from Book 4")

    # Save combined file
    output_file = '../i8n/NL-EN-civil-procedure-all.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_translations, f, ensure_ascii=False, indent=2)

    print(f"\nTotal: {len(all_translations)} translation segments")
    print(f"Saved to {output_file}")

    # Print statistics
    print("\nBreakdown:")
    print(f"  Book 1:      {len(book1):,} segments")
    print(f"  Books 2-3:   {len(book2_3):,} segments")
    print(f"  Book 4:      {len(book4):,} segments")
    print(f"  Total:       {len(all_translations):,} segments")

if __name__ == '__main__':
    main()
