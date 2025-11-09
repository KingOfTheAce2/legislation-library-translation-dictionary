#!/usr/bin/env python3
"""
Parse Book 4 TMX file and convert to JSON format for legislation library
"""
import xml.etree.ElementTree as ET
import json
import sys

def parse_tmx(filename):
    """Parse TMX file and extract translation units"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        translations = []

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
                    'document': 'Wetboek van Burgerlijke Rechtsvordering - Book 4'
                })

        return translations
    except ET.ParseError as e:
        print(f"Error parsing TMX file: {e}", file=sys.stderr)
        return []

def main():
    input_file = 'book 4 (para level).tmx'
    output_file = '../legal-data/netherlands/legislation/civil-procedure/NL-EN-civil-procedure-book4.json'

    print(f"Parsing {input_file}...")
    translations = parse_tmx(input_file)

    print(f"Found {len(translations)} translation pairs")

    if translations:
        # Save to JSON
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(translations, f, ensure_ascii=False, indent=2)

        print(f"Saved to {output_file}")

        # Print first few examples
        print("\nFirst 5 translation pairs:")
        for i, t in enumerate(translations[:5], 1):
            print(f"\n{i}. NL: {t['source'][:80]}...")
            print(f"   EN: {t['target'][:80]}...")
    else:
        print("No translations found!")

if __name__ == '__main__':
    main()
