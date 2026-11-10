#!/usr/bin/env python3
"""
publish.py: turn one scan into every channel at once.

The scan is the only place facts are produced. Everything below is a rendering
of that single run, so no channel can drift from another or go stale on its
own. Add a channel by adding a renderer here, never by re-deriving the data.

Channels emitted:

  docs/index.md        human page, rendered by GitHub Pages
  docs/data.json       machine readable, stable shape, usable as an API
  docs/feed.xml        RSS, so the work syndicates without anyone's permission
  out/post-short.txt   ~280 chars, for a post
  out/post-long.md     a few paragraphs, for a forum or newsletter
  out/digest.txt       plain text, for an email
  history/YYYY-MM-DD.json  the archive, which is the asset that accrues
"""

import io
import json
import os
from datetime import datetime, timezone

SITE = "https://fstivicic.github.io/eol-watch/"
REPO = "https://github.com/fstivicic/eol-watch"

SEV_ORDER = {"critical": 0, "high": 1, "moderate": 2, "medium": 2, "low": 3}


def _ensure(path):
    d = os.path.dirname(path)
    if d and not os.path.isdir(d):
        os.makedirs(d)


def _write(path, text):
    _ensure(path)
    io.open(path, "w", encoding="utf-8", newline="\n").write(text)
    return path


def group(findings):
    """One entry per advisory, carrying every EOL line it lands on."""
    out = {}
    for f in findings:
        key = f["ghsa"]
        if key not in out:
            out[key] = {
                "ghsa": f["ghsa"],
                "cve": f["cve"],
                "severity": f["severity"],
                "published": f["published"],
                "summary": f["summary"],
                "product": f["product"],
                "package": f["package"],
                "ecosystem": f["ecosystem"],
                "range": f["range"],
                "patched_in": f["patched_in"],
                "lines": [],
            }
        out[key]["lines"].append({
            "line": f["eol_line"],
            "eol_since": f["eol_since"],
            "days_dead": f["days_dead"],
            "last_release": f["last_release"],
        })

    items = list(out.values())
    for it in items:
        it["lines"].sort(key=lambda l: l["days_dead"])
    items.sort(key=lambda i: (SEV_ORDER.get(i["severity"], 9), i["published"]))
    items.sort(key=lambda i: SEV_ORDER.get(i["severity"], 9))
    return items


def emit_json(items, stamp):
    payload = {
        "generated": stamp,
        "source": REPO,
        "note": ("Candidates, not confirmed exposures. A version range is not "
                 "proof that vulnerable code exists in an EOL branch. Each "
                 "entry needs the fix read and the construct located before "
                 "it can be called real."),
        "count": len(items),
        "exposures": items,
    }
    return _write("docs/data.json", json.dumps(payload, indent=2, ensure_ascii=False) + "\n")


def emit_markdown(items, stamp):
    L = []
    L.append("# EOL Watch")
    L.append("")
    L.append("Security advisories landing on end-of-life branches, where no fix "
             "is being shipped for the dead line.")
    L.append("")
    L.append("Updated automatically. Last run **%s**." % stamp)
    L.append("")
    L.append("> **These are candidates, not confirmed exposures.** A version range "
             "is a statement about what a vendor reviewed, not about where a bug "
             "lives. Every entry here needs the actual fix read and the vulnerable "
             "construct located in the dead branch before it means anything. "
             "See [the cookbook](COOKBOOK.md) for how that is done, and "
             "[calibration](CALIBRATION.md) for how often this tool is wrong.")
    L.append("")

    if not items:
        L.append("No exposures in the current window.")
        return _write("docs/index.md", "\n".join(L) + "\n")

    crit = [i for i in items if i["severity"] == "critical"]
    high = [i for i in items if i["severity"] == "high"]
    L.append("**%d advisories** currently land on dead branches. "
             "%d critical, %d high." % (len(items), len(crit), len(high)))
    L.append("")

    for it in items:
        lines = ", ".join("%s" % l["line"] for l in it["lines"])
        L.append("---")
        L.append("")
        L.append("### %s %s" % (it["product"], lines))
        L.append("")
        L.append("**%s** &middot; %s" % (it["severity"].upper(),
                                         it["cve"] or it["ghsa"]))
        L.append("")
        L.append(it["summary"])
        L.append("")
        L.append("| | |")
        L.append("|---|---|")
        L.append("| Advisory | [%s](https://github.com/advisories/%s) |"
                 % (it["ghsa"], it["ghsa"]))
        L.append("| Published | %s |" % it["published"])
        L.append("| Affected range | `%s` |" % it["range"])
        L.append("| Fixed in | `%s` |" % it["patched_in"])
        L.append("| Package | `%s` (%s) |" % (it["package"], it["ecosystem"]))
        L.append("")
        L.append("Dead branches in range:")
        L.append("")
        for l in it["lines"]:
            L.append("- **%s** &mdash; EOL since %s (%d days), last release `%s`"
                     % (l["line"], l["eol_since"], l["days_dead"], l["last_release"]))
        L.append("")

    return _write("docs/index.md", "\n".join(L) + "\n")


