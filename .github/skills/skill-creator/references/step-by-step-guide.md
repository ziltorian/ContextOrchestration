# Step-by-Step Skill Creation Guide

Detailed walkthrough for creating Agent Skills from scratch.

## Phase 1: Research and Planning

### Step 1.1: Gather Materials

**What to collect:**

- Official documentation (README, API docs, guides)
- Code examples and tutorials
- Common use cases and workflows
- Known issues and limitations
- Best practices and recommendations

**Sources:**

- Project's official website/docs
- GitHub repository (README, wiki, examples)
- Community resources (forums, Stack Overflow)
- Video tutorials and blog posts
- Changelog and release notes

**Quality check:**

- Is information current and accurate?
- Are examples from latest version?
- Is documentation comprehensive?

### Step 1.2: Identify Core Workflows

**Question to answer:**

- What are the 3-5 most common tasks users perform?
- What are the challenging or error-prone steps?
- What knowledge would save users the most time?
- What's unique or special about this tool/library?

**Example for PDF processing library:**

1. Extract text from PDF  
2. Extract tables from PDF
3. Fill PDF forms
4. Merge multiple PDFs
5. Split PDFs by pages

### Step 1.3: Analyze Target Audience

**Who will use this skill?**

- Beginners needing basic workflows?
- Intermediate users wanting optimization?
- Experts needing advanced techniques?
- Multiple skill levels (create tiered content)?

**Adjust detail level:**

- **Beginners:** More explanation, simpler examples
- **Intermediate:** Best practices, common patterns
- **Experts:** Advanced techniques, edge cases

### Step 1.4: Define Skill Scope

**In scope:**

- Universal workflows that work across projects
- Platform/tool-specific features and APIs
- Best practices and recommended patterns
- Common pitfalls and how to avoid them

**Out of scope:**

- Project-specific implementation details
- Deployment or infrastructure setup (unless that's the skill's focus)
- Business logic or domain-specific code
- Hardcoded paths, credentials, or project structure

## Phase 2: Structure Design

### Step 2.1: Create Skill Name

**Rules:**

- lowercase-hyphen-format
- 1-64 characters
- Descriptive but concise
- Match directory name exactly

**Examples:**

✅ Good:
- `pdf-processing`
- `github-copilot-sdk`
- `microsoft-agent-framework`
- `react-state-management`

❌ Bad:
- `PDFProcessing` (not lowercase)
- `pdf_processing` (underscores not hyphens)
- `pdf` (too vague)
- `advanced-comprehensive-pdf-document-processing-library` (too long)

### Step 2.2: Write Description

**Formula:**

```
[What it does] + [When to use it] + [Trigger keywords]
```

**Components:**

1. **What:** Primary capabilities (1-2 sentences)
2. **When:** Trigger conditions ("Use when...")
3. **Keywords:** Terms that should activate skill

**Example:**

```yaml
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF documents, extracting data, filling forms, combining PDFs, or when user mentions PDFs, forms, or document processing.
```

**Test your description:**

- Does it clearly state what the skill does?
- Does it cover common use cases?
- Does it include trigger keywords?
- Is it under 500 characters?

### Step 2.3: Plan SKILL.md Structure

**Recommended sections:**

```markdown
# [Skill Title]

Brief intro (1-2 sentences)

## Overview

What this skill teaches (3-5 sentences)

## When to Use This Skill

Bullet list of use cases

## Core Workflows

### Workflow 1: [Name]

Brief description + minimal example

### Workflow 2: [Name]

Brief description + minimal example

## Common Patterns

### Pattern 1: [Name]

When to use + minimal example

## Quick Reference

Essential cheat sheet

## Further Reading

Links to detailed documentation
```

**Keep SKILL.md concise:**

- Target: 300-500 lines
- Essential info only
- Link to references for details
- Examples should be minimal but complete

### Step 2.4: Plan References Structure

**Create these files as needed:**

```
references/
  ├── getting-started.md       # Installation, setup, basic usage
  ├── advanced-techniques.md   # Advanced features and patterns
  ├── api-reference.md         # Detailed API documentation
  ├── examples.md              # Code examples with explanations
  ├── troubleshooting.md       # Common issues and solutions
  ├── best-practices.md        # Recommendations and patterns
  └── migration-guide.md       # Version updates, breaking changes
```

**Guidelines:**

- Each file focuses on one topic
- Can be long and detailed
- Loaded on-demand when needed
- Include comprehensive examples

## Phase 3: Content Creation

### Step 3.1: Write Metadata

**Create YAML frontmatter:**

```yaml
---
name: skill-name
description: Comprehensive description with use cases and keywords
license: MIT
compatibility: Python 3.8+ with packagename
metadata:
  version: "1.0"
  category: relevant-category
  author: your-name
---
```

**Optional fields:**

