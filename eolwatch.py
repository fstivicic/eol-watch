#!/usr/bin/env python3
"""
eol-watch: find security advisories that land on end-of-life branches.

The gap this detects was found twice by hand, slowly:

  * Joomla 3.10 - CVE-2026-92222 is published as affecting 4.0.0+, but the fix
    backports cleanly and the vulnerable construct is present in 3.10. The
    range describes the vendor's review scope, not where the bug lives.
  * PrestaShop 1.7 - advisories list ranges like "< 8.2.6" which numerically
    include every 1.7 release, yet no 1.7 fix is ever shipped.

Both are the same underlying fact: an advisory exists, an EOL branch is in or
near its range, and nobody is shipping a patch for that branch. This script
finds those automatically by joining two public sources:

  endoflife.date   -> which release lines are EOL, and when
  GitHub Advisory  -> which advisories exist, and what they claim to affect

Output is a ranked list of exposures. Each one is a candidate for a patch set,
a write-up, or simply a warning to people still on that branch.
"""

import json
import urllib.parse
import re
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone

# Windows consoles default to cp1252 and choke on anything outside it.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

EOL_API = "https://endoflife.date/api/v1/products/%s"
GH_API = "https://api.github.com/advisories"

UA = {"User-Agent": "eol-watch/0.1 (+https://github.com/fstivicic)"}

# Package coordinates mapped to endoflife.date product slugs. Hand-curated:
# the two namespaces do not share identifiers and never will, so this mapping
# is the one part that genuinely needs a human.
WATCH = [
    # (ecosystem, package, eol-slug, human name)
    ("composer", "joomla/joomla-cms",        "joomla",     "Joomla"),
    ("composer", "prestashop/prestashop",    "prestashop", "PrestaShop"),
    ("composer", "drupal/core",              "drupal",     "Drupal"),
    ("composer", "typo3/cms-core",           "typo3",      "TYPO3"),
    ("composer", "magento/product-community-edition", "magento", "Magento"),
    ("composer", "laravel/framework",        "laravel",    "Laravel"),
    ("composer", "symfony/symfony",          "symfony",    "Symfony"),
    ("composer", "silverstripe/framework",   "silverstripe", "SilverStripe"),
    ("composer", "contao/core-bundle",       "contao",     "Contao"),
    ("composer", "moodle/moodle",            "moodle",     "Moodle"),
    ("npm",      "next",                     "nextjs",     "Next.js"),
    ("npm",      "nuxt",                     "nuxt",       "Nuxt"),
    ("pip",      "django",                   "django",     "Django"),
]


