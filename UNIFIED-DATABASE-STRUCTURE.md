# Unified Database Structure

## Overview
This structure supports:
- Multiple translations from different sources
- Definitions when available
- Multiple example sentences with licensing
- Premium content gating
- Multi-source attribution

## File: `unified-dictionary.json`

```json
[
  {
    "id": "term_00001",
    "term": "aanhangig",
    "lang": "nl-nl",

    "translations": [
      {
        "translation": "pending",
        "lang": "en-gb",
        "definition": "awaiting decision or settlement in legal proceedings",
        "source": "Burrough/Machon/Oranje/Frakes/Visser",
        "source-type": "Civil Procedure Glossary",
        "license": "CC BY 4.0",
        "sme-reviewed": true,
        "context": "procedural law"
      },
      {
        "translation": "pending before the court",
        "lang": "en-gb",
        "definition": null,
        "source": "Dutch Ministry of Finance",
        "source-type": "Legal Glossary",
        "license": "CC0",
        "sme-reviewed": true,
        "context": "general legal"
      }
    ],

    "examples": [
      {
        "id": "ex_00001_001",
        "nl": "De zaak is nog aanhangig bij de rechtbank.",
        "en": "The case is still pending before the court.",
        "source": "Civil Procedure Textbook",
        "license": "CC BY-NC 4.0",
        "premium": false,
        "sme-reviewed": true,
        "context": "court proceedings"
      },
      {
        "id": "ex_00001_002",
        "nl": "Tijdens de aanhangige procedure mag de rechter...",
        "en": "During the pending proceedings, the court may...",
        "source": "Professional Translation Database",
        "license": "Proprietary",
        "premium": true,
        "sme-reviewed": true,
        "context": "procedural rights"
      }
    ],

    "metadata": {
      "frequency": "high",
      "domain": ["civil procedure", "court proceedings"],
      "related-terms": ["rechtspraak", "procesrecht", "dagvaarding"],
      "articles": ["Rv 111", "Rv 96"],
      "last-updated": "2024-11-05"
    }
  }
]
```

## Field Definitions

### Root Level
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes | Unique identifier (e.g., "term_00001") |
| `term` | string | Yes | The source term (Dutch) |
| `lang` | string | Yes | Language code (nl-nl) |
| `translations` | array | Yes | Array of translation objects |
| `examples` | array | No | Array of example sentence objects |
| `metadata` | object | No | Additional metadata |

### Translation Object
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `translation` | string | Yes | The translated term (English) |
| `lang` | string | Yes | Target language code (en-gb) |
| `definition` | string\|null | No | Dictionary definition of the translation |
| `source` | string | Yes | Author/organization (e.g., "Burrough et al.") |
| `source-type` | string | Yes | Type of source (e.g., "Legal Dictionary", "Glossary") |
| `license` | string | Yes | License (CC0, CC BY 4.0, CC BY-NC 4.0, Proprietary) |
| `sme-reviewed` | boolean | Yes | Subject Matter Expert reviewed |
| `context` | string | No | Context/domain where this translation applies |

### Example Object
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes | Unique example ID (e.g., "ex_00001_001") |
| `nl` | string | Yes | Dutch example sentence |
| `en` | string | Yes | English example sentence |
| `source` | string | Yes | Source document/database |
| `license` | string | Yes | License type |
| `premium` | boolean | Yes | Whether example is premium content |
| `sme-reviewed` | boolean | Yes | SME reviewed status |
| `context` | string | No | Usage context |

### Metadata Object (Optional)
| Field | Type | Description |
|-------|------|-------------|
| `frequency` | string | Usage frequency (high/medium/low) |
| `domain` | array | Legal domains (e.g., ["civil procedure", "contract law"]) |
| `related-terms` | array | Related Dutch terms |
| `articles` | array | Relevant legal article references |
| `last-updated` | string | ISO date of last update |

## Merging Rules

