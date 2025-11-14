# ⚖️ International Legal Dictionary & Legislation Library

**A global open-access legal terminology resource** for **lawyers**, **tax professionals**, **legal translators**, and **researchers** worldwide.

**[📖 View the Dictionary](https://kingoftheace2.github.io/legislation-library-translation-dictionary/)**
**[📜 View Legislation Library](https://kingoftheace2.github.io/legislation-library-translation-dictionary/legislation.html)**
**[📜 Authors & Licenses](https://kingoftheace2.github.io/legislation-library-translation-dictionary/authors-licenses.html)**

## 🌍 International Scope

This project provides **verified open-access legal terminology** from jurisdictions worldwide:

- **Current Implementation:** Netherlands legal terminology and Code of Civil Procedure (3,400+ terms, 3,118 translation segments)
- **Research Completed:** 33 verified open-data sources covering **80+ languages** across Europe, Americas, Asia, Africa, and Middle East
- **Estimated Global Capacity:** 808,000-1,193,000 legal terms from international sources ready for integration

### 📍 Jurisdiction-Specific Content

**Netherlands (Current Implementation):**
All current dictionary terms and legislation are specific to **Dutch law as applied in the Netherlands** (nl-NL), even when displayed in other languages. This content is NOT applicable to Dutch law in Belgium, Suriname, or other Dutch-speaking jurisdictions.

**Future Jurisdictions (Research Phase):**
See [OPEN-DATA-LEGAL-SOURCES-VERIFIED.md](OPEN-DATA-LEGAL-SOURCES-VERIFIED.md) for researched sources covering EU, Switzerland, France, UK, USA, Canada, Japan, South Korea, South Africa (11 languages), India (22+ languages), and 50+ other jurisdictions.

## 📊 Overview

**Current Implementation (Netherlands):**
- **3,400+ professional legal terms** (Netherlands law) - Subject Matter Expert reviewed
- **3,118 legislation translation segments** - Complete Dutch Code of Civil Procedure
- **Multilingual support** (NL ↔ EN, FR, DE, ES)
- **Monolingual dictionaries** (NL-NL Dutch legal definitions, FR-FR French legal definitions)
- **Authoritative sources:** Raad van de Rechtspraak (Dutch Judiciary), Dutch Ministry of Finance, business.gov.nl, legal translation experts

**Research Completed (Global Expansion):**
- **33 verified open-data sources** across 80+ languages
- **808,000-1,193,000 estimated terms** from international jurisdictions
- **Geographic coverage:** Europe (11 sources), Americas & International (12 sources), Asia-Pacific (7 sources), Africa & Middle East (5 sources)
- **All open licenses:** CC BY 4.0, CC0, CC BY-NC-SA, OGL v3.0, Apache 2.0, Public Domain
- **Source provenance:** Each source includes jurisdiction, license, and SME review status

## ✨ Features

### 📚 Two Complementary Resources

#### 🔍 Legal Dictionary
- **Multilingual search**: Search in Dutch, English, French, German, or Spanish
- **3,400+ professional legal terms** with Subject Matter Expert review
- **Real-time filtering**: Instant results as you type
- **Translation dictionaries** (bilingual NL ↔ EN/FR/DE/ES)
- **Monolingual dictionaries** for in-depth explanations:
  - **Dutch Legal Dictionary (NL-NL)**: 1,500+ terms with definitions in Dutch
  - **French Legal Dictionary (FR-FR)**: 495 terms with definitions in French
- **Multiple authoritative sources** with proper attribution
- **Comprehensive definitions** and contextual usage

#### 📜 Legislation Library
- **Complete legislation translations**: Dutch Code of Civil Procedure - All Books (NL-EN)
- **3,118 optimized translation segments** professionally translated (originally 4,252, merged for readability)
  - Complete coverage: Books 1, 2-3, and 4
  - Article numbers integrated with text for better readability
  - Formatted like official wetten.overheid.nl
- **Side-by-side viewing**: Compare Dutch and English texts
- **Full-text search**: Find specific articles and provisions
- **Book filtering**: View individual books or complete code
- **Based on official text**: Synchronized with wetten.overheid.nl

### 📱 User Experience
- **Responsive design**: Works on desktop, tablet, and mobile
- **Clean interface**: Focus on the content
- **Fast & lightweight**: No external dependencies
- **Offline capable**: Works without internet after first load

### 🎯 Professional Quality
- All terms and translations reviewed by Subject Matter Experts
- Proper linguistic attribution
- Clear source and target language markers
- Professional translation by legal experts

## 🚀 Quick Start

### View Online
- **Legal Dictionary**: `https://kingoftheace2.github.io/legislation-library-translation-dictionary/`
- **Legislation Library**: `https://kingoftheace2.github.io/legislation-library-translation-dictionary/legislation.html`

### Use Locally
```bash
# Clone the repository
git clone https://github.com/kingoftheace2/legislation-library-translation-dictionary.git

# Open in browser
open index.html              # For legal dictionary
open legislation.html        # For legislation library
```

No build process required - it's pure HTML/CSS/JS!

## 📖 Usage Examples

### For Lawyers & Tax Professionals (Primary Use Case)
- **Primary Resource**: Professional legal dictionary and legislation for Netherlands law practice
- **Dictionary**: Quick reference for Dutch legal terms with expert-reviewed translations
- **Legislation**: Complete bilingual Code of Civil Procedure for case research and citations
- **Monolingual Dictionary**: In-depth Dutch legal definitions (NL-NL) for precise understanding
- Standardize terminology across your practice and documents
- Access authoritative sources (Dutch Judiciary, Ministry of Finance)
- Cross-reference between dictionary and legislation

### For Legal Translators (Secondary Use Case)
- **Secondary Resource**: Professional reference guide for legal translation work
- **Dictionary**: Expert-reviewed translations across NL, EN, FR, DE, ES
- **Legislation**: See how legal professionals translate complex procedural law
- Quality assurance and terminology consistency checking
- Full context with complete legislative provisions
- Multiple sources for comparison and validation

### For Students & Researchers
- **Dictionary**: Learn Dutch legal terminology across multiple domains
- **Legislation**: Study Dutch civil procedure with English translations
- Compare legal concepts across jurisdictions
- Academic research on comparative law
- Access to open-licensed legal terminology and translations

## 🗂️ Data Structure

The project uses structured JSON formats for different content types:

### Dictionary - Bilingual Translation Entries
```json
{
  "source": "aanhangig",
  "lang-source": "nl-nl",
  "target": "pending",
  "lang-target": "en-gb",
  "lang-target-dict": "A case is pending when it has been filed with the court",
  "author": "Burrough/Machon/Oranje/Frakes/Visser",
  "license": "CC BY 4.0",
  "sme-reviewed": true,
  "premium": false
}
```

### Dictionary - Monolingual Dictionary Entries
```json
{
  "source": "baldadigheid",
  "lang-source": "nl-nl",
  "lang-source-dict": "Strafbare overtreding wanneer er gevaar of nadeel voor goederen of personen in de openbare ruimte wordt veroorzaakt...",
  "author": "Raad van de Rechtspraak",
  "license": "CC0",
  "sme-reviewed": true,
  "premium": false
}
```

### Legislation - Translation Segments
```json
{
  "tuid": "0000002",
  "source": "Wetboek van Burgerlijke Rechtsvordering",
  "target": "Code of Civil Procedure",
  "lang-source": "nl-nl",
  "lang-target": "en-gb",
  "author": "Burrough/Machon/Oranje/Frakes/Visser",
  "license": "CC BY 4.0",
  "sme-reviewed": true,
  "premium": false,
  "type": "legislation",
  "document": "Wetboek van Burgerlijke Rechtsvordering - Book 1"
}
```

### Fields
- **source**: Original term or text
- **target**: Translation (for bilingual entries)
- **lang-source**: Source language code (nl-nl, en-gb, etc.)
- **lang-target**: Target language code (for bilingual entries)
- **lang-source-dict**: Definition in source language (for monolingual entries)
- **lang-target-dict**: Definition in target language (optional)
- **author**: Author(s)/source organization
- **license**: Usage license (CC BY 4.0, CC0)
- **sme-reviewed**: Subject Matter Expert review status (boolean)
- **premium**: Premium content flag (boolean)
- **tuid**: Translation unit ID (for legislation entries)
- **type**: Content type ("legislation" for legislation entries)
- **document**: Source document name (for legislation entries)

## 📜 License & Attribution

### License
This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

You are free to:
- **Share**: Copy and redistribute in any format
- **Adapt**: Remix, transform, and build upon the material
- **Commercial use**: Use for commercial purposes

Under these terms:
- **Attribution**: Give appropriate credit to the authors

### Authors & Sources

**For complete details, see:** [Authors & Licenses Page](https://kingoftheace2.github.io/legislation-library-translation-dictionary/authors-licenses.html)

**Translation Dictionaries (Bilingual):**
- **Civil Procedure Glossary (NL↔EN)**: Burrough / Machon / Oranje / Frakes / Visser - CC BY 4.0
- **Ministry of Finance Legal Glossary**: Dutch Ministry of Finance - CC0
- **Business Law Dictionary**: business.gov.nl - CC0
- **Multilingual Glossaries (FR/DE/ES)**: Various Subject Matter Experts - CC BY 4.0 / CC0

**Monolingual Dictionaries:**
- **Dutch Legal Dictionary (NL-NL)**: Raad van de Rechtspraak (Dutch Judiciary) - CC0
- **French Legal Dictionary (FR-FR)**: Ministère de la Justice (France) - Licence Ouverte 2.0

**Legislation Translations:**
- **Code of Civil Procedure**: Burrough / Machon / Oranje / Frakes / Visser - CC BY 4.0

### Citation
```
Legislation Library Translation Dictionary. (2025).
Multilingual Legal Dictionary & Translation Library.
Legislation Library Translation Project.
Licensed under CC BY 4.0 and CC0.
Available at: https://github.com/kingoftheace2/legislation-library-translation-dictionary
```

## 💡 Contributing

This is an open-access project. Contributions are welcome!

### How to Contribute
1. **Report issues**: Found an error? Open an issue
2. **Suggest terms**: Missing important terms? Let us know
3. **Improve translations**: Better translation? Submit a PR
4. **Enhance the website**: Code improvements welcome

### Contribution Guidelines
- Maintain Subject Matter Expert review standards
- Provide context for specialized terms
- Follow the existing JSON structure
- Include source attribution
- Specify appropriate license (CC BY 4.0 or CC0)
- Mark Subject Matter Expert review status accurately

## 🎯 Roadmap

### Current Version (v2.1)
- ✅ 650+ professional legal terms
- ✅ 3,118 optimized legislation translation segments (Complete Code of Civil Procedure)
  - ✅ Covers all Books (1, 2-3, 4) comprehensively
  - ✅ Article numbers merged with text for readability
  - ✅ Professional formatting matching wetten.overheid.nl
- ✅ 64 new glossary terms extracted from legislation (ready for curation)
- ✅ Multilingual support (NL, EN, FR, DE, ES)
- ✅ Monolingual Dutch dictionary with comprehensive definitions
- ✅ Bilingual legislation browser (wetten.overheid.nl-style)
- ✅ Book filtering and navigation
- ✅ Responsive web interface
- ✅ Subject Matter Expert-reviewed content
- ✅ Multiple licenses (CC BY 4.0, CC0)

### Future Plans

**Phase 1: Infrastructure (Next)**
- 📊 Source attribution system - Track jurisdiction and license for each term
- 🏷️ SME review workflow - Flag terms requiring expert verification
- 🌐 Multi-jurisdiction database structure - Support terms from multiple legal systems
- 🔍 Advanced filtering - Search by jurisdiction, language pair, legal domain

**Phase 2: International Content Integration**
- 🇪🇺 EUR-Lex integration - 50,000-100,000 EU legal terms (24 languages)
- 🇨🇭 Swiss Federal Supreme Court - 40,000-60,000 terms (DE, FR, IT)
- 🇿🇦 South Africa Constitution - 30,000+ terms (11 official languages)
- 🇮🇳 India Constitution - 60,000+ terms (22+ languages)
- 🌍 UN Parallel Corpus - 30,000-50,000 international law terms (6 UN languages)

**Phase 3: Advanced Features**
- 📝 Additional Netherlands legislation (Criminal Code, Civil Code)
- 🔗 Cross-reference links between dictionary and legislation
- 📑 Article number indexing and navigation
- 🔊 Audio pronunciation guides
- 💾 Enhanced export functionality (PDF, CSV, XML)
- 🔌 API access for developers
- 🤖 Integration with translation tools

## 💰 Support This Project

This dictionary is **free and open-access**. If you find it valuable:

- ☕ **[Support with a donation](#)** _(Add your link: Ko-fi, Buy Me a Coffee, Patreon)_
- ⭐ **Star this repository** to increase visibility
- 📢 **Share with colleagues** in legal profession
- 🤝 **Contribute improvements** via pull requests
- 🏢 **Institutional support**: Contact for sponsorship opportunities

### Monetization Options
While maintaining open access, consider:
- **Freemium**: Premium features (bulk export, API) for paid users
- **Institutional licenses**: Law firms get priority support
- **Consulting**: Professional translation services
- **Training**: Workshops on legal translation

## 🛠️ Technical Details

### Technology Stack
- **Frontend**: Pure HTML5, CSS3, JavaScript (ES6+)
- **Hosting**: GitHub Pages
- **Data**: JSON format
- **No dependencies**: Works without external libraries
- **No build process**: Edit and deploy instantly

### Browser Support
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

### Performance
- ⚡ Loads in < 1 second
- 📦 Total size: ~155 KB
- 🔍 Search results: < 50ms
- 📱 Mobile-optimized

## 📞 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/kingoftheace2/legislation-library-translation-dictionary/issues)
- **Discussions**: [GitHub Discussions](https://github.com/kingoftheace2/legislation-library-translation-dictionary/discussions)
- **Repository**: [GitHub Repo](https://github.com/kingoftheace2/legislation-library-translation-dictionary)

## 🏛️ Related Projects

Part of the **Legislation Library Translation Project** - making legal texts accessible across language barriers.

### Related Resources
- [Wetboek van Burgerlijke Rechtsvordering](https://wetten.overheid.nl/BWBR0001827/) (Official Dutch text)
- [Dutch Civil Law in English](https://www.dutchcivillaw.com/)
- [Rechtspraak.nl](https://www.rechtspraak.nl/) (Dutch judiciary)

## 🙏 Acknowledgments

- **Civil Procedure Authors**: Burrough, Machon, Oranje, Frakes, Visser
- **Raad van de Rechtspraak**: For providing comprehensive legal terminology
- **Subject Matter Expert Reviewers**: Legal professionals who validated the content
- **business.gov.nl**: For business law terminology
- **Community**: All contributors and users providing feedback

---

**Made with ⚖️ for the legal community** | [Report an Issue](https://github.com/kingoftheace2/legislation-library-translation-dictionary/issues) | [View Repository](https://github.com/kingoftheace2/legislation-library-translation-dictionary)
