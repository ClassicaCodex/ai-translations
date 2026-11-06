# Testimonia passages

English for the Greek and Latin passages cited on [Testimonia](https://skirnirstudios.com/testimonia/) that had no published English. These are places where one ancient or medieval writer cites or quotes another. Testimonia shows this English under each passage.

> **AI translation.** Every passage was translated by Claude Opus 5.5 (Anthropic). Codex (OpenAI) checked 5,467 of the 18,211 passages against the original, and the errors that held up were corrected. **The other 12,744 passages were not checked, and no specialist has reviewed any of it.** About 1 passage in 23 that Codex read held a major error. Use these as plain working versions, not authoritative translations, and keep this label with them wherever you use them.

| Language | Editions | Passages | English words |
|---|---:|---:|---:|
| Greek | 584 | 13,473 | 1,209,954 |
| Latin | 551 | 4,738 | 465,796 |
| **All** | **1,135** | **18,211** | **1,675,750** |

| Source | Editions | Passages |
|---|---:|---:|
| First1KGreek | 469 | 11,723 |
| Patrologia Latina | 335 | 2,625 |
| Perseus (Greek) | 115 | 1,750 |
| Perseus (Latin) | 129 | 1,240 |
| CSEL | 87 | 873 |

`catalogue.csv` has one row per edition. `passages/` has one JSON file per edition, described in [`FORMAT.md`](../FORMAT.md#the-testimonia-folder). Classica Codex's importer reads only `translations/`, so these are not imported into a library.

## How they were made

1. **Selection.** Every passage Testimonia cites that had no published English and was not already in `translations/`. Passages citing only scripture were left out.
2. **Scope.** Each passage is the run of whole sentences around the cited words. A long line of an edition can hold several passages, so these do not fit the line-by-line format of `translations/`. A passage can run a little beyond what Testimonia quotes.
3. **Translation.** Claude Opus 5.5 at low effort, chosen by a 500-passage trial of models and effort levels. It saw the passage, up to 60 words on either side, and the author and work. It was told not to reproduce a published translation. The brief is in [`method/BRIEF-testimonia-translate.md`](../method/BRIEF-testimonia-translate.md).
4. **Automatic checks.** A script checked each result: present, not empty, and no Greek or stray Latin left in the English.
5. **Review.** Codex read each translation against its original, without any other source. Its brief is in [`method/BRIEF-testimonia-judge.md`](../method/BRIEF-testimonia-judge.md).
   - It read every passage citing a lost author (3,870), a random tenth of the rest (1,416), and the trial's passages (181).
   - Each of its 280 major objections to the first two groups was weighed against the original, and each decision is recorded in [`method/reviews/`](../method/reviews/).
   - 230 were upheld as major errors, 23 were real but minor, and 27 were rejected. All 253 upheld errors were corrected.
   - Its 180 minor objections were not weighed or applied.

## How good it is

A major error is one that would give a reader the wrong sense.

| Passages Codex read | Passages | Words of original | Major errors | One in |
|---|---:|---:|---:|---:|
| Citing a lost author | 3,870 | 279,742 | 166 | 1,685 words |
| Random tenth of the rest | 1,416 | 97,377 | 64 | 1,522 words |
| **Both** | **5,286** | **377,119** | **230** | **1,640 words** |

- 227 of those 5,286 passages held a major error, about 1 in 23.
- At least 14 of the 166 errors in the first group reversed the meaning.
- Lexica and scholia were the hardest: 1 error in about 770 words in Herodian, the Iliad scholia and the Suda, against 1 in 4,525 in CSEL.
- These rates are a minimum, because a reviewer misses some errors.
- **The 12,744 passages Codex did not read will have errors at about the same rate:** about 550 passages with a major error, none of them corrected. Every passage says whether it was read, in its `reviewed` field.

## What is not here

- **Passages citing only scripture:** about 25,000 passages, left out for cost.
- **One passage,** whose text turned out to be a critical apparatus cited by mistake.
- **The links between authors.** Which author a passage cites is on Testimonia, not here.

## Licence

All 1,135 files are CC BY-SA 4.0, as their sources require. Each source edition's licence was checked: 1,038 by the edition's own header and 97 by its repository's statement. Credit the source edition named in the file and this AI translation. See [`LICENSES.md`](../LICENSES.md) for a suitable credit.
