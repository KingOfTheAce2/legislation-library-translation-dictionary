# Incomplete Translations Issue

## Problem Identified

During import of the sentence-level TMX files, **123 incomplete translations** were detected across all books.

### Statistics

| Category | Count | Description |
|----------|-------|-------------|
| **Mutatis Mutandis** | 33 | Intentionally shortened (legal convention) |
| **Ellipsis/Parenthesis** | 44 | End with `...` or `(` - incomplete |
| **Too Short** | 46 | English much shorter than Dutch - incomplete |
| **Total** | **123** | Incomplete translations |

## Example of the Problem

### Example 1: Mutatis Mutandis (May be intentional)
```
NL: Het tweede tot en met zesde lid zijn van overeenkomstige toepassing als een partij de rechter meedeelt dat zij zelf bepaalde stellingen wil toelichten of bepaalde, op de zaak betrekking hebbende gegevens in de procedure wil overleggen waarvan uitsluitend de rechter of ook een gemachtigde als bedoeld in artikel 22a kennis mag nemen.

EN: Article 22(2) to (6) inclusive apply
```

**Issue:** The Dutch text has a long conditional clause, but the English translation only says which articles apply, without translating the condition.

**Proper translation might be:**
"Article 22(2) to (6) inclusive apply mutatis mutandis where a party informs the court that it wishes to explain certain positions itself or submit certain case-related information in the proceedings of which only the court or also an authorized representative as referred to in Article 22a may take notice."

### Example 2: Incomplete Parenthesis
```
NL: Onverminderd het omtrent rechtsmacht in verdragen en EG-verordeningen bepaalde en onverminderd artikel 13a van de Wet algemene bepalingen wordt de rechtsmacht van de Nederlandse rechter beheerst door de volgende bepalingen.

EN: Without prejudice to the provisions on international jurisdiction in treaties and EC regulations and without prejudice to Article 13a of the General Provisions Act (
```

**Issue:** English ends mid-sentence with an open parenthesis

### Example 3: Ellipsis
```
NL: De Autoriteit Consument en Markt of de Europese Commissie kan, niet optredende als partij, schriftelijke opmerkingen maken ingevolge artikel 15, derde lid, van Verordening (EG) nr. 1/2003...

EN: Having given prior notice, the Authority for Consumers and Markets (...
```

**Issue:** English ends with `(...` indicating text is missing

## Root Cause

The **TMX files themselves** contain these incomplete translations. This issue exists in:
- ✗ `Book 1 paragraphed.tmx` (original)
- ✗ `Book 1 sentenced.tmx` (sentence-level)
- ✗ `book 2-3 (para).tmx`
- ✗ `book 2-3 (sentence).tmx`
- ✗ `book 4 (para level).tmx`
- ✗ `book 4 (sentence level).tmx`

**Both paragraph-level AND sentence-level TMX files have the same incomplete translations.**

## Current Status

### Files Imported (with incomplete translations)
- `i8n/NL-EN-civil-procedure-book1.json` - 2,879 segments (82 incomplete)
- `i8n/NL-EN-civil-procedure-book2-3.json` - 809 segments (26 incomplete)
- `i8n/NL-EN-civil-procedure-book4.json` - 693 segments (15 incomplete)

### Report Generated
- `i8n/incomplete-translations-report.json` - Full list of all 123 incomplete items

## Possible Solutions

### Option 1: Accept Mutatis Mutandis Abbreviations (33 items)
Many legal texts use shortened "mutatis mutandis" references. For example:
- "Article X applies mutatis mutandis" instead of repeating all the text with modifications

**Action:** These 33 items may be acceptable as-is (common legal practice)

### Option 2: Fix Genuinely Incomplete (90 items)
The 90 items with ellipsis or significantly truncated text need to be completed.

**Required:** Access to complete English translations from:
- Original translation memory (if more complete version exists)
- The English DOCX files (`EN Book 1.docx`, `EN Book 4.docx`)
- Re-translation of the incomplete segments

### Option 3: Extract from DOCX Files
The `EN Book 1.docx` and `EN Book 4.docx` files may contain complete English text.

**Action Needed:**
1. Extract text from DOCX files
2. Match with Dutch source text
3. Replace incomplete translations

## Recommended Action

1. **Verify source files:** Check if the original DejaVu translation memory has complete translations
2. **Review DOCX files:** The English DOCX files may have the complete text
3. **Manual review:** The 33 "mutatis mutandis" items may be legally acceptable abbreviations
4. **Fix critical items:** Focus on the 90 items with ellipsis/parentheses/severe truncation

## Files for Review

- `import/EN Book 1.docx` - English text for Book 1
- `import/EN Book 4.docx` - English text for Book 4
- `i8n/incomplete-translations-report.json` - Complete list of issues

## Next Steps

Please provide:
1. ✓ Complete TMX files (if available)
2. ✓ Or confirm that DOCX files have complete translations
3. ✓ Or clarify if "mutatis mutandis" abbreviations are acceptable

---

**Issue Discovered:** 2025-11-05
**Total Incomplete:** 123 segments (2.9% of 4,252 total)
**Status:** Awaiting source material with complete translations
