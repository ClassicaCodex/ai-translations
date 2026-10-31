# Translating for the Classica Codex AI translations

You are translating ancient and medieval texts into English for an open library of translations. They will be published and clearly labelled as AI translations. Readers will use them as plain English versions of texts that have none, and will set them beside the original. Accuracy matters more than elegance.

## What you get

You get a JSON file of units. Each unit has:
- `id`
- `lang`: the original's language code (grc Greek, lat Latin, akk Akkadian, cop Coptic, hbo Biblical Hebrew, heb rabbinic Hebrew, arc Aramaic, ara Arabic, gmh Middle High German, non/isl/nor/swe Old Norse and its relatives, fro Old French, ita Italian, egy Egyptian in transliteration)
- `work` and `author`
- `mode`: "prose" or "verse"
- `lines`: a list of `{ref, text}` in order. This is the original, as the library holds it, one passage or verse line to each reference.

Some units also carry `context_before` and `context_after`. These are the lines just before and after the unit, to help you understand it. Do not translate them.

## What you write

Write one JSON file to the path you were given. It is a list with one object per unit, in the same order:

```json
{"id": "c001", "lines": ["English for the first line", "English for the second line"], "notes": "..."}
```

- **`lines`.** Give exactly as many English lines as the unit has original lines, in order. Each English line is filed under its original line's reference.
  - When a sentence runs across lines, break the English where the original breaks, as nearly as the sense allows. Move a word across the break only when English word order forces it.
  - Never merge two lines into one, or leave a line empty because its words went elsewhere. If a line holds only a word or two that belong with the next line, give those words their own short line.
- **`notes`.** Use this only for what a careful reader would want flagged, briefly:
  - a reading you are unsure of
  - a word whose sense is disputed
  - a passage where the text is broken, or seems corrupt
  - a name you could not identify

  Leave it as "" when there is nothing to flag. Never put notes inside the translation.

## How to translate

- **Translate from the original you are given, word by word in sense.** Render every clause. Do not omit, summarise or expand.
  - When English needs a word the original only implies, put it in square brackets: "he gave [it] to her". Do this sparingly.
  - Do not explain inside the translation.
- **Use plain, accurate modern English.** No archaism (no "thee", "thou", "hath"), unless the original is itself formulaic and archaising.
  - Keep the original's register: a law reads like a law, a curse like a curse, a joke like a joke.
  - Verse becomes lineated plain English, with no rhyme and no padding to fill a metre.
- **Give names in their usual English forms:** Zeus, Athena, Heracles, Jupiter, Augustine, Marduk, Solomon. Where a technical term has no English equivalent (a demon class, an office, a ritual), keep the original word in italics, *alû* or *daimōn*, and gloss it in brackets the first time it appears in a unit.
- **Damaged text:**
  - Keep the edition's signs for lost text as `[...]`.
  - Translate restored words, inside square brackets as the edition marks them.
  - Translate what can be read, and say in `notes` what could not.
  - For Akkadian and Sumerian transliteration, read the logograms (KÙ.BABBAR is silver, DINGIR is god), and translate the sense.
- **Do not look anything up.**
  - Do not use the web, other files, or the library.
  - Do not reproduce a published translation from memory; translate afresh from the text in front of you.
  - Do not open any file except your input file and this brief.

  This is a test of what the text alone supports. If the original is too damaged to translate, say so in `notes` and translate the fragments.

## Before you finish

Check each unit: the line count matches, nothing is left out, and no notes have crept into `lines`. Then write the file, and reply with one line: the path written, the number of units, and how many carry notes.
