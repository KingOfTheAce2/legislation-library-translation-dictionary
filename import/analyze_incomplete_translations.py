#!/usr/bin/env python3
"""
Analyze incomplete translations and create a report
"""
import json
import re

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def is_mutatis_mutandis(nl_text):
    """Check if text is a mutatis mutandis clause"""
    patterns = [
        r'van overeenkomstige toepassing',
        r'is van toepassing',
        r'zijn van toepassing'
    ]
    return any(re.search(pattern, nl_text, re.IGNORECASE) for pattern in patterns)

def analyze_incomplete(data):
    """Analyze incomplete translations"""
    incomplete = []

    for item in data:
        nl = item['source']
        en = item['target']

        # Check if translation seems incomplete
        is_incomplete = False
        reason = ""

        # Pattern 1: Ends with "apply" but Dutch has more text
        if en.strip().endswith('apply') and len(nl) > len(en) * 1.5:
            if is_mutatis_mutandis(nl):
                is_incomplete = True
                reason = "Mutatis mutandis clause - truncated"

        # Pattern 2: Very short English compared to Dutch
        if len(en) < len(nl) * 0.4 and len(nl) > 50:
            is_incomplete = True
            reason = "English much shorter than Dutch"

        # Pattern 3: Ends with ellipsis or (
        if en.strip().endswith('...') or en.strip().endswith('('):
            is_incomplete = True
            reason = "Ellipsis or incomplete parenthesis"

        if is_incomplete:
            incomplete.append({
                'tuid': item.get('tuid', ''),
                'nl': nl,
                'en': en,
                'nl_len': len(nl),
                'en_len': len(en),
                'reason': reason,
                'document': item.get('document', '')
            })

    return incomplete

def main():
    print("=" * 80)
    print("ANALYZING INCOMPLETE TRANSLATIONS")
    print("=" * 80)

    # Load data
    files = [
        '../i8n/netherlands/NL-EN-civil-procedure-book1.json',
        '../i8n/netherlands/NL-EN-civil-procedure-book2-3.json',
        '../i8n/netherlands/NL-EN-civil-procedure-book4.json'
    ]

    all_incomplete = []

    for filepath in files:
        print(f"\nAnalyzing {filepath}...")
        try:
            data = load_json(filepath)
            incomplete = analyze_incomplete(data)
            all_incomplete.extend(incomplete)
            print(f"  Found {len(incomplete)} incomplete translations")
        except FileNotFoundError:
            print(f"  File not found: {filepath}")

    print(f"\n{'=' * 80}")
    print(f"TOTAL INCOMPLETE: {len(all_incomplete)}")
    print(f"{'=' * 80}")

    # Group by reason
    by_reason = {}
    for item in all_incomplete:
        reason = item['reason']
        if reason not in by_reason:
            by_reason[reason] = []
        by_reason[reason].append(item)

    print("\nBreakdown by reason:")
    for reason, items in sorted(by_reason.items(), key=lambda x: len(x[1]), reverse=True):
        print(f"  {reason:40s}: {len(items):4d} items")

    # Show some examples
    print(f"\n{'=' * 80}")
    print("EXAMPLES OF INCOMPLETE TRANSLATIONS")
    print(f"{'=' * 80}\n")

    for i, item in enumerate(all_incomplete[:10], 1):
        print(f"{i}. TUID: {item['tuid']} - {item['reason']}")
        print(f"   Document: {item['document']}")
        print(f"   NL ({item['nl_len']} chars): {item['nl'][:150]}...")
        print(f"   EN ({item['en_len']} chars): {item['en'][:150]}...")
        print()

    # Save report
    output_file = '../i8n/netherlands/incomplete-translations-report.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_incomplete, f, ensure_ascii=False, indent=2)

    print(f"Full report saved to: {output_file}")
    print(f"\nNote: Many 'mutatis mutandis' clauses are legitimately shortened")
    print(f"in legal English. Manual review recommended.")

if __name__ == '__main__':
    main()
