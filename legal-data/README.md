# Legal Data - Multilingual Legal Resources by Jurisdiction

This directory contains all legal dictionaries, legislation translations, and related resources, organized by **jurisdiction** and **content type**.

## Directory Structure

```
legal-data/
├── netherlands/              # Netherlands law and jurisdiction
│   ├── dictionaries/        # Legal dictionaries and glossaries (8 files)
│   ├── legislation/         # Laws and statutes
│   │   └── civil-procedure/ # Code of Civil Procedure (6 files, 8.5 MB)
│   ├── reports/             # Quality assurance reports
│   └── README.md
│
├── france/                  # French law and jurisdiction
│   ├── dictionaries/
│   ├── legislation/
│   ├── reports/
│   └── README.md
│
└── README.md               # This file
```

## Why This Structure?

### 1. **Jurisdiction-Based Organization**

Law is inherently jurisdiction-specific. A legal term in Netherlands law may have different meaning or application than in French, Belgian, or German law, even when using the same language.

**Example:** "rechtspersoon" in Dutch Netherlands law ≠ "rechtspersoon" in Belgian law

### 2. **Content Type Subfolders**

Within each jurisdiction, content is organized by type:

- **`dictionaries/`** - Legal dictionaries, glossaries, and terminology databases
- **`legislation/`** - Complete legal codes, statutes, and regulations (organized by legal domain)
- **`reports/`** - Quality assurance reports, translation completeness metrics

### 3. **Scalability**

This structure makes it easy to add:
- New jurisdictions (Belgium, Germany, Luxembourg, EU)
- New legislation types (criminal code, tax code, commercial code)
- New content types (case law, legal forms, contracts)

## Content Types

### Dictionaries (`dictionaries/`)

Legal terminology with translations and definitions:
- **Monolingual dictionaries** - Terms with definitions in the same language (e.g., NL-NL for Dutch learners)
- **Bilingual dictionaries** - Term translations with definitions (e.g., NL-EN for translators)
- **Specialized glossaries** - Domain-specific terminology (e.g., tax law, procedural law)

**File naming:** `[SOURCE-LANG]-[TARGET-LANG]-[TYPE].json`
- `NL-legal-dictionary.json` - Dutch monolingual
- `NL-EN-legal-dictionary.json` - Dutch to English
- `NL-EN-legal-glossary.json` - Specialized glossary

### Legislation (`legislation/`)

Complete legal codes and statutes with paragraph-by-paragraph translations.

Organized by legal domain:
- **`civil-procedure/`** - Code of Civil Procedure (Wetboek van Burgerlijke Rechtsvordering)
  - Paragraph-level translations
  - Sentence-level segmentation for linguistic analysis
- **`civil-code/`** - Civil Code (Burgerlijk Wetboek) *(future)*
- **`criminal-code/`** - Criminal Code (Wetboek van Strafrecht) *(future)*
- **`tax-code/`** - Tax legislation *(future)*

**File naming:** `[SOURCE-LANG]-[TARGET-LANG]-[LEGISLATION-NAME]-[SEGMENT].json`
- `NL-EN-civil-procedure-all.json` - Complete code
- `NL-EN-civil-procedure-book1.json` - Book 1 only
- `NL-EN-example-sentences.json` - Book 1 sentence-level (for linguistic analysis)

**Note:** The "example sentences" file contains Book 1 of the Civil Procedure Code split at the sentence level rather than paragraph level. This is useful for:
- Linguistic research and analysis
- Translation memory systems
- Fine-grained term extraction
- Natural language processing

### Reports (`reports/`)

Quality assurance and metrics:
- Translation completeness reports
- SME review status
- Coverage statistics
- Consistency checks

## Jurisdictions

### Netherlands (`netherlands/`)

**Legal System:** Dutch civil law (Continental European tradition)
**Primary Language:** Dutch (Nederlands, nl-NL)
**Geographic Scope:** Kingdom of the Netherlands (European territory)

**Current Content:**
- 8 dictionaries/glossaries (~3,400+ terms)
- Complete Code of Civil Procedure (3,118 segments)
- Multiple translation pairs (EN, FR, DE, ES)
- Sentence-level segmentation for linguistic research

**See:** `netherlands/README.md` for details

### France (`france/`)

**Legal System:** French civil law (Code civil)
**Primary Language:** French (Français, fr-FR)
**Geographic Scope:** French Republic

**Status:** Directory prepared for future content

**Planned Content:**
- French monolingual legal dictionaries
- Code civil (Civil Code)
- Code de procédure civile (Code of Civil Procedure)
- Administrative law glossaries

