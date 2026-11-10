# EOL Watch

Security advisories landing on end-of-life branches, where no fix is being shipped for the dead line.

Updated automatically. Last run **2026-11-10 13:28 UTC**.

> **These are candidates, not confirmed exposures.** A version range is a statement about what a vendor reviewed, not about where a bug lives. Every entry here needs the actual fix read and the vulnerable construct located in the dead branch before it means anything. See [the cookbook](COOKBOOK.md) for how that is done, and [calibration](CALIBRATION.md) for how often this tool is wrong.

**17 advisories** currently land on dead branches. 5 critical, 12 high.

---

### Drupal 10.3, 11.0, 10.2, 10.1, 10.0

**CRITICAL** &middot; CVE-2026-9082

Drupal Core has a SQL Injection issue

| | |
|---|---|
| Advisory | [GHSA-ghwc-95x2-682j](https://github.com/advisories/GHSA-ghwc-95x2-682j) |
| Published | 2026-05-20 |
| Affected range | `>= 8.9.0, < 10.4.10` |
| Fixed in | `10.4.10` |
| Package | `drupal/core` (composer) |

Dead branches in range:

- **10.3** &mdash; EOL since 2025-06-16 (512 days), last release `10.3.14`
- **11.0** &mdash; EOL since 2025-06-16 (512 days), last release `11.0.13`
- **10.2** &mdash; EOL since 2024-12-17 (693 days), last release `10.2.12`
- **10.1** &mdash; EOL since 2024-06-20 (873 days), last release `10.1.8`
- **10.0** &mdash; EOL since 2023-12-15 (1061 days), last release `10.0.11`

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

- **14** &mdash; EOL since 2025-10-26 (380 days), last release `14.2.35`
- **13** &mdash; EOL since 2024-12-21 (689 days), last release `13.5.11`

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

- **14** &mdash; EOL since 2025-10-26 (380 days), last release `14.2.35`
- **13** &mdash; EOL since 2024-12-21 (689 days), last release `13.5.11`

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

- **14** &mdash; EOL since 2025-10-26 (380 days), last release `14.2.35`
- **13** &mdash; EOL since 2024-12-21 (689 days), last release `13.5.11`

---

### Laravel 11, 10, 9

**CRITICAL** &middot; CVE-2026-114509

Laravel TokenGuard authentication bypass through non-string API credentials

| | |
|---|---|
| Advisory | [GHSA-f9x3-7vq9-cph6](https://github.com/advisories/GHSA-f9x3-7vq9-cph6) |
| Published | 2026-10-23 |
| Affected range | `< 12.68.0` |
| Fixed in | `12.68.0` |
| Package | `laravel/framework` (composer) |

Dead branches in range:

- **11** &mdash; EOL since 2026-03-12 (243 days), last release `11.57.1`
- **10** &mdash; EOL since 2025-02-04 (644 days), last release `10.50.4`
- **9** &mdash; EOL since 2024-02-06 (1008 days), last release `9.52.23`

---

### Symfony 7.3, 7.2, 7.1, 7.0, 6.3, 4.4

**HIGH** &middot; CVE-2026-45077

Symfony has Unauthenticated PHP Object Deserialization in MonologBridge server:log Listener

| | |
|---|---|
| Advisory | [GHSA-m7v2-7gxm-vc2v](https://github.com/advisories/GHSA-m7v2-7gxm-vc2v) |
| Published | 2026-05-27 |
| Affected range | `< 5.4.52` |
| Fixed in | `5.4.52` |
| Package | `symfony/symfony` (composer) |

Dead branches in range:

- **7.3** &mdash; EOL since 2026-01-31 (283 days), last release `7.3.11`
- **7.2** &mdash; EOL since 2025-07-31 (467 days), last release `7.2.9`
- **7.1** &mdash; EOL since 2025-01-31 (648 days), last release `7.1.11`
- **7.0** &mdash; EOL since 2024-07-31 (832 days), last release `7.0.10`
- **6.3** &mdash; EOL since 2024-01-31 (1014 days), last release `6.3.12`
- **4.4** &mdash; EOL since 2023-11-21 (1085 days), last release `4.4.51`

---

### Symfony 7.3, 7.2, 7.1, 7.0, 6.3, 4.4

**HIGH** &middot; CVE-2026-45067

Symfony has Email Header / SMTP Command Injection via CRLF in Symfony\Component\Mime\Address

| | |
|---|---|
| Advisory | [GHSA-qpmx-3rfj-7rhv](https://github.com/advisories/GHSA-qpmx-3rfj-7rhv) |
| Published | 2026-05-27 |
| Affected range | `< 5.4.52` |
| Fixed in | `5.4.52` |
| Package | `symfony/symfony` (composer) |

Dead branches in range:

- **7.3** &mdash; EOL since 2026-01-31 (283 days), last release `7.3.11`
- **7.2** &mdash; EOL since 2025-07-31 (467 days), last release `7.2.9`
- **7.1** &mdash; EOL since 2025-01-31 (648 days), last release `7.1.11`
- **7.0** &mdash; EOL since 2024-07-31 (832 days), last release `7.0.10`
- **6.3** &mdash; EOL since 2024-01-31 (1014 days), last release `6.3.12`
- **4.4** &mdash; EOL since 2023-11-21 (1085 days), last release `4.4.51`

---

### Symfony 7.3, 7.2, 7.1, 7.0, 6.3, 4.4

**HIGH** &middot; CVE-2026-45063

Symfony Vulnerable to Identity Spoofing via Unanchored DN Regex in X509Authenticator

| | |
|---|---|
| Advisory | [GHSA-ph86-p8f6-f9r2](https://github.com/advisories/GHSA-ph86-p8f6-f9r2) |
| Published | 2026-05-27 |
| Affected range | `< 5.4.52` |
| Fixed in | `5.4.52` |
| Package | `symfony/symfony` (composer) |

Dead branches in range:

- **7.3** &mdash; EOL since 2026-01-31 (283 days), last release `7.3.11`
- **7.2** &mdash; EOL since 2025-07-31 (467 days), last release `7.2.9`
- **7.1** &mdash; EOL since 2025-01-31 (648 days), last release `7.1.11`
- **7.0** &mdash; EOL since 2024-07-31 (832 days), last release `7.0.10`
- **6.3** &mdash; EOL since 2024-01-31 (1014 days), last release `6.3.12`
- **4.4** &mdash; EOL since 2023-11-21 (1085 days), last release `4.4.51`

---

### Symfony 7.3, 7.2, 7.1, 7.0, 6.3, 4.4

**HIGH** &middot; CVE-2026-48489

Symfony: Security Firewall Bypass via failure_forward Subrequest: Unauthenticated Access to access_control-Protected GET

| | |
|---|---|
| Advisory | [GHSA-6h46-9jf5-q59x](https://github.com/advisories/GHSA-6h46-9jf5-q59x) |
| Published | 2026-06-15 |
| Affected range | `< 5.4.53` |
| Fixed in | `5.4.53` |
| Package | `symfony/symfony` (composer) |

Dead branches in range:

- **7.3** &mdash; EOL since 2026-01-31 (283 days), last release `7.3.11`
- **7.2** &mdash; EOL since 2025-07-31 (467 days), last release `7.2.9`
- **7.1** &mdash; EOL since 2025-01-31 (648 days), last release `7.1.11`
- **7.0** &mdash; EOL since 2024-07-31 (832 days), last release `7.0.10`
- **6.3** &mdash; EOL since 2024-01-31 (1014 days), last release `6.3.12`
- **4.4** &mdash; EOL since 2023-11-21 (1085 days), last release `4.4.51`

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

- **11** &mdash; EOL since 2026-03-12 (243 days), last release `11.57.1`
- **10** &mdash; EOL since 2025-02-04 (644 days), last release `10.50.4`
- **9** &mdash; EOL since 2024-02-06 (1008 days), last release `9.52.23`

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

- **14** &mdash; EOL since 2025-10-26 (380 days), last release `14.2.35`

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

- **14** &mdash; EOL since 2025-10-26 (380 days), last release `14.2.35`
- **13** &mdash; EOL since 2024-12-21 (689 days), last release `13.5.11`

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

- **14** &mdash; EOL since 2025-10-26 (380 days), last release `14.2.35`
- **13** &mdash; EOL since 2024-12-21 (689 days), last release `13.5.11`

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

- **4.2** &mdash; EOL since 2026-04-07 (217 days), last release `4.2.30`
- **5.1** &mdash; EOL since 2025-12-03 (342 days), last release `5.1.15`
- **5.0** &mdash; EOL since 2025-04-02 (587 days), last release `5.0.14`
- **3.2** &mdash; EOL since 2024-04-01 (953 days), last release `3.2.25`
- **4.1** &mdash; EOL since 2023-12-01 (1075 days), last release `4.1.13`

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

- **14** &mdash; EOL since 2025-10-26 (380 days), last release `14.2.35`
- **13** &mdash; EOL since 2024-12-21 (689 days), last release `13.5.11`

---

### Symfony 8.0, 7.3, 7.2, 7.1, 7.0, 6.3, 4.4

**HIGH** &middot; CVE-2026-109413

Symfony: Unbounded Recursion in the YAML Inline Lexer Lets a Single Document Crash the Process

| | |
|---|---|
| Advisory | [GHSA-2v3c-qxhr-7vpv](https://github.com/advisories/GHSA-2v3c-qxhr-7vpv) |
| Published | 2026-10-27 |
| Affected range | `>= 2.0.0, < 5.4.54` |
| Fixed in | `5.4.54` |
| Package | `symfony/symfony` (composer) |

Dead branches in range:

- **8.0** &mdash; EOL since 2026-07-31 (102 days), last release `8.0.16`
- **7.3** &mdash; EOL since 2026-01-31 (283 days), last release `7.3.11`
- **7.2** &mdash; EOL since 2025-07-31 (467 days), last release `7.2.9`
- **7.1** &mdash; EOL since 2025-01-31 (648 days), last release `7.1.11`
- **7.0** &mdash; EOL since 2024-07-31 (832 days), last release `7.0.10`
- **6.3** &mdash; EOL since 2024-01-31 (1014 days), last release `6.3.12`
- **4.4** &mdash; EOL since 2023-11-21 (1085 days), last release `4.4.51`

---

### Symfony 8.0, 7.3, 7.2, 7.1, 7.0, 6.3, 4.4

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

- **8.0** &mdash; EOL since 2026-07-31 (102 days), last release `8.0.16`
- **7.3** &mdash; EOL since 2026-01-31 (283 days), last release `7.3.11`
- **7.2** &mdash; EOL since 2025-07-31 (467 days), last release `7.2.9`
- **7.1** &mdash; EOL since 2025-01-31 (648 days), last release `7.1.11`
- **7.0** &mdash; EOL since 2024-07-31 (832 days), last release `7.0.10`
- **6.3** &mdash; EOL since 2024-01-31 (1014 days), last release `6.3.12`
- **4.4** &mdash; EOL since 2023-11-21 (1085 days), last release `4.4.51`