- `license`: MIT, Apache-2.0, CC-BY-4.0, etc.
- `compatibility`: Version requirements
- `metadata`: Additional structured data

### Step 3.2: Write Overview

**Template:**

```markdown
## Overview

[Tool/Library name] [what it does in one sentence].

This skill teaches you to [primary capability], [secondary capability], 
and [tertiary capability]. Master [key concept 1], [key concept 2], and 
[key concept 3].

Key features covered:
- [Feature 1]
- [Feature 2]
- [Feature 3]
```

**Example:**

```markdown
## Overview

PDFPlumber is a Python library for extracting text and tables from PDF files.

This skill teaches you to extract text, parse tables, and manipulate PDF 
documents programmatically. Master PDF parsing, table detection, and data 
extraction workflows.

Key features covered:
- Text extraction with position and formatting
- Table detection and parsing
- Page-level analysis
- Metadata extraction
```

### Step 3.3: Write Core Workflows

**For each workflow:**

1. **Name it clearly** (verb + object)
2. **Explain when to use it** (1-2 sentences)
3. **Show minimal working example**
4. **Link to detailed guide** in references

**Template:**

```markdown
### Workflow: [Verb] [Object]

[When to use this workflow - 1-2 sentences]

**Basic example:**

\```language
[Minimal code that works]
\```

**Output:**

\```
[Expected output]
\```

See [detailed guide](references/workflow-name.md) for advanced usage.
```

### Step 3.4: Add Common Patterns

**Pattern template:**

```markdown
### Pattern: [Pattern Name]

**Use case:** [When to apply this pattern]

**Implementation:**

\```language
[Code example]
\```

**When to use:**
- [Scenario 1]
- [Scenario 2]

**When not to use:**
- [Anti-pattern warning]
```

### Step 3.5: Create Quick Reference

**Cheat sheet with essentials:**

```markdown
## Quick Reference

### Essential Imports

\```language
[Common imports]
\```

### Common Operations

| Task | Code |
|------|------|
| [Task 1] | `code_snippet()` |
| [Task 2] | `code_snippet()` |

### Key Concepts

- **[Concept]**: [Brief explanation]
- **[Concept]**: [Brief explanation]
```

## Phase 4: Create Supporting Files

### Step 4.1: Write reference/getting-started.md

**Contents:**

1. Installation instructions
2. Initial setup/configuration
3. Your first example (complete walkthrough)
4. Verification steps
5. Next steps

**Structure:**

```markdown
# Getting Started with [Tool Name]

## Installation

### Prerequisites
[System requirements]

### Install Package
\```bash
[Installation command]
\```

## Initial Setup

[Configuration steps]

## Your First [Task]

Complete walkthrough:

\```language
[Step-by-step code with explanations]
\```

## Verification

[How to confirm it works]

## Next Steps

- [Link to next tutorial]
- [Link to examples]
```

### Step 4.2: Write reference/examples.md

**Structure:**

```markdown
# Code Examples

## Basic Examples

### Example 1: [Task Name]

**Scenario:** [What this example demonstrates]

\```language
[Complete, runnable code]
\```

**Explanation:**
- [Step 1 explained]
- [Step 2 explained]

**Output:**
\```
[Expected output]
\```

## Intermediate Examples

[More complex examples]

## Advanced Examples

[Advanced use cases]
```

### Step 4.3: Write reference/troubleshooting.md

**Common issues template:**

```markdown
# Troubleshooting Guide

## Common Issues

### Issue: [Error Message or Problem]

**Symptoms:**
- [What user sees]

**Cause:**
[Why it happens]

**Solution:**
\```language
[Code fix or configuration change]
\```

**Prevention:**
[How to avoid in future]

---

[Repeat for each common issue]
```

### Step 4.4: Create scripts/ (if applicable)

**When to create scripts:**

- Repetitive setup tasks
- Code generation helpers
- Validation tools
- Template generators

**Script structure:**

```
scripts/
  ├── setup.sh              # Environment setup
  ├── generate_template.py  # Code template generator
  └── validate.py           # Validation helper
```

**Add README:**

```markdown
# Scripts

## setup.sh

Automated environment setup.

Usage:
\```bash
./scripts/setup.sh
\```

## generate_template.py

Generate boilerplate code.

Usage:
\```bash
python scripts/generate_template.py --name MyProject
\```
```

## Phase 5: Quality Assurance

### Step 5.1: Content Review

**Checklist:**

- [ ] SKILL.md is under 500 lines
- [ ] All code examples tested and working
- [ ] No hardcoded secrets or project-specific paths
- [ ] Links to references are correct
- [ ] Description includes trigger keywords
- [ ] Name matches directory and uses hyphens
- [ ] Examples are complete and runnable
- [ ] No broken external links

### Step 5.2: Test Examples

**For each code example:**

