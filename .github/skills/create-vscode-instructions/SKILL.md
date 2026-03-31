---
name: create-vscode-instructions
description: Create VS Code custom instructions files (.instructions.md) and prompt files (.prompt.md) for GitHub Copilot. Use when creating agent rules, coding standards, module-specific instructions, or reusable prompts for VS Code projects. Includes YAML frontmatter format, markdown formatting standards, and file organization patterns.
compatibility: VS Code with GitHub Copilot extension
metadata:
  version: "1.0"
  category: ai-assistant-configuration
  author: ziltorian
---

# VS Code Agent Rules Creator

Create professional custom instructions and prompt files for GitHub Copilot in VS Code following official specifications and best practices.

## Overview

This skill teaches how to create two types of VS Code customization files:

1. **Custom Instructions** (`.instructions.md`) - Auto-applied coding standards and module-specific guidelines
2. **Prompt Files** (`.prompt.md`) - On-demand reusable prompts for development tasks

Both use YAML frontmatter + Markdown, but differ in purpose, name format, and triggering mechanism.

**Quick comparison:**

| Aspect | Custom Instructions | Prompt Files |
|--------|-------------------|--------------|
| **Trigger** | Automatic via `applyTo` glob | Manual via `/prompt-name` |
| **Name format** | `Module_Name` (underscores) | `module-name` (hyphens) |
| **Purpose** | Standards, guidelines | Specific tasks |
| **Variables** | Not supported | `${input:var}` supported |

## When to Use This Skill

- Creating project coding standards
- Writing module-specific guidelines
- Building reusable prompts for common tasks
- Setting up VS Code agent customization
- Migrating team conventions to agent rules

## Custom Instructions Files

### Quick Start

**Create:** `.github/instructions/Module_Name.instructions.md`

```yaml
---
name: "Python_Standards"
description: "Python coding standards for project"
applyTo: "**/*.py"
---

## Code Style
- Use type hints
- Follow PEP 8

## MUST DO
- Run tests before commit

## MUST NOT DO
- Commit commented-out code
```

**Triggers:** Automatically when editing matching files (`applyTo` pattern)

### File Locations

- **Workspace:** `.github/instructions/{name}.instructions.md` (project-specific)
- **User profile:** Cross-workspace instructions (global)

### YAML Frontmatter Essentials

```yaml
---
name: "Module_Name_Instructions"        # Underscores for display
description: "Brief description"         # What these instructions do
applyTo: "**/*.py"                      # Glob pattern (optional)
---
```

**Glob patterns:**
- `**/*.py` - All Python files
- `modules/api/**` - Specific directory
- `**/*.{ts,tsx}` - Multiple extensions

See [complete YAML guide](references/yaml-frontmatter-guide.md) for all field specifications.

### Body Content Guidelines

**Length limits:**
- Simple instructions: max 3,000 characters
- Complex instructions: max 12,000 characters

**Structure:**
- Use markdown by default (headings, lists, code blocks)
- Use XML tags **sparingly** for complex hierarchies only
- Directive, neutral tone with imperative verbs
- One idea per bullet point

**Essential sections:**
```markdown
## Main Section

### Code Style
[Rules using bullet lists]

### MUST DO
[Required actions]

### MUST NOT DO
[Prohibited actions]
```

See [formatting guide](references/formatting-guide.md) for complete markdown and XML formatting rules.

### Examples

See [instruction examples](references/instruction-examples.md) for complete working examples.
See [common patterns](references/common-patterns.md) for ready-to-use templates.

## Prompt Files

### Quick Start

**Create:** `.github/prompts/create-component.prompt.md`

```yaml
---
name: create-component
description: "Generate React component"
argument-hint: "component name"
agent: "agent"
---

Generate React component for ${input:componentName}.

## Process
1. Check existing patterns
2. Generate component with types
3. Add styles and tests
```

**Trigger:** Type `/create-component` in chat

### File Locations

- **Workspace:** `.github/prompts/{name}.prompt.md` (project-specific)
- **User profile:** Cross-workspace prompts (global)

### YAML Frontmatter Essentials

```yaml
---
name: prompt-name                        # Hyphens for command
description: "What the prompt does"
argument-hint: "input hint"              # Optional
agent: "agent"                           # Optional: ask|edit|agent
model: "GPT-4o"                         # Optional
tools: ["githubRepo", "search"]          # Optional
---
```

**Key fields:**
- `name` - Lowercase with hyphens (used after `/`)
- `argument-hint` - Shown in chat input
- `tools` - Available: githubRepo, search/codebase, terminal, fileEditor

See [complete YAML guide](references/yaml-frontmatter-guide.md) for all options.

### Body Guidelines

**Essential elements:**
- Clear goal statement
- Specific requirements
- Step-by-step process
- Expected outcome

**Variables:**
- `${workspaceFolder}` - Workspace root
- `${file}` - Current file path
- `${selection}` - Selected text
- `${input:varName}` - User input

See [prompt examples](references/prompt-examples.md) for complete prompt templates.
See [common patterns](references/common-patterns.md) for ready-to-use prompts.

## Quick Reference

### Key Differences

| Aspect | Custom Instructions | Prompt Files |
|--------|-------------------|--------------|
| **Extension** | `.instructions.md` | `.prompt.md` |
| **Trigger** | Automatic via `applyTo` | Manual `/name` |
| **Name format** | `Module_Name` (underscores) | `module-name` (hyphens) |
| **Variables** | Not supported | `${var}` supported |

### File Organization

```
.github/
├── instructions/
│   ├── Python_Standards.instructions.md
│   └── API_Module.instructions.md
└── prompts/
    ├── create-component.prompt.md
    └── security-review.prompt.md
```

### Creating Files

**Via UI:**
- Chat view → **Configure Chat** → **New instruction/prompt file**

**Via Command Palette:**
- `Chat: New Instructions File`
- `Chat: New Prompt File`

### Using Files

**Instructions:** Automatic when `applyTo` matches, or add via **Add Context**
**Prompts:** Type `/prompt-name` in chat

## Best Practices

**DO:**
- Keep instructions under length limits (3k/12k chars)
- Use directive, neutral tone
- Test all examples
- Use markdown by default
- Link to external resources

**DON'T:**
- Use emojis or emotional language
- Hardcode project-specific paths
- Overuse XML tags
- Duplicate content across files

## Further Reading

- [Formatting guide](references/formatting-guide.md) - Complete markdown and XML formatting rules
- [YAML frontmatter guide](references/yaml-frontmatter-guide.md) - All field specifications
- [Instruction examples](references/instruction-examples.md) - Working instruction templates
- [Prompt examples](references/prompt-examples.md) - Working prompt templates
- [Common patterns](references/common-patterns.md) - Ready-to-use templates
- [VS Code Custom Instructions Docs](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
- [VS Code Prompt Files Docs](https://code.visualstudio.com/docs/copilot/customization/prompt-files)
