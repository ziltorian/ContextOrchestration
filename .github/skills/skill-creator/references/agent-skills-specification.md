# Agent Skills Specification

The open standard specification for Agent Skills format from agentskills.io.

## Overview

Agent Skills is an open standard format that allows skills to work across multiple AI agent platforms including Claude, GitHub Copilot, Cursor, Windsurf, Aider, and others.

## Directory Structure

Minimum structure:

```
skill-name/
└── SKILL.md          # Required
```

With optional directories:

```
skill-name/
├── SKILL.md          # Required
├── scripts/          # Optional: Executable code
├── references/       # Optional: Additional documentation
└── assets/           # Optional: Static resources
```

## SKILL.md Format

Must contain YAML frontmatter followed by Markdown content.

### Required Frontmatter

```yaml
---
name: skill-name
description: A description of what this skill does and when to use it.
---
```

### Optional Frontmatter

```yaml
---
name: pdf-processing
description: Extract text and tables from PDF files, fill forms, merge documents.
license: Apache-2.0
compatibility: Requires Python 3.8+, pdfplumber package
metadata:
  author: example-org
  version: "1.0"
  category: document-processing
allowed-tools: Bash(git:*) Bash(jq:*) Read
---
```

## Field Specifications

### name (required)

**Constraints:**

- 1-64 characters maximum
- Only lowercase letters, numbers, and hyphens (`a-z`, `0-9`, `-`)
- Must not start or end with hyphen
- Must not contain consecutive hyphens (`--`)
- Must match parent directory name

**Valid examples:**

```yaml
name: pdf-processing
name: data-analysis
name: code-review
```

**Invalid examples:**

```yaml
name: PDF-Processing    # uppercase not allowed
name: -pdf              # cannot start with hyphen
name: pdf--processing   # consecutive hyphens not allowed
```

### description (required)

**Constraints:**

- 1-1024 characters
- Must be non-empty
- Should describe both what the skill does AND when to use it
- Should include specific keywords for agent discovery

**Good example:**

```yaml
description: Extracts text and tables from PDF files, fills PDF forms, and merges multiple PDFs. Use when working with PDF documents or when the user mentions PDFs, forms, or document extraction.
```

**Poor example:**

```yaml
description: Helps with PDFs.
```

### license (optional)

License name or reference to bundled license file.

**Examples:**

```yaml
license: Apache-2.0
license: MIT
license: Proprietary. LICENSE.txt has complete terms
```

### compatibility (optional)

**Constraints:**

- 1-500 characters if provided
- Only include if skill has specific environment requirements
- Can indicate: intended product, required system packages, network access needs

**Examples:**

```yaml
compatibility: Designed for Claude Code (or similar products)
compatibility: Requires git, docker, jq, and access to the internet
compatibility: Python 3.8+ with pandas and numpy packages
```

**Note:** Most skills don't need this field.

### metadata (optional)

Arbitrary key-value mapping for additional properties.

**Example:**

```yaml
metadata:
  author: example-org
  version: "1.0"
  category: data-processing
  tags: pdf,documents,extraction
```

**Recommendation:** Use reasonably unique key names to avoid conflicts.

### allowed-tools (optional)

**Status:** Experimental - support varies between agent implementations

Space-delimited list of pre-approved tools that the skill may use.

**Example:**

```yaml
allowed-tools: Bash(git:*) Bash(jq:*) Read
```

## Body Content

The Markdown body after frontmatter contains skill instructions. No format restrictions.

**Recommended sections:**

- Step-by-step instructions
- Examples of inputs and outputs
- Common edge cases
- References to additional files

**Important:** Agent loads entire SKILL.md when skill activates. Consider splitting longer content into referenced files.

## Optional Directories

### scripts/

Contains executable code that agents can run.

**Use for:**

- Self-contained scripts
- Code with documented dependencies
- Scripts with helpful error messages
- Edge case handling

**Supported languages:** Depends on agent implementation

- Common: Python, Bash, JavaScript

**Example:**

