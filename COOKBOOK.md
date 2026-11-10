# The cookbook

How to turn a flagged candidate into something real. Written to be followed by
someone who has never seen the codebase in question, because that is the normal
case.

The tool finds candidates. It cannot confirm them. Everything below is the part
a person has to do, and it is the part that carries all the value.

---

## 0. The rule that decides whether to start at all

**Patch a vacuum, never an occupied market.**

Search the project name with "extended support", "ELTS", "LTS" and "end of
life". Then:

- Someone is **currently selling** support for that branch → **stop.** Free
  patches there take revenue from whoever funds the project. TYPO3 is the clean
  example: v12.4 free support ended April 2026, and TYPO3 GmbH sells ELTS to
  2029. Everything else about it fits. It is still the wrong target.
- A paid programme **existed and lapsed** → **best possible signal.** It proves
  people paid, and that nobody serves them now. Joomla 3's eLTS ended February
  2025.
- **Nothing ever existed** → fine, but check nobody is doing it for free
  either. Magento 1 looks abandoned; OpenMage ships CVE fixes free and faster
  than you would.

Do this before anything else. It takes two minutes and it is the only step that
can invalidate all the others.

---

## 1. Read the advisory, not the range

The range is the single most misleading field in the whole dataset. It
describes **what the vendor reviewed**, not where the bug lives. It fails in
both directions:

**Too wide.** CVE-2026-92232 claims Joomla 1.5.0 onward. Joomla 3.10 has no
`cleanAttribute()` method and no data-URI handling at all, so there is no
vulnerable code path. The lower bound was a conservative "everything before the
fix", not a finding.

**Too narrow.** CVE-2026-92222 says Joomla 4.0.0 and later. The construct is
present in 3.10, the validator already supports the fix, and the dangerous
schemes are demonstrably accepted. Joomla does not assess EOL branches, so the
bound describes their review scope and nothing more.

The second failure is the dangerous one. A too-wide range wastes your time. A
too-narrow range produces a reassuring false negative, and nobody goes looking
for something they have already been told does not apply to them.

---

## 2. Find the actual fix

Some projects make this easy. Some do not.

- **Fix in the commit log** → read it directly.
- **Fix squashed into a release commit** → read the release diff instead.
  Joomla does this. The public commit list between 5.4.8 and 5.4.9 contains
  translation updates and template manager fixes and nothing resembling
  security work. The diff of 268 files contains the fix.
- **Filter the diff by filename** before reading it. For an SSRF, anything
  matching `http|uri|url|feed|request|transport`. The signal is usually a tiny
  change in an unexpected place: four files, one line added to each.
- **Expect near misses.** The same Joomla release changed `Uri.php` with a new
  unit test, which looks exactly like a URL-validation security fix and is a
  different one. It also cast a `preg_match` result to bool, which looks like
  input hardening and is a static-analysis cleanup. Attributing either would
  have produced a confident, wrong patch.

---

## 3. Confirm the construct exists in the dead branch

Check out the EOL tag and look for the specific thing the fix changed. Not
something similar. The thing.

Three outcomes:

- **Present and identical** → backport the upstream fix.
- **Present but different shape** → backport the *intent*, and write down every
  deviation and why. PHP version floors force this constantly.
- **Absent** → not applicable. Record it. A documented "we looked and it does
  not apply" is worth as much as a patch and costs a tenth as much.

Beware deleted branches. PrestaShop removed every `1.7.x` branch from the
repository; only the `1.7.8.11` tag survives. You can patch against a tag, but
there is nowhere for anyone to contribute.

---

## 4. Prove it twice

Two suites, and they answer different questions. Shipping only the first is the
classic mistake.

**Does the attack work, and does it stop working?** Run the probe against a
stock tree and confirm it reports vulnerable. If a probe reports clean on an
unpatched install, the probe is broken and would have passed anything.

**Does ordinary software still work?** This is the one people skip. A patch can
close every vector and break every page. The Joomla set needed 40 assertions
drawn from real core call sites, and they caught the thing that mattered:
`JRoute::_()` already HTML-escapes ampersands, so re-encoding would have turned
every paginated link into `&amp;amp;`.

Then install it and click through. Unit tests never start the application.

---

## 5. Preserve bugs on purpose

Legacy code is full of things that are wrong and have been wrong for twenty
years. Other code depends on them.

osCommerce guards an assignment with `gettype($x) != "user function"`.
`gettype()` has not returned that since PHP 3, so the guard has never fired. A
reasonable developer tidying up would make it work, and silently change
behaviour on every installation.

Capture current behaviour as tests **including the bugs**, then assert them
explicitly so a future "fix" cannot pass quietly. Document each one and let the
owner decide. You are not there to improve the software, you are there to move
it without changing it.

---

## 6. Say what you did not do

Every claim invites someone to check it, so bound them before they do.

The Joomla set states plainly that JSEC-0004's end-to-end exploitability is
unproven: the unit-level bypass is real, but `clean()` dropped the payload
anyway in both configurations tested. That admission costs nothing and buys
every other claim credibility.

Likewise prior art. Publishing "nobody is patching this" when someone is makes
you look careless at best. mySites.guru had covered CVE-2026-92222 for Joomla 3
a month earlier. Finding that out before publishing is a footnote. Finding out
after is a retraction.

---

## 7. Only then, publish

- The patches, with the generator that produced them, so anyone can rebuild
  them byte-identically.
- The advisories, including the ones you decided **not** to patch.
- The probe, so a stranger can check their own install without trusting you.
- CI that re-runs the whole claim on a schedule, because a patch set nobody
  re-verifies is one nobody should trust.

---

## The honest economics

Steps 1 through 6 take days per advisory and cannot be automated. The tool
collapses the *finding* from hours to seconds and leaves the *verifying*
untouched.

That is the right division. Finding is cheap and nobody pays for it. Verifying
is expensive, and it is the whole product.
