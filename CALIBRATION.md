# Calibration

How often this tool is wrong, measured rather than asserted.

A detector that nobody scores drifts into decoration. Every candidate that gets
manually checked is recorded here with its outcome, whatever that outcome is.
Refutations are the point of the file, not an embarrassment in it.

---

## Scoring

Each candidate ends in exactly one state.

| State | Meaning |
|---|---|
| **CONFIRMED** | Vulnerable construct found in the dead branch and a patch written |
| **REFUTED** | Checked properly, the construct is not there, no exposure |
| **UNREACHABLE** | Construct present but not reachable in that branch's configuration |
| **OPEN** | Flagged, not yet checked |

Precision counts CONFIRMED against everything resolved. UNREACHABLE counts
against it, because a candidate nobody can exploit still wasted the time.

---

## Results

| Date | Product | Advisory | Flagged by | Outcome | Notes |
|---|---|---|---|---|---|
| 2026-11-09 | Joomla 3.10 | CVE-2026-92222 | manual | **CONFIRMED** | Advisory says 4.0.0+. Construct present in 3.10, validator already supports the fix, dangerous schemes demonstrably accepted. Patched as JSEC-0005. |
| 2026-11-09 | Joomla 3.10 | CVE-2026-90906 | manual | **CONFIRMED** | `HTMLHelper::link()` interpolates `$url` with no escaping. Patched as JSEC-0001. |
| 2026-11-09 | Joomla 3.10 | CVE-2026-90907 | manual | **CONFIRMED** | `profile.save` checks the CSRF token, never the login state. Patched as JSEC-0002. |
| 2026-11-09 | Joomla 3.10 | CVE-2026-73373 | manual | **CONFIRMED** | Forbidden extension list missing shtml and friends. Patched as JSEC-0003. |
| 2026-11-09 | Joomla 3.10 | CVE-2026-92231 | manual | **CONFIRMED** | Entity decode mismatch in `checkAttribute()`. Patched as JSEC-0004, though end-to-end exploitability remains unproven. |
| 2026-11-09 | Joomla 3.10 | CVE-2026-92232 | manual | **REFUTED** | Range claims 1.5.0 onward. 3.10 has no `cleanAttribute()` and no data-URI handling, so there is no vulnerable path. Range was conservative, not a finding. |

**Precision so far: 5 of 6 resolved, 83%.**

Six data points is not a measurement, it is an anecdote. The number is here to
be moved by the next twenty.

---

## Known failure modes

Written down so the number above is interpretable.

**Range inclusion is not code inclusion.** The dominant false positive. An
advisory saying `< 8.2.6` numerically includes every PrestaShop 1.7 release,
but 8.x and 9.x carry architecture 1.7 never had. Expect a meaningful share of
candidates to refute on this alone.

**Severity is inherited, not recomputed.** A critical rating reflects impact on
the branch the vendor assessed. The same construct in an older branch may be
unreachable, or worse. The tool copies the vendor's rating because inventing
its own would be false precision.

**Recency filters trade recall for usefulness.** Advisories older than 180 days
and branches dead more than about three years are dropped. That is a commercial
judgement, not a security one: nobody pays to secure a branch dead a decade.
Real exposures are being hidden by this and that is accepted deliberately.

**Package to product mapping is hand-maintained.** The two namespaces share no
identifiers. Anything not in the watch list is invisible, so absence from this
report means nothing at all.

**Deleted branches break the workflow, not the detection.** PrestaShop removed
every `1.7.x` branch. The tag survives, so a patch is possible, but there is no
branch to track or contribute to.

---

## What would make this file dishonest

- Recording CONFIRMED on the strength of a range rather than a code reading.
- Quietly dropping candidates that turned out wrong.
- Reporting precision without the sample size next to it.
- Letting OPEN accumulate so the denominator stays flattering.

If the precision here ever climbs toward 100%, assume the scoring broke before
assuming the tool improved.
