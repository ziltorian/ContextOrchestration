# License Guide for Agent Skills

Comprehensive guide to selecting and applying licenses to Agent Skills.

## Overview

The `license` field in YAML frontmatter is optional but recommended for skills intended for sharing or reuse. It defines how others can use, modify, and distribute your skill.

## Why Add a License?

**Without a license:**

- Default copyright applies (all rights reserved)
- Others legally cannot use, modify, or share your skill
- Reduces adoption and collaboration

**With a license:**

- Clear legal terms for usage
- Encourages community contributions
- Enables commercial/open-source projects to adopt safely

## License Field Syntax

### Simple License Reference

```yaml
---
name: my-skill
description: Skill description
license: MIT
---
```

### Reference to Bundled License File

```yaml
---
name: my-skill
description: Skill description
license: Proprietary. See LICENSE.txt for complete terms
---
```

## Recommended Licenses for Skills

### MIT License (Most Popular)

**Best for:** Open skills intended for wide adoption

**Permissions:**

- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use

**Conditions:**

- 📌 License and copyright notice must be included

**Limitations:**

- ⚠️ No liability
- ⚠️ No warranty

**Example:**

```yaml
license: MIT
```

**When to use:**

- Educational skills (like prompt-engineering)
- Community-contributed skills
- Skills for open-source projects
- Maximum compatibility with any project

### Apache License 2.0

**Best for:** Skills with patent concerns

**Permissions:**

- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Patent use
- ✅ Private use

**Conditions:**

- 📌 License and copyright notice
- 📌 State changes made to code
- 📌 Include NOTICE file if provided

**Limitations:**

- ⚠️ Trademark use prohibited
- ⚠️ No liability
- ⚠️ No warranty

**Example:**

```yaml
license: Apache-2.0
```

**When to use:**

- Corporate-backed skills
- Skills involving patented algorithms
- Organizations requiring patent protection
- Large open-source projects

### Creative Commons Zero (CC0 / Public Domain)

**Best for:** Maximum freedom with no restrictions

**Permissions:**

- ✅ All permissions granted
- ✅ No conditions
- ✅ No attribution required

**Example:**

```yaml
license: CC0-1.0
```

**When to use:**

- Simple, universal skills
- Reference implementations
- Educational examples
- Government/public sector skills

### BSD 3-Clause

**Best for:** Academic and research institutions

**Permissions:**

- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use

**Conditions:**

- 📌 License and copyright notice
- 📌 No endorsement without permission

**Example:**

```yaml
license: BSD-3-Clause
```

**When to use:**

- Academic institutions
- Research projects
- Similar to MIT but with non-endorsement clause

### Proprietary License

**Best for:** Private/internal corporate skills

**Example:**

```yaml
license: Proprietary. LICENSE.txt has complete terms
```

**When to use:**

- Internal company skills
- Commercial products
- Skills with restricted distribution
- Custom licensing terms

**Requirements:**

- Must include LICENSE.txt file with full terms
- Clearly state restrictions

## Decision Tree

```
Is this skill for public sharing?
├─ No → Use Proprietary or omit license field
└─ Yes
   ├─ Do you want maximum adoption?
   │  └─ Yes → Use MIT
   ├─ Are patents involved?
   │  └─ Yes → Use Apache-2.0
   ├─ Want zero restrictions?
   │  └─ Yes → Use CC0
   └─ Academic context?
      └─ Yes → Use BSD-3-Clause
```

## License Comparison Table

| License | Commercial | Modify | Distribute | Patent Grant | Attribution | Copyleft |
|---------|-----------|--------|------------|--------------|-------------|----------|
| MIT | ✅ | ✅ | ✅ | ❌ | Required | No |
| Apache-2.0 | ✅ | ✅ | ✅ | ✅ | Required | No |
| CC0 | ✅ | ✅ | ✅ | ❌ | Optional | No |
| BSD-3-Clause | ✅ | ✅ | ✅ | ❌ | Required | No |
| GPL-3.0 | ✅ | ✅ | ✅ | ✅ | Required | Strong |
| Proprietary | ⚠️ | ⚠️ | ⚠️ | ⚠️ | Varies | N/A |

