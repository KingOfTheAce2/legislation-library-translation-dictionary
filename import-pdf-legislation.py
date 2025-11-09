#!/usr/bin/env python3
"""
Import PDF legislation files and match them paragraph by paragraph.

This script extracts text from bilingual PDF files (e.g., Dutch and English versions
of the same legal code) and creates paragraph-by-paragraph matched translations.

Requirements:
    pip install pdfplumber python-docx

Usage:
    python import-pdf-legislation.py --nl dutch.pdf --en english.pdf --output NL-EN-legislation.json
    python import-pdf-legislation.py --nl dutch.pdf --en english.pdf --mode sentence --output NL-EN-legislation-sentences.json
"""

import argparse
import json
import re
from pathlib import Path
from typing import List, Dict, Tuple

try:
    import pdfplumber
except ImportError:
    print("ERROR: pdfplumber not installed. Install with: pip install pdfplumber")
    exit(1)


class PDFLegislationImporter:
    """Import and match bilingual PDF legislation"""

    def __init__(self, nl_pdf: str, en_pdf: str, mode: str = 'paragraph'):
        """
        Initialize importer

        Args:
            nl_pdf: Path to Dutch PDF file
            en_pdf: Path to English PDF file
            mode: Segmentation mode ('paragraph' or 'sentence')
        """
        self.nl_pdf = Path(nl_pdf)
        self.en_pdf = Path(en_pdf)
        self.mode = mode

        if not self.nl_pdf.exists():
            raise FileNotFoundError(f"Dutch PDF not found: {nl_pdf}")
        if not self.en_pdf.exists():
            raise FileNotFoundError(f"English PDF not found: {en_pdf}")

    def extract_paragraphs(self, pdf_path: Path) -> List[str]:
        """
        Extract paragraphs from PDF

        Args:
            pdf_path: Path to PDF file

        Returns:
            List of paragraphs
        """
        paragraphs = []

        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, 1):
                text = page.extract_text()

                if not text:
                    continue

                # Split by double newlines or article numbers
                # Common patterns: "Artikel 1", "Article 1", "Art. 1"
                chunks = re.split(
                    r'\n\s*\n|(?=(?:Artikel|Article|Art\.)\s+\d+)',
                    text
                )

                for chunk in chunks:
                    chunk = chunk.strip()
                    if chunk and len(chunk) > 10:  # Skip very short fragments
                        paragraphs.append(chunk)

        return paragraphs

    def extract_sentences(self, pdf_path: Path) -> List[str]:
        """
        Extract sentences from PDF

        Args:
            pdf_path: Path to PDF file

        Returns:
            List of sentences
        """
        paragraphs = self.extract_paragraphs(pdf_path)
        sentences = []

        for para in paragraphs:
            # Split by sentence endings (. ! ?) followed by space and capital letter
            # But preserve abbreviations like "Art.", "Rv.", etc.
            para_sentences = re.split(
                r'(?<!\bArt)(?<!\bRv)(?<!\bNr)(?<!\bDr)(?<!\bMr)\. (?=[A-Z])',
                para
            )

            for sent in para_sentences:
                sent = sent.strip()
                if sent and len(sent) > 5:
                    sentences.append(sent)

        return sentences

    def detect_article_numbers(self, text: str) -> str:
        """
        Detect article numbers in text

        Args:
            text: Text to analyze

        Returns:
            Article number if found, else empty string
        """
        # Common patterns
        patterns = [
            r'(?:Artikel|Article|Art\.)\s+(\d+[a-z]?)',
            r'^(\d+[a-z]?)\.',
        ]

        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1)

        return ''

    def match_paragraphs(self, nl_paras: List[str], en_paras: List[str]) -> List[Dict]:
        """
        Match Dutch and English paragraphs

        Args:
            nl_paras: Dutch paragraphs
            en_paras: English paragraphs

        Returns:
            List of matched translation units
        """
        translation_units = []

        # Simple 1:1 matching
        max_len = min(len(nl_paras), len(en_paras))

        for i in range(max_len):
            nl_text = nl_paras[i]
            en_text = en_paras[i]

            # Detect article number
            article_num = self.detect_article_numbers(nl_text) or \
                         self.detect_article_numbers(en_text)

            tu = {
                'id': f'tu_{i+1:04d}',
                'nl': nl_text,
                'en': en_text,
                'article': article_num or None,
                'segmentation': self.mode,
                'source': 'PDF Import',
                'license': 'TBD',  # User should update this
            }

            translation_units.append(tu)

        # Report mismatches
        if len(nl_paras) != len(en_paras):
            print(f"\n⚠️  WARNING: Paragraph count mismatch!")
            print(f"   Dutch paragraphs: {len(nl_paras)}")
            print(f"   English paragraphs: {len(en_paras)}")
            print(f"   Matched: {max_len}")
            print(f"   Unmatched: {abs(len(nl_paras) - len(en_paras))}")

        return translation_units

    def import_pdfs(self) -> List[Dict]:
        """
        Import and match PDFs

        Returns:
            List of translation units
        """
        print("=" * 70)
        print("PDF LEGISLATION IMPORTER")
        print("=" * 70)
        print(f"\nDutch PDF:  {self.nl_pdf}")
        print(f"English PDF: {self.en_pdf}")
        print(f"Mode: {self.mode}")

        print(f"\n📄 Extracting {self.mode}s from Dutch PDF...")
        if self.mode == 'sentence':
            nl_segments = self.extract_sentences(self.nl_pdf)
        else:
            nl_segments = self.extract_paragraphs(self.nl_pdf)
        print(f"  ✓ Extracted {len(nl_segments)} Dutch {self.mode}s")

        print(f"\n📄 Extracting {self.mode}s from English PDF...")
        if self.mode == 'sentence':
            en_segments = self.extract_sentences(self.en_pdf)
        else:
            en_segments = self.extract_paragraphs(self.en_pdf)
        print(f"  ✓ Extracted {len(en_segments)} English {self.mode}s")

        print(f"\n🔗 Matching {self.mode}s...")
        translation_units = self.match_paragraphs(nl_segments, en_segments)
        print(f"  ✓ Matched {len(translation_units)} translation units")

        # Quality checks
        print(f"\n📊 Quality Checks:")

        # Check for very short segments
        short_segments = [tu for tu in translation_units if len(tu['nl']) < 20 or len(tu['en']) < 20]
        if short_segments:
            print(f"  ⚠️  {len(short_segments)} segments are very short (< 20 chars)")

        # Check for length mismatches (ratio > 2:1 or < 1:2)
        length_mismatches = []
        for tu in translation_units:
            ratio = len(tu['nl']) / max(len(tu['en']), 1)
            if ratio > 2.5 or ratio < 0.4:
                length_mismatches.append(tu)

        if length_mismatches:
            print(f"  ⚠️  {len(length_mismatches)} segments have suspicious length ratios")
            print(f"      (May indicate alignment issues)")

        # Article number coverage
        with_articles = [tu for tu in translation_units if tu['article']]
        print(f"  ✓ {len(with_articles)} segments have article numbers")

        return translation_units

    def save_json(self, translation_units: List[Dict], output_path: str):
        """
        Save translation units to JSON

        Args:
            translation_units: List of translation units
            output_path: Output JSON file path
        """
        output_file = Path(output_path)

        # Ensure output directory exists
        output_file.parent.mkdir(parents=True, exist_ok=True)

        print(f"\n💾 Saving to {output_file}...")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(translation_units, f, ensure_ascii=False, indent=2)

        file_size = output_file.stat().st_size / 1024  # KB
        print(f"  ✓ Saved {len(translation_units)} translation units")
        print(f"  ✓ File size: {file_size:.1f} KB")

    def generate_report(self, translation_units: List[Dict]) -> str:
        """
        Generate import report

        Args:
            translation_units: List of translation units

        Returns:
            Report as string
        """
        report = []
        report.append("=" * 70)
        report.append("IMPORT REPORT")
        report.append("=" * 70)
        report.append(f"\nTotal translation units: {len(translation_units)}")

        if translation_units:
            avg_nl_length = sum(len(tu['nl']) for tu in translation_units) / len(translation_units)
            avg_en_length = sum(len(tu['en']) for tu in translation_units) / len(translation_units)

            report.append(f"Average Dutch length: {avg_nl_length:.0f} characters")
            report.append(f"Average English length: {avg_en_length:.0f} characters")

            with_articles = [tu for tu in translation_units if tu['article']]
            report.append(f"Segments with article numbers: {len(with_articles)}")

        report.append("\n" + "=" * 70)
        report.append("NEXT STEPS")
        report.append("=" * 70)
        report.append("\n1. Review the generated JSON file")
        report.append("2. Check for alignment issues (length mismatches)")
        report.append("3. Update 'license' field with correct license")
        report.append("4. Update 'source' field with actual source")
        report.append("5. Add metadata (jurisdiction, legislation name, etc.)")
        report.append("6. Run quality assurance scripts")
        report.append("\n✅ Import complete!")

        return '\n'.join(report)


def main():
    parser = argparse.ArgumentParser(
        description='Import PDF legislation and create paragraph-by-paragraph translations'
    )
    parser.add_argument('--nl', required=True, help='Dutch PDF file path')
    parser.add_argument('--en', required=True, help='English PDF file path')
    parser.add_argument('--output', required=True, help='Output JSON file path')
    parser.add_argument('--mode', choices=['paragraph', 'sentence'], default='paragraph',
                       help='Segmentation mode (default: paragraph)')

    args = parser.parse_args()

    try:
        importer = PDFLegislationImporter(args.nl, args.en, args.mode)
        translation_units = importer.import_pdfs()
        importer.save_json(translation_units, args.output)

        report = importer.generate_report(translation_units)
        print(f"\n{report}")

    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        exit(1)


if __name__ == '__main__':
    main()
