"""Check the collection before a release.

py -3 tools/check_release.py      (from the repository's root)

- every translation file has the expected shape, the AI label, and a licence its source allows;
- catalogue.csv lists exactly the files there are, with their licences, lines and words;
- no file holds a local path or a private detail, and nothing comes from a source that is non-commercial or marked
  not for distribution;
- every file in testimonia/passages has the expected shape, the AI label and CC BY-SA 4.0, and its catalogue and README match it.
Prints PASS, or every problem found and exits 1.
"""
import csv, glob, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
problems = []
KEYS = ["work_urn", "edition_urn", "source_edition", "language", "translator", "model", "made", "updated", "header", "notes", "nodes"]
HEADER = ["title", "author", "publisher", "date", "source", "statement", "availability"]
# Geste marks these transcriptions "Fichier de travail, à ne pas diffuser"
NOT_FOR_DISTRIBUTION = ("urn:geste:transcr-otin-a", "urn:geste:transcr-otin-b", "urn:geste:transcr-otin-m")

files = {}
for path in sorted(glob.glob(os.path.join(ROOT, "translations", "*.json"))):
    name = "translations/" + os.path.basename(path)
    try:
        d = json.load(open(path, encoding="utf-8"))
    except ValueError as ex:
        problems.append(f"{name}: not valid JSON ({ex})")
        continue
    files[name] = d
    missing = [k for k in KEYS if k not in d] + [f"header.{k}" for k in HEADER if k not in d.get("header", {})]
    if missing:
        problems.append(f"{name}: missing {missing}")
        continue
    if d["translator"] != "Claude (AI-generated)" or d["edition_urn"] != d["work_urn"] + ".ai-claude":
        problems.append(f"{name}: translator or edition identifier is not the collection's")
    if "AI-generated" not in d["header"]["statement"] or "No specialist has reviewed it" not in d["header"]["statement"]:
        problems.append(f"{name}: the header does not carry the AI label")
    if "whole_work" in d and (d["whole_work"] is not True or "only in samples" not in d["header"]["statement"]):
        problems.append(f"{name}: a whole work whose header does not say it was checked only in samples")
    av = d["header"]["availability"]
    if not (av.startswith("CC BY-SA 4.0") or av.startswith("CC BY 4.0")):
        problems.append(f"{name}: licence is neither CC BY-SA 4.0 nor CC BY 4.0")
    if "BY-SA" in d["header"]["source"] and not av.startswith("CC BY-SA 4.0"):
        problems.append(f"{name}: the source is share-alike but the translation is not")
    if re.search(r"\bNC\b|non-?commercial", d["header"]["source"] + av, re.I):
        problems.append(f"{name}: a non-commercial source")
    if d["source_edition"].startswith(NOT_FOR_DISTRIBUTION):
        problems.append(f"{name}: a source marked not for distribution")
    refs = [n.get("ref") for n in d["nodes"]]
    if not refs or len(set(refs)) != len(refs) or any(not (n.get("text") or "").strip() for n in d["nodes"]):
        problems.append(f"{name}: lines missing, repeated or empty")

with open(os.path.join(ROOT, "catalogue.csv"), encoding="utf-8", newline="") as fh:
    rows = {r["file"]: r for r in csv.DictReader(fh)}
if set(rows) != set(files):
    problems.append(f"catalogue.csv and translations/ differ: {sorted(set(rows) ^ set(files))[:5]}")
for name, d in files.items():
    r = rows.get(name)
    if not r:
        continue
    words = sum(len(n["text"].split()) for n in d["nodes"])
    if (r["source_edition"] != d["source_edition"] or int(r["lines"]) != len(d["nodes"]) or int(r["english_words"]) != words
            or not d["header"]["availability"].startswith(r["licence"]) or r["credit"] != d["header"]["availability"]):
        problems.append(f"catalogue.csv: the row for {name} does not match the file")