def emit_feed(items, stamp):
    now = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")
    X = []
    X.append('<?xml version="1.0" encoding="UTF-8"?>')
    X.append('<rss version="2.0"><channel>')
    X.append("<title>EOL Watch</title>")
    X.append("<link>%s</link>" % SITE)
    X.append("<description>Security advisories landing on end-of-life branches "
             "with no fix shipped for the dead line. Candidates, not confirmed "
             "exposures.</description>")
    X.append("<lastBuildDate>%s</lastBuildDate>" % now)

    def esc(t):
        return (str(t).replace("&", "&amp;").replace("<", "&lt;")
                .replace(">", "&gt;"))

    for it in items[:40]:
        lines = ", ".join(l["line"] for l in it["lines"])
        X.append("<item>")
        X.append("<title>%s: %s %s</title>" % (
            esc(it["severity"].upper()), esc(it["product"]), esc(lines)))
        X.append("<link>https://github.com/advisories/%s</link>" % esc(it["ghsa"]))
        X.append("<guid isPermaLink='false'>%s</guid>" % esc(it["ghsa"]))
        X.append("<description>%s Affected range %s, fixed in %s, nothing shipped "
                 "for %s.</description>" % (
                     esc(it["summary"]), esc(it["range"]),
                     esc(it["patched_in"]), esc(lines)))
        X.append("</item>")

    X.append("</channel></rss>")
    return _write("docs/feed.xml", "\n".join(X) + "\n")


def emit_short(items, stamp):
    if not items:
        text = "EOL Watch ran clean today. No new advisories landing on dead branches. %s" % SITE
        return _write("out/post-short.txt", text + "\n")

    top = items[0]
    lines = ", ".join(l["line"] for l in top["lines"])
    text = ("%s in %s %s. Range %s, fixed in %s, nothing shipped for the dead lines.\n\n"
            "%d advisories currently land on EOL branches.\n%s" % (
                top["severity"].upper(), top["product"], lines,
                top["range"], top["patched_in"], len(items), SITE))
    return _write("out/post-short.txt", text + "\n")


def emit_long(items, stamp):
    L = []
    L.append("## What is exposed today (%s)" % stamp)
    L.append("")
    if not items:
        L.append("Nothing new. The scan found no advisories landing on branches "
                 "inside the window.")
        return _write("out/post-long.md", "\n".join(L) + "\n")

    L.append("%d security advisories currently land on end-of-life branches "
             "where no fix is being shipped for the dead line. The scan joins "
             "the GitHub Advisory Database against endoflife.date and runs "
             "daily." % len(items))
    L.append("")
    for it in items[:5]:
        lines = ", ".join(l["line"] for l in it["lines"])
        oldest = max(l["days_dead"] for l in it["lines"])
        L.append("**%s, %s %s.** %s Affected range `%s`, fixed in `%s`. "
                 "The oldest affected line has been dead %d days." % (
                     it["severity"].upper(), it["product"], lines,
                     it["summary"], it["range"], it["patched_in"], oldest))
        L.append("")
    L.append("These are candidates. A version range describes what a vendor "
             "reviewed, not where a bug lives, so each one still needs the fix "
             "read and the construct located in the dead branch. The method is "
             "written up in the cookbook.")
    L.append("")
    L.append("Full list and machine readable data: %s" % SITE)
    return _write("out/post-long.md", "\n".join(L) + "\n")


def emit_digest(items, stamp):
    L = []
    L.append("EOL Watch, %s" % stamp)
    L.append("=" * 50)
    L.append("")
    if not items:
        L.append("No exposures in the current window.")
    else:
        for it in items:
            lines = ", ".join(l["line"] for l in it["lines"])
            L.append("[%s] %s %s" % (it["severity"].upper(), it["product"], lines))
            L.append("  %s" % it["summary"])
            L.append("  %s  range %s  fixed in %s" % (
                it["cve"] or it["ghsa"], it["range"], it["patched_in"]))
            L.append("")
    L.append("Candidates, not confirmed exposures.")
    L.append(SITE)
    return _write("out/digest.txt", "\n".join(L) + "\n")


def emit_history(items, stamp):
    day = stamp[:10]
    return _write("history/%s.json" % day,
                  json.dumps({"date": day, "count": len(items),
                              "exposures": items}, indent=2,
                             ensure_ascii=False) + "\n")


def publish(findings):
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    items = group(findings)

    written = [
        emit_markdown(items, stamp),
        emit_json(items, stamp),
        emit_feed(items, stamp),
        emit_short(items, stamp),
        emit_long(items, stamp),
        emit_digest(items, stamp),
        emit_history(items, stamp),
    ]

    print("published %d advisories to %d channels:" % (len(items), len(written)))
    for w in written:
        print("  %s" % w)
    return items


if __name__ == "__main__":
    import eolwatch
    publish(eolwatch.scan())