def get(url, tries=3):
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=40) as fh:
                return json.loads(fh.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return None
            if exc.code in (403, 429) and attempt < tries - 1:
                time.sleep(5 * (attempt + 1))
                continue
            return None
        except Exception:
            if attempt < tries - 1:
                time.sleep(2)
                continue
            return None
    return None


def parse_version(text):
    """Leading numeric components of a version string, as a comparable tuple."""
    if not text:
        return ()
    nums = re.findall(r"\d+", str(text))
    return tuple(int(n) for n in nums[:4])


def eol_releases(slug):
    """Release lines already past EOL, newest first."""
    data = get(EOL_API % slug)
    if not data:
        return []

    result = data.get("result", data)
    today = datetime.now(timezone.utc).date()
    out = []

    for rel in result.get("releases", []):
        eol = rel.get("eolFrom")
        if not eol:
            continue
        try:
            eol_date = datetime.strptime(eol, "%Y-%m-%d").date()
        except ValueError:
            continue
        if eol_date > today:
            continue

        latest = (rel.get("latest") or {}).get("name") or rel.get("name")
        out.append({
            "line": str(rel.get("name")),
            "eol": eol,
            "days_dead": (today - eol_date).days,
            "last_release": latest,
            "version": parse_version(latest),
        })

    out.sort(key=lambda r: r["version"], reverse=True)
    return out


def advisories(ecosystem, package, per_page=40):
    url = "%s?ecosystem=%s&affects=%s&per_page=%d&sort=published&direction=desc" % (
        GH_API, ecosystem, urllib.parse.quote(package), per_page)
    data = get(url)
    return data if isinstance(data, list) else []


def range_touches(vuln_range, eol_version):
    """
    Does this advisory's vulnerable range cover the EOL line's last release?

    Deliberately permissive on the upper bound. The whole point is that an
    advisory saying "< 8.2.6" numerically includes 1.7.8.11, and the vendor
    simply never ships the 1.7 fix. Those are exactly the cases worth seeing.
    """
    if not vuln_range or not eol_version:
        return False

    lower_ok = True
    upper_ok = False

    for clause in vuln_range.split(","):
        clause = clause.strip()
        m = re.match(r"(>=|>|<=|<|=)\s*(.+)", clause)
        if not m:
            continue
        op, raw = m.group(1), m.group(2).strip()
        bound = parse_version(raw)
        if not bound:
            continue

        if op in (">=", ">"):
            if eol_version < bound:
                lower_ok = False
        elif op in ("<=", "<"):
            if eol_version < bound or (op == "<=" and eol_version == bound):
                upper_ok = True
        elif op == "=":
            if eol_version == bound:
                return True

    return lower_ok and upper_ok


# Relevance filters. Without these the tool reports that a 2026 advisory with
# range "< 7.1" numerically includes Symfony 3.2, which is true and useless:
# nobody is paying to secure a branch that died a decade ago. The commercially
# interesting window is a recent advisory against a branch recently enough dead
# that real systems are still on it.
MAX_ADVISORY_AGE_DAYS = 180
MAX_BRANCH_DEAD_DAYS = 1095          # ~3 years
SEVERITIES = {"critical", "high"}


def scan(max_age=MAX_ADVISORY_AGE_DAYS, max_dead=MAX_BRANCH_DEAD_DAYS,
         severities=SEVERITIES):
    findings = []
    today = datetime.now(timezone.utc).date()

    for ecosystem, package, slug, label in WATCH:
        dead = eol_releases(slug)
        if not dead:
            continue

        advs = advisories(ecosystem, package)
        if not advs:
            continue

        for adv in advs:
            published = (adv.get("published_at") or "")[:10]
            severity = (adv.get("severity") or "unknown").lower()

            if severity not in severities:
                continue
            try:
                age = (today - datetime.strptime(published, "%Y-%m-%d").date()).days
            except ValueError:
                continue
            if age > max_age:
                continue

            for vuln in adv.get("vulnerabilities") or []:
                pkg = (vuln.get("package") or {}).get("name") or ""
                if pkg.lower() != package.lower():
                    continue

                vrange = vuln.get("vulnerable_version_range")
                patched = (vuln.get("first_patched_version") or "")

                for rel in dead:
                    if rel["days_dead"] > max_dead:
                        continue
                    if not range_touches(vrange, rel["version"]):
                        continue

                    # If the published fix lands inside the EOL line itself,
                    # the vendor did patch it. Not a gap.
                    if patched and parse_version(patched)[:2] == rel["version"][:2]:
                        continue

                    findings.append({
                        "product": label,
                        "ecosystem": ecosystem,
                        "package": package,
                        "eol_line": rel["line"],
                        "eol_since": rel["eol"],
                        "days_dead": rel["days_dead"],
                        "last_release": rel["last_release"],
                        "ghsa": adv.get("ghsa_id"),
                        "cve": adv.get("cve_id"),
                        "severity": severity,
                        "published": published,
                        "summary": (adv.get("summary") or "")[:120],
                        "range": vrange,
                        "patched_in": patched or "(none)",
                    })

    rank = {"critical": 0, "high": 1, "moderate": 2, "medium": 2, "low": 3, "unknown": 4}
    findings.sort(key=lambda f: (rank.get(f["severity"], 9), f["published"]), reverse=False)
    findings.sort(key=lambda f: f["published"], reverse=True)
    findings.sort(key=lambda f: rank.get(f["severity"], 9))
    return findings


def main():
    findings = scan()

    print("eol-watch  %s" % datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"))
    print("advisories landing on end-of-life branches")
    print("=" * 78)

    if not findings:
        print("\nno exposures found")
        return 0

    seen = set()
    for f in findings:
        key = (f["ghsa"], f["eol_line"])
        if key in seen:
            continue
        seen.add(key)

        print()
        print("%-10s %s %s  (EOL %s, %d days)" % (
            f["severity"].upper(), f["product"], f["eol_line"], f["eol_since"], f["days_dead"]))
        print("  %s" % f["summary"])
        print("  %s / %s   published %s" % (f["cve"] or "no CVE", f["ghsa"], f["published"]))
        print("  range: %s" % f["range"])
        print("  fixed in: %s   last EOL release: %s" % (f["patched_in"], f["last_release"]))

    print()
    print("=" * 78)
    print("%d exposure(s) across %d product line(s)" % (
        len(seen), len({f["eol_line"] + f["product"] for f in findings})))
    return 0


if __name__ == "__main__":
    import urllib.parse
    sys.exit(main())