**Legend:**

- ✅ = Explicitly permitted
- ❌ = Not addressed
- ⚠️ = Depends on specific terms

## When to Omit License Field

The `license` field is optional. Omit it when:

**1. Repository-level license covers skills**

```
repository/
├── LICENSE (applies to all skills)
├── .github/
│   └── skills/
│       ├── skill-1/SKILL.md
│       └── skill-2/SKILL.md
```

**2. Experimental/demo skills**

- Proof of concept
- Learning exercises
- Not intended for production use

**3. Private repositories**

- Internal company use only
- No external distribution planned

**4. Work-for-hire situations**

- Client owns all rights
- Employment contract specifies ownership

## Best Practices

### ✅ DO

- **Match your project's license** - Use same license as main project
- **Use standard SPDX identifiers** - MIT, Apache-2.0, GPL-3.0
- **Be consistent** - Same license across all your skills
- **Consider users** - Choose licenses that don't create friction
- **Document exceptions** - If bundled code has different license

### ❌ DON'T

- **Use custom licenses** - Stick to well-known licenses
- **Mix incompatible licenses** - Check compatibility first
- **Leave licensing ambiguous** - Either specify or omit clearly
- **Copy-paste license text in YAML** - Reference only, full text in LICENSE file
- **Forget attribution** - Honor upstream licenses in derived skills

## Examples from Real Skills

### Open Source Educational Skill

```yaml
---
name: prompt-engineering
description: Guide for creating effective prompts for AI coding assistants
license: MIT
metadata:
  author: ziltorian
  version: "1.0"
  category: ai-assistant-configuration
---
```

### Corporate Internal Skill

```yaml
---
name: acme-deployment
description: Deploy applications to Acme Corp infrastructure
license: Proprietary. Internal use only. See LICENSE.txt
metadata:
  author: acme-platform-team
  version: "2.3"
  category: deployment
---
```

### Community Contribution

```yaml
---
name: data-visualization
description: Create charts and graphs from data
license: Apache-2.0
metadata:
  author: data-science-community
  version: "1.5"
  category: data-analysis
---
```

### Public Domain Reference

```yaml
---
name: http-status-codes
description: Reference guide for HTTP status codes
license: CC0-1.0
metadata:
  author: web-standards-group
  version: "1.0"
  category: reference
---
```

## License Compatibility

When building skills that depend on or reference other skills:

### Compatible Combinations

✅ **MIT + Apache-2.0** - Can combine freely  
✅ **MIT + BSD** - Can combine freely  
✅ **Apache-2.0 + BSD** - Can combine freely  
✅ **CC0 + Anything** - CC0 is compatible with all

### Problematic Combinations

⚠️ **GPL + MIT** - GPL is copyleft, requires derived work to be GPL  
⚠️ **GPL + Apache-2.0** - Similar copyleft issue  
⚠️ **Proprietary + GPL** - Generally incompatible

### Best Practice

For skill collections in one repository:

- Use single permissive license (MIT or Apache-2.0)
- Or use CC0 for maximum flexibility
- Avoid GPL unless you understand implications

## Adding License File

If using standard license, create separate LICENSE file:

**For MIT:**

```
MIT License

Copyright (c) 2026 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

Place in:

- Repository root (covers all skills), OR
- Individual skill directory (skill-specific)

## Resources

**License Choosers:**

- <https://choosealicense.com/> - Simple license selector
- <https://tldrlegal.com/> - Plain English license explanations
- <https://spdx.org/licenses/> - Standard license identifiers

**Full License Texts:**

- MIT: <https://opensource.org/licenses/MIT>
- Apache-2.0: <https://www.apache.org/licenses/LICENSE-2.0>
- BSD-3-Clause: <https://opensource.org/licenses/BSD-3-Clause>
- Creative Commons: <https://creativecommons.org/choose/>

**Legal Advice:**
For complex licensing situations, consult with legal counsel. This guide provides general information, not legal advice.

---

**Summary:** For most public skills, use MIT (maximum adoption) or Apache-2.0 (patent protection). Omit the field for private/internal skills. Always honor licenses of upstream dependencies.
