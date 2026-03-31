# YAML Frontmatter Specification

Complete guide to YAML frontmatter headers in implementation instruction files.

## Overview

Every `*-implementation.instructions.md` file must begin with YAML frontmatter enclosed by triple dashes (`---`). This metadata defines the implementation scope and helps AI agents understand when and where to apply the plan.

## Required Fields

### name

**Purpose:** Human-readable title for the implementation plan

**Format:**
```yaml
name: Module_Name Implementation
```

**Rules:**
- Describe what the implementation achieves
- Use title case
- Include module/feature name
- Keep concise (50 characters or less)

**Examples:**
```yaml
name: Pagination Fix Implementation
name: User Authentication Module
name: API Error Handling Improvements
```

### description

**Purpose:** Brief summary of what the implementation accomplishes

**Format:**
```yaml
description: Implementation for feature_name with detailed explanation.
```

**Rules:**
- 1-2 sentences maximum
- Clearly state the outcome
- Avoid technical jargon unless necessary
- Focus on business value or user impact

**Examples:**
```yaml
description: Fix pagination detection logic to handle dynamic page counts and improve error messages.
description: Implement OAuth 2.0 authentication flow with token refresh and session management.
description: Standardize API error responses across all endpoints with proper status codes.
```

### applyTo

**Purpose:** Glob pattern specifying which files this implementation applies to

**Format:**
```yaml
applyTo: "path/to/files/**/*.ext"
```

**Rules:**
- Use relative paths from workspace root
- Specify file types when possible
- **Avoid `**` for global scope** - be specific
- Use quotes around patterns
- Multiple patterns can be specified (see examples)

**Pattern Syntax:**
- `*` - Matches any characters except `/`
- `**` - Matches any characters including `/`
- `?` - Matches single character
- `[abc]` - Matches any character in brackets
- `{js,ts}` - Matches either pattern

**Examples:**

Single module:
```yaml
applyTo: "src/auth/**"
```

Specific file types:
```yaml
applyTo: "src/**/*.{ts,tsx}"
```

Multiple directories:
```yaml
applyTo: "src/api/** src/models/**"
```

Specific module:
```yaml
applyTo: "src/features/pagination/**"
```

Test files:
```yaml
applyTo: "tests/**/*.test.ts"
```

**Anti-patterns (avoid):**

❌ Too broad:
```yaml
applyTo: "**"
```

❌ Missing quotes:
```yaml
applyTo: src/**/*.ts
```

❌ Absolute paths:
```yaml
applyTo: "/home/user/project/src/**"
```

## Optional Fields

### agent

**Purpose:** Specify which agent should handle this implementation

**Format:**
```yaml
agent: agent_name
```

**Examples:**
```yaml
agent: agent
agent: implementation-agent
```

**When to use:**
- Working with multiple specialized agents
- Delegating specific implementation types
- Integrating with agent orchestration systems

### version

**Purpose:** Track implementation plan versions

**Format:**
```yaml
version: "1.0.0"
```

**Examples:**
```yaml
version: "1.0.0"
version: "2.1.0"
```

**When to use:**
- Managing multiple iterations of same plan
- Tracking breaking changes in requirements
- Coordinating with version control

### tags

**Purpose:** Categorize implementations for filtering and search

**Format:**
```yaml
tags: [tag1, tag2, tag3]
```

**Examples:**
```yaml
tags: [bugfix, high-priority, backend]
tags: [feature, frontend, authentication]
```

**When to use:**
- Organizing many implementation plans
- Filtering by priority or category
- Tracking implementation types

## Complete Examples

### Example 1: Bug Fix Implementation

```yaml
---
name: Pagination Bug Fix
description: Fix page detection logic to correctly identify last page in paginated results.
applyTo: "src/pagination/**/*.ts"
tags: [bugfix, pagination]
version: "1.0.0"
---
```

### Example 2: New Feature Implementation

