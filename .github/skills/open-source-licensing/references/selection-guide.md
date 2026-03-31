# License Selection Guide

Detailed comparison and use-case guidance for choosing the right license.

## Table of Contents

1. [License Spectrum](#license-spectrum)
2. [Permissive Licenses](#permissive-licenses)
3. [Copyleft Licenses](#copyleft-licenses)
4. [Non-Software Licenses](#non-software-licenses)
5. [Special Situations](#special-situations)
6. [Compatibility Matrix](#compatibility-matrix)
7. [By Ecosystem / Community](#by-ecosystem--community)

---

## License Spectrum

```
Most permissive ←————————————————————————————→ Most restrictive

Unlicense  MIT/ISC  BSD  BSL  Apache2  MPL2  LGPL  GPL  AGPL
│          │        │    │    │        │     │     │    │
Public     Do what  Same Same Adds     File  Lib   All  All + SaaS
domain     you want      +no  patents  level only  deriv
           no sue   endorse            copyleft
```

---

## Permissive Licenses

These licenses impose minimal requirements. Derivatives can be closed-source.

### MIT License
**Best for:** Libraries, utilities, frameworks, small scripts  
**Used by:** React, Rails, jQuery, .NET, Babel  
**Conditions:** Include copyright + license notice in all copies  
**No patent grant:** If a contributor has relevant patents, MIT doesn't protect you  

**Choose MIT when:**
- You want maximum adoption with minimum friction
- Your audience includes corporate developers
- You don't care if someone builds a closed-source product from your code
- You want the simplest, most universally understood license

**Avoid MIT when:**
- Your project involves patented algorithms (use Apache 2.0)
- You want a non-endorsement clause (use BSD-3)

### Apache License 2.0
**Best for:** SDKs, enterprise libraries, corporate-backed projects  
**Used by:** Android, Kubernetes, TensorFlow, Swift, VS Code  
**Key advantage:** Explicit patent grant + patent retaliation clause  
**Conditions:** Include copyright + license notice; mark changed files; include NOTICE if provided  

**Choose Apache 2.0 when:**
- Your project may be used by large companies concerned about patent litigation
- You're building developer tools or SDKs
- You want more legal clarity than MIT provides
- Your project receives contributions from corporations

### BSD 2-Clause (Simplified BSD)
**Best for:** Unix-derived tools, networking software  
**Conditions:** Keep copyright notice in source and binaries  
**Vs MIT:** Functionally nearly identical; MIT is more widely recognized today

### BSD 3-Clause (Modified BSD)
**Best for:** Academic software, tools used in products where endorsement matters  
**Extra clause:** Names of contributors may not be used to endorse derived products  
**Used by:** FreeBSD, NumPy, SciPy  

**Choose BSD-3 when:**
- You're an academic institution
- Brand protection matters (prevent "Powered by [Your Project]" without permission)

### ISC License
**Best for:** Node.js ecosystem, Unix utilities  
**Functionally:** Same as MIT, slightly shorter  
**Used by:** OpenBSD, many npm packages  

### Boost Software License 1.0
**Best for:** C++ libraries intended as header-only or compiled  
**Key feature:** No copyright notice required in binary distributions  
**Used by:** Boost C++ Libraries, many C++ projects  

---

## Copyleft Licenses

These licenses require derivative works to be open source.

### Mozilla Public License 2.0 (MPL-2.0)
**Copyleft strength:** Weak — file-level  
**Used by:** Mozilla Firefox, LibreOffice  
**Rule:** Modified files must stay under MPL-2.0, but larger works incorporating MPL code can be closed-source  
**Used by projects that want:** Core code to stay open, proprietary extensions OK  

### GNU Lesser General Public License v3.0 (LGPL-3.0)
**Copyleft strength:** Medium — library level  
**Rule:** Modifications to the library must stay LGPL; programs that use (link against) the library don't have to be open source  
**Used by:** GNU C Library (glibc), Qt (partially), FFmpeg (partly)  

**Choose LGPL when:**
- Building a reusable library that you want to remain open
- You want commercial developers to be able to use your library without open-sourcing their app
- You want something stronger than MPL-2.0 but less restrictive than GPL

### GNU General Public License v3.0 (GPL-3.0)
**Copyleft strength:** Strong — project level  
**Rule:** Any project that includes or links to GPL code must release all source under GPL  
**Used by:** Linux kernel (GPL-2.0), Bash, GCC, WordPress, VLC  

**Choose GPL-3.0 when:**
- You feel strongly that users should always have access to source code
- You're building a program (not a library)
- You want to prevent closed-source exploitation of your work
- You don't need to allow commercial closed-source integration

**GPL-3.0 vs GPL-2.0:**
- GPL-3.0 adds patent protection and anti-tivoization clauses
- Linux kernel uses GPL-2.0 only (not compatible with 3.0 due to "or later" clause)
- For new projects, prefer GPL-3.0-or-later

### GNU Affero General Public License v3.0 (AGPL-3.0)
**Copyleft strength:** Strongest — includes network use  
**Rule:** Same as GPL-3.0, but running the software as a service (SaaS) also triggers the copyleft requirement  
**Used by:** Nextcloud, Mastodon, MongoDB (partially), Grafana (previously)  

**Choose AGPL-3.0 when:**
- Building web services, APIs, or SaaS applications
- You want cloud providers to not exploit your software without contributing back
- You're building developer tools that competitors might offer as hosted services

**AGPL strategy (commercial monetization):**
AGPL + Commercial dual license is common:
- Free for open-source projects (AGPL)
- Paid commercial license for proprietary or SaaS use cases

---

## Non-Software Licenses

### Creative Commons — Quick Reference

| License | Code | Share | Adapt | Commercial | ShareAlike |
|---------|------|-------|-------|-----------|-----------|
| CC0 | CC0-1.0 | ✅ | ✅ | ✅ | — |
| CC BY | CC-BY-4.0 | ✅ | ✅ | ✅ | No |
| CC BY-SA | CC-BY-SA-4.0 | ✅ | ✅ | ✅ | Required |
| CC BY-NC | CC-BY-NC-4.0 | ✅ | ✅ | 🚫 | No |
| CC BY-ND | CC-BY-ND-4.0 | ✅ | 🚫 | ✅ | — |
| CC BY-NC-SA | CC-BY-NC-SA-4.0 | ✅ | ✅ | 🚫 | Required |
| CC BY-NC-ND | CC-BY-NC-ND-4.0 | ✅ | 🚫 | 🚫 | — |

**Important:** Creative Commons explicitly does NOT recommend using CC licenses for software. Use MIT/Apache/GPL for code.

**Use CC for:**
- Written documentation / articles / tutorials
- Artwork, illustrations, photography
- Datasets and research data
- Educational materials
- Audio and video content

**CC0 vs Unlicense:**
- CC0 is designed for all works, worldwide
- Unlicense is software-specific
- For datasets: prefer CC0
- For code: prefer Unlicense or MIT

### SIL Open Font License 1.1 (OFL-1.1)
**Use for:** Typefaces and font files  
**Rule:** Fonts may be used freely in documents; derivative fonts must be released under OFL; fonts cannot be sold standalone  

### CERN Open Hardware Licenses
- **CERN-OHL-P-2.0:** Permissive — for hardware designs
- **CERN-OHL-W-2.0:** Weakly reciprocal — modified designs must be shared
- **CERN-OHL-S-2.0:** Strongly reciprocal — all derivatives must stay open

---

## Special Situations

### No License (Not Recommended)
Without a license file, default copyright applies: **all rights reserved**. Even in public GitHub repos, nobody can legally use, copy, or distribute your code. This is rarely intentional.

### Mixed Licenses in One Repository
When different parts of a repo use different licenses:
```
repo/
├── LICENSE              ← main license for code
├── docs/LICENSE         ← CC BY-4.0 for documentation
├── assets/LICENSE       ← CC BY-SA-4.0 for artwork
└── README.md            ← explain what applies where
```

Clearly document in README.md which license covers which directories.

### Dual Licensing (Open Source + Commercial)
**How it works:**
1. You own 100% copyright (or have CLAs from all contributors)
2. Publish under a strong copyleft license (GPL/AGPL) for open source users
3. Offer a separate commercial license for companies that don't want copyleft obligations

**Requirements:**
- Contributor License Agreement (CLA) to relicense contributions
- Clear documentation of both licenses
- Pricing and contact for commercial license

**File structure:**
```
LICENSE           ← open source (GPL/AGPL)
LICENSE-COMMERCIAL.md ← commercial terms
NOTICE            ← explains dual licensing
.github/
  └── CLA.md      ← contributor agreement
```

**Real examples:** MySQL (GPL + commercial), Qt (LGPL/GPL + commercial), MongoDB (SSPL + commercial)

### Business Source License (BUSL / BSL)
A time-delayed open source license: the code is source-available with commercial restrictions, but automatically converts to an OSI-approved license after a specified date (typically 4 years). Used by: HashiCorp Terraform (before fork), MariaDB.

**Not considered open source** by the Open Source Initiative (OSI).

---

## Compatibility Matrix

Whether you can combine code from two licenses in one project:

| Your project → | MIT | Apache 2.0 | GPL-3.0 | AGPL-3.0 | LGPL-3.0 |
|----------------|-----|-----------|---------|----------|---------|
| **+ MIT dependency** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **+ Apache 2.0 dep.** | ✅ | ✅ | ✅* | ✅* | ✅ |
| **+ GPL-3.0 dep.** | ✅ (becomes GPL) | ✅ (becomes GPL) | ✅ | ✅ | ✅ |
| **+ AGPL-3.0 dep.** | ✅ (becomes AGPL) | ✅ (becomes AGPL) | ✅ (becomes AGPL) | ✅ | ⚠️ |
| **+ GPL-2.0 dep.** | ✅ (becomes GPL-2) | ❌ | ❌** | ❌ | ⚠️ |

`*` Apache 2.0 and GPL-3.0 are compatible when the combined work is under GPL-3.0  
`**` GPL-2.0-only and GPL-3.0-only are NOT compatible with each other; use "GPL-2.0-or-later" for compatibility

**Rule of thumb:** More restrictive license wins. MIT + GPL = GPL project.

---

## By Ecosystem / Community

Use the license preferred by the ecosystem to fit in naturally:

| Ecosystem | Typical license |
|-----------|----------------|
| JavaScript / Node.js | MIT or ISC |
| Python | MIT or Apache 2.0 |
| Rust (crates.io) | MIT OR Apache-2.0 (dual listed) |
| C / C++ (Boost) | BSL-1.0 or MIT |
| Java / JVM | Apache 2.0 |
| Go | BSD-3-Clause or Apache 2.0 |
| Android apps | Apache 2.0 |
| Linux kernel modules | GPL-2.0-only |
| GNU projects | GPL-3.0-or-later |
| Server software (SaaS-risk) | AGPL-3.0 |
| Database engines | GPL-2.0 or AGPL-3.0 + commercial |
| Documentation | CC BY-4.0 |
| Datasets | CC0-1.0 or CC BY-4.0 |
| Fonts | OFL-1.1 |
| Hardware | CERN-OHL-P/W/S-2.0 |

**Note on Rust:** The Rust community strongly prefers dual-licensing as `MIT OR Apache-2.0`. This is idiomatic and allows downstream projects to choose either license.

```toml
# Cargo.toml (Rust dual license convention)
[package]
license = "MIT OR Apache-2.0"
```
