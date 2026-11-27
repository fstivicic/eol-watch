# EOL Watch

Security advisories landing on end-of-life branches, where no fix is being shipped for the dead line.

Updated automatically. Last run **2026-11-27 07:05 UTC**.

> **These are candidates, not confirmed exposures.** A version range is a statement about what a vendor reviewed, not about where a bug lives. Every entry here needs the actual fix read and the vulnerable construct located in the dead branch before it means anything. See [the cookbook](COOKBOOK.md) for how that is done, and [calibration](CALIBRATION.md) for how often this tool is wrong.

**15 advisories** currently land on dead branches. 4 critical, 11 high.

---

### Next.js 14, 13

**CRITICAL** &middot; GHSA-2xp9-vwfh-vxw4

Next.js: Unauthenticated Remote Code Execution in Image Optimization API when AVIF files are used

| | |
|---|---|
| Advisory | [GHSA-2xp9-vwfh-vxw4](https://github.com/advisories/GHSA-2xp9-vwfh-vxw4) |
| Published | 2026-09-08 |
| Affected range | `>= 10.0.0, < 15.5.24` |
| Fixed in | `15.5.24` |
| Package | `next` (npm) |

Dead branches in range:

- **14** &mdash; EOL since 2025-10-26 (397 days), last release `14.2.35`
- **13** &mdash; EOL since 2024-12-21 (706 days), last release `13.5.11`

---

### Next.js 14, 13

**CRITICAL** &middot; CVE-2026-75604

Next.js: Unauthenticated Remote Code Execution on windows-hosted servers

| | |
|---|---|
| Advisory | [GHSA-p293-qw3h-jr36](https://github.com/advisories/GHSA-p293-qw3h-jr36) |
| Published | 2026-09-08 |
| Affected range | `>= 13.4.0, < 15.5.24` |
| Fixed in | `15.5.24` |
| Package | `next` (npm) |

Dead branches in range:

- **14** &mdash; EOL since 2025-10-26 (397 days), last release `14.2.35`
- **13** &mdash; EOL since 2024-12-21 (706 days), last release `13.5.11`

---

### Next.js 14, 13

**CRITICAL** &middot; GHSA-2464-fhr4-w9xw

Next.js: Unauthenticated Remote Code Execution in Image Optimization API when SVG files are used

| | |
|---|---|
| Advisory | [GHSA-2464-fhr4-w9xw](https://github.com/advisories/GHSA-2464-fhr4-w9xw) |
| Published | 2026-10-22 |
| Affected range | `>= 10.0.0, <= 15.5.27` |
| Fixed in | `15.5.28` |
| Package | `next` (npm) |

Dead branches in range:

- **14** &mdash; EOL since 2025-10-26 (397 days), last release `14.2.35`
- **13** &mdash; EOL since 2024-12-21 (706 days), last release `13.5.11`

---

### Laravel 9

**CRITICAL** &middot; CVE-2026-114509

Laravel TokenGuard authentication bypass through non-string API credentials

| | |
|---|---|
| Advisory | [GHSA-f9x3-7vq9-cph6](https://github.com/advisories/GHSA-f9x3-7vq9-cph6) |
| Published | 2026-10-23 |
| Affected range | `< 10.50.4` |
| Fixed in | `10.50.4` |
| Package | `laravel/framework` (composer) |

Dead branches in range:

- **9** &mdash; EOL since 2024-02-06 (1025 days), last release `9.52.24`

---

### Symfony 7.3, 7.2, 7.1, 7.0, 6.3

**HIGH** &middot; CVE-2026-48489

Symfony: Security Firewall Bypass via failure_forward Subrequest: Unauthenticated Access to access_control-Protected GET

| | |
|---|---|
| Advisory | [GHSA-6h46-9jf5-q59x](https://github.com/advisories/GHSA-6h46-9jf5-q59x) |
| Published | 2026-06-15 |
| Affected range | `>= 6.0.0, < 6.4.41` |
| Fixed in | `6.4.41` |
| Package | `symfony/symfony` (composer) |

Dead branches in range:

- **7.3** &mdash; EOL since 2026-01-31 (300 days), last release `7.3.11`
- **7.2** &mdash; EOL since 2025-07-31 (484 days), last release `7.2.9`
- **7.1** &mdash; EOL since 2025-01-31 (665 days), last release `7.1.11`
- **7.0** &mdash; EOL since 2024-07-31 (849 days), last release `7.0.10`
- **6.3** &mdash; EOL since 2024-01-31 (1031 days), last release `6.3.12`

---

### Laravel 11, 10, 9

**HIGH** &middot; GHSA-5vg9-5847-vvmq

Laravel Framework: CRLF injection in default email rule 

| | |
|---|---|
| Advisory | [GHSA-5vg9-5847-vvmq](https://github.com/advisories/GHSA-5vg9-5847-vvmq) |
| Published | 2026-06-17 |
| Affected range | `< 12.60.0` |
| Fixed in | `12.60.0` |
| Package | `laravel/framework` (composer) |

Dead branches in range:

- **11** &mdash; EOL since 2026-03-12 (260 days), last release `11.57.2`
- **10** &mdash; EOL since 2025-02-04 (661 days), last release `10.50.5`
- **9** &mdash; EOL since 2024-02-06 (1025 days), last release `9.52.24`

---

### Next.js 14

**HIGH** &middot; CVE-2026-64649

Next.js: Server-Side Request Forgery in Server Actions on custom servers

| | |
|---|---|
| Advisory | [GHSA-89xv-2m56-2m9x](https://github.com/advisories/GHSA-89xv-2m56-2m9x) |
| Published | 2026-07-22 |
| Affected range | `>= 14.1.1, < 15.5.21` |
| Fixed in | `15.5.21` |
| Package | `next` (npm) |

Dead branches in range:

- **14** &mdash; EOL since 2025-10-26 (397 days), last release `14.2.35`

---

### Next.js 14, 13

**HIGH** &middot; CVE-2026-64645

Next.js: Server-Side Request Forgery in rewrites via attacker-controlled destination hostname

| | |
|---|---|
| Advisory | [GHSA-p9j2-gv94-2wf4](https://github.com/advisories/GHSA-p9j2-gv94-2wf4) |
| Published | 2026-07-22 |
| Affected range | `>= 12.0.0, < 15.5.21` |
| Fixed in | `15.5.21` |
| Package | `next` (npm) |

Dead branches in range:

- **14** &mdash; EOL since 2025-10-26 (397 days), last release `14.2.35`
- **13** &mdash; EOL since 2024-12-21 (706 days), last release `13.5.11`

---

### Next.js 14, 13

**HIGH** &middot; CVE-2026-64641

Next.js: Denial of Service in App Router using Server Actions

| | |
|---|---|
| Advisory | [GHSA-m99w-x7hq-7vfj](https://github.com/advisories/GHSA-m99w-x7hq-7vfj) |
| Published | 2026-07-22 |
| Affected range | `>= 13.0.0, < 15.5.21` |
| Fixed in | `15.5.21` |
| Package | `next` (npm) |

Dead branches in range:

- **14** &mdash; EOL since 2025-10-26 (397 days), last release `14.2.35`
- **13** &mdash; EOL since 2024-12-21 (706 days), last release `13.5.11`

---

### Django 4.2, 5.1, 5.0, 3.2, 4.1

**HIGH** &middot; CVE-2026-15307

Django GeoDjango spatial lookups allow file writes and outbound requests through GDAL raster parsing

| | |
|---|---|
| Advisory | [GHSA-wvqv-fj8w-qmhm](https://github.com/advisories/GHSA-wvqv-fj8w-qmhm) |
| Published | 2026-08-04 |
| Affected range | `< 5.2.17` |
| Fixed in | `5.2.17` |
| Package | `django` (pip) |

Dead branches in range:

- **4.2** &mdash; EOL since 2026-04-07 (234 days), last release `4.2.30`
- **5.1** &mdash; EOL since 2025-12-03 (359 days), last release `5.1.15`
- **5.0** &mdash; EOL since 2025-04-02 (604 days), last release `5.0.14`
- **3.2** &mdash; EOL since 2024-04-01 (970 days), last release `3.2.25`
- **4.1** &mdash; EOL since 2023-12-01 (1092 days), last release `4.1.13`

---

### Next.js 14, 13

**HIGH** &middot; CVE-2026-94482

Next.js: Denial of Service in App Router using Server Actions

| | |
|---|---|
| Advisory | [GHSA-p3m5-59mp-jv5r](https://github.com/advisories/GHSA-p3m5-59mp-jv5r) |
| Published | 2026-10-22 |
| Affected range | `>= 13.0.0, <= 15.5.27` |
| Fixed in | `15.5.28` |
| Package | `next` (npm) |

Dead branches in range:

- **14** &mdash; EOL since 2025-10-26 (397 days), last release `14.2.35`
- **13** &mdash; EOL since 2024-12-21 (706 days), last release `13.5.11`

---

### Symfony 8.0, 7.3, 7.2, 7.1, 7.0, 6.3

**HIGH** &middot; CVE-2026-109413

Symfony: Unbounded Recursion in the YAML Inline Lexer Lets a Single Document Crash the Process

| | |
|---|---|
| Advisory | [GHSA-2v3c-qxhr-7vpv](https://github.com/advisories/GHSA-2v3c-qxhr-7vpv) |
| Published | 2026-10-27 |
| Affected range | `>= 6.0.0, < 6.4.45` |
| Fixed in | `6.4.45` |
| Package | `symfony/symfony` (composer) |

Dead branches in range:

- **8.0** &mdash; EOL since 2026-07-31 (119 days), last release `8.0.16`
- **7.3** &mdash; EOL since 2026-01-31 (300 days), last release `7.3.11`
- **7.2** &mdash; EOL since 2025-07-31 (484 days), last release `7.2.9`
- **7.1** &mdash; EOL since 2025-01-31 (665 days), last release `7.1.11`
- **7.0** &mdash; EOL since 2024-07-31 (849 days), last release `7.0.10`
- **6.3** &mdash; EOL since 2024-01-31 (1031 days), last release `6.3.12`

---

### Symfony 8.0, 7.3, 7.2, 7.1, 7.0, 6.3

**HIGH** &middot; CVE-2026-108082

Symfony: ReDoS in HeaderUtils::split() Reachable Through the Cache-Control Request Header

| | |
|---|---|
| Advisory | [GHSA-r925-mgvr-h9cc](https://github.com/advisories/GHSA-r925-mgvr-h9cc) |
| Published | 2026-10-27 |
| Affected range | `>= 6.0.1, < 6.4.46` |
| Fixed in | `6.4.46` |
| Package | `symfony/symfony` (composer) |

Dead branches in range:

- **8.0** &mdash; EOL since 2026-07-31 (119 days), last release `8.0.16`
- **7.3** &mdash; EOL since 2026-01-31 (300 days), last release `7.3.11`
- **7.2** &mdash; EOL since 2025-07-31 (484 days), last release `7.2.9`
- **7.1** &mdash; EOL since 2025-01-31 (665 days), last release `7.1.11`
- **7.0** &mdash; EOL since 2024-07-31 (849 days), last release `7.0.10`
- **6.3** &mdash; EOL since 2024-01-31 (1031 days), last release `6.3.12`

---

### SilverStripe 6.1, 6.0

**HIGH** &middot; CVE-2026-91115

Silverstripe Framework: RCE via i18nTextCollectorTask writer parameter

| | |
|---|---|
| Advisory | [GHSA-c94f-87xg-65wf](https://github.com/advisories/GHSA-c94f-87xg-65wf) |
| Published | 2026-11-16 |
| Affected range | `>= 6.0.0, < 6.2.13` |
| Fixed in | `6.2.13` |
| Package | `silverstripe/framework` (composer) |

Dead branches in range:

- **6.1** &mdash; EOL since 2026-10-18 (40 days), last release `6.1.0`
- **6.0** &mdash; EOL since 2026-04-14 (227 days), last release `6.0.0`

---

### Contao 5.6, 5.5, 5.4, 5.2

**HIGH** &middot; CVE-2026-104883

contao/core-bundle: Non-admin users can self-grant permissions that implicitly make them administrators

| | |
|---|---|
| Advisory | [GHSA-r9qp-pqx5-8369](https://github.com/advisories/GHSA-r9qp-pqx5-8369) |
| Published | 2026-11-20 |
| Affected range | `>= 5.0.0, < 5.3.50` |
| Fixed in | `5.3.50` |
| Package | `contao/core-bundle` (composer) |

Dead branches in range:

- **5.6** &mdash; EOL since 2026-02-14 (286 days), last release `5.6.11`
- **5.5** &mdash; EOL since 2025-08-14 (470 days), last release `5.5.16`
- **5.4** &mdash; EOL since 2025-02-14 (651 days), last release `5.4.14`
- **5.2** &mdash; EOL since 2024-02-14 (1017 days), last release `5.2.10`

