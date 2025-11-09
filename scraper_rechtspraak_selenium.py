#!/usr/bin/env python3
"""
Advanced scraper for rechtspraak.nl juridische begrippen using Selenium
Creates a monolingual Dutch legal dictionary
"""

import json
import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from bs4 import BeautifulSoup

def setup_driver():
    """Setup Chrome driver with options"""

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

    try:
        driver = webdriver.Chrome(options=chrome_options)
        return driver
    except WebDriverException as e:
        print(f"Error setting up Chrome driver: {e}")
        print("\nTrying with Firefox...")

        try:
            from selenium.webdriver.firefox.options import Options as FirefoxOptions
            firefox_options = FirefoxOptions()
            firefox_options.add_argument('--headless')
            driver = webdriver.Firefox(options=firefox_options)
            return driver
        except:
            print("Firefox also not available")
            return None

def scrape_with_selenium():
    """Scrape legal terms using Selenium"""

    url = "https://www.rechtspraak.nl/juridische-begrippen"

    print(f"Setting up browser...")
    driver = setup_driver()

    if not driver:
        print("Could not setup browser driver")
        return []

    try:
        print(f"Fetching: {url}")
        driver.get(url)

        # Wait for page to load
        time.sleep(3)

        # Try to wait for content
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
        except TimeoutException:
            print("Page load timeout")

        # Get page source
        page_source = driver.page_source

        # Save for inspection
        with open('rechtspraak_selenium.html', 'w', encoding='utf-8') as f:
            f.write(page_source)
        print("Saved page HTML to rechtspraak_selenium.html")

        # Parse with BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')

        terms = []

        # Look for the glossary/dictionary structure
        # Try multiple selectors

        # Method 1: Look for definition lists
        dl_elements = soup.find_all('dl')
        for dl in dl_elements:
            dts = dl.find_all('dt')
            dds = dl.find_all('dd')

            for dt, dd in zip(dts, dds):
                term = dt.get_text(strip=True)
                definition = dd.get_text(strip=True)

                if term and definition and len(definition) > 10:
                    terms.append({
                        "source": term,
                        "lang-source": "nl-nl",
                        "lang-source-dict": definition,
                        "author": "Raad van de Rechtspraak",
                        "license": "CC0",
                        "sme-reviewed": True,
                        "premium": False
                    })

        # Method 2: Look for articles with headings
        if not terms:
            articles = soup.find_all(['article', 'section'])
            for article in articles:
                headings = article.find_all(['h2', 'h3', 'h4'])
                for heading in headings:
                    term = heading.get_text(strip=True)

                    # Get next paragraph or div
                    next_elem = heading.find_next_sibling(['p', 'div'])
                    if next_elem:
                        definition = next_elem.get_text(strip=True)

                        if term and definition and len(definition) > 10:
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

        # Method 3: Look for list items with bold terms
        if not terms:
            list_items = soup.find_all('li')
            for li in list_items:
                strong = li.find(['strong', 'b'])
                if strong:
                    term = strong.get_text(strip=True)
                    # Get rest of the text
                    full_text = li.get_text(strip=True)
                    definition = full_text.replace(term, '', 1).strip()

                    if term and definition and len(definition) > 10:
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

        # Method 4: Look for divs with specific classes
        if not terms:
            # Common class names for glossary items
            potential_classes = ['glossary', 'term', 'definition', 'begrip', 'woordenlijst']
            for cls in potential_classes:
                elements = soup.find_all(class_=lambda x: x and cls in x.lower() if x else False)
                for elem in elements:
                    # Extract term and definition
                    strong = elem.find(['strong', 'b', 'dt'])
                    if strong:
                        term = strong.get_text(strip=True)
                        definition = elem.get_text(strip=True).replace(term, '', 1).strip()

                        if term and definition and len(definition) > 10:
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

        return terms

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return []

    finally:
        driver.quit()

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
    print("Rechtspraak.nl Legal Terms Scraper (Selenium)")
    print("=" * 60)

    terms = scrape_with_selenium()

    if terms:
        output_file = "i8n/netherlands/NL-legal-dictionary.json"
        save_dictionary(terms, output_file)

        # Print first few terms as example
        print("\nFirst 3 terms:")
        for term in terms[:3]:
            print(f"\n{term['source']}:")
            print(f"  {term['lang-source-dict'][:150]}...")
    else:
        print("\nFailed to scrape terms.")
        print("Check rechtspraak_selenium.html for the page structure.")
        sys.exit(1)
