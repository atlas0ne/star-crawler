#!/usr/bin/env python3
"""Shared front-matter builder. One metadata source, every generated document.

Nothing downstream restates project metadata - restated metadata goes stale,
which this project has already paid for more than once.
"""
import io, os, subprocess, datetime, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def project():
    return yaml.safe_load(io.open(os.path.join(ROOT, "project.yaml"), encoding="utf-8"))

def git_commit():
    try:
        return subprocess.check_output(["git", "-C", ROOT, "rev-parse", "--short", "HEAD"],
                                       stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        return None

def front_matter(doc_id, doc_title, doc_subtitle, status, summary,
                 generated_by=None, source=None, extra=None):
    """Return a YAML front-matter block as a string, fenced with ---."""
    p = project()
    fm = {
        # --- Pandoc-standard: these drive a PDF/EPUB build with no mapping ---
        "title": doc_title,
        "subtitle": doc_subtitle,
        "author": [p["author"]["name"]],
        "date": datetime.date.today().isoformat(),
        "lang": p["language"],
        "keywords": p["keywords"],
        "abstract": " ".join(str(summary).split()),
        # --- identity ---
        "id": doc_id,
        "series": p["title"],
        "version": p["version"],
        "status": status,
        "rights": p["rights"],
        # --- Dublin Core equivalents, for anything that gets catalogued ---
        "dc:creator": p["author"]["name"],
        "dc:publisher": p["publisher"],
        "dc:language": p["language"],
        "dc:rights": p["rights"],
        "dc:source": p["repository"],
        # --- contact ---
        "website": p["author"]["website"],
        "repository": p["repository"],
    }
    if generated_by:
        fm["generated"] = {
            "by": generated_by,
            "from": source,
            "at": datetime.datetime.now().isoformat(timespec="seconds"),
            "commit": git_commit(),
            "warning": "Generated file. Edit the source, then regenerate. "
                       "Hand edits here are lost on the next build.",
        }
    if extra:
        fm.update(extra)
    body = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=88).rstrip()
    return f"---\n{body}\n---\n"


def mutation_entries(muts):
    """Every purchasable mutation entry, flattened, as (section, dict).

    Indexes rather than .get()s on purpose. When the chapter was restructured,
    the `.get(key) or []` version of this logic left four tools silently
    reading nothing and reporting success. A KeyError is the correct outcome
    for a section that no longer exists.
    """
    out = []
    for t in muts["chimeric_traits"]["list"]:
        out.append(("chimeric", t))
    for s in muts["strains"]["list"]:
        for t in s["perks"]:
            out.append(("strain/" + s["id"], t))
    for t in muts["anatomy_flaws"]["list"]:
        out.append(("anatomy_flaw", t))
    for t in muts["defects"]["list"]:
        out.append(("defect", t))
    return out
