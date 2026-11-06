# File format

Each file in `translations/` is one JSON object for one work, in UTF-8. The `testimonia/` folder has [a format of its own](#the-testimonia-folder).

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

## The Testimonia folder

Each file in `testimonia/passages/` is one JSON object for one source edition, in UTF-8, named after that edition. These passages are whole sentences around a citation, and a long line of an edition can hold several, so they do not fit the line-by-line format above.

```json
{
  "source_edition": "tlg0007.tlg075.perseus-grc2",
  "source_urn": "urn:cts:greekLit:tlg0007.tlg075.perseus-grc2",
  "title": "De virtute et vitio",
  "author": "Plutarch",
  "language": "Greek",
  "source_project": "perseus-greek",
  "translator": "Claude (AI-generated)",
  "model": "claude-opus-5-5",
  "made": "2026-11-06",
  "source": "Translated by Claude from tlg0007.tlg075.perseus-grc2, as held by the Perseus Digital Library.",
  "statement": "An AI-generated translation. No specialist has reviewed it.",
  "availability": "CC BY-SA 4.0, as its source requires: credit ... and this AI translation, ...",
  "passages": [
    {
      "id": "p06163",
      "ref": "2.1",
      "original": "ἐν δὲ τοῖς ὕπνοις ἀποφυγοῦσα δόξας ...",
      "english": "But in sleep, having escaped opinions and laws ...",
      "notes": "A translator's note on the passage, or an empty string.",
      "reviewed": true,
      "corrected": false
    }
  ]
}
```

- **`source_edition`, `source_urn`:** the edition in Classica Codex's identifiers.
- **`id`:** the passage's identifier, unique across the folder. The review records in `method/reviews/` use it.
- **`ref`:** the edition's own reference for the line holding the passage. It is not unique in a file, because one line can hold several passages.
- **`original`:** the words covered, exactly as the edition holds them, with any scanning errors.
- **`english`:** the translation, as one paragraph. Where the original has an obvious scanning error, the English follows the evident reading, and the note says so if it changes the sense.
- **`notes`:** the translator's own notes on doubtful readings, disputed words and damaged text. Codex did not review them. A note was written with the first English, so on a corrected passage it can still describe that English, although those found were changed.
- **`reviewed`:** whether Codex checked this passage against the original.
- **`corrected`:** whether the English or the note was changed after translation. A passage can be corrected without being reviewed, where the translator's own note showed the English was wrong.

The English follows the conventions above.
