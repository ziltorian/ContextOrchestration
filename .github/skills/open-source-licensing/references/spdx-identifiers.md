# SPDX Identifiers & Package Manifest Integration

SPDX (Software Package Data Exchange) provides machine-readable license identifiers used by package managers, GitHub, and license scanning tools.

## Most Common SPDX Identifiers

| License | SPDX Identifier | Notes |
|---------|----------------|-------|
| MIT | `MIT` | Most popular |
| Apache 2.0 | `Apache-2.0` | |
| GPL v2 only | `GPL-2.0-only` | Linux kernel |
| GPL v2 or later | `GPL-2.0-or-later` | |
| GPL v3 only | `GPL-3.0-only` | |
| GPL v3 or later | `GPL-3.0-or-later` | Recommended for new projects |
| AGPL v3 | `AGPL-3.0-only` | |
| AGPL v3 or later | `AGPL-3.0-or-later` | |
| LGPL v2.1 | `LGPL-2.1-only` | |
| LGPL v3 | `LGPL-3.0-only` | |
| BSD 2-Clause | `BSD-2-Clause` | |
| BSD 3-Clause | `BSD-3-Clause` | |
| ISC | `ISC` | |
| MPL 2.0 | `MPL-2.0` | |
| Unlicense | `Unlicense` | |
| CC0 1.0 | `CC0-1.0` | |
| CC BY 4.0 | `CC-BY-4.0` | |
| CC BY-SA 4.0 | `CC-BY-SA-4.0` | |
| CC BY-NC 4.0 | `CC-BY-NC-4.0` | |
| BSL 1.0 | `BSL-1.0` | Boost |
| OFL 1.1 | `OFL-1.1` | Fonts |
| EUPL 1.2 | `EUPL-1.2` | EU public sector |
| CDDL 1.0 | `CDDL-1.0` | Oracle/Sun |
| EPL 2.0 | `EPL-2.0` | Eclipse |
| BUSL 1.1 | `BUSL-1.1` | Business Source (NOT OSI open source) |
| Proprietary | `LicenseRef-Proprietary` | Custom identifier |

Full list: https://spdx.org/licenses/

---

## Package Manifest Integration

### Node.js / npm — package.json

```json
{
  "name": "my-package",
  "version": "1.0.0",
  "license": "MIT"
}
```

For dual/multiple licenses:
```json
{
  "license": "(MIT OR Apache-2.0)"
}
```

For proprietary (UNLICENSED = all rights reserved):
```json
{
  "license": "UNLICENSED",
  "private": true
}
```

### Python — pyproject.toml (PEP 639, modern)

```toml
[project]
name = "my-package"
license = "MIT"
license-files = ["LICENSE"]
```

Multiple licenses:
```toml
[project]
license = "MIT AND Apache-2.0"
license-files = ["LICENSE", "LICENSE-APACHE"]
```

Custom/proprietary:
```toml
[project]
license = "LicenseRef-Proprietary"
license-files = ["LICENSE"]
```

### Python — setup.py (legacy, still common)

```python
from setuptools import setup

setup(
    name='my-package',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ],
)
```

### Rust — Cargo.toml

```toml
[package]
name = "my-crate"
version = "0.1.0"
license = "MIT"
```

Rust community convention — dual license:
```toml
[package]
license = "MIT OR Apache-2.0"
license-file = "LICENSE"
```

Proprietary (no spdx):
```toml
[package]
license-file = "LICENSE"
```

### Go — go.mod (no license field)

Go modules don't have a license field in go.mod. Rely on:
1. `LICENSE` file in repo root
2. GitHub detection via Licensee
3. Optional SPDX header in each source file

### Java / Maven — pom.xml

```xml
<licenses>
  <license>
    <name>MIT License</name>
    <url>https://opensource.org/licenses/MIT</url>
    <distribution>repo</distribution>
  </license>
</licenses>
```

### Java / Gradle — build.gradle

```groovy
// No standard field; document in README and LICENSE file
// For publishing to Maven Central via Gradle:
publishing {
    publications {
        maven(MavenPublication) {
            pom {
                licenses {
                    license {
                        name = 'MIT License'
                        url = 'https://opensource.org/licenses/MIT'
                    }
                }
            }
        }
    }
}
```

### PHP — composer.json

```json
{
  "name": "vendor/package",
  "license": "MIT"
}
```

Multiple licenses:
```json
{
  "license": ["MIT", "Apache-2.0"]
}
```

Proprietary:
```json
{
  "license": "proprietary"
}
```

### Ruby — .gemspec

```ruby
Gem::Specification.new do |spec|
  spec.license = 'MIT'
  # or multiple:
  spec.licenses = ['MIT', 'Apache-2.0']
end
```

---

## SPDX File Headers (Source Files)

Adding SPDX identifiers to individual source files allows tools to scan license info without reading the LICENSE file:

**Python:**
```python
# SPDX-FileCopyrightText: 2025 Your Name <email@example.com>
# SPDX-License-Identifier: MIT
```

**JavaScript / TypeScript:**
```javascript
// SPDX-FileCopyrightText: 2025 Your Name <email@example.com>
// SPDX-License-Identifier: Apache-2.0
```

**C / C++:**
```c
/* SPDX-FileCopyrightText: 2025 Your Name <email@example.com>
 * SPDX-License-Identifier: GPL-3.0-or-later
 */
```

**Bash / Shell:**
```bash
# SPDX-FileCopyrightText: 2025 Your Name <email@example.com>
# SPDX-License-Identifier: MIT
```

**Go:**
```go
// SPDX-FileCopyrightText: 2025 Your Name <email@example.com>
// SPDX-License-Identifier: Apache-2.0
```

**Rust:**
```rust
// SPDX-FileCopyrightText: 2025 Your Name <email@example.com>
// SPDX-License-Identifier: MIT OR Apache-2.0
```

**HTML / XML:**
```html
<!--
SPDX-FileCopyrightText: 2025 Your Name <email@example.com>
SPDX-License-Identifier: CC-BY-4.0
-->
```

---

## SPDX Expressions

Complex license expressions using operators:

| Operator | Meaning | Example |
|----------|---------|---------|
| `OR` | User chooses one | `MIT OR Apache-2.0` |
| `AND` | Both apply simultaneously | `MIT AND CC-BY-4.0` |
| `WITH` | License with exception | `GPL-2.0-only WITH Classpath-exception-2.0` |

```
# Rust idiomatic dual license
MIT OR Apache-2.0

# Code + content mixed
MIT AND CC-BY-4.0

# GPL with classpath exception (Java)
GPL-2.0-only WITH Classpath-exception-2.0

# Custom license not in SPDX list
LicenseRef-My-Custom-License
```

---

## GitHub Licensee Detection

GitHub uses the [Licensee](https://github.com/licensee/licensee) gem to detect licenses.

**Detection rules:**
- Looks for files: `LICENSE`, `LICENSE.txt`, `LICENSE.md`, `LICENSE.rst`, `COPYING`, `COPYING.txt`
- Only checks the **default branch** (main/master)
- Matches by content similarity (Sørensen–Dice coefficient)
- 100% confidence = exact match → modify nothing in the license body
- < 90% confidence = not detected → GitHub shows "View license" without identifying it

**To maximize detection:**
1. Use exactly `LICENSE` (no extension, all caps) in repo root
2. Copy the license text verbatim — do not paraphrase or reformat
3. Only change placeholder fields: `[year]`, `[fullname]` in MIT/BSD
4. For Apache 2.0: do not add custom text to the LICENSE body — use a NOTICE file instead

**Testing detection locally:**
```bash
gem install licensee
licensee detect .
```
