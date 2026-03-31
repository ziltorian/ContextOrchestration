# YAML Frontmatter Complete Guide

Comprehensive guide for YAML frontmatter syntax in VS Code custom instructions and prompt files.

## Custom Instructions Frontmatter

### Required Fields

```yaml
---
name: "Module_Name_Instructions"
description: "Brief description of what these instructions do"
---
```

### Optional Fields

```yaml
---
name: "Module_Name_Instructions"
description: "Brief description"
applyTo: "**/*.py"                     # Glob pattern for auto-apply
---
```

### Field Specifications

#### `name` Field

**Format:** Use underscores between words for display names

**Examples:**

```yaml
name: "Python_Code_Standards"
name: "API_Module_Instructions"
name: "React_TypeScript_Guidelines"
```

**Rules:**

- Use underscores (not hyphens or spaces)
- Start with capital letter
- Keep under 50 characters
- Be descriptive and specific

#### `description` Field

**Purpose:** Explain what the instructions do and when they apply

**Examples:**

```yaml
description: "Python coding standards for the project"
description: "Instructions for API module development"
description: "React and TypeScript best practices for frontend"
```

**Rules:**

- Keep under 200 characters
- Be specific about scope
- Explain the purpose clearly
- Use present tense

#### `applyTo` Field (Optional)

**Purpose:** Glob pattern defining which files trigger auto-application

**Common patterns:**

```yaml
# All Python files
applyTo: "**/*.py"

# Specific directory
applyTo: "modules/api/**"

# Multiple extensions
applyTo: "**/*.{ts,tsx}"

# Nested directories
applyTo: "src/components/**/*.tsx"

# All files
applyTo: "**"
```

**Rules:**

- Use `**` for recursive matching
- Use `*` for single-level wildcard
- Use `{ext1,ext2}` for multiple extensions
- If omitted, instructions are manual-only

### Complete Example

```yaml
---
name: "Database_Module_Standards"
description: "Coding standards and architecture guidelines for database module"
applyTo: "backend/src/db/**/*.py"
---
```

## Prompt Files Frontmatter

### Required Fields

```yaml
---
name: create-component
description: "Generate React component from template"
---
```

### Optional Fields

```yaml
---
name: create-component
description: "Generate React component from template"
argument-hint: "component name and props"
agent: "agent"
model: "GPT-4o"
tools: ["githubRepo", "search/codebase"]
---
```

### Field Specifications

#### `name` Field

**Format:** Use hyphens (lowercase-hyphen-case) for command names

**Examples:**

```yaml
name: create-react-form
name: security-review
name: generate-tests
```

**Rules:**

- Use hyphens only (not underscores or spaces)
- All lowercase
- Keep under 30 characters
- Match what user types after `/`

#### `argument-hint` Field

**Purpose:** Hint text shown in chat input field

**Examples:**

```yaml
argument-hint: "module name"
argument-hint: "form name and fields"
argument-hint: "file path to review"
```

**Rules:**

- Keep very short (under 50 chars)
- Describe what user should provide
- Use lowercase
- No punctuation

#### `agent` Field

**Values:** Which agent runs the prompt

```yaml
agent: "ask"      # Ask agent (read-only)
agent: "edit"     # Edit agent (file modifications)
agent: "agent"    # Full agent (tools + edits)
agent: "custom"   # Custom agent name
```

**Default:** If omitted, uses current agent selection

#### `model` Field

**Purpose:** Specific LLM model to use

**Examples:**

```yaml
model: "GPT-4o"
model: "Claude Sonnet 4"
model: "o3-mini"
```

**Rules:**

- If omitted, uses current model selection
- Must be exact model name from provider
- Case-sensitive

#### `tools` Field

**Purpose:** List of available tools for this prompt

**Available tools:**

```yaml
tools:
  - "githubRepo"           # GitHub repository access
  - "search/codebase"      # Semantic code search
  - "search/web"           # Web search
  - "terminal"             # Terminal commands
  - "fileEditor"           # File editing
```

**Examples:**

```yaml
# Single tool
tools: ["githubRepo"]

# Multiple tools
tools: ["githubRepo", "search/codebase", "terminal"]
```

### Complete Example

```yaml
---
name: create-test-suite
description: "Generate comprehensive test suite for module"
argument-hint: "module path"
agent: "agent"
model: "GPT-4o"
tools: ["search/codebase", "githubRepo", "fileEditor"]
---
```

## YAML Syntax Rules

### General Rules

- Use spaces for indentation (not tabs)
- Indentation is 2 spaces
- Wrap strings with special characters in quotes
- Start and end with `---` delimiters

### String Quoting

**Always quote:**

```yaml
description: "Contains: special characters"
applyTo: "**/*.{ts,tsx}"  # Contains braces
```

**Can omit quotes:**

```yaml
name: simple-name
agent: ask
```

### Lists

**Inline format:**

```yaml
tools: ["tool1", "tool2", "tool3"]
```

**Block format:**

```yaml
tools:
  - "tool1"
  - "tool2"
  - "tool3"
```

### Common Errors

**❌ Wrong indentation:**

```yaml
---
name: "Test"
  description: "Wrong indent"  # Too much indent
---
```

**❌ Tabs instead of spaces:**

```yaml
---
name: "Test"
	description: "Using tabs"  # Will fail to parse
---
```

**❌ Missing quotes with special characters:**

```yaml
description: Contains: colons  # Will fail
applyTo: **/*.{ts,tsx}        # Will fail
```

**✅ Correct:**

```yaml
---
name: "Test_Instructions"
description: "Contains: properly quoted colons"
applyTo: "**/*.{ts,tsx}"
---
```

## Validation Checklist

Before saving your file:

- [ ] YAML starts and ends with `---`
- [ ] All required fields present (`name`, `description`)
- [ ] Proper indentation (2 spaces, no tabs)
- [ ] Strings with special characters are quoted
- [ ] `name` format matches file type (underscores for instructions, hyphens for prompts)
- [ ] `applyTo` pattern is valid glob syntax (for instructions)
- [ ] `tools` are from available list (for prompts)

## Testing Your Frontmatter

### Instructions Files

1. Save file in `.github/instructions/`
2. Open VS Code Chat
3. Check "Configure Chat" > "Chat Instructions"
4. Verify file appears in list
5. Check file with `applyTo` pattern by opening matching file

### Prompt Files

1. Save file in `.github/prompts/`
2. Open VS Code Chat
3. Type `/` and verify prompt appears
4. Check argument hint shows correctly
5. Test prompt execution

## Further Reading

- [VS Code Custom Instructions Docs](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
- [VS Code Prompt Files Docs](https://code.visualstudio.com/docs/copilot/customization/prompt-files)
- [YAML Specification](https://yaml.org/spec/1.2.2/)
