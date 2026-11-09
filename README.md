# Classica Codex AI translations

English translations of ancient and medieval texts that have no published English, made by AI and labelled as such: passages that other projects cite, and whole works.

> **AI translation.** Every translation here was made by Claude (Anthropic) from the original text and checked against the original by a second AI, Codex (OpenAI). Objections that held up were corrected. Codex read every cited passage in `translations/`, but only a sample of the whole works and of the `testimonia/` folder: see below. **No specialist has reviewed any of it.** Use these as plain working versions, not authoritative translations, and keep this label with them wherever you use them.

The `translations/` folder has 557 files.
- **446 hold cited passages** from works in 12 languages: about 302,100 English words on 15,887 lines. They are the passages that three projects quote or cite and that had no English in the library:
  - the [Atlas of Ancient Myth](https://skirnirstudios.com/atlas-of-ancient-myth/);
  - [Magic in the Ancient Texts](https://skirnirstudios.com/magic-in-the-ancient-texts/);
  - a study of demons and angels.
- **111 are whole works** in Latin and Greek for which no English translation could be found: about 654,800 English words on 6,322 lines. See [Whole works](#whole-works).

You can read the cited passages beside their originals at [skirnirstudios.com/translations](https://skirnirstudios.com/translations/), and import everything in `translations/` into a [Classica Codex](https://github.com/ClassicaCodex/ClassicaCodex) library from its setup screens.

**The [`testimonia/`](testimonia/README.md) folder** holds 18,211 more passages, in Greek and Latin, about 1.68 million English words from 1,135 editions. They are the English shown on [Testimonia](https://skirnirstudios.com/testimonia/). Codex checked only 5,467 of them, so they are kept apart, with their own README and format. About 1 passage in 23 that Codex read held a major error, and the 12,744 it did not read will have errors at about the same rate.

The cited passages, by language:

| Language | Works | Lines | English words |
|---|---:|---:|---:|
| Greek | 144 | 1,805 | 96,217 |
| Latin | 112 | 2,924 | 93,680 |
| Old Icelandic, Old Norse, Old Norwegian, Old Swedish | 42 | 3,612 | 35,522 |
| Egyptian | 61 | 2,153 | 26,150 |
| Middle High German | 69 | 2,783 | 19,696 |
| Italian (Dante) | 3 | 1,569 | 12,681 |
| Old French | 9 | 960 | 8,236 |
| Hebrew and Aramaic | 6 | 81 | 9,931 |

`catalogue.csv` lists every file in `translations/`, with its work, language, source edition, licence and the credit its licence requires.

## How the cited passages were made and checked

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

## Whole works

**111 files in `translations/` translate a whole work,** every line of the source edition from first to last. Each is marked `"whole_work": true`, and its header says so.
- **What they are.** 73 are Latin and 38 Greek: about 473,000 words of original and 654,800 of English, on 6,322 lines. 70 come from Migne's Patrologia Latina, 38 from First1KGreek, 2 from CSEL and 1 from Perseus.
  - Most are short: theology, sermons, letters, monastic rules, canons and lives of saints, with 19 of Libanius's orations and declamations, six works of Galen, and Hero of Alexandria. The longest has about 6,600 words.
  - Authors and titles are the library's, which follow Migne and the other editions. Many attributions there are doubtful, and works marked *incertus* are not by the author named.
- **Why these works.** They are the first 111 finished of 314 Latin and Greek works in the library for which no English translation could be found. The run goes shortest first.
  - An AI searched the web for each work's English: translation series, journals, theses and open projects. Claude did most of the searching and Codex some.
  - Machine-made English did not count.
  - Against an earlier, separate search, the list agreed on 72 of 82 works, and it missed one recent translation, since corrected.
  - A search is not proof. If you know an English translation of one of these works, please open an issue.
- **Translation.** Claude (claude-opus-5-5) translated each work straight through, in stretches of about 1,200 words.
  - With each stretch it saw the lines it had just translated, the next lines of the original, and a running glossary of the names and terms used so far, so that a work reads as one translation.
  - As with the passages, it gave one English line for each line of the original, did not consult a published translation, and put doubtful readings in notes.
  - The brief is in `method/BRIEF-whole-works-translate.md`.
- **Review.** Codex read a random sample of 41 stretches, one from each of 41 works: 49,463 words of original, about a tenth of the whole works. It used the waves' brief.
  - It scored Latin 4.08 and Greek 3.67 out of 5, below the cited passages' 4.7 to 4.9, and raised a major objection in 17 of the 41 stretches. A stretch is about 1,200 words, several times the length of a cited passage.
  - Each objection was weighed against the original. Of Codex's 22 major objections, 13 were upheld as major errors, 7 were upheld as minor ones, and 2 were not upheld. Of its 13 minor objections, 10 were upheld.
  - So 10 of the 41 stretches held a major error: 6 of 26 in Latin and 4 of 15 in Greek. Libanius was the hardest author: three of the four Greek major errors were in his eight stretches.
  - Every upheld objection was corrected, and so was the same error where it recurred elsewhere in its work. The decisions are in `method/reviews/whole-works-1.json`.
- **The rest was not read by a second AI.** It will hold errors at about the sample's rate: roughly one major error in every 3,800 words of original, or about 110 in the 424,000 words not read.
- **More to come.** The same run is translating the other 203 Latin and Greek works on the list, about 7.4 million words. They will be added in batches.

## What is not here

- **Akkadian and Coptic.** The test showed them too weak to publish without a specialist.
- **One Old French passage (Otinel, manuscript A).** Its transcription in the Geste corpus is marked as a working file not for distribution.
- **25 lines of Gregory's Homily 34 in AM 677 4to (folios 18r–18v).** They are translated, and wait in `pending/` until Classica Codex can hold their original. See `pending/README.md`.
- **Most works whole.** Apart from the 111 whole works, only the cited passages are translated, and each of those files says so.

## Licences

Each translation carries its source's terms, and its header names them. In `translations/`:
- **520 files are CC BY-SA 4.0**, because their sources are. They include all 111 whole works, whose sources' licences were read from each edition's own header, or for one Perseus text from its repository's statement.
- **37 are CC BY 4.0:**
  - translations of CC BY sources (papyri.info and the Online Critical Pseudepigrapha);
  - translations of public-domain texts (Eisenstein's Otzar Midrashim).

All 1,135 files in `testimonia/` are CC BY-SA 4.0.

Credit the source edition named in the file and this AI translation. See `LICENSES.md` for each source.

Under current US law, purely AI-generated text may not be protected by copyright. The source's terms still apply to what is made from it.

## Files

- **`translations/`:** one JSON file per work, holding its cited passages or, where it says `"whole_work": true`, the whole work. The format is in `FORMAT.md`.
- **`catalogue.csv`:** one row per file in `translations/`.
- **`testimonia/`:** the Testimonia passages, one JSON file per source edition, with their own README and catalogue.
- **`pending/`:** translations held back until a library can hold their original. Classica Codex does not read this folder.
- **`method/`:** the briefs and every review decision.
- **`tools/check_release.py`:** checks the collection before a release: every file's shape and licence, the catalogue, and that nothing private or restricted is in it.
- **`CITATION.cff`:** how to cite the collection.
