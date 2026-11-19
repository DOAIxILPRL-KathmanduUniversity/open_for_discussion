# Nepali → English parallel corpus

One JSON file per paper, named `<paper_id>.json` (see `manifest.csv`).

## Schema

```json
{
  "paper_id": "tucl_27278",
  "source": "TUCL eLibrary",
  "title": "<original title, verbatim>",
  "authors": ["<verbatim>"],
  "date": "<verbatim>",
  "doi": "<verbatim or empty>",
  "url": "<verbatim>",
  "nepali": "<original abstract, byte-for-byte unchanged>",
  "american_english": "<translation>",
  "british_english": "<translation>",
  "australian_english": "<translation>",
  "informal_english": "<translation>",
  "informal_flavour": "<flavour assigned in manifest.csv>",
  "translator_notes": "<optional short note; e.g. OCR damage, missing ending>"
}
```

## Rules

1. `nepali` is copied verbatim from the harvested abstract. Never clean, normalise,
   summarise or fix OCR errors in this field.
2. Translate the abstract faithfully into English. Do not add facts, citations or
   interpretation. Keep the original paragraph order and, where sensible, paragraph breaks.
3. **Strict sentence order.** Translate clause by clause and sentence by sentence in
   exactly the order of the Nepali abstract. Do not merge, split, move or reorder
   sentences, even when English would prefer a different flow.
4. The three standard variants (`american_english`, `british_english`,
   `australian_english`) should be genuinely distinct translations where the variety
   offers a natural alternative: vocabulary, idiom, verb choice, punctuation and
   register, not just spelling swaps. Do **not** invent differences where the text
   gives none: if a sentence reads the same in two varieties, let it. It is acceptable
   for two variants to be close when the source leaves little room.
5. `informal_english` is a proper relaxed, conversational rendering in the flavour
   given by `informal_flavour` (rotates per paper across American, British,
   Australian, Indian, Canadian, Irish, Scottish, South African and New Zealand
   casual English). It may shorten formulaic academic phrasing and use local idiom,
   but it must keep the original order, findings, numbers and caveats.
6. Keep Devanagari names/titles in the translation if they have no established
   English form; otherwise transliterate them consistently.
7. Preserve in-text numbering, years, sample sizes and quoted terms.
8. Do not use the source English glosses inside `{...}` as a substitute for
   translating the Nepali; translate the Nepali itself.
