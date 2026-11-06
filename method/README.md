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
