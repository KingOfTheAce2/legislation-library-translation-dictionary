# ⚖️ Multilingual Legal Dictionary & Legislation Library

A professional multilingual legal translation resource covering Dutch legal terminology and complete legislation translations.

**[📖 View the Dictionary](https://kingoftheace2.github.io/legislation-library-translation-dictionary/)**
**[📜 View Legislation Library](https://kingoftheace2.github.io/legislation-library-translation-dictionary/legislation.html)**

## 📊 Overview

- **650+ professional legal terms** across multiple domains
- **3,118 legislation translation segments** - Dutch Code of Civil Procedure (Complete, optimized)
- **Subject Matter Expert reviewed** by legal professionals
- **Multilingual support** (NL ↔ EN, FR, DE, ES, and monolingual NL)
- **Open licenses** (CC BY 4.0, CC0) - free and open access
- **Multiple sources:** Raad van de Rechtspraak, legal experts, and professional translators

## ✨ Features

### 📚 Two Complementary Resources

#### 🔍 Legal Dictionary
- **Multilingual search**: Search in Dutch, English, French, German, or Spanish
- **650+ professional legal terms** with Subject Matter Expert review
- **Real-time filtering**: Instant results as you type
- **Contextual translations** and comprehensive definitions
- **Monolingual dictionary** for in-depth term explanations

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

### For Legal Professionals
- **Dictionary**: Translate Dutch legal documents across multiple languages
- **Legislation**: Reference bilingual Code of Civil Procedure provisions
- Understand Dutch legal terms with comprehensive definitions
- Standardize translations across your practice
- Access subject matter expert-reviewed terminology

### For Translators
- **Dictionary**: Reference guide for legal translation work across NL, EN, FR, DE, ES
- **Legislation**: See how legal professionals translate procedural law
- Quality assurance for legal translations
- Terminology consistency checking
- Full context with complete legislative provisions

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
- **Civil Procedure Terms**: Burrough / Machon / Oranje / Frakes / Visser
- **Monolingual Dutch Dictionary**: Raad van de Rechtspraak (Dutch Judiciary)
- **Business Terms**: business.gov.nl
- **Additional translations**: Various Subject Matter Experts

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
- 📝 Expand to other Dutch legislation (Criminal Code, Civil Code, etc.)
- 🔗 Cross-reference links between dictionary and legislation
- 🌐 Add more language pairs for legislation
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
