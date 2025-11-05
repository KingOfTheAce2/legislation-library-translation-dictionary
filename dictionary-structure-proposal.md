# Proposed Enhanced Dictionary Structure

## Goal
Merge translation glossary + dictionary definitions + example sentences with proper licensing tiers.

## Current Structure (619 entries)
```json
{
  "source": "aanbrengen (een geschil bij de rechter)",
  "lang-source": "nl-nl",
  "target": "to seise the court of a dispute",
  "lang-target": "en-gb",
  "author": "Burrough/Machon/Oranje/Frakes/Visser",
  "license": "CC BY 4.0",
  "sme-reviewed": "yes"
}
```

## Enhanced Structure (Proposal)
```json
{
  "id": "term_001",
  "source": "aanbrengen (een geschil bij de rechter)",
  "lang-source": "nl-nl",
  "target": "to seise the court of a dispute",
  "lang-target": "en-gb",

  "definition": {
    "en-gb": "To formally submit a dispute to the court's jurisdiction for resolution; to initiate legal proceedings.",
    "license": "CC BY 4.0",
    "source": "Dutch Civil Procedure Dictionary"
  },

  "author": "Burrough/Machon/Oranje/Frakes/Visser",
  "license": "CC BY 4.0",
  "sme-reviewed": "yes",

  "examples": [
    {
      "id": "ex_001_001",
      "nl": "De zaak is aanhangig gemaakt bij de rechtbank Rotterdam.",
      "en": "The case was brought before the Rotterdam District Court.",
      "license": "CC BY-NC 4.0",
      "source": "Dutch Civil Procedure Textbook, Chapter 3",
      "premium": false,
      "verified": true
    },
    {
      "id": "ex_001_002",
      "nl": "Partijen hebben het geschil bij de rechter aangebracht conform artikel 111 Rv.",
      "en": "The parties have seised the court of the dispute in accordance with Article 111 of the Dutch Code of Civil Procedure.",
      "license": "Proprietary",
      "source": "Professional Legal Translation Database",
      "premium": true,
      "verified": true
    }
  ],

  "related-terms": ["rechtspraak", "procesrecht", "dagvaarding"],
  "articles": ["Rv 111", "Rv 96"],
  "usage-notes": "Formal legal term used in procedural contexts"
}
```

## Licensing Strategy

### Open Access (Free Tier)
- **CC BY 4.0**: Full commercial use allowed
- **CC BY-NC 4.0**: Non-commercial use only
- All base translations and definitions
- 1-2 example sentences per term

### Premium (Paid Tier)
- **Proprietary examples**: Your own professional translations
- **Extended examples**: 5-10 examples per term
- **Context-rich examples**: Court documents, contracts, etc.
- **Audio pronunciations** (future)
- **Usage notes** and best practices

## Implementation Phases

### Phase 1: Merge Dictionaries (Current Priority)
- [ ] Import second dictionary with `lang-target-dict`
- [ ] Merge with existing glossary
- [ ] Add `definition` field to all entries
- [ ] Maintain backward compatibility

### Phase 2: Add Example Sentences
- [ ] Create examples data structure
- [ ] Add 1-2 CC BY-NC examples per term (free)
- [ ] Add proprietary examples (premium)
- [ ] Build UI to display examples (Linguee-style)

### Phase 3: Premium Gating
- [ ] Implement "Show Premium Examples" buttons
- [ ] Gate proprietary content behind paywall
- [ ] Add "Unlock" modals
- [ ] Track example views (analytics)

### Phase 4: Advanced Features
- [ ] Related terms linking
- [ ] Article references (link to legal code)
- [ ] Usage notes and context
- [ ] Search within examples
- [ ] Pronunciation guides

## UI Design (Linguee-inspired)

```
┌──────────────────────────────────────────────────────┐
│ aanhangig                                       [NL] │
├──────────────────────────────────────────────────────┤
│                                                       │
│ TRANSLATION                                          │
│ → pending                                   [EN-GB]  │
│                                                       │
│ DICTIONARY DEFINITION                                │
│ awaiting decision or settlement in legal             │
│ proceedings; not yet resolved                        │
│                                                       │
│ EXAMPLES (2 free, 5 premium)                         │
│                                                       │
│ ✓ FREE - CC BY-NC 4.0                               │
│ ┌────────────────────────────────────────────────┐  │
│ │ NL: De zaak is nog aanhangig bij de rechtbank. │  │
│ │ EN: The case is still pending before the court.│  │
│ │ Source: Civil Procedure Textbook               │  │
│ └────────────────────────────────────────────────┘  │
│                                                       │
│ 🔒 PREMIUM - 5 more examples                         │
│ ┌────────────────────────────────────────────────┐  │
│ │ NL: Tijdens de aanhangige procedure...         │  │
│ │ EN: [Unlock to view] 👉 Upgrade to Pro         │  │
│ └────────────────────────────────────────────────┘  │
│                                                       │
│ [Show Premium Examples - $19/mo]                     │
│                                                       │
│ RELATED TERMS                                         │
│ rechtspraak | procesrecht | dagvaarding              │
│                                                       │
│ LEGAL REFERENCES                                      │
│ Rv Art. 111 | Rv Art. 96                             │
│                                                       │
│ ✓ SME Reviewed | Authors: Burrough et al.            │
└──────────────────────────────────────────────────────┘
```

## Technical Implementation

### Data Files
- `dictionary-main.json` - Main merged dictionary
- `examples-free.json` - CC BY-NC 4.0 examples (bundled)
- `examples-premium.json` - Proprietary examples (API only)

### API Endpoints
```
GET /dictionary-main.json          # Free tier
GET /api/term/:id                   # Free tier (includes free examples)
GET /api/term/:id/examples/premium  # Premium tier (requires auth)
GET /api/search?q=pending           # Free tier
```

## Next Steps

1. **Upload your second dictionary file** with `lang-target-dict` field
2. **Provide sample example sentences** (if you have them)
3. **Clarify licensing**:
   - Which examples are CC BY-NC 4.0?
   - Which examples are proprietary?
   - Do you have examples ready, or should we create the structure first?

4. **Review this proposal** and let me know what to adjust

Once you upload the files, I'll:
- Parse and merge the dictionaries
- Build the enhanced UI
- Implement the premium gating
- Create the example sentences system
