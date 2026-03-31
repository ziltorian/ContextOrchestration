# Skills Specifications Quick Comparison

Fast reference for differences between skill formats across platforms.

## Required Fields (All Platforms)

| Field | All Platforms |
|-------|---------------|
| `name` | ✅ Required (1-64 chars, lowercase, hyphens only) |
| `description` | ✅ Required (explains what + when to use) |

**Note:** Both fields are required in YAML frontmatter for all platforms.

---

## Optional Fields - By Platform

| Field | Agent Skills Spec | Claude Skills | GitHub Copilot |
|-------|------------------|---------------|----------------|
| `license` | ✅ License name or file reference | ✅ License info | ✅ License info |
| `compatibility` | ✅ Environment requirements (1-500 chars) | ✅ Rarely needed | ❌ Not used |
| `dependencies` | ❌ Not used | ❌ Not used | ✅ Package requirements |
| `metadata` | ✅ Arbitrary key-value pairs | ✅ Key-value pairs | ❌ Not documented |
| `allowed-tools` | ✅ Experimental, pre-approved tools | ❌ Not used | ❌ Not used |

### Key Differences

**Environment Requirements:**

- **Agent Skills & Claude**: Use `compatibility` field
- **GitHub Copilot**: Use `dependencies` field
- **Recommendation**: Use `compatibility` for universal skills (converts to `dependencies` on GitHub)

**Metadata:**

- **Agent Skills & Claude**: Support arbitrary metadata
- **GitHub**: Not documented but may be ignored
- **Recommendation**: Safe to include, won't break GitHub

**Allowed Tools:**

- **Agent Skills**: Experimental feature
- **Others**: Not supported
- **Recommendation**: Omit unless targeting Agent Skills spec specifically

---

## Directory Structure Comparison

### Agent Skills Specification

```
skill-name/
├── SKILL.md          # Required
├── scripts/          # Executable code
├── references/       # Documentation
└── assets/           # Static resources
```

### Claude Skills

```
skill-name/
├── SKILL.md          # Required
├── scripts/          # Executable code
├── references/       # Documentation
└── assets/           # Templates, images
```

### GitHub Copilot Skills

```
skill-name/
├── SKILL.md          # Required
└── resources/        # All supporting files
```

**Difference:** GitHub simplifies to single `resources/` directory, while Agent Skills and Claude separate into three directories.

**Recommendation for Universal Skills:**

- Use Agent Skills 3-directory structure (`scripts/`, `references/`, `assets/`)
- GitHub platforms will still work with this structure
- Provides better organization and progressive disclosure

---

## Skill Location

| Platform | Primary Location | Alternative Location |
|----------|------------------|---------------------|
| Agent Skills | Any directory | Platform-dependent |
| Claude | Upload as .skill file | Web interface |
| GitHub Copilot | `.github/skills/` | `.claude/skills/` |

**Note:** GitHub specifically requires repository-based skills in `.github/skills/` or `.claude/skills/`.

---

## Field Constraints Quick Reference

### name Field

| Constraint | Rule | Example |
|------------|------|---------|
| Length | 1-64 characters | ✅ `pdf-processing` |
| Characters | Lowercase, numbers, hyphens only | ❌ `PDF-Processing` |
| Start/End | Cannot start or end with hyphen | ❌ `-pdf` or `pdf-` |
| Consecutive | No consecutive hyphens | ❌ `pdf--processor` |
| Match | Must match directory name | ✅ Directory: `pdf/`, name: `pdf` |

### description Field

| Platform | Max Length | Requirements |
|----------|-----------|--------------|
| Agent Skills | 1024 chars | What it does + when to use |
| Claude (claude.ai) | 200 chars | What it does + when to use |
| GitHub Copilot | Not specified | Clear explanation of purpose |

**Critical:** Description determines when agents activate the skill. Be comprehensive and include trigger keywords.

**Good Example:**

```yaml
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF documents, extracting data, filling forms, combining documents, or when user mentions PDFs, forms, or document processing.
```

**Poor Example:**

```yaml
description: PDF helper
```

---

## Progressive Disclosure (Context Management)

All platforms follow similar pattern:

| Level | Content | When Loaded | Token Budget |
|-------|---------|-------------|--------------|
| 1. Metadata | name + description | At agent startup (all skills) | ~100 tokens |
| 2. Instructions | SKILL.md body | When skill activates | <5000 tokens |
| 3. Resources | Supporting files | On-demand as needed | Unlimited* |

*Scripts may execute without loading into context.

**Best Practice:** Keep SKILL.md under 500 lines. Move detailed docs to `references/`.

---

## Platform-Specific Features

### Claude Skills Only

