---
name: open-source-licensing
description: Select, customize, and create software license files for projects. Use this skill whenever the user mentions license, LICENSE file, copyright, open source, MIT/Apache/GPL/BSD, adding license to project, licensing their code, SPDX, Creative Commons, dual licensing, or asks what license to use. Trigger on any request to generate, write, or place a license file — even vague ones like "add a license" or "I need a license for my repo".
compatibility: Any project repository
metadata:
  version: "1.0"
  category: project-management
  author: ziltorian
---

# Open Source Licensing

Select the right license, customize it, and generate a ready-to-use LICENSE file — in chat or directly in a project.

## Overview

This skill covers the full licensing workflow: choosing a license that fits the project's goals, filling in copyright details, optionally customizing terms, and producing a properly formatted LICENSE file. In a chat context the file is returned as output; in an IDE/editor context (VS Code, Cursor, JetBrains, etc.) it is written to the correct path in the repository root.

## Quick Decision Tree

```
What are your goals?
├── Maximum adoption, no restrictions  → MIT
├── Maximum adoption + patent safety   → Apache 2.0
├── Library usable in closed projects  → LGPL-3.0
├── Force derivatives to stay open     → GPL-3.0
├── Force open even for SaaS/network   → AGPL-3.0
├── File-level weak copyleft           → MPL-2.0
├── Public domain, zero conditions     → Unlicense / CC0-1.0
├── Documentation / content / datasets → CC BY-4.0 / CC BY-SA-4.0
├── Dataset public domain dedication   → CC0-1.0
├── Font files                         → OFL-1.1 (SIL Open Font License)
├── Open hardware designs              → CERN-OHL-P-2.0 (permissive)
├── Commercial + open source           → Dual license (GPL + Commercial)
└── Internal / proprietary             → Proprietary (custom text)
```

## Core Workflows

### Workflow 1: Create LICENSE for a New Project

