# Creative Commons License Guide

For documentation, datasets, content, and non-software creative works.

> ⚠️ Creative Commons explicitly recommends NOT using CC licenses for software code. Use MIT/Apache/GPL for code.

## The Six Main CC Licenses

CC licenses are built from four elements:

| Element | Symbol | Meaning |
|---------|--------|---------|
| Attribution | BY | Must credit the creator |
| ShareAlike | SA | Derivatives must use same license |
| NonCommercial | NC | No commercial use |
| NoDerivatives | ND | No modifications allowed |

### CC0 1.0 Universal (Public Domain Dedication)
**SPDX:** `CC0-1.0`  
**Technically:** Not a license — a waiver of all rights  
**What it means:** No conditions, no attribution required, public domain worldwide  
**Best for:** Datasets, reference implementations, government data, research data  
**Used by:** Wikipedia (some content), many research datasets, US federal government data

```
# README.md notice
This dataset is dedicated to the public domain under CC0 1.0.
No rights reserved. https://creativecommons.org/publicdomain/zero/1.0/
```

### CC BY 4.0 (Attribution)
**SPDX:** `CC-BY-4.0`  
**What it means:** Use freely for any purpose (including commercial), but must credit the author  
**Best for:** Documentation, tutorials, articles, educational materials  
**Used by:** Wikipedia, Khan Academy, many academic papers

```
# README.md notice
This work is licensed under a Creative Commons Attribution 4.0 International License.
https://creativecommons.org/licenses/by/4.0/
```

### CC BY-SA 4.0 (Attribution-ShareAlike)
**SPDX:** `CC-BY-SA-4.0`  
**What it means:** Use freely including commercially; derivatives must use same CC BY-SA license  
**Best for:** Wiki-style content, collaborative documentation  
**Used by:** Wikipedia (most content), OpenStreetMap

### CC BY-NC 4.0 (Attribution-NonCommercial)
**SPDX:** `CC-BY-NC-4.0`  
**What it means:** Free to use and modify, but not for commercial purposes  
**Best for:** Academic content, personal creative work  
**Warning:** "Non-commercial" is ambiguous and frequently disputed

### CC BY-ND 4.0 (Attribution-NoDerivatives)
**SPDX:** `CC-BY-ND-4.0`  
**What it means:** Can share verbatim copies commercially; cannot create derivative works  
**Best for:** Official reports, legal documents, where integrity is critical  
**Used by:** Some government and research data, reference imagery

### CC BY-NC-SA 4.0
**SPDX:** `CC-BY-NC-SA-4.0`  
**What it means:** Non-commercial use only; derivatives must use same license  
**Best for:** Educational content where commercial licensing is controlled

### CC BY-NC-ND 4.0 (Most Restrictive)
**SPDX:** `CC-BY-NC-ND-4.0`  
**What it means:** Can only share verbatim, non-commercially  
**Best for:** Works where you want visibility but maximum control

---

## How to Apply a CC License

### Option 1: LICENSE file

```
Creative Commons Attribution 4.0 International (CC BY 4.0)

Copyright (c) [year] [Author Name]

This work is licensed under the Creative Commons Attribution 4.0
International License. To view a copy of this license, visit
http://creativecommons.org/licenses/by/4.0/ or send a letter to
Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
```

### Option 2: README badge + notice

```markdown
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

This documentation is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
```

### Option 3: Mixed repo (code + docs)

```markdown
## License

- **Code:** MIT License — see [LICENSE](LICENSE)
- **Documentation:** CC BY 4.0 — see [docs/LICENSE](docs/LICENSE)
- **Dataset:** CC0 1.0 — see [data/LICENSE](data/LICENSE)
```

---

## CC License Attribution Best Practice

When using someone else's CC-licensed work, provide attribution:

```
"[Title]" by [Author], licensed under CC BY 4.0.
Source: [URL]
```

For datasets:
```
Dataset: [Name] by [Organization], CC0 1.0.
Retrieved from: [URL] on [date].
```

---

## CC vs Software Licenses for Mixed Projects

When a repo has both code and documentation:

| Content | Recommended |
|---------|-------------|
| Source code files (.py, .js, .go, etc.) | MIT, Apache 2.0, or GPL |
| README, guides, tutorials | CC BY-4.0 (or same as code is fine too) |
| API reference docs | Same as code license |
| Example code in docs | Explicitly same as code license |
| Dataset files | CC0-1.0 or CC BY-4.0 |
| Artwork / images | CC BY-4.0 or CC BY-SA-4.0 |

**Important note from choosealicense.com:**  
> If you use different licenses for your software and its documentation, be sure to specify that source code examples in the documentation are also licensed under the software license.
