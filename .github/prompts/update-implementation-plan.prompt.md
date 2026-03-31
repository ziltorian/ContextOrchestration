---
name: update-implementation-plan
description: "Add tasks or update existing implementation plan"
argument-hint: "plan identifier"
---

Update implementation plan by adding tasks, marking completion, or adjusting estimates.

## Prerequisites

**Load the implementation-planning skill first:**
Read `.github/skills/implementation-planning/SKILL.md` to understand plan structure, task format conventions, and section organization before making changes.

## Input

Plan to update: `${input:planIdentifier}`

## Workflow

### Step 1: Locate and Read Plan

1. Find the implementation plan in project's implementation directory
2. Read current plan to understand:
   - Existing task IDs (avoid conflicts)
   - Section structure and organization
   - Completed vs pending tasks

### Step 2: Read Related Context

If adding new features, check:
- Related specification documents
- Associated design documentation
- Dependencies with other plans

### Step 3: Apply Updates

Choose update type based on need.

## Update Types

### Type 1: Add New Feature Module

Add complete module description with implementation tasks:

1. Add section in "Proposed Changes" describing the module
2. Add corresponding tasks in "Task" section
3. Include file creation, implementation, and testing tasks
4. Use proper task IDs following project convention

### Type 2: Add Tasks to Existing Section

Extend existing feature with more tasks:

1. Locate target section in "Task" part
2. Add tasks with incremented IDs from last used
3. Use checkbox format: `- [ ]` for pending

### Type 3: Mark Tasks Complete

Update task status:
- Change `- [ ]` to `- [x]`
- Keep task ID intact
- Never remove completed tasks

### Type 4: Split Task into Subtasks

Break complex task into smaller units:
- Keep parent task
- Add subtasks with letter suffixes (`2a`, `2b`, `2c`)
- Each subtask gets proper checkbox

## Task Format Standards

### Task Structure

```markdown
### Section Name

- [ ] Task description <!-- id: PREFIX-N -->
- [ ] Task with subtasks <!-- id: PREFIX-N+1 -->
  - [ ] Subtask A <!-- id: PREFIX-N+1a -->
  - [ ] Subtask B <!-- id: PREFIX-N+1b -->
- [ ] Another task <!-- id: PREFIX-N+2 -->
```

### ID Convention

**Format:** `<!-- id: PREFIX-NUMBER[LETTER] -->`

**Rules:**
- Choose prefix matching the section (e.g., `API-`, `DB-`, `UI-`, `TEST-`)
- Start from 1 per prefix
- Increment sequentially
- Subtasks use letters: `2a`, `2b`, `2c`
- Never reuse IDs
- Continue from highest existing ID in plan

### Task Description Principles

**Good practices:**
- Be specific about files, classes, or functions
- Use action verbs: Create, Implement, Update, Test, Verify
- Include verification criteria for test tasks

**Avoid:**
- Vague descriptions ("Fix bugs", "Update code")
- Missing context
- Ambiguous scope

## Content Placement

**"Proposed Changes" section:**
- Add module/component descriptions
- Group related changes together
- Maintain logical order

**"Task" section:**
- Add tasks under appropriate headers
- Create new header if new feature area
- Order by implementation dependencies

**"Verification" section:**
- Add verification steps for new components
- Update test procedures if needed

## Verification Checklist

Before finalizing update:

- [ ] All new tasks have unique IDs
- [ ] IDs follow `PREFIX-NUMBER[LETTER]` format
- [ ] Task descriptions are specific and actionable
- [ ] Completed tasks marked with `[x]`
- [ ] Sections properly formatted
- [ ] No duplicate task IDs

## Output

Report changes clearly:

```
✅ Implementation plan updated: [file path]

Changes made:
- New sections added: [count]
- New tasks added: [count]
- Tasks marked complete: [count]
- Task IDs used: PREFIX-N through PREFIX-M
```
