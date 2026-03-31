---
name: implementation-planning
description: Create structured implementation plans with task breakdowns, phase delivery, risk assessment, and testing strategy. Use when starting new features, fixing bugs, refactoring code, or when user mentions "implementation plan", "design document", "technical spec", or needs to break down complex work into actionable tasks. Always use before writing any production code.
compatibility: VS Code with GitHub Copilot or similar AI coding assistants
metadata:
  author: ziltorian
  version: "2.0"
  category: project-management
---

# Implementation Planning

Systematically research codebases, design solutions, and create actionable implementation plans before writing code. Separates planning from execution with thorough context gathering, risk assessment, and phase-based delivery.

## Core Workflow

### Phase 1: Planning Mode

1. **Context Gathering** — Research the codebase comprehensively
2. **Red Flags Check** — Identify risks before writing the plan
3. **Plan Creation** — Document designs, phases, tasks, risks, and testing strategy
4. **User Review** — Present plan for feedback and refinement
5. **Iteration** — Refine based on feedback until approved

### Phase 2: Implementation Mode

1. **Task Execution** — Implement changes following the approved plan
2. **Progress Tracking** — Update task status `[ ]` → `[/]` → `[x]`
3. **Verification** — Test and validate changes
4. **Documentation** — Record what was done

## Planning Mode: Detailed Workflow

### Step 1: Context Gathering

Before writing any plan:

1. Read `SubAgents-tasks/task-{task-name}.md` — goal, scope, done criteria, constraints
2. Read `SubAgents-context/{task-name}-subagent-context.md` — prior agent findings
3. Read project instructions in `.github/instructions/` related to the task
4. Start with high-level searches, then read specific files
5. For every affected component: find exact file paths, class/method names, line numbers
6. Stop at 80% confidence — you can articulate root causes and proposed changes

### Step 2: Red Flags Check

Before writing the plan, check affected code for:

- Functions longer than 50 lines
- Nesting deeper than 4 levels
- Duplicated logic that will be touched
- Missing error handling in the execution path
- Missing or weak tests for affected areas
- Performance bottlenecks in the affected path
- Hardcoded values that should be configurable

Note any red flags in the Background section of the plan.

### Step 3: Document Structure

#### YAML Frontmatter

```yaml
---
name: Module_Name Implementation
description: Brief description of what this implementation achieves
applyTo: "src/module_name/**"
---
```

- `name` — descriptive title
- `description` — 1-2 sentence summary
- `applyTo` — specific glob, avoid `**`

#### Section 1: Goal + Background

```markdown
## Goal
[1-2 sentence outcome]

## Background
**Observed symptoms:**
- [Symptom with file/log reference]

**Root cause:**
- [Cause with file:function reference]
```

Rules: Goal = 1-2 sentences. Never mix symptoms and root causes in one paragraph.

#### Section 2: Phase Breakdown

Break large work into independently deliverable phases. Each phase must be mergeable without later phases to function.

```markdown
## Phases

**Phase 1: Minimum viable** — smallest slice that provides value
**Phase 2: Core experience** — complete happy path  
**Phase 3: Edge cases** — error handling, polish
**Phase 4: Optimization** — performance, monitoring (if needed)
```

For small tasks one phase is fine. For large features 2-4 phases prevent all-or-nothing delivery risk.

**Example — Bad (single monolithic phase):**
```markdown
## Task
- [ ] Implement entire auth system <!-- id: A-1 -->
```

**Example — Good (phased):**
```markdown
## Phases
**Phase 1:** Database schema + basic login
**Phase 2:** OAuth flow + session management
**Phase 3:** Rate limiting + security audit
```

#### Section 3: Proposed Changes

Group by component. For every file include: method, line range, what changes, **Why**, and **Risk**.

```markdown
## Proposed Changes

### [Component Name]

#### [MODIFY] `path/to/file.py`
**Method:** `method_name()` (lines X-Y)
**Changes:**
- [Specific change 1]
- [Specific change 2]
**Why:** [What breaks without this change]
**Risk:** Low | Medium | High

#### [NEW] `path/to/new_file.py`
**Purpose:** [What it does]
**Contains:**
- `ClassName` — [description]
**Why:** [Reason]
**Risk:** Low
```

**Risk levels:**
- **Low** — isolated change, no shared state, easy to revert
- **Medium** — touches shared interfaces, requires coordination with other components
- **High** — auth, payments, data integrity, webhooks, external integrations, migrations

**Why is mandatory.** Without it, the implementer cannot decide if an alternative approach is acceptable.

**Example — Bad:**
```markdown
#### [MODIFY] `utils.py`
**Method:** `validate_input()` (line ~45)
- Add multiple validation rules
```

**Example — Good:**
```markdown
#### [MODIFY] `utils.py`
**Method:** `validate_input()` (line 45)
- Add null/empty check before type validation
- Return `ValidationResult` dataclass instead of bool
**Why:** Current bool return loses error detail; callers cannot show actionable messages
**Risk:** Medium — changes return type, all callers must be updated (3 files identified)
```

#### Section 4: Task List

