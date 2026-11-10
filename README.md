# EOL Watch

Security advisories that land on end-of-life branches, where no fix is being
shipped for the dead line.

**[Current exposures](https://fstivicic.github.io/eol-watch/)** ·
[JSON](https://fstivicic.github.io/eol-watch/data.json) ·
[RSS](https://fstivicic.github.io/eol-watch/feed.xml) ·
[Cookbook](COOKBOOK.md) ·
[Calibration](CALIBRATION.md)

---

## The gap

When a project ships a breaking major release, it strands its existing install
base on a published schedule. Those branches keep running real systems, and
they keep appearing in new advisories. Nobody ships them a fix.

Two shapes, both real, both found by hand before this existed:

**The range excludes the dead branch, wrongly.** CVE-2026-92222 is published as
affecting Joomla 4.0.0 and later. The vulnerable construct is present in 3.10,
the validator already supports the fix, and the dangerous schemes are
demonstrably accepted. Joomla does not assess EOL branches, so the bound
describes their review scope, not where the bug lives.

**The range includes the dead branch, pointlessly.** PrestaShop advisories list
ranges like `< 8.2.6`, which numerically covers every 1.7 release. No 1.7 fix is
ever published. Security maintenance for 1.7 stopped in June 2025.

This tool finds both automatically by joining two public sources:

- [endoflife.date](https://endoflife.date) for which release lines are dead
- [GitHub Advisory Database](https://github.com/advisories) for what exists

## These are candidates, not confirmed exposures

A version range is a statement about what a vendor reviewed. It is not proof
that vulnerable code exists in a dead branch, and treating it as proof is the
mistake this project is built around avoiding.

Every entry needs the actual fix read and the construct located in the dead
branch before it means anything. That part is manual, it takes days, and it is
where all the value is. [The cookbook](COOKBOOK.md) is how it is done.
[Calibration](CALIBRATION.md) records how often the tool turns out to be wrong.

## Running it

```sh
python publish.py
```

No dependencies beyond the standard library. Writes every channel from one
scan, so no output can drift from another.

| Output | Channel |
|---|---|
| `docs/index.md` | Human page via GitHub Pages |
| `docs/data.json` | Machine readable, stable shape |
| `docs/feed.xml` | RSS, syndicates without permission |
| `out/post-short.txt` | Short post |
| `out/post-long.md` | Forum or newsletter |
| `out/digest.txt` | Plain text email |
| `history/*.json` | The archive, which is the asset that accrues |

Tuning lives at the top of `scan()` in `eolwatch.py`: advisory age, how long a
branch may have been dead, which severities count. The watch list is
hand-curated in `WATCH` because package names and EOL product slugs share no
identifiers.

## Before patching anything

Read [step 0 of the cookbook](COOKBOOK.md). If someone is currently selling
support for a branch, publishing free patches for it takes money from whoever
funds that project. A lapsed paid programme is the opposite: proof people paid,
and that nobody serves them now.

## Licence

MIT. The advisory data belongs to its publishers.