- Packaged as `.skill` ZIP files
- Built-in validation via `scripts/package_skill.py`
- Progressive disclosure heavily emphasized
- Integration with Claude Code

### GitHub Copilot Only

- Repository-based (`.github/skills/`)
- Integration with GitHub MCP Server tools
- Automatic skill discovery in repos
- Works with Copilot coding agent, CLI, VS Code

### Agent Skills Spec Only

- Open standard for all platforms
- `allowed-tools` field (experimental)
- Validation via `skills-ref` tool
- Platform-agnostic design

---

## Universal Skill Recommendations

For maximum compatibility across all platforms:

### ✅ DO Use

```yaml
---
name: lowercase-with-hyphens
description: Comprehensive description with what it does and when to use it, including trigger keywords
license: MIT
compatibility: Python 3.8+ with required packages
metadata:
  author: your-name
  version: "1.0"
---
```

### Structure

```
skill-name/
├── SKILL.md          # Under 500 lines
├── scripts/          # Executable code
├── references/       # Detailed docs
└── assets/           # Templates
```

### ❌ AVOID

```yaml
---
name: UPPERCASE-Name          # Wrong: must be lowercase
description: Short desc       # Wrong: needs triggers
dependencies: python>=3.8     # Platform-specific
---
```

---

## Quick Decision Tree

**Q: Which field for environment requirements?**

- Universal skill → Use `compatibility`
- GitHub-only skill → Use `dependencies`

**Q: Where to put detailed documentation?**

- All platforms → `references/REFERENCE.md`

**Q: How to organize supporting files?**

- Universal skill → Use `scripts/`, `references/`, `assets/`
- GitHub-only → Can use single `resources/` directory

**Q: Where to store skills?**

- Claude → Upload .skill file or use web interface
- GitHub → `.github/skills/` in repository
- Universal → Follow Agent Skills spec, package as needed

**Q: What's the safe maximum for SKILL.md?**

- All platforms → 500 lines, <5000 tokens

**Q: Required fields?**

- All platforms → `name` and `description` only

---

## Validation Checklist

Before sharing a skill, verify:

- [ ] `name` is lowercase with hyphens (1-64 chars)
- [ ] `description` includes what it does AND when to use it
- [ ] SKILL.md is under 500 lines
- [ ] No hardcoded secrets or API keys
- [ ] Skills are universal, not project-specific
- [ ] Supporting files in appropriate directories
- [ ] File references use relative paths
- [ ] Works without platform-specific fields

---

## When to Use Each Specification

### Use Agent Skills Spec When

- Creating universal, cross-platform skills
- Maximum portability is goal
- Open standard compliance matters
- Targeting multiple AI platforms

### Use Claude-Specific Features When

- Only deploying to Claude
- Need Claude Code integration
- Want built-in validation tools

### Use GitHub-Specific Features When

- Only using GitHub Copilot
- Need MCP Server integration
- Working in `.github/skills/` repos

### Best Practice

**Start with Agent Skills spec** as baseline, add platform-specific fields only when necessary.

---

## Common Mistakes

### ❌ Mistake 1: Platform-Specific Only

Creating skills that only work on one platform.

**Fix:** Follow Agent Skills spec for universal compatibility.

### ❌ Mistake 2: Poor Descriptions

```yaml
description: Helper for stuff
```

**Fix:** Include triggers and specifics:

```yaml
description: Process CSV files with pandas. Use when analyzing data, working with spreadsheets, or handling tabular data formats.
```

### ❌ Mistake 3: Everything in SKILL.md

1500-line SKILL.md files.

**Fix:** Keep under 500 lines, move details to `references/`.

### ❌ Mistake 4: Wrong Field Names

Using `dependencies` when following Agent Skills spec.

**Fix:** Use `compatibility` for universal skills.

### ❌ Mistake 5: Project-Specific Skills

```yaml
name: acme-corp-deployment
```

**Fix:** Make universal: `name: kubernetes-deployment`

---

## Summary Table

| Aspect | Agent Skills | Claude | GitHub Copilot |
|--------|-------------|---------|----------------|
| **Format** | Open standard | Extends Agent Skills | Extends Agent Skills |
| **Location** | Any | .skill upload | `.github/skills/` |
| **Required Fields** | name, description | name, description | name, description |
| **Env Requirements** | `compatibility` | `compatibility` | `dependencies` |
| **Directory Structure** | 3 dirs (scripts/references/assets) | 3 dirs | 1 dir (resources) |
| **Validation** | skills-ref tool | package_skill.py | Not specified |
| **Best For** | Universal skills | Claude ecosystem | GitHub ecosystem |

**Recommendation:** Use Agent Skills spec as foundation, add platform-specific fields only when needed.
