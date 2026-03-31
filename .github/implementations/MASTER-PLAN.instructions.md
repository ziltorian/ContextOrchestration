---
name: Master Plan
description: Master development plan for the project
---

# Development Master Plan

**Version:** 1.0  
**Date:** {YYYY-MM-DD}  
**Status:** {Planning | In Progress | Pre-Release | Released}  

---

## Project Overview

{Brief description: what the project does, who it is for, and its key capabilities.}

**Technology stack** (fill in what applies to your project):

| Layer | Choice |
|-------|--------|
| {e.g., Backend} | {e.g., Python + FastAPI} |
| {e.g., Frontend} | {e.g., React} |
| {e.g., Storage} | {e.g., PostgreSQL} |
| ... | ... |

**Key documentation:**

- `README.md`
- {Add paths to specifications, API docs, architecture docs relevant to your project}

---

## Current Status

<!-- Update this section as phases progress -->

| Phase | Status | Date |
|-------|--------|------|
| Phase 1 | ✅ Completed | {date} |
| Phase 2 | 🔄 In Progress | {date} |
| Phase 3 | ⬚ Not Started | — |

---

## Phases

Define as many or as few phases as your project needs. Each phase should be independently deliverable — merging Phase N should not require Phase N+1 to function.

### Phase 1: {Name}

**Goal:** {One sentence describing the outcome}  
**Deliverables:** {List of artifacts this phase produces}  
**Acceptance criteria:** {How to verify this phase is done}  
**Plan file:** `.github/implementations/{phase-1}-implementation.instructions.md`

### Phase 2: {Name}

**Goal:** {One sentence}  
**Deliverables:** {List}  
**Acceptance criteria:** {Verification}  
**Plan file:** `.github/implementations/{phase-2}-implementation.instructions.md`

<!-- Add more phases as needed. Remove unused ones. -->

---

## Phase Dependencies

Describe how phases depend on each other. Not all projects are strictly sequential — some phases may run in parallel.

```text
Phase 1
    ↓
Phase 2 ──→ Phase 3
    ↓
Phase 4
```

<!-- Adapt this diagram to your actual dependency graph -->

---

## Artifacts Checklist

List the deliverables your project requires. This is project-specific — include only what applies.

**Documentation:**

- [ ] {e.g., Technical design document}
- [ ] {e.g., API documentation}
- [ ] {e.g., User guide}

**Code:**

- [ ] {e.g., Core module}
- [ ] {e.g., Test suites}

**Infrastructure:**

- [ ] {e.g., CI/CD pipeline}
- [ ] {e.g., Deployment configuration}

---

## Release Criteria

Define what "done" looks like for a release. Include criteria relevant to your project.

**Functional:**

- [ ] {e.g., Core user flows work end-to-end}
- [ ] {e.g., All critical paths have tests}

**Non-functional (if applicable):**

- [ ] {e.g., Response time under X ms for key operations}
- [ ] {e.g., No critical or high-severity security issues}

---

## Deferred Scope

<!-- Optional. List features that are out of scope for the current version but planned for future releases. -->

- {e.g., Feature X — planned for v2.0}
- {e.g., Integration with Y — pending upstream API stability}

---

## Risks and Mitigations

<!-- Identify risks specific to your project. Use the format below. -->

1. **{Risk title}**
   Mitigation: {How you plan to address it}

2. **{Risk title}**
   Mitigation: {How you plan to address it}

<!-- Add more as needed. Common risk categories:
     - Technical complexity / unknowns
     - External dependencies / API stability
     - Performance / scalability
     - Security
     - Team capacity / knowledge gaps
-->

---