```markdown
## Task

### [Phase 1 — Component Name]
- [ ] Task description <!-- id: C1-1 -->
- [ ] Task description <!-- id: C1-2 -->

### [Phase 2 — Component Name]
- [ ] Task description <!-- id: C2-1 -->

### Tests
- [ ] Create test_X.py for [component] <!-- id: T-1 -->
- [ ] Add integration test for [flow] <!-- id: T-2 -->
```

Rules:
- Group by phase AND component
- Each task = one atomic action
- Unique IDs in HTML comments: `C` for component, `T` for tests
- NEVER duplicate tasks
- Tests always in a separate group at the end
- Map every Done Criterion from task file to at least one task ID

#### Section 5: Testing Strategy (Required)

Unlike Verification (which is optional), Testing Strategy is mandatory.

```markdown
## Testing Strategy

**Unit tests:**
- `test_validators.py` — `validate_input()` null/empty/type cases

**Integration tests:**
- Full auth flow: login → token issue → protected route access

**Manual verification:**
1. [Action]
2. [Expected result]

**Edge cases:**
- Empty input to `validate_input()`
- Concurrent webhook events for same subscription
- Token expiry during multi-step flow
```

#### Section 6: Success Criteria

Copy directly from `SubAgents-tasks/task-{task-name}.md` Done Criteria:

```markdown
## Success Criteria
- [ ] [Done criterion 1]
- [ ] [Done criterion 2]
```

Every criterion must map to at least one task ID. If a criterion has no corresponding task, the plan is incomplete.

#### Section 7: Risks & Mitigations

For every Medium/High risk item in Proposed Changes:

```markdown
## Risks & Mitigations

- **Risk:** Webhook events arrive out of order
  - Mitigation: Use event timestamps, idempotent updates
- **Risk:** Return type change breaks existing callers
  - Mitigation: Update all 3 callers in Phase 1 before merging
```

#### Section 8: User Review Required (Optional)

Only for breaking changes or decisions the implementer cannot make:

```markdown
## User Review Required

> [!IMPORTANT]
> Should we migrate existing sessions or invalidate all on deploy?

> [!WARNING]
> Phase 2 requires a database migration that cannot be rolled back without data loss.
```

Omit entirely if no critical decisions needed.

### Step 4: File Constraints

- Maximum 12,000 characters
- No code snippets — method/class names only
- No duplicate tasks
- Every `[MODIFY]` must have Why + Risk
- Every Done Criterion must have a corresponding task

### Step 5: Present and Iterate

After creating the file:
1. Present to user as draft for feedback
2. Request approval or changes
3. Iterate — do NOT start implementation until explicitly approved

## Implementation Mode: Execution Workflow

### Locate Plan

Search for `**/*implementation.instructions.md` in `.github/implementations/`.

### Execute Tasks

For each task:
1. Read task description
2. Implement changes
3. Mark `[/]` when starting, `[x]` when complete
4. If blocked: mark `[/]`, investigate, add findings to plan, report

### Report Progress

After completing:
1. Mark all tasks `[x]`
2. Add "Changes Made" section:

```markdown
## Changes Made

### Validation Module (`src/utils.py`)
- Added `ValidationResult` dataclass (lines 10-15)
- Refactored `validate_input()` (lines 45-78)

### Tests
- Created `tests/test_validation.py` — 12 unit tests, all passing
```

## Key Differences from ECC Planner

Your planning agent uses a different philosophy than ECC's `planner.md`:

| Aspect | ECC planner | This skill |
|--------|------------|------------|
| Output | Free-form plan in chat | `.instructions.md` file with YAML frontmatter |
| Task tracking | No IDs | Unique IDs for traceability |
| Done Criteria | Success Criteria checklist | Mapped to SubAgents-tasks done criteria |
| Context | CLAUDE.md only | SubAgents-context + task file auto-injected |
| Testing | Testing Strategy section | Testing Strategy (required) + Verification (manual) |
| Phases | Phase 1-4 pattern | Phase breakdown section |
| Risk | Per-step Low/Medium/High | Per-file Why + Risk |

Both approaches share: specific file paths, method names, line numbers, Why reasoning, and phased delivery.

## Common Pitfalls

❌ Plan without Why for each change → implementer makes wrong tradeoffs  
✅ Every `[MODIFY]` has Why explaining what breaks without it

❌ Single phase for large feature → all-or-nothing delivery risk  
✅ Phase breakdown with independently mergeable slices

❌ Vague tasks like "improve validation"  
✅ Specific: "Add null check to `validate_input()` before type check"

❌ Testing Strategy omitted  
✅ Always include — at minimum unit tests and one manual verification step

❌ Done Criteria not mapped to tasks  
✅ Every criterion from task file has at least one task ID

❌ Files over 12,000 characters  
✅ Split into multiple plan files by component or phase

## References

- `references/YAML_FRONTMATTER.md` — Frontmatter specification
- `references/VS_CODE_INTEGRATION.md` — VS Code setup
- `references/EXAMPLES.md` — Real-world plan examples
- `references/TASK_TRACKING.md` — Advanced task management