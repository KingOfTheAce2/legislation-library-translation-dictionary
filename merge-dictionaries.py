#!/usr/bin/env python3
"""
Merge all dictionary sources into unified structure
"""

import json
from collections import defaultdict
from typing import Dict, List, Any
import re

def normalize_term(term: str) -> str:
    """Normalize term for matching (lowercase, strip whitespace)"""
    return term.lower().strip()

def extract_terms_from_sentence(sentence: str) -> List[str]:
    """Extract potential legal terms from a sentence"""
    # Remove common words and extract multi-word legal terms
    # This is a simple heuristic - can be improved with NLP
    words = sentence.split()

    # Extract single words and 2-3 word phrases that might be terms
    terms = []

    # Single words (longer than 4 chars, likely legal terms)
    for word in words:
        cleaned = re.sub(r'[^\w\s]', '', word.lower())
        if len(cleaned) > 4:
            terms.append(cleaned)

    # 2-word phrases
    for i in range(len(words) - 1):
        phrase = f"{words[i]} {words[i+1]}"
        cleaned = re.sub(r'[^\w\s]', '', phrase.lower())
        if len(cleaned) > 8:
            terms.append(cleaned)

    # 3-word phrases
    for i in range(len(words) - 2):
        phrase = f"{words[i]} {words[i+1]} {words[i+2]}"
        cleaned = re.sub(r'[^\w\s]', '', phrase.lower())
        if len(cleaned) > 12:
            terms.append(cleaned)

    return list(set(terms))

