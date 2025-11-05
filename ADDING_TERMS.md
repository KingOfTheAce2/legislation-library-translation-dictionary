# Adding Terms to the Monolingual Dictionary

## Overview

The monolingual Dutch legal dictionary (`i8n/NL-legal-dictionary.json`) contains comprehensive definitions of legal terms in Dutch, sourced from Raad van de Rechtspraak (Dutch Judiciary).

## Current Status

✅ **27 starter terms** have been added, including:
- baldadigheid (as per your example)
- aanhangig, aanklacht, aansprakelijkheid
- beroep, cassatie, dagvaarding
- And more...

## Adding More Terms

### Manual Method

Since rechtspraak.nl blocks automated scraping, you can add terms manually by:

1. **Visit the source**: https://www.rechtspraak.nl/juridische-begrippen
2. **Browse terms alphabetically** (A-Z navigation on the site)
3. **Copy the term and definition**
4. **Add to the JSON file** following this format:

```json
{
  "source": "term-name",
  "lang-source": "nl-nl",
  "lang-source-dict": "Complete definition in Dutch...",
  "author": "Raad van de Rechtspraak",
  "license": "CC0",
  "sme-reviewed": true,
  "premium": false
}
```

### Field Descriptions

- **source**: The Dutch legal term (e.g., "baldadigheid")
- **lang-source**: Language code (always "nl-nl" for this dictionary)
- **lang-source-dict**: The full definition/explanation in Dutch
- **author**: Source of the definition (use "Raad van de Rechtspraak" for terms from rechtspraak.nl)
- **license**: License type (use "CC0" for rechtspraak.nl terms)
- **sme-reviewed**: Subject Matter Expert review status (set to `true` for official rechtspraak.nl definitions)
- **premium**: Premium content flag (set to `false` for public terms)

### Example Entry

```json
{
  "source": "baldadigheid",
  "lang-source": "nl-nl",
  "lang-source-dict": "Strafbare overtreding wanneer er gevaar of nadeel voor goederen of personen in de openbare ruimte wordt veroorzaakt. Het gaat meestal om ruw, onbezonnen of kwaadwillig gedrag, bijvoorbeeld (expres) vernielen van openbare of particuliere eigendommen of veroorzaken van overlast. Baldadigheid kan ook gaan om overtreden van een toegangsverbod.",
  "author": "Raad van de Rechtspraak",
  "license": "CC0",
  "sme-reviewed": true,
  "premium": false
}
```

## Tips

1. **Validate JSON**: Use a JSON validator (like jsonlint.com) to check your file after adding terms
2. **Maintain alphabetical order**: Keep terms sorted by the "source" field for easier navigation
3. **Use proper Dutch characters**: Ensure special characters (ë, ï, etc.) are preserved
4. **Be comprehensive**: Include the full definition from rechtspraak.nl
5. **Check for duplicates**: Search the file before adding to avoid duplicate entries

## Alternative Approaches

### Using PDFs

Rechtspraak.nl publishes PDF glossaries:
- https://www.rechtspraak.nl/SiteCollectionDocuments/begrippenlijst-in-de-rechtspraak-alttekst.pdf

You can:
1. Download the PDF
2. Extract text (using PDF readers or online tools)
3. Parse and structure into JSON format
4. Add to the dictionary

### Batch Import

If you have a list of terms in a spreadsheet:
1. Create columns matching the JSON fields
2. Export as CSV
3. Use a script to convert CSV to JSON
4. Merge with existing dictionary

## Contributing

After adding terms:
1. Test the dictionary on the website (reload index.html)
2. Commit your changes with a descriptive message
3. Push to the repository
4. Create a pull request if contributing to the main project

## Questions?

- Check the main README.md for project overview
- Review existing entries in `i8n/NL-legal-dictionary.json` for formatting examples
- Open an issue on GitHub: https://github.com/kingoftheace2/legislation-library-translation-dictionary/issues
