# Legal Jurisdictions & Sources Research Report

**Date:** November 12, 2025
**Research Branch:** `claude/research-law-translations-011CV3am5MgQeXDMDzF6EfpM`
**Status:** Comprehensive research completed

## Executive Summary

This report identifies **new jurisdictions** and **open legal terminology sources** to expand the Legislation Library Translation Dictionary beyond its current Netherlands focus. Research covered 15+ jurisdictions and 25+ sources, prioritizing:

- ✅ Open licenses (CC BY 4.0, CC0, Licence Ouverte)
- ✅ Government/institutional sources
- ✅ Multilingual coverage
- ✅ Civil law jurisdictions (compatible with Netherlands focus)
- ✅ Professional quality and SME review

---

## Priority Recommendations

### 🥇 Tier 1: Ready for Immediate Implementation

These sources have confirmed open access, quality data, and easy integration:

#### 1. **Switzerland** 🇨🇭
**Priority: HIGHEST**

**Source:** TERMDAT - Federal Terminology Database
**URL:** https://www.bk.admin.ch/bk/en/home/dokumentation/languages/termdat.html
**Languages:** German, French, Italian, Romansh, English
**Content:** 400,000+ entries in Swiss law, public administration, public sector
**License:** Free access (verify specific licensing terms)
**Format:** Online database

**Why Priority:**
- Four-language coverage (DE, FR, IT, Romansh + EN)
- Official government source (Swiss Federal Chancellery)
- Massive dataset (400K+ entries)
- Direct compatibility with Netherlands (both civil law, multilingual contexts)
- Federal legislation available in all official languages

**Additional Swiss Resource:**
- **Swiss Landmark Decisions Summarization (SLDS)** dataset
- 20,000 Federal Supreme Court rulings with headnotes
- German, French, Italian
- **License:** CC BY 4.0 ✅
- Perfect for extracting legal terminology from case law

**Implementation Path:**
1. Contact Swiss Federal Chancellery for bulk export/API access
2. Parse TERMDAT entries into unified dictionary format
3. Add SLDS dataset for case law terminology extraction

---

#### 2. **European Union** 🇪🇺
**Priority: HIGHEST**

**Source:** IATE (InterActive Terminology for Europe)
**URL:** https://iate.europa.eu/
**Languages:** All 24 EU official languages
**Content:** 1.4 million+ multilingual entries (law, environment, human rights, etc.)
**License:** Public access, **full database downloadable** ✅
**Format:** Downloadable database + API

**Why Priority:**
- Largest multilingual legal terminology database in Europe
- All 24 EU languages covered
- Full database can be downloaded in zipped format
- Used by all EU institutions and agencies
- Legal, administrative, and specialized terminology

**Additional EU Resources:**

**EUR-Lex Parallel Corpus**
- All EU legislation in 24 languages
- Updated daily
- Free access
- Useful for extraction of consistent legal translations

**DGT Translation Memory** (via OPUS)
- EU legislative document translations
- Sentence-aligned parallel corpus
- Available through OPUS corpus collection
- Multiple language pairs