def load_json(filename: str) -> List[Dict]:
    """Load JSON file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: {filename} not found, skipping...")
        return []

def create_translation(entry: Dict, source_type: str) -> Dict:
    """Create a translation object from source entry"""
    # Handle boolean conversion for sme-reviewed
    sme_reviewed = entry.get('sme-reviewed')
    if isinstance(sme_reviewed, str):
        sme_reviewed = sme_reviewed.lower() in ['yes', 'true', '1']
    elif sme_reviewed is None:
        sme_reviewed = False

    return {
        'translation': entry.get('target', ''),
        'lang': entry.get('lang-target', 'en-gb'),
        'definition': entry.get('lang-target-dict'),  # Will be None if not present
        'source': entry.get('author', 'Unknown'),
        'source-type': source_type,
        'license': entry.get('license', 'Unknown'),
        'sme-reviewed': bool(sme_reviewed),
        'context': None  # Can be added later
    }

def create_example(entry: Dict, example_id: str) -> Dict:
    """Create an example object from source entry"""
    # Handle boolean conversion
    sme_reviewed = entry.get('sme-reviewed')
    if isinstance(sme_reviewed, str):
        sme_reviewed = sme_reviewed.lower() in ['yes', 'true', '1']
    elif sme_reviewed is None:
        sme_reviewed = False

    premium = entry.get('premium', False)
    if isinstance(premium, str):
        premium = premium.lower() in ['yes', 'true', '1']

    return {
        'id': example_id,
        'nl': entry.get('source', ''),
        'en': entry.get('target', ''),
        'source': entry.get('author', 'Unknown'),
        'license': entry.get('license', 'Unknown'),
        'premium': bool(premium),
        'sme-reviewed': bool(sme_reviewed),
        'context': None
    }

def merge_dictionaries():
    """Main merge function"""
    print("🔄 Starting dictionary merge process...")

    # Load all source files
    print("\n📂 Loading source files...")
    glossary = load_json('Glossary-of-Dutch-Procedural-Terminology.json')
    print(f"  ✓ Loaded {len(glossary)} entries from Glossary-of-Dutch-Procedural-Terminology.json")

    dictionary = load_json('NL-EN-legal-dictionary.json')
    print(f"  ✓ Loaded {len(dictionary)} entries from NL-EN-legal-dictionary.json")

    legal_glossary = load_json('NL-EN-legal-glossary.json')
    print(f"  ✓ Loaded {len(legal_glossary)} entries from NL-EN-legal-glossary.json")

    examples_data = load_json('NL-EN-example-sentences.json')
    print(f"  ✓ Loaded {len(examples_data)} entries from NL-EN-example-sentences.json")

    # Dictionary to store merged data
    # Key: normalized term, Value: term data
    unified = {}
    term_to_id = {}
    id_counter = 1

    print("\n🔨 Merging translations...")

    # Process Civil Procedure Glossary
    print("  Processing Civil Procedure Glossary...")
    for entry in glossary:
        term = entry.get('source', '').strip()
        if not term:
            continue

        norm_term = normalize_term(term)

        if norm_term not in unified:
            term_id = f"term_{str(id_counter).zfill(5)}"
            term_to_id[norm_term] = term_id
            id_counter += 1

            unified[norm_term] = {
                'id': term_id,
                'term': term,  # Keep original case
                'lang': entry.get('lang-source', 'nl-nl'),
                'translations': [],
                'examples': [],
                'metadata': {}
            }

        translation = create_translation(entry, 'Civil Procedure Glossary')
        unified[norm_term]['translations'].append(translation)

    # Process Legal Dictionary (has definitions!)
    print("  Processing Legal Dictionary...")
    for entry in dictionary:
        term = entry.get('source', '').strip()
        if not term:
            continue

        norm_term = normalize_term(term)

        if norm_term not in unified:
            term_id = f"term_{str(id_counter).zfill(5)}"
            term_to_id[norm_term] = term_id
            id_counter += 1

            unified[norm_term] = {
                'id': term_id,
                'term': term,
                'lang': entry.get('lang-source', 'nl-nl'),
                'translations': [],
                'examples': [],
                'metadata': {}
            }

        translation = create_translation(entry, 'Legal Dictionary')
        unified[norm_term]['translations'].append(translation)

    # Process Legal Glossary
    print("  Processing Legal Glossary...")
    for entry in legal_glossary:
        term = entry.get('source', '').strip()
        if not term:
            continue

        norm_term = normalize_term(term)

        if norm_term not in unified:
            term_id = f"term_{str(id_counter).zfill(5)}"
            term_to_id[norm_term] = term_id
            id_counter += 1

            unified[norm_term] = {
                'id': term_id,
                'term': term,
                'lang': entry.get('lang-source', 'nl-nl'),
                'translations': [],
                'examples': [],
                'metadata': {}
            }

        translation = create_translation(entry, 'Legal Glossary')
        unified[norm_term]['translations'].append(translation)

    print(f"\n  ✓ Created {len(unified)} unique terms")

    # Process Examples
    print("\n📝 Processing example sentences...")
    example_counter = defaultdict(int)
    examples_matched = 0
    examples_unmatched = 0

    for example_entry in examples_data:
        nl_sentence = example_entry.get('source', '').strip()
        if not nl_sentence:
            continue

        # Extract potential terms from the sentence
        potential_terms = extract_terms_from_sentence(nl_sentence)

        # Try to match to existing terms
        matched = False
        for potential_term in potential_terms:
            norm_potential = normalize_term(potential_term)

            if norm_potential in unified:
                # Match found!
                term_id = unified[norm_potential]['id']
                example_counter[term_id] += 1
                example_id = f"ex_{term_id.split('_')[1]}_{str(example_counter[term_id]).zfill(3)}"

                example_obj = create_example(example_entry, example_id)
                unified[norm_potential]['examples'].append(example_obj)

                matched = True
                examples_matched += 1
                break  # Only match to first found term

        if not matched:
            examples_unmatched += 1

    print(f"  ✓ Matched {examples_matched} examples to terms")
    print(f"  ⚠ {examples_unmatched} examples could not be matched to terms")

    # Remove duplicates within translations (same translation from same source)
    print("\n🧹 Cleaning duplicates...")
    for term_data in unified.values():
        translations = term_data['translations']
        unique_translations = []
        seen = set()

        for trans in translations:
            # Create a key for deduplication
            key = (trans['translation'], trans['source'], trans['source-type'])
            if key not in seen:
                seen.add(key)
                unique_translations.append(trans)

        term_data['translations'] = unique_translations

    # Convert to list and sort by term
    unified_list = list(unified.values())
    unified_list.sort(key=lambda x: x['term'].lower())

    # Calculate statistics
    print("\n📊 Statistics:")
    total_translations = sum(len(t['translations']) for t in unified_list)
    total_examples = sum(len(t['examples']) for t in unified_list)
    terms_with_examples = sum(1 for t in unified_list if len(t['examples']) > 0)
    terms_with_definitions = sum(1 for t in unified_list
                                 if any(tr.get('definition') for tr in t['translations']))

    print(f"  Total unique terms: {len(unified_list)}")
    print(f"  Total translations: {total_translations}")
    print(f"  Avg translations per term: {total_translations / len(unified_list):.1f}")
    print(f"  Total examples: {total_examples}")
    print(f"  Terms with examples: {terms_with_examples}")
    print(f"  Terms with definitions: {terms_with_definitions}")

    # License breakdown
    licenses = defaultdict(int)
    for term_data in unified_list:
        for trans in term_data['translations']:
            licenses[trans['license']] += 1

    print(f"\n  License breakdown:")
    for license, count in sorted(licenses.items()):
        print(f"    {license}: {count}")

    # Premium vs Free examples
    premium_examples = sum(1 for t in unified_list for ex in t['examples'] if ex['premium'])
    free_examples = total_examples - premium_examples
    print(f"\n  Examples breakdown:")
    print(f"    Free: {free_examples}")
    print(f"    Premium: {premium_examples}")

    # Save to file
    output_file = 'unified-dictionary.json'
    print(f"\n💾 Saving to {output_file}...")

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(unified_list, f, ensure_ascii=False, indent=2)

    # Calculate file size
    import os
    file_size = os.path.getsize(output_file)
    file_size_mb = file_size / (1024 * 1024)

    print(f"  ✓ Saved {len(unified_list)} terms to {output_file}")
    print(f"  File size: {file_size_mb:.2f} MB")

    print("\n✅ Merge complete!")

    return unified_list

if __name__ == '__main__':
    merge_dictionaries()
