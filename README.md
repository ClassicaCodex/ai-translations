# Classica Codex AI translations

English translations of ancient and medieval passages that have no published English, made by AI and labelled as such.

> **AI translation.** Every translation here was made by Claude (Anthropic) from the original text, then checked against the original by a second AI, Codex (OpenAI). Objections that held up were corrected. **No specialist has reviewed any of it.** Use these as plain working versions, not authoritative translations, and keep this label with them wherever you use them.

The collection has 446 works in 12 languages: about 302,600 English words on 15,912 lines. The passages are the ones that three projects quote or cite and that had no English in the library:
- the [Atlas of Ancient Myth](https://skirnirstudios.com/atlas-of-ancient-myth/);
- [Magic in the Ancient Texts](https://skirnirstudios.com/magic-in-the-ancient-texts/);
- a study of demons and angels.

You can read them beside their originals at [skirnirstudios.com/translations](https://skirnirstudios.com/translations/), and import them into a [Classica Codex](https://github.com/ClassicaCodex/ClassicaCodex) library from its setup screens.

| Language | Works | Lines | English words |
|---|---:|---:|---:|
| Greek | 144 | 1,805 | 96,217 |
| Latin | 112 | 2,924 | 93,680 |
| Old Icelandic, Old Norse, Old Norwegian, Old Swedish | 42 | 3,637 | 35,978 |
| Egyptian | 61 | 2,153 | 26,150 |
| Middle High German | 69 | 2,783 | 19,696 |
| Italian (Dante) | 3 | 1,569 | 12,681 |
| Old French | 9 | 960 | 8,236 |
| Hebrew and Aramaic | 6 | 81 | 9,931 |

`catalogue.csv` lists every file, with its work, language, source edition, licence and the credit its licence requires.

## How they were made and checked

1. **Translation.** Claude translated each passage from the original text as the library holds it.
   - It worked line by line, one English line for each line or section of the original.
   - It did not consult a published translation, and was told not to reproduce one from memory.
   - Doubtful readings went into notes rather than into the translation.
   - The translators' brief is in `method/BRIEF-translate.md`, together with the guidance each language had: manuscript lines and diplomatic spelling for Old Norse, skaldic word order, transliteration conventions for Egyptian, the Talmud's dialectic, and so on.
2. **Review.** Codex checked every passage against the original and listed what it took for errors, each marked major or minor, with an accuracy score from 1 to 5. Its brief is in `method/BRIEF-judge.md`.
3. **Decision.** Each objection was weighed against the original:
   - **Upheld:** corrected in the text, with the translator's note corrected too where it was affected.
   - **Defensible either way:** the alternative reading added to the notes.
   - **Not upheld:** recorded with the reason, where the translation follows a standard reading.

   Every decision, with the line before and after, is in `method/reviews/`.

**Before any of this,** a blind test set 187 AI translations beside the published translations of the same passages.
- Codex scored the AI translations 4.79 out of 5 and the published ones 4.32.
- Greek and Latin prose had no major error in 75 passages.
- Akkadian and Coptic were weaker than their published translations, so they are not translated here.

**Across the twelve waves,** Codex reviewed 1,460 passages and raised 187 objections: 153 led to a correction or a note, and 37 were not upheld (a few objections led to both).

The major-error rates before correction were:

| Language | Major-error rate |
|---|---|
| Greek and Latin | about one passage in twenty |
| Old Norse | about one in twelve, most of them in skaldic verse |
| Middle High German | about one in seventeen |
| Egyptian | about one in sixteen |
| Dante | one in 69 |
| Old French | one in 34 |
| Hebrew and Aramaic | one in 23 |

## What is not here

- **Akkadian and Coptic.** The test showed them too weak to publish without a specialist.
- **One Old French passage (Otinel, manuscript A).** Its transcription in the Geste corpus is marked as a working file not for distribution.
- **Whole works.** Only the cited passages are translated; each file says so.

## Licences

Each translation carries its source's terms, and its header names them.
- **409 files are CC BY-SA 4.0**, because their sources are.
- **37 are CC BY 4.0:**
  - translations of CC BY sources (papyri.info and the Online Critical Pseudepigrapha);
  - translations of public-domain texts (Eisenstein's Otzar Midrashim).

Credit the source edition named in the file and this AI translation. See `LICENSES.md` for each source.

Under current US law, purely AI-generated text may not be protected by copyright. The source's terms still apply to what is made from it.

## Files

- **`translations/`:** one JSON file per work. The format is in `FORMAT.md`.
- **`catalogue.csv`:** one row per file.
- **`method/`:** the briefs and every review decision.
- **`tools/check_release.py`:** checks the collection before a release: every file's shape and licence, the catalogue, and that nothing private or restricted is in it.
- **`CITATION.cff`:** how to cite the collection.