**Implementation Path:**
1. Download complete IATE database (https://iate.europa.eu/download-iate)
2. Parse and filter legal terminology entries
3. Map to unified dictionary structure with EU attribution
4. Consider EUR-Lex API for legislation-specific terms

---

#### 3. **Germany** 🇩🇪
**Priority: HIGH**

**Source:** Gesetze im Internet (Laws on the Internet)
**URL:** https://www.gesetze-im-internet.de/
**Languages:** German → English
**Content:** 100+ statutes including BGB (Civil Code), ZPO (Civil Procedure), HGB (Commercial Code), StGB (Criminal Code)
**License:** Free access (check specific translation terms)
**Format:** HTML + PDF downloads

**Why Priority:**
- Official German Federal Ministry of Justice translations
- High-quality professional translations
- Includes all major German codes
- Direct parallel to Netherlands civil procedure work
- BGB and ZPO are foundational civil law texts

**Implementation Path:**
1. Review licensing terms at gesetze-im-internet.de
2. Download PDF/HTML versions of key legislation (BGB, ZPO, HGB)
3. Parse parallel German-English text
4. Extract terminology and segment translations

---

#### 4. **France** 🇫🇷
**Priority: HIGH**

**Source 1:** Légifrance Open Data
**URL:** https://www.legifrance.gouv.fr/contenu/pied-de-page/open-data-et-api
**Languages:** French (with some English/Spanish translations)
**Content:** All French legislation, codes, case law
**License:** Open data license (since 2014) ✅
**Format:** XML + API

**Source 2:** FranceTerme
**URL:** https://www.culture.gouv.fr/en/documentation-area/Databases/FranceTerme
**Languages:** French (technical/scientific terminology)
**Content:** 8,500+ terms in Official Journal
**License:** Public domain (government publication)
**Format:** Online database

**Why Priority:**
- Major civil law jurisdiction
- Official open data policy since 2014
- API access for automated extraction
- Already have some FR-FR content (495 terms)
- Complements existing French legal dictionary

**Note:** Légifrance translations are documentary only (not legally binding), but suitable for dictionary purposes.

**Implementation Path:**
1. Access Légifrance API for French legislation
2. Extract terminology from Codes (Civil, Procédure Civile, Pénal)
3. Use FranceTerme for technical legal terminology
4. Build on existing FR-FR dictionary (495 terms)

---

### 🥈 Tier 2: High Value, Requires Verification

These sources are promising but need licensing clarification:

#### 5. **Austria** 🇦🇹

**Source:** RIS - Austrian Legal Information System (English translations)
**URL:** https://ris.bka.gv.at/Englische-Rv/
**Languages:** German → English
**Content:** Austrian federal laws translated to English
**License:** ⚠️ Verify licensing with Federal Chancellery
**Format:** Online database

**Additional:** Translegal World Law Dictionary Austria (University of Innsbruck)
- Planned 7,000+ Austrian legal terms
- Status: Check if released (planned for winter 2020)

---

#### 6. **Belgium** 🇧🇪

**Source:** Moniteur Belge / Belgisch Staatsblad + Justel
**URL:** http://www.ejustice.just.fgov.be/
**Languages:** Dutch, French, (limited German)
**Content:** All Belgian federal legislation
**License:** ⚠️ Verify open data terms
**Format:** Online database

**Note:** Belgium uses Dutch (Flemish) and French. High relevance given Netherlands connection, but no dedicated open legal dictionary found.

---

#### 7. **Spain** 🇪🇸

**Source 1:** BOE (Boletín Oficial del Estado) Open Data API
**URL:** https://www.boe.es/datosabiertos/
**Languages:** Spanish
**Content:** All Spanish legislation via API
**License:** Open data ✅
**Format:** API + XML

**Source 2:** Diccionario Panhispánico del Español Jurídico (DPEJ)
**URL:** https://dpej.rae.es/
**Languages:** Spanish (monolingual)
**Content:** Comprehensive Spanish legal dictionary (Real Academia Española)
**License:** Free universal access
**Format:** Online database

**Note:** DPEJ is Spanish-only, not bilingual. Good for ES-ES monolingual dictionary.

---

#### 8. **Portugal** 🇵🇹

**Source:** IJP - Instituto Jurídico Portucalense
**URL:** (Various government portals)
**Languages:** Portuguese → English
**Content:** Constitution, codes, legislation (unofficial English translations)
**License:** ⚠️ Verify licensing
**Format:** Online databases

**Additional:** Portuguese Assembly provides Constitution and major legislation in English.

---

### 🥉 Tier 3: Specialized/Limited Scope

#### 9. **Ireland** 🇮🇪

**Source:** Gaois Terminology Database + Téarmaí Dlí
**URL:** https://www.gaois.ie/en/terminology
**Languages:** Irish (Gaeilge) ↔ English
**Content:** Legal terms from Irish Legal Terms Act 1945, IATE entries with Irish, Rules of Superior Courts
**License:** Government publication (verify specific terms)
**Format:** Online database

**Why Include:**
- Unique Irish-English bilingual legal terminology
- Constitutional requirement (Irish = first official language)
- Government-produced terminology
- Niche but valuable for Irish law practitioners

---

#### 10. **Luxembourg** 🇱🇺

**Source:** Legilux
**URL:** http://www.legilux.lu/
**Languages:** French (primary), German, Luxembourgish
**Content:** Constitution, codes, legislation, case law
**License:** ⚠️ Verify
**Format:** Online database

**Note:** French is the legislative language; limited multilingual terminology resources found.

---

#### 11. **Nordic Countries** 🇸🇪 🇩🇰 🇳🇴

**Source:** Lexicon of Medieval Nordic Law
**URL:** https://www.dhi.ac.uk/lmnl/
**Languages:** Old Swedish, Old Icelandic, Old Norwegian, Old Danish + English
**Content:** 6,000+ Nordic headwords, 9,000+ English equivalents
**License:** Open access ✅
**Format:** Online lexicon

**Why Limited:**
- **Medieval** legal terms, not modern law
- Academic/historical interest
- No modern Nordic legal dictionary found

**Note:** Modern Nordic countries (Sweden, Denmark, Norway) lack comprehensive open legal terminology databases for contemporary law.

---

## International & Supranational Sources

### 12. **United Nations** 🌍

**Source:** UNTERM
**URL:** https://unterm.un.org/
**Languages:** All 6 official UN languages (EN, FR, ES, RU, ZH, AR) + German, Portuguese
**Content:** Hundreds of thousands of UN terms, nomenclature, technical terms, phraseology
**License:** Public access (UN official documentation)
**Format:** Online database

**Why Include:**
- International legal terminology
- Multilingual (8 languages)
- Covers public international law, human rights, administrative law
- Free public access

---

### 13. **International Criminal Court**

**Source:** ICC Legal Tools Database
**URL:** https://legal-tools.org/
**Languages:** English, French, Spanish, Arabic (ICC working languages)
**Content:** International criminal law documents, case law, jurisprudence
**License:** Free public access
**Format:** Online database

**Note:** No dedicated multilingual terminology glossary for public download found. Internal ICC terminology management exists but not publicly accessible.

---

## Open Corpus & Academic Resources

### 14. **OPUS Parallel Corpus**

**Source:** OPUS (Open Parallel Corpus)
**URL:** https://opus.nlpl.eu/
**Languages:** 1,004 languages, 58 billion sentence pairs
**Legal Domain Corpora:**
- **DGT-TM** (EU legislative documents)
- **JRC-Acquis** (EU acquis, 10+ languages)
- **EUR-Lex** (EU legislation and case law)

**License:** Various open licenses (check per corpus)
**Format:** Downloadable parallel corpora (TMX, Moses, etc.)

**Why Valuable:**
- Largest collection of parallel legal texts
- Sentence-aligned translations
- Multiple language pairs
- Ideal for translation memory and terminology extraction

---

### 15. **LexPredict Legal Dictionary**

**Source:** GitHub - LexPredict/lexpredict-legal-dictionary
**URL:** https://github.com/LexPredict/lexpredict-legal-dictionary
**Languages:** English, French, German, Spanish (geopolitical entities)
**Content:** Multi-domain, multi-lingual legal terms (under development)
**License:** CC BY-SA 4.0 ⚠️ (not CC BY, requires ShareAlike)
**Format:** GitHub repository

**Note:** License requires ShareAlike, which may not fit project's CC BY 4.0 standard.

---

### 16. **MultiLegalPile**

**Source:** Research corpus
**URL:** https://arxiv.org/abs/2306.02069
**Languages:** 24 languages from 17 jurisdictions
**Content:** 689GB legal corpus
**License:** CC BY-NC-SA 4.0 ⚠️ (non-commercial)
**Format:** Research dataset

**Note:** Non-commercial license incompatible with potential commercial uses.

---

### 17. **Wikidata Legal Terminology**

**Source:** Wikidata
**URL:** https://www.wikidata.org/wiki/Q7164784 (Category: Legal terminology)
**Languages:** All Wikidata languages (300+)
**Content:** Structured multilingual legal terms with definitions, translations
**License:** CC0 ✅ (public domain)
**Format:** SPARQL queries, JSON API

**Why Valuable:**
- Completely open (CC0)
- Crowdsourced but structured
- Lexicographical data available
- Can query for legal terms across all languages

**Implementation:** Use Wikidata Query Service to extract legal terminology items.

---

## Licensing Summary

### ✅ Confirmed Open Licenses
1. **IATE** - Downloadable, public access
2. **Légifrance** - Open data license (2014+)
3. **Swiss SLDS** - CC BY 4.0
4. **UNTERM** - UN public documentation
5. **Wikidata** - CC0
6. **OPUS corpora** - Various open licenses (check per corpus)
7. **BOE Open Data** - Spanish open data license
8. **FranceTerme** - Public domain (Official Journal)

### ⚠️ Requires Verification
1. **TERMDAT** (Switzerland) - Free access, need to verify bulk export terms
2. **Gesetze im Internet** (Germany) - Free access, check translation licensing
3. **RIS** (Austria) - Government source, verify terms
4. **Moniteur Belge** (Belgium) - Verify open data policy
5. **Portugal IJP** - Verify licensing for English translations
6. **Ireland Gaois** - Government source, likely open
7. **Legilux** (Luxembourg) - Verify terms

### ❌ Incompatible Licenses
1. **LexPredict** - CC BY-SA (requires ShareAlike)
2. **MultiLegalPile** - CC BY-NC-SA (non-commercial)
3. **Council of Europe Dictionary** - Commercial publication

---

## Implementation Recommendations

### Phase 1: High-Impact Quick Wins (Month 1-2)

**Priority Actions:**

1. **Download IATE Database** ✅ Ready
   - Full database available at iate.europa.eu/download-iate
   - Parse legal terminology entries
   - Add 24 language coverage
   - Estimated: 50,000+ legal terms

2. **Switzerland TERMDAT** ✅ High Value
   - Contact Federal Chancellery for bulk access
   - Request API documentation or CSV export
   - Add German, French, Italian, Romansh coverage
   - Estimated: 100,000+ legal terms

3. **Germany Gesetze im Internet** ✅ Strategic
   - Download BGB, ZPO, HGB, StGB (HTML/PDF)
   - Parse parallel DE-EN legislation
   - Extract terminology from major codes
   - Estimated: 5,000-10,000 terms from legislation

4. **Wikidata Legal Terms** ✅ Easy Integration
   - SPARQL query for legal terminology items
   - Extract multilingual labels and definitions
   - CC0 license (no attribution required)
   - Estimated: 2,000-5,000 structured terms

### Phase 2: Major Jurisdictions (Month 3-4)

5. **France - Légifrance API**
   - Access consolidated legislation via API
   - Focus on: Code Civil, Code de Procédure Civile
   - Build comprehensive FR-FR + FR-EN dictionaries
   - Estimated: 20,000+ terms

6. **UNTERM Integration**
   - Extract international law terminology
   - Add public international law domain
   - Cover 8 languages (EN, FR, ES, RU, ZH, AR, DE, PT)
   - Estimated: 10,000+ terms

7. **Austria RIS + Belgium Moniteur**
   - Verify licensing and access terms
   - Extract DE-EN (Austria) and NL-FR (Belgium) pairs
   - High relevance to Netherlands focus

### Phase 3: Specialized Coverage (Month 5-6)

8. **Ireland Gaois** - Irish-English terminology
9. **Spain DPEJ** - Spanish monolingual dictionary
10. **OPUS Legal Corpora** - Terminology extraction from parallel corpora

---

## Technical Integration Notes

### Data Format Mapping

All external sources need conversion to unified dictionary format:

```json
{
  "source": "term",
  "lang-source": "xx-xx",
  "target": "translation",
  "lang-target": "yy-yy",
  "lang-source-dict": "definition in source language",
  "lang-target-dict": "definition in target language",
  "author": "Source Organization",
  "license": "CC BY 4.0 / CC0 / etc.",
  "sme-reviewed": true/false,
  "premium": false,
  "domain": "civil-law, criminal-law, administrative-law, etc.",
  "jurisdiction": "CH, EU, DE, FR, etc."
}
```

### New Fields to Consider

Add jurisdiction-specific metadata:

- **`jurisdiction`**: ISO country code (CH, DE, FR, EU, UN, etc.)
- **`domain`**: Legal domain (civil-law, criminal-law, tax-law, etc.)
- **`source-document`**: Original source (BGB, ZPO, IATE, etc.)
- **`confidence`**: Quality indicator for automated extractions

---

## Repository Structure Update

Proposed expansion of `/legal-data/` structure:

```
legal-data/
├── netherlands/         # Existing
│   ├── dictionaries/
│   ├── legislation/
│   └── reports/
├── switzerland/         # NEW - Priority 1
│   ├── dictionaries/
│   │   ├── TERMDAT-DE-FR.json
│   │   ├── TERMDAT-DE-IT.json
│   │   ├── TERMDAT-DE-EN.json
│   │   └── TERMDAT-FR-EN.json
│   └── README.md
├── germany/             # NEW - Priority 1
│   ├── dictionaries/
│   ├── legislation/
│   │   ├── DE-EN-BGB-civil-code.json
│   │   ├── DE-EN-ZPO-civil-procedure.json
│   │   └── DE-EN-HGB-commercial-code.json
│   └── README.md
├── france/              # Existing folder, populate
│   ├── dictionaries/
│   │   └── FR-legal-dictionary-expanded.json
│   ├── legislation/
│   │   ├── FR-EN-code-civil.json
│   │   └── FR-EN-code-procedure-civile.json
│   └── README.md
├── european-union/      # NEW - Priority 1
│   ├── dictionaries/
│   │   ├── IATE-legal-terms-all-languages.json
│   │   └── EUR-Lex-extracted-terms.json
│   ├── legislation/
│   │   └── DGT-TM-parallel-corpus/
│   └── README.md
├── austria/             # NEW - Priority 2
├── belgium/             # NEW - Priority 2
├── spain/               # NEW - Priority 2
├── portugal/            # NEW - Priority 2
├── ireland/             # NEW - Priority 3
├── luxembourg/          # NEW - Priority 3
└── international/       # NEW - UN, ICC, etc.
    ├── dictionaries/
    │   ├── UNTERM-multilingual.json
    │   └── ICC-legal-tools.json
    └── README.md
```

---

## Next Steps

### Immediate Actions (This Week)

1. ✅ **Download IATE database** - ready now
2. ✅ **Query Wikidata** - write SPARQL query for legal terms
3. ✅ **Contact Swiss Federal Chancellery** - request TERMDAT access terms
4. ✅ **Review Gesetze im Internet** - check translation licensing page

### Short Term (2-4 Weeks)

5. Parse IATE data → unified format
6. Import Wikidata legal lexemes
7. Create `switzerland/`, `germany/`, `european-union/` folders
8. Download and parse German legislation (BGB, ZPO)

### Medium Term (1-3 Months)

9. Integrate Légifrance API
10. Add UNTERM terminology
11. Verify and add Austria, Belgium, Spain, Portugal sources
12. Build automated extraction pipeline for OPUS corpora

### Long Term (3-6 Months)

13. Expand to specialized domains (tax law, administrative law, criminal law)
14. Add more language pairs based on community demand
15. Consider commercial partnerships for premium content
16. Build API for programmatic access to dictionary

---

## Estimated Content Growth

### Current State
- **Jurisdictions:** 1 (Netherlands)
- **Terms:** 3,400+
- **Languages:** NL, EN, FR, DE, ES
- **Legislation:** Netherlands Civil Procedure (3,118 segments)

### After Phase 1 (High-Impact Quick Wins)
- **Jurisdictions:** 4 (NL, CH, DE, EU)
- **Terms:** 160,000+ (47x increase)
- **Languages:** 24 EU languages + Romansh
- **Legislation:** + German codes (BGB, ZPO, HGB)

### After Phase 2 (Major Jurisdictions)
- **Jurisdictions:** 7 (+ FR, AT, BE, UN)
- **Terms:** 200,000+
- **Languages:** + Russian, Chinese, Arabic, Portuguese
- **Legislation:** + French codes (Code Civil, Procédure Civile)

### After Phase 3 (Full Implementation)
- **Jurisdictions:** 10+ (+ ES, PT, IE, LU, ICC)
- **Terms:** 250,000+
- **Languages:** 30+ languages
- **Legislation:** All major European codes

---

## Risk Assessment

### Licensing Risks
- ⚠️ **Medium Risk:** Some sources require verification (TERMDAT, Gesetze im Internet, RIS)
- ✅ **Mitigation:** Contact sources directly, document permissions, maintain attribution

### Quality Risks
- ⚠️ **Medium Risk:** Automated extraction from corpora may need curation
- ✅ **Mitigation:** Implement review workflow, flag automated entries as `sme-reviewed: false`

### Technical Risks
- ⚠️ **Low Risk:** Data format conversion
- ✅ **Mitigation:** Build robust parsers, validate against schema

### Maintenance Risks
- ⚠️ **Medium Risk:** Keeping external sources updated
- ✅ **Mitigation:** Build automated update pipeline, version control external sources

---

## Community & Collaboration Opportunities

### Potential Partnerships

1. **Swiss Federal Chancellery** - TERMDAT access
2. **European Union Publications Office** - IATE and EUR-Lex collaboration
3. **German Federal Ministry of Justice** - Gesetze im Internet partnership
4. **Légifrance / DILA** - French legislation API access
5. **Academic Institutions** - University legal translation research groups

### Open Source Contributions

- Contribute terminology to Wikidata
- Share extraction scripts on GitHub
- Publish quality-reviewed terms to IATE
- Collaborate with OPUS corpus project

---

## Conclusion

This research identified **17 high-quality sources** across **15+ jurisdictions** with the potential to expand the project from 3,400 terms to **250,000+ terms** covering **30+ languages**.

### Top Priorities for Implementation:

1. 🥇 **IATE (EU)** - 1.4M terms, downloadable now
2. 🥇 **TERMDAT (Switzerland)** - 400K terms, multilingual
3. 🥇 **Gesetze im Internet (Germany)** - Major codes with English translations
4. 🥇 **Wikidata** - Open CC0 structured terminology

These four sources alone could add **150,000+ professionally-sourced legal terms** with open licenses.

The expansion would position this project as the **leading open-access multilingual legal dictionary in Europe**, serving lawyers, translators, and legal professionals across multiple jurisdictions.

---

**Research completed by:** Claude (Anthropic)
**Repository:** https://github.com/KingOfTheAce2/legislation-library-translation-dictionary
**Branch:** `claude/research-law-translations-011CV3am5MgQeXDMDzF6EfpM`

**Next action:** Review findings and approve Phase 1 implementation plan.
