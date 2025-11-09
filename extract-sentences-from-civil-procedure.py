#!/usr/bin/env python3
"""
Extract individual sentences from civil procedure paragraphs.

This script:
1. Reads all civil procedure JSON files (paragraph-level)
2. Splits paragraphs into individual sentences
3. Detects incomplete/missing translations
4. Combines everything into one comprehensive sentence file

Output: NL-EN-civil-procedure-sentences-all.json
"""

import json
import re
from pathlib import Path
from typing import List, Dict, Tuple


class SentenceExtractor:
    """Extract sentences from civil procedure paragraphs"""

    def __init__(self):
        self.base_path = Path('legal-data/netherlands/legislation/civil-procedure')
        self.input_files = [
            'NL-EN-civil-procedure-book1.json',
            'NL-EN-civil-procedure-book2-3.json',
            'NL-EN-civil-procedure-book4.json',
        ]
        self.sentences = []
        self.incomplete_count = 0

    def split_into_sentences(self, text: str) -> List[str]:
        """
        Split text into sentences intelligently

        Args:
            text: Input text

        Returns:
            List of sentences
        """
        if not text or len(text.strip()) < 5:
            return [text] if text else []

        # If text is very short (likely already a sentence or title), don't split
        if len(text) < 50 or text.count('.') <= 1:
            return [text.strip()]

        # Split on sentence boundaries
        # Match: ". " followed by capital letter, but not after common abbreviations
        sentences = re.split(
            r'(?<!\bArt)(?<!\bRv)(?<!\bNr)(?<!\bDr)(?<!\bMr)(?<!\bProf)(?<!\bJr)'
            r'(?<!\bSr)(?<!\betc)(?<!\bi\.e)(?<!\be\.g)(?<!\bvgl)(?<!\bbv)'
            r'(?<!\beg)(?<!\bviz)(?<!\bcf)\.\s+(?=[A-Z])',
            text
        )

        # Clean up sentences
        result = []
        for sent in sentences:
            sent = sent.strip()
            if sent:
                # Re-add period if it was removed
                if not sent.endswith('.') and not sent.endswith('?') and not sent.endswith('!'):
                    sent += '.'
                result.append(sent)

        return result if result else [text.strip()]

    def is_incomplete_translation(self, nl_text: str, en_text: str) -> Tuple[bool, str]:
        """
        Detect if translation is incomplete

        Args:
            nl_text: Dutch text
            en_text: English text

        Returns:
            Tuple of (is_incomplete, reason)
        """
        if not en_text or not en_text.strip():
            return True, "Empty translation"

        en_text = en_text.strip()

        # Check for placeholder patterns
        placeholder_patterns = [
            r'\[.*?\]',  # [placeholder]
            r'TODO',
            r'TBD',
            r'XXX',
            r'\?\?\?',
        ]

        for pattern in placeholder_patterns:
            if re.search(pattern, en_text, re.IGNORECASE):
                return True, f"Contains placeholder: {pattern}"

        # Check if English is just a copy of Dutch
        if nl_text.strip() == en_text:
            return True, "English is copy of Dutch"

        # Check length ratio (translation should be similar length)
        if len(nl_text) > 0:
            ratio = len(en_text) / len(nl_text)
            if ratio < 0.3:
                return True, f"Too short (ratio: {ratio:.2f})"
            if ratio > 3.0:
                return True, f"Too long (ratio: {ratio:.2f})"

        # Check if contains only non-alphabetic characters
        if not re.search(r'[a-zA-Z]', en_text):
            return True, "No alphabetic characters"

        return False, ""

    def process_file(self, filename: str) -> List[Dict]:
        """
        Process one civil procedure file

        Args:
            filename: Name of JSON file

        Returns:
            List of sentence entries
        """
        filepath = self.base_path / filename
        print(f"\n📄 Processing: {filename}")

        if not filepath.exists():
            print(f"  ⚠️  File not found: {filepath}")
            return []

        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        print(f"  ✓ Loaded {len(data)} paragraph entries")

        sentence_entries = []

        for entry in data:
            nl_text = entry.get('source', '').strip()
            en_text = entry.get('target', '').strip()

            # Skip if both are empty
            if not nl_text and not en_text:
                continue

            # Skip very short entries (titles, article numbers, etc.)
            # But keep them if they're actual sentences
            if len(nl_text) < 50 and '.' not in nl_text:
                # Likely a title or article number, keep as-is
                is_incomplete, reason = self.is_incomplete_translation(nl_text, en_text)

                sentence_entry = {
                    'id': f"{entry.get('tuid', 'unknown')}_s001",
                    'nl': nl_text,
                    'en': en_text,
                    'type': 'title-or-header',
                    'document': entry.get('document', ''),
                    'author': entry.get('author', ''),
                    'license': entry.get('license', 'CC BY 4.0'),
                    'sme-reviewed': entry.get('sme-reviewed', False),
                    'incomplete': is_incomplete,
                    'incomplete-reason': reason if is_incomplete else None,
                }
                sentence_entries.append(sentence_entry)
                if is_incomplete:
                    self.incomplete_count += 1
                continue

            # Split into sentences
            nl_sentences = self.split_into_sentences(nl_text)
            en_sentences = self.split_into_sentences(en_text)

            # Match sentences
            max_len = max(len(nl_sentences), len(en_sentences))

            for i in range(max_len):
                nl_sent = nl_sentences[i] if i < len(nl_sentences) else ""
                en_sent = en_sentences[i] if i < len(en_sentences) else ""

                # Check if incomplete
                is_incomplete, reason = self.is_incomplete_translation(nl_sent, en_sent)

                sentence_entry = {
                    'id': f"{entry.get('tuid', 'unknown')}_s{i+1:03d}",
                    'nl': nl_sent,
                    'en': en_sent,
                    'type': 'sentence',
                    'document': entry.get('document', ''),
                    'author': entry.get('author', ''),
                    'license': entry.get('license', 'CC BY 4.0'),
                    'sme-reviewed': entry.get('sme-reviewed', False),
                    'incomplete': is_incomplete,
                    'incomplete-reason': reason if is_incomplete else None,
                }

                sentence_entries.append(sentence_entry)

                if is_incomplete:
                    self.incomplete_count += 1

        print(f"  ✓ Extracted {len(sentence_entries)} sentence entries")

        return sentence_entries

    def extract_all(self) -> List[Dict]:
        """
        Extract sentences from all files

        Returns:
            Combined list of all sentences
        """
        print("=" * 70)
        print("CIVIL PROCEDURE SENTENCE EXTRACTOR")
        print("=" * 70)

        all_sentences = []

        for filename in self.input_files:
            sentences = self.process_file(filename)
            all_sentences.extend(sentences)

        return all_sentences

    def save_json(self, sentences: List[Dict], output_filename: str):
        """
        Save sentences to JSON file

        Args:
            sentences: List of sentence entries
            output_filename: Output file name
        """
        output_path = self.base_path / output_filename

        print(f"\n💾 Saving to {output_path}...")
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(sentences, f, ensure_ascii=False, indent=2)

        file_size = output_path.stat().st_size / 1024  # KB
        print(f"  ✓ Saved {len(sentences)} sentence entries")
        print(f"  ✓ File size: {file_size:.1f} KB")

    def generate_report(self, sentences: List[Dict]):
        """
        Generate extraction report

        Args:
            sentences: List of sentence entries
        """
        print("\n" + "=" * 70)
        print("EXTRACTION REPORT")
        print("=" * 70)

        print(f"\nTotal sentences extracted: {len(sentences)}")
        print(f"Incomplete translations: {self.incomplete_count}")
        print(f"Complete translations: {len(sentences) - self.incomplete_count}")

        completion_rate = ((len(sentences) - self.incomplete_count) / len(sentences) * 100) if sentences else 0
        print(f"Completion rate: {completion_rate:.1f}%")

        # Breakdown by reason
        print("\n📊 Incomplete Translation Reasons:")
        reasons = {}
        for sent in sentences:
            if sent['incomplete']:
                reason = sent.get('incomplete-reason', 'Unknown')
                reasons[reason] = reasons.get(reason, 0) + 1

        for reason, count in sorted(reasons.items(), key=lambda x: x[1], reverse=True):
            print(f"  • {reason}: {count}")

        # Breakdown by document
        print("\n📚 By Document:")
        documents = {}
        incomplete_by_doc = {}
        for sent in sentences:
            doc = sent.get('document', 'Unknown')
            documents[doc] = documents.get(doc, 0) + 1
            if sent['incomplete']:
                incomplete_by_doc[doc] = incomplete_by_doc.get(doc, 0) + 1

        for doc in sorted(documents.keys()):
            total = documents[doc]
            incomplete = incomplete_by_doc.get(doc, 0)
            complete = total - incomplete
            pct = (complete / total * 100) if total > 0 else 0
            print(f"  • {doc}: {complete}/{total} ({pct:.1f}%)")

        print("\n" + "=" * 70)
        print("NEXT STEPS")
        print("=" * 70)
        print("\n1. Review NL-EN-civil-procedure-sentences-all.json")
        print("2. Filter entries where 'incomplete' = true")
        print("3. Manually add English translations")
        print("4. Set 'incomplete' = false when done")
        print("5. Optionally set 'sme-reviewed' = true after review")
        print("\n✅ Extraction complete!")


def main():
    """Main execution"""
    extractor = SentenceExtractor()

    # Extract all sentences
    sentences = extractor.extract_all()

    # Save to file
    output_filename = 'NL-EN-civil-procedure-sentences-all.json'
    extractor.save_json(sentences, output_filename)

    # Generate report
    extractor.generate_report(sentences)


if __name__ == '__main__':
    main()
