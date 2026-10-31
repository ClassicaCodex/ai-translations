# File format

Each file in `translations/` is one JSON object for one work, in UTF-8.

```json
{
  "work_urn": "urn:dante:commedia:paradiso",
  "edition_urn": "urn:dante:commedia:paradiso.ai-claude",
  "source_edition": "urn:dante:commedia:paradiso:petrocchi",
  "language": "eng",
  "translator": "Claude (AI-generated)",
  "model": "claude-opus-5-5",
  "made": "2026-10-31",
  "updated": "2026-10-31",
  "header": {
    "title": "Commedia III: Paradiso: AI translation (Claude)",
    "author": "Dante Alighieri",
    "publisher": "Classica Codex AI translations",
    "date": "2026",
    "source": "Translated by Claude ... from the library's urn:dante:commedia:paradiso:petrocchi, from ...",
    "statement": "An AI-generated translation. No specialist has reviewed it.",
    "availability": "CC BY-SA 4.0, as its source requires: credit ... and this AI translation, ..."
  },
  "notes": { "7.147": "A translator's note on the passage that begins at 7.147." },
  "nodes": [ { "ref": "1.11", "text": "I could store up as treasure in my mind" } ]
}
```

## Fields

- **`work_urn`, `source_edition`:** the work and the edition it was translated from, in Classica Codex's identifiers. For Perseus and Open Greek and Latin texts these are CTS URNs.
- **`edition_urn`:** this translation's own identifier, always the work's URN followed by `.ai-claude`.
- **`translator`:** always "Claude (AI-generated)". Classica Codex marks any edition whose translator says "(AI-generated)" as AI-made wherever it shows it.
- **`model`:** the model that translated.
- **`made`, `updated`:** dates.
- **`header`:** the edition's bibliographic header:
  - `source` says what it was translated from;
  - `statement` is the label;
  - `availability` is the licence and the credit it requires.
- **`nodes`:** the translated lines, in the source edition's order.
  - Each `ref` is the source edition's own reference, verbatim: a book and line, a manuscript leaf and line (`52v.9c`), a Talmud folio and line (`68b.13`), and so on. A line can be matched to its original by that reference alone.
  - Only cited passages are translated, so a file covers some of a work, not all of it.
- **`notes`:** the translators' notes on doubtful readings, disputed words and damaged text, keyed by the first reference of the passage they belong to.

## Conventions in the English

- **Square brackets** mark words English needs that the original only implies.
- **`[...]`** marks text lost in the original.
- **`*word*`** marks a term kept in the original language, glossed the first time it appears.