**See:** `france/README.md` for details

## File Naming Conventions

All files follow consistent naming patterns:

### Language Codes
ISO 639-1 (language) + ISO 3166-1 (country), lowercase:
- `nl-nl` - Dutch (Netherlands)
- `en-gb` - English (British, for legal English)
- `fr-fr` - French (France)
- `de-de` - German (Germany)
- `es-es` - Spanish (Spain)

### Dictionary Files
`[SOURCE-LANG]-[TARGET-LANG]-[TYPE].json`

Examples:
- `NL-EN-legal-dictionary.json`
- `NL-legal-dictionary.json` (monolingual, implicit NL-NL)
- `FR-FR-legal-dictionary.json`

### Legislation Files
`[SOURCE-LANG]-[TARGET-LANG]-[LEGISLATION]-[SEGMENT].json`

Examples:
- `NL-EN-civil-procedure-all.json`
- `NL-EN-civil-procedure-book1.json`
- `NL-EN-example-sentences.json` (Book 1 sentence-level)

## Data Format

All JSON files follow the unified dictionary structure documented in:
- `/UNIFIED-DATABASE-STRUCTURE.md`
- `/dictionary-structure-proposal.md`

Each entry includes:
- Term and translation
- Definitions (where applicable)
- Source attribution
- License information
- SME review status
- Metadata (frequency, domain, related terms)

## Licenses

All content is provided under open licenses:
- **CC BY 4.0** - Creative Commons Attribution (most content)
- **CC0** - Public Domain (government sources)
- **Licence Ouverte 2.0** - French open data license
- **CC BY-NC 4.0** - Non-commercial (some example sentences)

See `/authors-licenses.html` for complete attribution and licensing details.

## Usage in Website

These files are used by:
- **`index.html`** - Main dictionary interface (loads unified-dictionary.json)
- **`legislation.html`** - Legislation browser (loads civil procedure files)
- **Import scripts** - Data processing and quality assurance

## Adding New Content

### Adding a New Jurisdiction

1. Create directory structure:
   ```bash
   mkdir -p legal-data/[jurisdiction]/{dictionaries,legislation,reports}
   ```

2. Add README documenting legal system, sources, licenses

3. Add dictionary/legislation files following naming conventions

4. Update this main README

### Adding New Legislation

1. Create subdirectory in `legislation/`:
   ```bash
   mkdir legal-data/[jurisdiction]/legislation/[legal-domain]
   ```

2. Add translated files with proper segmentation

3. Update jurisdiction README

### Adding New Dictionaries

1. Place in appropriate `dictionaries/` folder

2. Follow naming conventions

3. Include source attribution and licensing

## Migration History

- **2025-11-09 (v2):** Restructured into content-type subfolders (dictionaries, legislation, reports)
- **2025-11-09 (v1):** Restructured from flat `/i8n/` to jurisdiction-based `/legal-data/`
- **Previous structure:** `/i8n/NL-EN-*.json` (language-pair prefixed files)
- **Reason:** Better scalability, clearer legal context, professional organization

### Path Changes

```
OLD: i8n/NL-EN-legal-dictionary.json
NEW: legal-data/netherlands/dictionaries/NL-EN-legal-dictionary.json

OLD: i8n/NL-EN-civil-procedure-all.json
NEW: legal-data/netherlands/legislation/civil-procedure/NL-EN-civil-procedure-all.json

OLD: i8n/NL-EN-example-sentences.json
NEW: legal-data/netherlands/legislation/civil-procedure/NL-EN-example-sentences.json
```

## Future Jurisdictions

Planned additions:
- **Belgium** - Belgian law (Dutch, French, German versions)
- **Luxembourg** - Luxembourg law (French, German, Luxembourgish)
- **Germany** - German law (Bürgerliches Gesetzbuch, etc.)
- **European Union** - EU directives, regulations, ECJ decisions

## Contributing

To contribute:
1. Choose appropriate jurisdiction and content type
2. Follow naming conventions and data structure
3. Include proper attribution and licensing
4. Update relevant README files
5. See `/CONTRIBUTING.md` for detailed guidelines

## Questions or Suggestions?

Please open an issue on GitHub or contact the maintainers.

---

**Project:** Legislation Library Translation Dictionary
**Repository:** https://github.com/KingOfTheAce2/legislation-library-translation-dictionary
**License:** Various open licenses (CC BY 4.0, CC0, see individual files)
**Maintained by:** Legal translation community