**Step 1 — Gather info from the user (ask only what's missing):**
- Author name or organization
- Year (default: current year)
- License type (use the decision tree if unknown)
- Any extra restrictions or clauses

**Step 2 — Fetch the canonical license text** from `references/license-texts.md`.

**Step 3 — Fill in the template** (replace `[year]`, `[fullname]`, etc.).

**Step 4 — Deliver:**
- **Chat / no project context:** output the file content in a code block and offer to save it.
- **IDE / editor context:** write to `LICENSE` (no extension) in the repository root.

```
repo-root/
├── LICENSE          ← write here (GitHub auto-detects this name)
├── README.md
└── src/
```

> **GitHub detection rule:** GitHub uses the [Licensee](https://github.com/licensee/licensee) gem to identify licenses. It matches `LICENSE`, `LICENSE.txt`, `LICENSE.md`, or `COPYING` in the repo root. Use plain `LICENSE` (no extension, all caps) for guaranteed detection. Do **not** modify the license body text — even small edits can drop detection confidence below 100%.

---

### Workflow 2: Add License to an Existing Project

1. Check if a LICENSE file already exists.
2. If yes — read it and identify the current license type.
3. Confirm with user whether to replace or update copyright year/holder only.
4. Generate the new or updated LICENSE file.
5. Suggest updating `README.md` with a license badge and notice (see Quick Reference).

---

### Workflow 3: Customize a License

Some licenses allow customization; others must not be modified. Follow this rule:

| License | May customize? | What can change |
|---------|---------------|-----------------|
| MIT | ✅ Yes | Year, author name only |
| Apache 2.0 | ✅ Yes | Year, author name in NOTICE |
| GPL-3.0 / AGPL-3.0 / LGPL-3.0 | ⚠️ Year/name only | Body text must stay verbatim |
| BSD-2/3-Clause | ✅ Yes | Year, author name only |
| MPL-2.0 | ⚠️ Partial | Cannot modify grant language |
| Unlicense / CC0 | 🚫 No | No customization needed or allowed |
| Proprietary | ✅ Full | Draft from scratch |
| Creative Commons | 🚫 No | Cannot modify CC license text |

**Adding extra terms (MIT / Apache 2.0 only):**  
You may append a separate `NOTICE` file with attribution requirements, warranty disclaimers, or usage restrictions. Never embed extra terms inside the LICENSE body itself.

---

### Workflow 4: Dual Licensing

Dual licensing means shipping the **same code** under two licenses — typically one copyleft (GPL/AGPL) for open source users, and one commercial license for businesses.

**File structure:**
```
LICENSE           ← open source license (e.g. AGPL-3.0)
LICENSE-COMMERCIAL.md  ← commercial license terms
NOTICE            ← attribution & dual-license notice
```

**NOTICE file template:**
```
This software is available under two licenses:

1. GNU Affero General Public License v3.0 (AGPL-3.0)
   See LICENSE file. Free for open source projects.

2. Commercial License
   See LICENSE-COMMERCIAL.md. For proprietary/closed-source use.

Contact: [email] for commercial licensing.
```

---

### Workflow 5: Non-Software Projects

Use Creative Commons licenses for documentation, art, datasets, or content.  
See `references/creative-commons.md` for full CC license guide.

| Content type | Recommended license |
|-------------|-------------------|
| Documentation accompanying software | Same as code (MIT/Apache) |
| Standalone docs / articles / tutorials | CC BY-4.0 |
| Datasets | CC0-1.0 or CC BY-4.0 |
| Educational content allowing remixing | CC BY-SA-4.0 |
| Proprietary content, no derivatives | CC BY-ND-4.0 |

> Creative Commons explicitly recommends **not** using CC licenses for software code.

---

## Package Manifest Integration

After creating the LICENSE file, update the project's package manifest:

```jsonc
// package.json (Node.js)
{ "license": "MIT" }

// Cargo.toml (Rust)
[package]
license = "MIT"

// pyproject.toml (Python, PEP 639)
[project]
license = "MIT"
license-files = ["LICENSE"]
```

Full SPDX identifier list → `references/spdx-identifiers.md`

---

## Quick Reference

### README License Badge (Shields.io)

```markdown
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
```

### README License Section (minimum)

```markdown
## License

This project is licensed under the [MIT License](LICENSE).
Copyright (c) 2025 Your Name
```

### SPDX File Header (source files)

```python
# SPDX-FileCopyrightText: 2025 Your Name <email@example.com>
# SPDX-License-Identifier: MIT
```

```javascript
// SPDX-FileCopyrightText: 2025 Your Name <email@example.com>
// SPDX-License-Identifier: Apache-2.0
```

---

## Common Pitfalls

- **No license = all rights reserved.** Without a LICENSE file, nobody can legally use, copy, or fork your code even in a public repo.
- **Editing GPL/CC body text** breaks GitHub's Licensee detection and may make the license legally invalid.
- **Using CC licenses for software** — not recommended by Creative Commons themselves; use MIT/Apache/GPL instead.
- **Multiple LICENSE files in root** confuse Licensee. Keep one file named `LICENSE`.
- **Forgetting to update the year** — best practice is `2020-2025 Author` for long-running projects.
- **Dual licensing without a CLA** — contributors can block relicensing. Require a CLA if you plan dual licensing.

---

## Further Reading

- [License texts & templates](references/license-texts.md) — copy-ready full text for MIT, Apache 2.0, GPL-3.0, AGPL-3.0, LGPL-3.0, BSD-2, BSD-3, MPL-2.0, Unlicense, and Proprietary
- [License selection guide](references/selection-guide.md) — detailed comparison with use-case scenarios
- [Creative Commons guide](references/creative-commons.md) — CC license types for non-software projects
- [SPDX identifiers](references/spdx-identifiers.md) — machine-readable license IDs for package manifests
- [choosealicense.com](https://choosealicense.com) — interactive GitHub license picker
- [SPDX license list](https://spdx.org/licenses/) — complete official list
