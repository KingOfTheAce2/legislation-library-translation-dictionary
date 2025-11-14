#!/usr/bin/env python3
"""
Ingest International Legal Sources from Research Document

This script parses OPEN-DATA-LEGAL-SOURCES-VERIFIED.md and creates structured
source metadata for integration into the legal dictionary database.

All sources are marked as sme-reviewed: false (research phase) and include
full attribution information (jurisdiction, source URL, license).
"""

import json
import re
from typing import List, Dict, Optional


def parse_source_section(text: str, source_number: int) -> Optional[Dict]:
    """
    Parse a source section from the markdown and extract metadata.

    Returns a dictionary with source information or None if parsing fails.
    """
    # Extract title (format: ### 1. EUR-Lex (European Union) 🇪🇺)
    title_match = re.search(r'### \d+\.\s+(.+?)(?:\n|\*\*)', text)
    if not title_match:
        return None

    source_name_raw = title_match.group(1).strip()
    # Remove flag emojis from the end
    source_name = re.sub(r'\s*[🌍🇪🇺🇺🇸🇨🇭🇫🇷🇬🇧🇯🇵🇰🇷🇹🇭🇻🇳🇿🇦🇮🇳🇧🇷🇨🇿🇭🇰🇹🇼🇰🇪🇪🇬🇺🇬🇬🇭🇹🇿🇷🇺]+\s*$', '', source_name_raw).strip()

    # Extract priority
    priority_match = re.search(r'\*\*Priority:\s+(.+?)\*\*', text)
    priority = priority_match.group(1).strip() if priority_match else "MEDIUM"

    # Extract URL
    url_match = re.search(r'\*\*URL:\*\*\s+(.+?)(?:\n|\*\*)', text)
    source_url = url_match.group(1).strip() if url_match else None

    # Extract languages
    languages_match = re.search(r'\*\*Languages:\*\*\s+(.+?)(?:\n|\*\*)', text)
    languages = languages_match.group(1).strip() if languages_match else "Unknown"

    # Extract content description
    content_match = re.search(r'\*\*Content:\*\*\s+(.+?)(?:\n\n|\*\*)', text, re.DOTALL)
    content = content_match.group(1).strip() if content_match else ""

    # Extract license
    license_match = re.search(r'\*\*License:\*\*\s+(.+?)(?:\n|✅)', text)
    license_text = license_match.group(1).strip() if license_match else "Unknown"

    # Determine license type
    if "CC BY 4.0" in license_text or "CC BY 4.0" in text:
        license_type = "CC BY 4.0"
        license_url = "https://creativecommons.org/licenses/by/4.0/"
    elif "CC0" in license_text or "CC0" in text:
        license_type = "CC0"
        license_url = "https://creativecommons.org/publicdomain/zero/1.0/"
    elif "CC BY-NC-SA" in license_text:
        license_type = "CC BY-NC-SA 3.0"
        license_url = "https://creativecommons.org/licenses/by-nc-sa/3.0/"
    elif "CC BY-NC" in license_text:
        license_type = "CC BY-NC 3.0"
        license_url = "https://creativecommons.org/licenses/by-nc/3.0/"
    elif "OGL" in license_text or "Open Government Licence" in license_text:
        license_type = "OGL v3.0"
        license_url = "https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"
    elif "Apache 2.0" in license_text:
        license_type = "Apache 2.0"
        license_url = "https://www.apache.org/licenses/LICENSE-2.0"
    elif "Public Domain" in license_text or "US Government Works" in license_text:
        license_type = "Public Domain"
        license_url = None
    elif "Licence Ouverte" in license_text:
        license_type = "Licence Ouverte 2.0"
        license_url = "https://www.etalab.gouv.fr/licence-ouverte-open-licence"
    else:
        license_type = "Open Access"
        license_url = None

    # Determine jurisdiction from source name
    jurisdiction = determine_jurisdiction(source_name, text)

    # Extract estimated terms
    terms_match = re.search(r'\*\*Estimated Terms:\*\*\s+(.+?)(?:\n|$)', text)
    estimated_terms = terms_match.group(1).strip() if terms_match else "Unknown"

    # Extract source type
    source_type = determine_source_type(source_name, content)

    return {
        "id": f"source_{source_number:03d}",
        "name": source_name,
        "source_url": source_url,
        "source_type": source_type,
        "jurisdiction": jurisdiction,
        "languages": languages,
        "content_description": content,
        "license": license_type,
        "license_url": license_url,
        "estimated_terms": estimated_terms,
        "priority": priority,
        "sme_reviewed": False,
        "status": "research_phase",
        "notes": "Terms not yet extracted. Requires SME review before integration."
    }


