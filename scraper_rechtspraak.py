#!/usr/bin/env python3
"""
Scraper for rechtspraak.nl juridische begrippen (legal terms)
Creates a monolingual Dutch legal dictionary
"""

import json
import requests
from bs4 import BeautifulSoup
import time
import sys

def scrape_rechtspraak_terms():
    """Scrape legal terms from rechtspraak.nl"""

    url = "https://www.rechtspraak.nl/juridische-begrippen"

    print(f"Fetching: {url}")

    # Set headers to avoid 403
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'nl-NL,nl;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        print(f"Status: {response.status_code}")

        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all legal terms - they might be in various formats
        # Let's look for common patterns

        terms = []

        # Try to find terms in definition lists
        dl_elements = soup.find_all('dl')
        for dl in dl_elements:
            dts = dl.find_all('dt')
            dds = dl.find_all('dd')

            for dt, dd in zip(dts, dds):
                term = dt.get_text(strip=True)
                definition = dd.get_text(strip=True)

                if term and definition:
                    terms.append({
                        "source": term,
                        "lang-source": "nl-nl",
                        "lang-source-dict": definition,
                        "author": "Raad van de Rechtspraak",
                        "license": "CC0",
                        "sme-reviewed": True,
                        "premium": False
                    })

        # Also try article or section elements
        if not terms:
            articles = soup.find_all(['article', 'section', 'div'], class_=lambda x: x and 'term' in x.lower() if x else False)
            for article in articles:
                # Look for heading and content
                heading = article.find(['h2', 'h3', 'h4', 'strong', 'b'])
                if heading:
                    term = heading.get_text(strip=True)
                    # Get the rest of the content
                    paragraphs = article.find_all('p')
                    definition = ' '.join(p.get_text(strip=True) for p in paragraphs)

                    if term and definition:
                        terms.append({
                            "source": term,
                            "lang-source": "nl-nl",
                            "lang-source-dict": definition,
                            "author": "Raad van de Rechtspraak",
                            "license": "CC0",
                            "sme-reviewed": True,
                            "premium": False
                        })

        # If still no terms, try a more general approach
        if not terms:
            # Look for any strong/bold tags followed by text
            all_text_elements = soup.find_all(['div', 'section', 'article'])
            for element in all_text_elements:
                strong_tags = element.find_all(['strong', 'b', 'dt'])
                for strong in strong_tags:
                    term = strong.get_text(strip=True)
                    # Get next sibling or parent's next text
                    definition = ""

                    # Try next sibling
                    next_elem = strong.find_next_sibling()
                    if next_elem:
                        definition = next_elem.get_text(strip=True)
                    elif strong.parent:
                        # Try parent's text after the strong tag
                        parent_text = strong.parent.get_text(strip=True)
                        term_pos = parent_text.find(term)
                        if term_pos != -1:
                            definition = parent_text[term_pos + len(term):].strip()

                    if term and definition and len(definition) > 20:
                        # Avoid duplicates
                        if not any(t['source'] == term for t in terms):
                            terms.append({
                                "source": term,
                                "lang-source": "nl-nl",
                                "lang-source-dict": definition,
                                "author": "Raad van de Rechtspraak",
                                "license": "CC0",
                                "sme-reviewed": True,
                                "premium": False
                            })

        print(f"Found {len(terms)} terms")

        if not terms:
            print("\nNo terms found. HTML structure might be different.")
            print("Saving HTML for manual inspection...")
            with open('rechtspraak_page.html', 'w', encoding='utf-8') as f:
                f.write(soup.prettify())
            print("Saved to rechtspraak_page.html")

        return terms

    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return []
    except Exception as e:
        print(f"Error parsing page: {e}")
        import traceback
        traceback.print_exc()
        return []

def save_dictionary(terms, output_file):
    """Save terms to JSON file"""

    if not terms:
        print("No terms to save")
        return False

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(terms, f, ensure_ascii=False, indent=2)

    print(f"\nSaved {len(terms)} terms to {output_file}")
    return True

if __name__ == "__main__":
    print("Rechtspraak.nl Legal Terms Scraper")
    print("=" * 50)

    terms = scrape_rechtspraak_terms()

    if terms:
        output_file = "i8n/netherlands/NL-legal-dictionary.json"
        save_dictionary(terms, output_file)

        # Print first few terms as example
        print("\nFirst 3 terms:")
        for term in terms[:3]:
            print(f"\n{term['source']}:")
            print(f"  {term['lang-source-dict'][:100]}...")
    else:
        print("\nFailed to scrape terms. Check rechtspraak_page.html for structure.")
        sys.exit(1)
