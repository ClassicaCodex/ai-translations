"""Check the collection before a release.

py -3 tools/check_release.py      (from the repository's root)

- every translation file has the expected shape, the AI label, and a licence its source allows;
- catalogue.csv lists exactly the files there are, with their licences, lines and words;
- no file holds a local path or a private detail, and nothing comes from a source that is non-commercial or marked
  not for distribution.
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

PRIVATE = [r"[A-Za-z]:\\\\?Users", r"[A-Za-z]:[\\/]Projects", r"AppData", r"scratchpad", r"_Backup", r"publish-antikythera",
           r"LOCALAPPDATA", r"passphrase", r"\bjonathan\b", r"\bmorin\b", r"[\w.+-]+@[\w-]+\.[\w.]+"]
for path in glob.glob(os.path.join(ROOT, "**", "*"), recursive=True):
    if os.path.isdir(path) or os.sep + ".git" + os.sep in path or path.endswith("check_release.py"):
        continue
    text = open(path, encoding="utf-8", errors="replace").read()
    for pat in PRIVATE:
        m = re.search(pat, text, re.I)
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
