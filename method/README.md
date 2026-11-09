# Method records

- **`BRIEF-translate.md`:** the brief every translator worked to.
  - Each wave also gave guidance for its language: Old Norse manuscript lines and diplomatic spelling; skaldic word order and kennings; the Middle High German false friends; Egyptian transliteration conventions; the Talmud's dialectic; and so on.
  - Every wave told the translators not to consult or reproduce a published translation.
- **`BRIEF-judge.md`:** the reviewer's brief. In each wave the reviewer saw one translation and judged it against the original, listing errors as major or minor with an accuracy score.
- **`reviews/wave-NN.json`:** every decision on the reviewer's objections, wave by wave.
  - `fixed` lists each change: the objection, the passage, the line, and the text before and after. Where only a note changed, `line` is "notes".
  - `not_upheld` gives each objection that was not accepted, with the reason.

| Wave | Languages | Passages | Reviewer's accuracy (of 5) |
|---|---|---:|---:|
| 1 | Greek, Latin, Old Icelandic, Egyptian, Middle High German, Italian, Old French | 164 | 4.85 |
| 2 | Greek, Latin | 150 | 4.92 |
| 3 | Greek, Latin | 129 | 4.72 |
| 4 | Greek, Latin | 122 | 4.84 |
| 5 | Greek, Latin | 134 | 4.87 |
| 6 | Greek, Latin | 109 | 4.75 |
| 7 | Old Icelandic, Old Norse, Old Norwegian, Old Swedish | 184 | 4.76 |
| 8 | Middle High German | 134 | 4.75 |
| 9 | Egyptian | 208 | 4.75 |
| 10 | Italian (Dante) | 69 | 4.94 |
| 11 | Old French | 34 | 4.79 |
| 12 | Hebrew, Aramaic | 23 | 4.70 |

## Testimonia

The passages in `testimonia/` were made in one run rather than in waves, and only some were reviewed. `testimonia/README.md` gives the method and the error rates.

- **`BRIEF-testimonia-translate.md`:** the brief Claude worked to. `context_before` and `context_after` are the words on either side of a passage, which it saw but did not translate.
- **`BRIEF-testimonia-judge.md`:** the reviewer's brief.
- **`reviews/testimonia-lost.json`:** the review of every passage citing a lost author.
- **`reviews/testimonia-sample.json`:** the review of a random tenth of the rest.
  - `objections` gives each major objection with its verdict (`upheld`, `minor` or `rejected`) and the reason. The reviewer's 180 minor objections were not weighed, and are not recorded.
  - `changes` gives each correction: the passage, the field, and the wording before and after.
- **`reviews/testimonia-trial.json`:** the corrections from the review of the trial's 181 passages.
- **`reviews/testimonia-notes.json`:** corrections made after the review, none of them from it: 3 to the English where the translator's own note showed it was wrong, and 24 to notes that still described English the review had changed.

## Whole works

The whole works in `translations/` (marked `"whole_work": true`) are made by one long run, a stretch of about 1,200 words at a time, and released in batches. The main README gives the method and the error rates.

- **`BRIEF-whole-works-translate.md`:** the brief Claude worked to. With each stretch it saw the last lines it had translated (`before`), the next lines of the original (`after`) and the glossary so far.
- **`BRIEF-judge.md`:** the reviewer's brief, as in the waves. The reviewer saw each sampled stretch line by line, the original and the English numbered alike.
- **`reviews/whole-works-1.json`:** the review of the first batch's sample.
  - `sample` lists the stretches the reviewer read.
  - `fixed` lists each change: the objection, the work, the line, and the text before and after.
    - `upheld_as` gives the severity the error was judged to have, which may be lower than the reviewer's.
    - Where a translator's note described the old English, the note was corrected too, and `ref` is "notes".
    - `outside_sample` marks a correction of the same error where it recurred in an unsampled stretch of the same work.
  - `noted` gives a note added to a stretch.
  - `not_upheld` gives each objection that was not accepted, with the reason.