# The Testimonia folder
PROJECTS = ("perseus-greek", "perseus-latin", "first1k-greek", "csel", "patrologia-latina")
TKEYS = ["source_edition", "source_urn", "title", "author", "language", "source_project", "translator", "model", "made", "source", "statement", "availability", "passages"]
PKEYS = ["id", "ref", "original", "english", "notes", "reviewed", "corrected"]
tfiles, ids = {}, set()
for path in sorted(glob.glob(os.path.join(ROOT, "testimonia", "passages", "*.json"))):
    name = "testimonia/passages/" + os.path.basename(path)
    try:
        d = json.load(open(path, encoding="utf-8"))
    except ValueError as ex:
        problems.append(f"{name}: not valid JSON ({ex})")
        continue
    tfiles[name] = d
    missing = [k for k in TKEYS if k not in d]
    if missing:
        problems.append(f"{name}: missing {missing}")
        continue
    if os.path.basename(path) != d["source_edition"] + ".json" or d["source_project"] not in PROJECTS or d["language"] not in ("Greek", "Latin"):
        problems.append(f"{name}: file name, source project or language is not the folder's")
    if d["translator"] != "Claude (AI-generated)" or "AI-generated" not in d["statement"] or "No specialist has reviewed it" not in d["statement"]:
        problems.append(f"{name}: the file does not carry the AI label")
    if not d["availability"].startswith("CC BY-SA 4.0") or re.search(r"\bNC\b|non-?commercial", d["source"] + d["availability"], re.I):
        problems.append(f"{name}: licence is not CC BY-SA 4.0")
    if not d["passages"]:
        problems.append(f"{name}: no passages")
    for p in d["passages"]:
        if [k for k in PKEYS if k not in p] or not (p["original"] or "").strip() or not (p["english"] or "").strip():
            problems.append(f"{name}: passage {p.get('id')} is missing a field or is empty")
        elif p["id"] in ids:
            problems.append(f"{name}: passage {p['id']} is repeated")
        elif not (isinstance(p["reviewed"], bool) and isinstance(p["corrected"], bool)):
            problems.append(f"{name}: passage {p['id']} has a reviewed or corrected flag that is not true or false")
        elif "context_before" in p["notes"] or "context_after" in p["notes"]:
            problems.append(f"{name}: passage {p['id']} has a note using the translators' field names")
        ids.add(p.get("id"))

with open(os.path.join(ROOT, "testimonia", "catalogue.csv"), encoding="utf-8", newline="") as fh:
    trows = {r["file"]: r for r in csv.DictReader(fh)}
if set(trows) != set(tfiles):
    problems.append(f"testimonia/catalogue.csv and testimonia/passages differ: {sorted(set(trows) ^ set(tfiles))[:5]}")
for name, d in tfiles.items():
    r = trows.get(name)
    if r and "passages" in d and (r["source_edition"] != d["source_edition"] or int(r["passages"]) != len(d["passages"]) or r["credit"] != d["availability"]
                                  or int(r["reviewed"]) != sum(p["reviewed"] for p in d["passages"])
                                  or int(r["corrected"]) != sum(p["corrected"] for p in d["passages"])
                                  or int(r["english_words"]) != sum(len(p["english"].split()) for p in d["passages"])):
        problems.append(f"testimonia/catalogue.csv: the row for {name} does not match the file")
all_p = [p for d in tfiles.values() for p in d.get("passages", [])]
readme = open(os.path.join(ROOT, "testimonia", "README.md"), encoding="utf-8").read()
for figure in (f"{len(tfiles):,}", f"{len(all_p):,}", f"{sum(p['reviewed'] for p in all_p):,}", f"{sum(not p['reviewed'] for p in all_p):,}",
               f"{sum(len(p['english'].split()) for p in all_p):,}"):
    if figure not in readme:
        problems.append(f"testimonia/README.md does not give {figure}")

PRIVATE = [r"[A-Za-z]:\\\\?Users", r"[A-Za-z]:[\\/]Projects", r"AppData", r"scratchpad", r"_Backup", r"publish-antikythera",
           r"LOCALAPPDATA", r"passphrase", r"[\w.+-]+@[\w-]+\.[\w.]+"]
NAMES = [r"\bjonathan\b", r"\bmorin\b"]   # not in the Testimonia texts and their reviews, where Jonathan is Saul's son
for path in glob.glob(os.path.join(ROOT, "**", "*"), recursive=True):
    if os.path.isdir(path) or os.sep + ".git" + os.sep in path or path.endswith("check_release.py"):
        continue
    text = open(path, encoding="utf-8", errors="replace").read()
    rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
    ancient = rel.startswith("testimonia/passages/") or rel.startswith("method/reviews/testimonia")
    # A whole work's English and notes are ancient text too (Jonathan is Saul's son there), so for those files the names
    # are looked for in everything else: the identifiers and the header.
    whole = files.get(rel, {}).get("whole_work") is True
    for pat in PRIVATE + ([] if ancient else NAMES):
        hay = text
        if whole and pat in NAMES:
            hay = json.dumps({k: v for k, v in files[rel].items() if k not in ("nodes", "notes")}, ensure_ascii=False)
        m = re.search(pat, hay, re.I)
        if m:
            problems.append(f"{os.path.relpath(path, ROOT)}: private detail or local path ({m.group(0)!r})")

if problems:
    print("\n".join(problems))
    print(f"FAIL: {len(problems)} problems")
    sys.exit(1)
by = {}
for r in rows.values():
    by[r["licence"]] = by.get(r["licence"], 0) + 1
print(f"PASS: {len(files)} translations, {sum(len(d['nodes']) for d in files.values()):,} lines, licences {by}; catalogue matches; "
      "nothing private, non-commercial or restricted.")
print(f"PASS: testimonia: {len(tfiles):,} editions, {len(all_p):,} passages, {sum(p['reviewed'] for p in all_p):,} reviewed, "
      f"{sum(p['corrected'] for p in all_p):,} corrected; catalogue and README match.")
