# i8n - Internationalization Dictionary Data

This directory contains all legal dictionary and legislation translation data, organized by **jurisdiction**.

## Directory Structure (New - 2025-11-09)

```
i8n/
├── netherlands/          # Netherlands law and jurisdiction
│   ├── NL-legal-dictionary.json            # Dutch monolingual
│   ├── NL-EN-civil-procedure-all.json      # Complete Civil Procedure Code
│   ├── NL-EN-legal-dictionary.json         # Business/admin terms
│   ├── NL-EN-legal-glossary.json           # Professional glossary
│   ├── NL-EN-example-sentences.json        # Usage examples
│   ├── NL-FR-legal-glossary.json           # Dutch-French
│   ├── NL-DE-legal-glossary.json           # Dutch-German
│   ├── NL-ES-legal-glossary.json           # Dutch-Spanish
│   └── ... (15 files total, ~8.6 MB)
│
└── france/              # French law and jurisdiction
    └── README.md        # Prepared for future French content
```

## Why Jurisdiction-Based?

**Previous Structure:** Organized by language pairs (NL-EN, NL-FR, etc.)

**Problem:** As we add more countries' legal systems, language-based organization becomes confusing:
- Is "NL-FR" Netherlands Dutch → French or Belgium/Luxembourg?
- Where do French legal terms from France go?
- How to separate different legal systems using the same language?

**Solution:** Organize by **jurisdiction first**, then by language.

### Benefits

1. **Legal Clarity** - Law is jurisdiction-specific, not language-specific
2. **Scalability** - Easy to add Belgium, Luxembourg, France, Germany, etc.
3. **Context Preservation** - Dutch law terms stay separate from Belgian law terms
4. **User Navigation** - Users can filter by relevant jurisdiction
5. **Source Attribution** - Clearer which legal system terms come from

## Jurisdiction Scope

Each jurisdiction directory contains:
- Legal terms and definitions specific to that jurisdiction's legal system
- Translations of legislation from that jurisdiction
- Official government sources from that jurisdiction
- Proper attribution to local authorities

### Netherlands (`/netherlands/`)

**Legal System:** Netherlands civil law
**Primary Language:** Dutch (Nederlands, nl-NL)
**Geographic Scope:** Kingdom of the Netherlands (European territory)

**Key Sources:**
- Raad van de Rechtspraak (Dutch Judiciary)
- wetten.overheid.nl (Official Legislation Portal)
- business.gov.nl
- Dutch Ministry of Finance

**Content:**
- 3,400+ legal terms
- Complete Code of Civil Procedure (Wetboek van Burgerlijke Rechtsvordering)
- Multilingual translations (EN, FR, DE, ES)

### France (`/france/`)

**Legal System:** French civil law (Code civil)
**Primary Language:** French (Français, fr-FR)
**Geographic Scope:** French Republic

**Status:** Directory prepared for future content

**Planned Sources:**
- Ministère de la Justice
- Légifrance (Official French legal portal)
- French government open data

## File Naming Convention

All files follow consistent naming:

```
[SOURCE-LANG]-[TARGET-LANG]-[CONTENT-TYPE].json
```

### Examples

- `NL-EN-legal-dictionary.json` - Dutch → English dictionary
- `NL-legal-dictionary.json` - Dutch monolingual (implicit NL-NL)
- `FR-FR-legal-dictionary.json` - French monolingual

### Language Codes

Follow ISO 639-1 (language) + ISO 3166-1 (country):
- `nl-nl` - Dutch (Netherlands)
- `en-gb` - English (British, used for legal English)
- `fr-fr` - French (France)
- `de-de` - German (Germany)
- `es-es` - Spanish (Spain)

**Note:** Use lowercase for consistency.

## Content Types

Each jurisdiction may have:

1. **Monolingual Dictionaries**
   - Pattern: `XX-legal-dictionary.json`
   - Contains terms with definitions in the same language
   - Used for native speakers learning legal terminology

2. **Bilingual Dictionaries**
   - Pattern: `XX-YY-legal-dictionary.json`
   - Contains terms with translations and definitions
   - Used for translators and multilingual professionals

3. **Legislation Translations**
   - Pattern: `XX-YY-[legislation-name].json`
   - Complete legal codes with paragraph-by-paragraph translations
   - Example: `NL-EN-civil-procedure-all.json`

4. **Legal Glossaries**
   - Pattern: `XX-YY-legal-glossary.json`
   - Curated professional terminology lists
   - Often subject-matter expert reviewed

5. **Example Sentences**
   - Pattern: `XX-YY-example-sentences.json`
   - Usage examples for terms
   - Helps understand context

## Migration from Old Structure

**Date:** 2025-11-09
**Reason:** Better scalability and legal clarity

### Old Structure (Deprecated)
```
i8n/
  NL-EN-legal-dictionary.json
  NL-FR-legal-glossary.json
  ...
```

### New Structure
```
i8n/
  netherlands/
    NL-EN-legal-dictionary.json
    NL-FR-legal-glossary.json
    ...
  france/
    ...
```

### Breaking Changes

If you're using these files in code, update paths:

```javascript
// OLD
fetch('i8n/NL-EN-legal-dictionary.json')

// NEW
fetch('i8n/netherlands/NL-EN-legal-dictionary.json')
```

## Future Jurisdictions

Planned additions:
- `belgium/` - Belgian law (Dutch/French/German versions)
- `luxembourg/` - Luxembourg law
- `germany/` - German law
- `spain/` - Spanish law
- `european-union/` - EU directives and regulations

Each will follow the same structure and naming conventions.

## Data Format

All JSON files follow the unified dictionary structure documented in:
- `/UNIFIED-DATABASE-STRUCTURE.md`
- `/dictionary-structure-proposal.md`

## Licenses

Content is provided under various open licenses:
- **CC BY 4.0** - Creative Commons Attribution
- **CC0** - Public Domain (government sources)
- **Licence Ouverte 2.0** - French open data license
- **CC BY-NC 4.0** - Non-commercial (some examples)

See `/authors-licenses.html` for complete attribution.

## Usage

These jurisdiction-specific files are:
1. Loaded directly by the website (`index.html`, `legislation.html`)
2. Merged into `unified-dictionary.json` for search functionality
3. Processed by import scripts in `/import/` directory

## Contributing

To add content to a jurisdiction:

1. Choose appropriate jurisdiction directory
2. Follow naming conventions
3. Use standard JSON structure
4. Include proper attribution and licensing
5. Update jurisdiction README
6. Update this main README

See `/CONTRIBUTING.md` for detailed guidelines.

---

**Previous structure:** Flat `/i8n/` with language-pair prefixed files
**New structure:** Jurisdiction-based subdirectories
**Migration date:** 2025-11-09
**Backward compatibility:** Update file paths in HTML/JS/Python files

*For questions or suggestions about this structure, please open an issue.*