```yaml
---
name: OAuth 2.0 Authentication
description: Implement complete OAuth 2.0 authentication flow with token management and session handling.
applyTo: "src/auth/** src/api/middleware/auth.ts"
agent: implementation-agent
tags: [feature, security, authentication]
version: "1.0.0"
---
```

### Example 3: Refactoring Implementation

```yaml
---
name: API Error Handling Refactor
description: Standardize error handling across all API endpoints using centralized error middleware.
applyTo: "src/api/**/*.ts"
tags: [refactor, api, error-handling]
---
```

### Example 4: Test Implementation

```yaml
---
name: Pagination Unit Tests
description: Add comprehensive unit tests for pagination module covering edge cases and error scenarios.
applyTo: "tests/pagination/**/*.test.ts"
tags: [testing, pagination]
---
```

### Example 5: Multi-Module Implementation

```yaml
---
name: User Profile Feature
description: Implement user profile management with CRUD operations, validation, and profile picture uploads.
applyTo: "src/features/profile/** src/api/routes/profile.ts src/models/user.ts"
tags: [feature, user-management]
version: "1.0.0"
---
```

## Validation Rules

### Required Validation

Before finalizing frontmatter, verify:

- [ ] All three required fields present (`name`, `description`, `applyTo`)
- [ ] `applyTo` uses quotes around pattern
- [ ] `applyTo` uses relative paths (not absolute)
- [ ] `description` is 1-2 sentences
- [ ] `name` is concise and descriptive

### Optional Validation

If using optional fields:

- [ ] `version` follows semantic versioning (if used)
- [ ] `tags` are lowercase and hyphenated (if used)
- [ ] `agent` matches available agent names (if used)

## Common Mistakes

### ❌ Mistake 1: Missing Required Fields

```yaml
---
name: My Implementation
# Missing description and applyTo
---
```

**Fix:**
```yaml
---
name: My Implementation
description: Brief description of what this implements.
applyTo: "src/module/**"
---
```

### ❌ Mistake 2: Overly Broad applyTo

```yaml
---
name: Bug Fix
description: Fix the bug
applyTo: "**"  # Too broad!
---
```

**Fix:**
```yaml
---
name: Bug Fix
description: Fix pagination detection in results processor
applyTo: "src/pagination/**/*.ts"
---
```

### ❌ Mistake 3: Unquoted Pattern

```yaml
---
name: Implementation
description: Description here
applyTo: src/**/*.ts  # Missing quotes
---
```

**Fix:**
```yaml
---
name: Implementation
description: Description here
applyTo: "src/**/*.ts"
---
```

### ❌ Mistake 4: Absolute Paths

```yaml
---
name: Implementation
description: Description here
applyTo: "/home/user/project/src/**"  # Absolute path
---
```

**Fix:**
```yaml
---
name: Implementation
description: Description here
applyTo: "src/**"  # Relative to workspace root
---
```

## Integration with VS Code

The frontmatter format aligns with VS Code's custom instructions specification:

- **Compatible with `.instructions.md` files** - Same YAML format
- **Follows GitHub Copilot conventions** - Uses standard fields
- **Works with custom agents** - Integrates with VS Code agent system

See [VS Code Custom Instructions documentation](https://code.visualstudio.com/docs/copilot/customization/custom-instructions) for more details on the underlying specification.

## Summary

**Minimum valid frontmatter:**
```yaml
---
name: Implementation Name
description: What this implementation does.
applyTo: "path/to/files/**"
---
```

**Full-featured frontmatter:**
```yaml
---
name: Feature Implementation
description: Detailed description of implementation goals and outcomes.
applyTo: "src/feature/** src/api/routes/feature.ts"
agent: implementation-agent
version: "1.0.0"
tags: [feature, high-priority]
---
```

The frontmatter provides crucial metadata that helps AI agents understand:
- **What** the implementation is (name, description)
- **Where** it applies (applyTo pattern)
- **How** to handle it (agent, version, tags)