1. Copy exactly as shown
2. Run in clean environment
3. Verify it produces expected output
4. Fix any errors
5. Update example if needed

**Test matrix:**

- Minimum version of dependencies
- Latest version of dependencies
- Different operating systems (if relevant)

### Step 5.3: Review for Universality

**Questions:**

- Can this be used in any project?
- Are there project-specific assumptions?
- Is there hardcoded configuration?
- Would this work for other users?

**Remove:**

- Project-specific paths
- Hardcoded credentials
- Specific project structure assumptions
- Internal tool references

### Step 5.4: Get Feedback

**Test with:**

- Someone unfamiliar with the tool
- Someone who knows the tool well
- AI assistant (test skill activation)

**Questions:**

- Is the skill easy to discover?
- Are examples clear and helpful?
- Is anything confusing or missing?
- Does it actually save time?

## Phase 6: Deployment

### Step 6.1: Organize Files

**Final structure:**

```
.github/skills/skill-name/
├── SKILL.md
├── references/
│   ├── getting-started.md
│   ├── examples.md
│   ├── troubleshooting.md
│   └── [other reference files]
├── scripts/         (if applicable)
│   └── [helper scripts]
└── assets/          (if applicable)
    └── [images, diagrams]
```

### Step 6.2: Create README (optional)

If skill has complex setup:

```markdown
# [Skill Name]

Brief description.

## Installation

[How to add skill to project]

## Usage

[Quick start]

## Documentation

- [SKILL.md](SKILL.md) - Main skill documentation
- [references/](references/) - Detailed guides

## Contributing

[How to improve this skill]
```

### Step 6.3: Version Control

**Initial commit:**

```bash
git add .github/skills/skill-name/
git commit -m "Add [skill-name] skill"
```

**Future updates:**

```bash
git commit -m "Update [skill-name]: [description of changes]"
```

## Phase 7: Maintenance

### Step 7.1: Keep Updated

**Monitor:**

- Tool/library version updates
- Breaking changes in APIs
- New features and capabilities
- Community feedback

**Update when:**

- Major version releases
- Deprecation warnings
- New recommended practices
- User reports issues

### Step 7.2: Improve Based on Usage

**Collect feedback:**

- Which workflows are most used?
- What questions do users ask?
- Where do users get stuck?
- What examples are helpful?

**Iterate:**

- Add missing workflows
- Clarify confusing sections
- Add more examples
- Update outdated information

## Common Pitfalls to Avoid

### Pitfall 1: Too Project-Specific

❌ **Wrong:**
```markdown
Use our authentication system by calling `app.auth.login()`
```

✅ **Right:**
```markdown
Implement authentication using [library]:
\```python
auth_manager = AuthManager(config)
auth_manager.login(credentials)
\```
```

### Pitfall 2: Incomplete Examples

❌ **Wrong:**
```python
result = process_data(data)
```

✅ **Right:**
```python
import library

data = {"key": "value"}
result = library.process_data(data)
print(result)  # Output: {"processed": True}
```

### Pitfall 3: Missing Context

❌ **Wrong:**
```markdown
Call the function with the parameter.
```

✅ **Right:**
```markdown
Call `process_text()` with the text content as a string parameter.
This function parses text and returns a structured dictionary.
```

### Pitfall 4: Overly Complex First Example

❌ **Wrong:** Start with complex, multi-step workflow

✅ **Right:** Start with simplest possible working example, then build up

### Pitfall 5: No Troubleshooting Help

❌ **Wrong:** Only show happy path

✅ **Right:** Include common errors and their solutions

## Templates and Checklists

### New Skill Checklist

- [ ] Created directory: `.github/skills/skill-name/`
- [ ] Created `SKILL.md` with all required sections
- [ ] Added YAML frontmatter with name and description
- [ ] Wrote 3-5 core workflows  
- [ ] Created `references/getting-started.md`
- [ ] Created `references/examples.md`
- [ ] Tested all code examples
- [ ] Verified all links work
- [ ] Reviewed for universality (no project-specific content)
- [ ] Got feedback from test user
- [ ] Committed to version control

### Update Skill Checklist

- [ ] Reviewed tool's latest version for changes
- [ ] Updated deprecated APIs or methods
- [ ] Added new features if significant
- [ ] Tested all examples still work
- [ ] Updated version in metadata
- [ ] Documented breaking changes (if any)
- [ ] Updated links to external resources
- [ ] Committed with clear description of changes

## Summary

Creating great skills is iterative:

1. **Research thoroughly** - understand the tool deeply
2. **Design well** - structure for progressive disclosure
3. **Write clearly** - be specific and comprehensive
4. **Test rigorously** - all examples must work
5. **Review critically** - ensure universality
6. **Iterate continuously** - improve based on feedback

**Remember:** The goal is to save users time by providing exactly the knowledge they need, exactly when they need it.
