---
name: create-technical-specification
description: "Create comprehensive technical specification document for new system or feature"
argument-hint: "system/feature name"
---

Create a detailed technical specification document for a new system, module, or feature.

## Input

System/Feature name: `${input:systemName}`

## Research Phase

### Step 1: Understand Requirements

Gather context before writing:

1. **Read related documentation:**
   - Project overview and architecture docs
   - Existing specifications for similar systems
   - Current technical stack documentation

2. **Search existing implementations:**
   - Check for related features or modules
   - Identify integration points
   - Understand current patterns

3. **Review implementation plans:**
   - Check project roadmap and priorities
   - Understand current development phase

### Step 2: Define Scope

Clarify coverage:
- **System boundary** - what's included and excluded
- **MVP vs future phases** - phasing strategy
- **Dependencies** - what must exist first
- **Integration points** - connections to existing systems

## Document Structure

### Required Sections

```markdown
# Specification: ${input:systemName}

**Version:** 1.0
**Date:** [Current Date]
**Context:** [One-sentence description]

---

## Contents

[Auto-generated table of contents]

---

## 1. Overview and Principles

### Problem
[Describe the problem this system solves]

### Solution
[High-level solution approach]

### Key Principles
[3-7 core design principles]

---

## 2. Architecture

### Overall Architecture
[Component diagram or description]

### Components
[Major component descriptions]

### Interactions
[How components interact]

---

## 3. Detailed Specification

[Technical details subdivided by component/feature]

### 3.1 [Component 1]

**Purpose:** [Why this exists]

**Structure:** [Files, classes, modules]

**API:** [Methods, functions, endpoints]

**Data Formats:** [Schemas, examples]

---

## 4. Integration

### 4.1 Integration with [System A]

**Integration Points:** [Specific connection points]

**Data Flow:** [Data exchange patterns]

**Dependencies:** [Prerequisites]

---

## 5. Security and Policies

[Security considerations, access control, threat model]

---

## 6. Data Formats and Configuration

[Complete schemas, configuration templates, validation rules]

---

## 7. Usage Examples

[3-5 practical examples with complete code]

### Example 1: [Use Case]

[Code with setup, execution, expected output]

---

## 8. Implementation

**MVP Scope:** [What must be in MVP]

**Future Enhancements:** [What's planned for later phases]

**Roadmap:** [Implementation phases]

---

## 9. Testing

[Testing strategy, critical test cases, verification methods]

---

## 10. Appendices

[Additional reference material, complete schemas]

---
```

## Writing Guidelines

### Content Requirements

**Section 1 (Overview):**
- Clear problem statement (2-4 paragraphs)
- High-level solution
- 3-7 core principles with rationale
- Length: 1,000-2,000 characters

**Section 2 (Architecture):**
- Visual/structural overview (text-based diagrams OK)
- Component list with descriptions
- Integration with existing architecture
- Length: 1,500-3,000 characters

**Section 3 (Detailed Specification):**
- Complete component descriptions
- Class/module structures with type hints
- Method signatures
- Data flow diagrams
- Configuration options
- Length: No limit (can be 20,000+ characters)

**Sections 4-6:**
- Specific integration points
- Security considerations when applicable
- Complete schemas with examples
- Length: Variable based on complexity

**Section 7 (Examples):**
- 3-5 realistic use cases
- Complete code (not pseudocode)
- Setup, execution, expected output
- Length: 3,000-8,000 characters

**Sections 8-9:**
- Clear MVP vs future split
- Implementation order
- Test strategy and critical test cases
- Length: 1,000-2,000 characters each

### Style Standards

**Language:**
- Technical but accessible
- Consistent terminology
- Define domain-specific terms

**Code examples:**
- Full context (imports, class definitions)
- Proper type hints
- Realistic examples (not `foo`, `bar`)
- Include docstrings
- Show error handling when relevant

**Formatting:**
- Use headings: `## 1. Top`, `### 1.1 Second`, `#### 1.1.1 Third`
- Code blocks with language: ` ```python`
- Bullet lists with hyphens
- Tables for comparisons

## Output

Save document to appropriate location (e.g., `docs/specifications/` or `specs/`) and report:

```
✅ Specification created: [file path]

Sections included:
- Overview and Principles
- Architecture
- Detailed Specification ([X] components)
- Integration ([Y] systems)
- Security (if applicable)
- Data Formats
- [Z] Usage Examples
- Implementation Roadmap
- Testing Strategy

Document length: ~[N] characters

Next steps:
- Review specification with stakeholders
- Create implementation plan based on specification
- Add specification to documentation index
```