```
scripts/
├── extract_pdf.py
├── convert_format.sh
└── api_client.js
```

### references/

Additional documentation loaded on-demand by agents.

**Use for:**

- `REFERENCE.md` - Detailed technical reference
- `FORMS.md` - Form templates or structured data formats
- Domain-specific files (`finance.md`, `legal.md`, etc.)

**Best practice:** Keep individual reference files focused. Agents load these on demand.

**Example:**

```
references/
├── REFERENCE.md
├── API_DOCS.md
├── SCHEMA.md
└── EXAMPLES.md
```

### assets/

Static resources used in outputs (NOT loaded into context).

**Use for:**

- Document templates
- Configuration templates
- Images and diagrams
- Data files (lookup tables, schemas)

**Example:**

```
assets/
├── template.docx
├── logo.png
├── config-template.json
└── data/
    └── lookup_table.csv
```

## Progressive Disclosure

Skills should be structured for efficient context usage:

**Level 1 - Metadata (~100 tokens):**

- `name` and `description` fields
- Loaded at startup for all skills
- Enables skill discovery

**Level 2 - Instructions (<5000 tokens recommended):**

- Full SKILL.md body
- Loaded when skill is activated
- Should be focused and actionable
- Keep under 500 lines

**Level 3 - Resources (as needed):**

- Files in `scripts/`, `references/`, `assets/`
- Loaded only when required
- Scripts may execute without loading into context

**Best practice:** Keep main SKILL.md under 500 lines. Move detailed reference material to separate files.

## File References

When referencing files, use relative paths from skill root:

```markdown
See [the reference guide](references/REFERENCE.md) for details.

Run the extraction script:
scripts/extract.py input.pdf
```

**Important:** Keep file references one level deep from SKILL.md. Avoid deeply nested reference chains.

## Validation

Use the skills-ref reference library to validate:

```bash
skills-ref validate ./my-skill
```

Validates:

- SKILL.md frontmatter format
- Required fields presence
- Naming conventions
- Directory structure

## Complete Example

**Directory structure:**

```
pdf-processor/
├── SKILL.md
├── scripts/
│   ├── extract_text.py
│   └── merge_pdfs.py
├── references/
│   ├── REFERENCE.md
│   └── EXAMPLES.md
└── assets/
    └── form_template.pdf
```

**SKILL.md:**

```yaml
---
name: pdf-processor
description: Extract text and tables from PDFs, fill forms, merge documents. Use when working with PDF files or document processing tasks.
license: MIT
compatibility: Requires Python 3.8+ with pdfplumber and PyPDF2
metadata:
  version: "1.2"
  author: example-team
---

# PDF Processor

Process PDF documents with text extraction, form filling, and merging capabilities.

## Core Workflows

### Extract Text from PDF

1. Use scripts/extract_text.py to extract text
2. For table extraction, see references/REFERENCE.md

### Merge Multiple PDFs

Use the merge script with file paths as arguments.

## Examples

See references/EXAMPLES.md for detailed use cases.

## Edge Cases

- Scanned PDFs require OCR (not included in this skill)
- Password-protected PDFs need password as argument
- Large PDFs (>100MB) may require streaming mode
```

## Platform Compatibility

Following this specification ensures skills work across:

- **Claude** (claude.ai, Claude Code)
- **GitHub Copilot** (coding agent, CLI, VS Code)
- **Cursor**
- **Windsurf**
- **Aider**
- **Any platform** implementing the Agent Skills standard

## Key Differences from Platform-Specific Formats

### vs. Claude Skills

- Agent Skills uses `compatibility` field; Claude may use additional validation
- Both support same core structure
- Agent Skills is the open standard baseline

### vs. GitHub Copilot Skills

- GitHub uses `dependencies` field; Agent Skills uses `compatibility`
- GitHub supports `.github/skills/` location
- Agent Skills is platform-agnostic

## References

- Specification: <https://agentskills.io/specification>
- Repository: <https://github.com/agentskills/agentskills>
- Validation tool: <https://github.com/agentskills/agentskills/tree/main/skills-ref>
