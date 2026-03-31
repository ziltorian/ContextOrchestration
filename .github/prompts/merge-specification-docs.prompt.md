---
name: merge-specification-docs
description: "Integrate new specification into main documentation and update implementation plans"
argument-hint: "path to new specification file"
---

Integrate new specification document into main project documentation and update implementation plans.

## Input

Specification file path: `${input:specificationPath}`

## Task Overview

When a new detailed specification is added:

1. **Extract key information** from specification
2. **Merge summaries** into relevant main documentation
3. **Update documentation index** (if project has one)
4. **Update implementation plans** with new tasks
5. **Add table of contents** to specification if missing

## Analysis Phase

### Step 1: Read Specification

Understand:
- Main concepts and architecture
- Key features and components
- MVP vs future phases
- Technical requirements
- Integration points

### Step 2: Identify Target Documents

Determine which main docs need updates based on content type:

**Architecture documents:**
- System architecture overview
- Component interaction diagrams
- Workflow descriptions

**Feature documents:**
- Feature lists and roadmaps
- MVP definitions
- Functional requirements

**Technical documents:**
- Technology stack
- Database schemas
- API specifications

**Implementation documents:**
- Phase plans
- Task lists
- Development roadmap

## Merging Strategy

### Key Principles

1. **No code duplication** - summarize, don't copy entire code blocks
2. **Natural language first** - describe concepts in prose, minimize code examples
3. **Reference detailed specs** - link to full specification for details
4. **Maintain consistency** - update conflicting information in main docs
5. **Length awareness** - keep main docs concise (prefer 5,000-10,000 chars per doc)

### What to Extract

From each specification section, extract:

**Essential concepts:**
- High-level architecture principles
- Key component descriptions
- Integration patterns

**MVP features:**
- What's included in MVP
- What's deferred to v1.5+
- Critical requirements

**Data structures:**
- Directory layouts (text diagrams)
- File organization patterns
- Key configuration formats (minimal examples)

**Workflows:**
- Process descriptions
- State transitions
- Component interactions

### What to Keep in Specification Only

Leave detailed content in the specification file:
- Complete code examples
- Full JSON/YAML schemas
- Detailed API signatures
- Implementation pseudocode
- Step-by-step tutorials
- Exhaustive security policies

## Integration Process

### Phase 1: Update Main Documentation

For each target document:

1. **Read current state** to understand existing structure
2. **Identify merge points** - which sections need updates
3. **Synthesize content** - create concise summaries of new concepts
4. **Resolve conflicts** - update contradictory information
5. **Add cross-references** - link to detailed specification

**Merge techniques:**

- **Extend existing sections** with new bullet points
- **Create new subsections** for entirely new concepts
- **Update diagrams** (text-based) with new components
- **Enrich architecture descriptions** with new layers

### Phase 2: Update Documentation Index

Edit `.github/instructions/Project_Docs_Context.instructions.md`:

1. **Add specification entry** in "Detailed Specifications (docs/specification/)" section
2. **Update matrices** - add specification to "Matrix: Task → Documentation"
3. **Add to workflow** - include in relevant workflow categories

**Entry format:**

```markdown
**Specification_File_Name.md**
One-sentence summary of what it covers: key concepts, what to read it for. Triggers: when working on [X], when planning [Y], when implementing [Z].
```

### Phase 3: Update Implementation Plans

For each affected phase plan in `.github/implementations/`:

1. **Read current tasks** to understand existing structure
2. **Add new sections** under "Proposed Changes" if new modules needed
3. **Add new tasks** in "Task" section with proper IDs
4. **Update time estimates** in master plan if significant additions
5. **Add references** to specification in Background/Context

**Task format:**

```markdown
### New Feature Name

- [ ] Create `path/to/new/module.py` <!-- id: XX-N -->
- [ ] Implement ClassName <!-- id: XX-N+1 -->
  - [ ] Subtask if needed <!-- id: XX-N+1a -->
- [ ] Test feature <!-- id: XX-N+2 -->
```

**ID Convention:**
- Use existing prefix (e.g., `WS-` for Workspace, `PM-` for Persistent Memory)
- Increment from highest existing ID

### Phase 4: Add Table of Contents

If specification lacks a table of contents, add at the beginning:

```markdown
## Table of Contents

- [Section 1](#1-section-1-title)
- [Section 2](#2-section-2-title)
  - [Subsection 2.1](#21-subsection-title)
```

**Format rules:**
- Use `[Display Text](#anchor-link)` format
- Anchor links: lowercase, numbers preserved, spaces→hyphens, no special chars
- Preserve original heading structure

## Guidelines

## Verification

After merging:

- [ ] No code duplication between main docs and specifications
- [ ] Main docs contain only summaries and key concepts
- [ ] Cross-references are correct
- [ ] Implementation plans updated with new tasks
- [ ] Documentation index updated (if applicable)
- [ ] No contradictions between documents
- [ ] Length limits respected
- [ ] Specification has table of contents

## Output Format

```markdown
✅ Specification integrated

### Specification File
Updated: [file path]

### Main Documentation
- [Document 1]: [summary of changes]
- [Document 2]: [summary of changes]

### Documentation Index
- [what was updated]

### Implementation Plans
- [Plan 1]: [new tasks added]
- [Plan 2]: [new tasks added]

## Verification
✅ No duplication
✅ No contradictions
✅ Minimal code in main docs
✅ TOC added to specification
✅ Implementation plans updated
```