### 1. Term Grouping
- Group by normalized `term` (lowercase, trim whitespace)
- Terms with context (e.g., "aanbrengen (een geschil)") keep full text
- Ignore parenthetical variations when matching

### 2. Translation Merging
- **DO NOT** deduplicate translations - keep all sources
- Each source may translate differently
- Show all translations side-by-side in UI
- Different translations from same source → keep most recent

### 3. Definition Priority
- If multiple sources have definitions, keep all
- Associate definition with its translation source
- `null` for translations without definitions

### 4. Example Matching
- Match examples to terms by:
  1. Exact term match in sentence
  2. Fuzzy match (term appears in inflected form)
  3. Manual linking (if needed)
- Keep ALL non-premium examples
- Premium examples only shown to paid users

### 5. License Handling
- Respect most restrictive license
- Track license per translation/example
- Display license badges in UI

## Source File Mapping

### From: Glossary-of-Dutch-Procedural-Terminology.json
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

**Maps to:**
```json
{
  "term": "aanbrengen (een geschil bij de rechter)",
  "lang": "nl-nl",
  "translations": [{
    "translation": "to seise the court of a dispute",
    "lang": "en-gb",
    "definition": null,
    "source": "Burrough/Machon/Oranje/Frakes/Visser",
    "source-type": "Civil Procedure Glossary",
    "license": "CC BY 4.0",
    "sme-reviewed": true
  }]
}
```

### From: NL-EN-legal-dictionary.json
```json
{
  "source": "A statutory requirement",
  "lang-source": "nl-nl",
  "target": "Wettelijk vereist",
  "lang-target": "en-gb",
  "lang-target-dict": "What the law demands.",
  "author": "business.gov.nl",
  "license": "CC0",
  "sme-reviewed": true,
  "premium": false
}
```

**Maps to:**
```json
{
  "term": "A statutory requirement",
  "lang": "nl-nl",
  "translations": [{
    "translation": "Wettelijk vereist",
    "lang": "en-gb",
    "definition": "What the law demands.",
    "source": "business.gov.nl",
    "source-type": "Legal Dictionary",
    "license": "CC0",
    "sme-reviewed": true
  }]
}
```

### From: NL-EN-example-sentences.json
```json
{
  "source": "De zaak is aanhangig.",
  "lang-source": "nl-nl",
  "target": "The case is pending.",
  "lang-target": "en-gb",
  "author": "Burrough/Machon/Oranje/Frakes/Visser",
  "license": "CC BY 4.0",
  "sme-reviewed": true,
  "premium": false
}
```

**Extract term "aanhangig" and add as example:**
```json
{
  "term": "aanhangig",
  "examples": [{
    "nl": "De zaak is aanhangig.",
    "en": "The case is pending.",
    "source": "Burrough/Machon/Oranje/Frakes/Visser",
    "license": "CC BY 4.0",
    "premium": false,
    "sme-reviewed": true
  }]
}
```

## Merge Algorithm (Pseudocode)

```python
unified = {}

# Step 1: Add all glossary entries
for entry in glossary:
    term = normalize(entry.source)
    if term not in unified:
        unified[term] = create_new_entry(entry)
    unified[term].translations.append(create_translation(entry))

# Step 2: Add dictionary entries
for entry in dictionary:
    term = normalize(entry.source)
    if term not in unified:
        unified[term] = create_new_entry(entry)

    # Add translation with definition
    translation = create_translation(entry)
    translation.definition = entry['lang-target-dict']
    unified[term].translations.append(translation)

# Step 3: Add examples
for example in examples:
    # Extract terms from example sentence
    terms = extract_terms(example.source)

    for term in terms:
        if term in unified:
            unified[term].examples.append(create_example(example))

# Step 4: Remove duplicates, sort
for term in unified:
    deduplicate_translations(unified[term])
    sort_by_source_priority(unified[term])

# Output
export_json(unified.values())
```

## Output Format

**Filename:** `unified-dictionary.json`

**Structure:** Array of term objects (see schema above)