def determine_jurisdiction(source_name: str, text: str) -> str:
    """Determine jurisdiction code from source name and content."""
    jurisdiction_map = {
        "European Union": "EU",
        "EUR-Lex": "EU",
        "DGT": "EU",
        "EuroVoc": "EU",
        "JRC-Acquis": "EU",
        "EUCLCORP": "EU",
        "ELRC-SHARE": "EU",
        "Switzerland": "CH",
        "Swiss": "CH",
        "France": "FR",
        "Légifrance": "FR",
        "United Kingdom": "GB",
        "UK Legislation": "GB",
        "United Nations": "UN",
        "MultiUN": "UN",
        "UN Parallel": "UN",
        "United States": "US",
        "US Library": "US",
        "Japan": "JP",
        "Japanese Law": "JP",
        "South Korea": "KR",
        "Korea": "KR",
        "Thailand": "TH",
        "Vietnam": "VN",
        "Hong Kong": "HK",
        "Taiwan": "TW",
        "South Africa": "ZA",
        "India": "IN",
        "Brazil": "BR",
        "Russia": "RU",
        "Kenya": "KE",
        "Uganda": "UG",
        "Ghana": "GH",
        "Tanzania": "TZ",
        "Czech": "CZ",
        "WTO": "INTL",
        "Asian Language Treebank": "ASEAN",
        "Leeds Arabic": "ARAB",
        "AfricanLII": "AFRICA",
        "ECHR": "ECHR",
        "Constitute Project": "INTL"
    }

    for key, code in jurisdiction_map.items():
        if key in source_name:
            return code

    return "INTL"  # Default to international


def determine_source_type(source_name: str, content: str) -> str:
    """Determine the type of legal source."""
    name_lower = source_name.lower()
    content_lower = content.lower()

    if "constitution" in name_lower or "constitution" in content_lower:
        return "Constitutional Law Corpus"
    elif "court" in name_lower or "judgment" in content_lower or "case law" in content_lower:
        return "Court Judgments"
    elif "legislation" in content_lower or "statute" in content_lower or "code" in content_lower:
        return "Legislation Corpus"
    elif "corpus" in name_lower or "parallel" in name_lower:
        return "Parallel Corpus"
    elif "thesaurus" in name_lower or "terminology" in name_lower:
        return "Legal Terminology Database"
    elif "translation memory" in name_lower or "TMX" in content:
        return "Translation Memory"
    else:
        return "Legal Database"


def parse_research_document(filepath: str) -> List[Dict]:
    """
    Parse the OPEN-DATA-LEGAL-SOURCES-VERIFIED.md file and extract all sources.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by source sections (### N. Source Name)
    sections = re.split(r'\n### \d+\.', content)

    sources = []
    for i, section in enumerate(sections[1:], start=1):  # Skip first split (header)
        # Re-add the section marker for parsing
        section_text = f"### {i}." + section

        # Only parse if it's in the "CONFIRMED OPEN DATA SOURCES" section
        if i <= 33:  # We have 33 confirmed sources
            source_data = parse_source_section(section_text, i)
            if source_data:
                sources.append(source_data)

    return sources


def generate_sources_json(sources: List[Dict], output_path: str):
    """Generate a structured JSON file with all source metadata."""
    output = {
        "metadata": {
            "generated_date": "2025-11-14",
            "total_sources": len(sources),
            "status": "research_phase",
            "sme_review_required": True,
            "description": "International legal translation sources verified for open licenses. All sources require Subject Matter Expert review before term integration."
        },
        "sources": sources
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"✅ Generated {output_path}")
    print(f"   Total sources: {len(sources)}")
    print(f"   All sources marked: sme_reviewed = false")


def generate_summary_report(sources: List[Dict]):
    """Print a summary report of the parsed sources."""
    print("\n" + "="*80)
    print("INTERNATIONAL LEGAL SOURCES - INGESTION SUMMARY")
    print("="*80)

    # Group by jurisdiction
    by_jurisdiction = {}
    for source in sources:
        jur = source['jurisdiction']
        if jur not in by_jurisdiction:
            by_jurisdiction[jur] = []
        by_jurisdiction[jur].append(source)

    print(f"\n📊 Total Sources: {len(sources)}")
    print(f"🌍 Jurisdictions: {len(by_jurisdiction)}")
    print(f"⚠️  SME Review Status: ALL SOURCES = false (research phase)")

    print("\n📍 Sources by Jurisdiction:")
    for jur in sorted(by_jurisdiction.keys()):
        count = len(by_jurisdiction[jur])
        print(f"   {jur:10s} - {count:2d} sources")

    print("\n📜 License Distribution:")
    license_counts = {}
    for source in sources:
        lic = source['license']
        license_counts[lic] = license_counts.get(lic, 0) + 1

    for lic, count in sorted(license_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"   {lic:25s} - {count:2d} sources")

    print("\n🔍 Source Types:")
    type_counts = {}
    for source in sources:
        stype = source['source_type']
        type_counts[stype] = type_counts.get(stype, 0) + 1

    for stype, count in sorted(type_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"   {stype:35s} - {count:2d} sources")

    print("\n" + "="*80)
    print()


def main():
    """Main execution function."""
    print("🚀 Starting International Legal Sources Ingestion...")
    print("   Input:  OPEN-DATA-LEGAL-SOURCES-VERIFIED.md")
    print("   Output: international-sources.json")
    print()

    # Parse the research document
    sources = parse_research_document('OPEN-DATA-LEGAL-SOURCES-VERIFIED.md')

    # Generate JSON output
    generate_sources_json(sources, 'international-sources.json')

    # Generate summary report
    generate_summary_report(sources)

    print("✅ Ingestion complete!")
    print()
    print("Next steps:")
    print("1. Review international-sources.json for accuracy")
    print("2. Use this metadata when extracting terms from sources")
    print("3. Each extracted term must include: jurisdiction, source_url, license, sme_reviewed=false")
    print("4. Terms require SME review before setting sme_reviewed=true")


if __name__ == "__main__":
    main()
