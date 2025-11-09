#!/usr/bin/env python3
"""
Extract refined glossary terms from legislation
Focus on legal terminology, not full sentences
"""
import json
import re
from typing import List, Dict, Set
from collections import defaultdict

def load_json(filepath: str) -> List[Dict]:
    """Load JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filepath: str, data: List[Dict]) -> None:
    """Save JSON file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def is_likely_legal_term(nl_text: str, en_text: str) -> bool:
    """Check if a text pair is likely a legal term (not a full sentence)"""
    # Skip if too long (likely sentences, not terms)
    if len(nl_text.split()) > 8 or len(en_text.split()) > 8:
        return False

    # Skip if too short
    if len(nl_text) < 5 or len(en_text) < 5:
        return False

    # Skip if contains certain sentence indicators
    sentence_indicators = [
        'indien', 'wanneer', 'zodra', 'moet', 'kan', 'wordt', 'zijn', 'heeft',
        'if', 'when', 'must', 'may', 'shall', 'is', 'are', 'has', 'have'
    ]

    nl_words = nl_text.lower().split()
    en_words = en_text.lower().split()

    # If starts with these words, likely a sentence not a term
    for word in sentence_indicators:
        if nl_words[0] == word or (en_words and en_words[0] == word):
            return False

    # Skip if contains numbers (except for legal references)
    if re.search(r'\d{2,}', nl_text) or re.search(r'\d{2,}', en_text):
        return False

    # Skip metadata/administrative text
    skip_patterns = [
        r'\[vervallen',
        r'\[lapsed',
        r'artikel \d+',
        r'article \d+',
        r'geldig',
        r'effective',
        r'^\d+\.',
        r'sub [a-z]'
    ]

    for pattern in skip_patterns:
        if re.search(pattern, nl_text.lower()) or re.search(pattern, en_text.lower()):
            return False

    return True

def extract_noun_phrases(text: str, lang: str) -> List[str]:
    """Extract potential legal noun phrases"""
    phrases = []

    # Common legal term patterns
    if lang == 'nl':
        # Dutch patterns: adjective + noun, compound nouns
        patterns = [
            r'\b[a-z]+-?\b[a-z]+(?:recht|wet|vordering|procedure|vonnis|beslissing|artikel|titel|afdeling)\b',
            r'\b(?:de|het|een)\s+[a-z]+(?:recht|wet|vordering|procedure|vonnis|beslissing)\b',
        ]
    else:  # English
        patterns = [
            r'\b[a-z]+\s+(?:court|law|procedure|judgment|decision|article|title|section)\b',
            r'\b(?:the|a|an)\s+[a-z]+\s+(?:court|law|procedure)\b',
        ]

    for pattern in patterns:
        matches = re.findall(pattern, text.lower())
        phrases.extend(matches)

    return phrases

def extract_legal_glossary(legislation_data: List[Dict], existing_glossary: List[Dict]) -> List[Dict]:
    """Extract legal terms suitable for glossary"""

    # Build existing terms set
    existing = set()
    for term in existing_glossary:
        if 'source' in term and 'target' in term:
            existing.add((term['source'].lower(), term['target'].lower()))

    print(f"Existing glossary: {len(existing)} term pairs")

    # Collect potential terms
    term_candidates = defaultdict(lambda: {'nl': '', 'en': '', 'count': 0, 'contexts': []})

    for item in legislation_data:
        source = item['source'].strip()
        target = item['target'].strip()

        # Skip headers and structural elements
        if source.isupper() or source.startswith('Artikel ') or source.startswith('Article '):
            continue

        # Only consider potential legal terms
        if is_likely_legal_term(source, target):
            key = (source.lower(), target.lower())

            if key not in existing:
                term_candidates[key]['nl'] = source
                term_candidates[key]['en'] = target
                term_candidates[key]['count'] += 1
                if len(term_candidates[key]['contexts']) < 3:
                    term_candidates[key]['contexts'].append({
                        'nl': source[:100],
                        'en': target[:100]
                    })

    print(f"Found {len(term_candidates)} potential new terms")

    # Convert to glossary format
    new_terms = []
    for (nl_lower, en_lower), data in term_candidates.items():
        # Only include terms that appear at least once and look like legal terminology
        if data['count'] >= 1:
            new_terms.append({
                'source': data['nl'],
                'lang-source': 'nl-nl',
                'target': data['en'],
                'lang-target': 'en-gb',
                'author': 'Burrough/Machon/Oranje/Frakes/Visser',
                'license': 'CC BY 4.0',
                'sme-reviewed': True,
                'premium': False,
                'type': 'legislation-derived',
                'occurrences': data['count']
            })

    # Sort by occurrence
    new_terms.sort(key=lambda x: x['occurrences'], reverse=True)

    return new_terms

def main():
    print("=" * 70)
    print("REFINED GLOSSARY EXTRACTION")
    print("=" * 70)

    # Load files
    legislation_file = '../legal-data/netherlands/legislation/civil-procedure/NL-EN-civil-procedure-all.json'
    glossary_file = '../legal-data/netherlands/dictionaries/NL-EN-legal-glossary.json'
    output_file = '../legal-data/netherlands/dictionaries/NL-EN-legislation-glossary-additions.json'

    print("\nLoading files...")
    legislation = load_json(legislation_file)
    glossary = load_json(glossary_file)

    print(f"  - {len(legislation)} legislation segments")
    print(f"  - {len(glossary)} existing glossary terms")

    # Extract terms
    print("\nExtracting legal terms...")
    new_terms = extract_legal_glossary(legislation, glossary)

    # Save top terms
    save_json(output_file, new_terms[:200])

    print(f"\nSaved {min(200, len(new_terms))} new terms to:")
    print(f"  {output_file}")

    # Show examples
    print("\nTop 20 extracted terms:")
    print("-" * 70)
    for i, term in enumerate(new_terms[:20], 1):
        print(f"{i:2d}. [{term['occurrences']:2d}x] {term['source']}")
        print(f"     → {term['target']}")
        print()

    print("=" * 70)
    print("Review the extracted terms and manually curate before adding to glossary")
    print("=" * 70)

if __name__ == '__main__':
    main()