**Size estimate:** ~6-8 MB for 5,000 terms

**Indexing:** Client-side search will index:
- `term` (primary)
- `translations[].translation`
- `examples[].nl` and `examples[].en`

## Validation Checklist

Before using the unified dictionary, validate:

- [ ] All required fields present
- [ ] No duplicate IDs
- [ ] All licenses are valid (CC0, CC BY 4.0, CC BY-NC 4.0, Proprietary)
- [ ] `sme-reviewed` is boolean (not "yes"/"no" string)
- [ ] `premium` is boolean
- [ ] Each term has at least one translation
- [ ] Language codes are consistent (nl-nl, en-gb)
- [ ] Examples have both `nl` and `en` fields

## JSON Schema (for validation)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "array",
  "items": {
    "type": "object",
    "required": ["id", "term", "lang", "translations"],
    "properties": {
      "id": { "type": "string", "pattern": "^term_[0-9]{5}$" },
      "term": { "type": "string", "minLength": 1 },
      "lang": { "type": "string", "enum": ["nl-nl"] },
      "translations": {
        "type": "array",
        "minItems": 1,
        "items": {
          "type": "object",
          "required": ["translation", "lang", "source", "source-type", "license", "sme-reviewed"],
          "properties": {
            "translation": { "type": "string" },
            "lang": { "type": "string", "enum": ["en-gb", "en-us"] },
            "definition": { "type": ["string", "null"] },
            "source": { "type": "string" },
            "source-type": { "type": "string" },
            "license": { "type": "string", "enum": ["CC0", "CC BY 4.0", "CC BY-NC 4.0", "Proprietary"] },
            "sme-reviewed": { "type": "boolean" },
            "context": { "type": "string" }
          }
        }
      },
      "examples": {
        "type": "array",
        "items": {
          "type": "object",
          "required": ["id", "nl", "en", "source", "license", "premium", "sme-reviewed"],
          "properties": {
            "id": { "type": "string", "pattern": "^ex_[0-9]{5}_[0-9]{3}$" },
            "nl": { "type": "string" },
            "en": { "type": "string" },
            "source": { "type": "string" },
            "license": { "type": "string" },
            "premium": { "type": "boolean" },
            "sme-reviewed": { "type": "boolean" },
            "context": { "type": "string" }
          }
        }
      },
      "metadata": {
        "type": "object",
        "properties": {
          "frequency": { "type": "string", "enum": ["high", "medium", "low"] },
          "domain": { "type": "array", "items": { "type": "string" } },
          "related-terms": { "type": "array", "items": { "type": "string" } },
          "articles": { "type": "array", "items": { "type": "string" } },
          "last-updated": { "type": "string", "format": "date" }
        }
      }
    }
  }
}
```

## Notes for Merging

1. **Term Normalization**: Decide on case sensitivity
   - Lowercase all? Keep original case?
   - My recommendation: Keep original case, normalize only for matching

2. **ID Generation**: Use sequential IDs
   - Terms: `term_00001` to `term_99999`
   - Examples: `ex_00001_001` (term_id + sequence)

3. **Duplicate Detection**: Same translation from multiple sources
   - Keep if sources differ
   - Keep if contexts differ
   - Merge if identical (keep one with best license)

4. **Example Extraction**: From sentence to term
   - Manual matching recommended
   - Or use NLP to extract legal terms from sentences
   - Fallback: Show examples at bottom without term matching

5. **Performance**: For 5000 terms
   - Unified JSON: ~6-8 MB
   - Client-side indexing: ~50-100ms load time
   - Search: <10ms with proper indexing

## Questions for You

1. **Should I create a merge script for you** or just this spec?
2. **Date format**: ISO (2024-11-05) or something else?
3. **Source priority**: Which source is most authoritative?
   - Burrough et al. (Civil Procedure)?
   - Ministry sources?
   - business.gov.nl?

Let me know when you have the unified dictionary ready, and I'll build the UI!
