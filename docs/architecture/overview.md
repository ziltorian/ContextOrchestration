# Architecture Overview

## Table of Contents

- [Agent Hierarchy](#agent-hierarchy)
- [Orchestration Layers](#orchestration-layers)
- [Components](#components)
- [Coordination Mechanisms](#coordination-mechanisms)
- [Key Decisions](#key-decisions)
- [Data Flow](#data-flow)

## Agent Hierarchy

```text
┌─────────────────────────────────────────────────┐
│                     USER                        │
└──────────────────────┬──────────────────────────┘
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
┌──────────────────┐    ┌──────────────────────┐
│ Program Director │    │   Direct Agent Call  │
│ (multi-project)  │    │   (single task)      │
└────────┬─────────┘    └──────────────────────┘
         │
    ┌────┴────┬──────────┐
    ▼         ▼          ▼
┌────────┐┌────────┐┌────────┐
│Project-││Project-││Project-│   (parallel Project Leads)
│Lead-   ││Lead-   ││Lead-   │
│Alpha   ││Beta    ││Gamma   │
└───┬────┘└───┬────┘└───┬────┘
    │         │         │
    ▼         ▼         ▼
┌────────────────────────────────────────────────┐
│           Specialized Subagents                │
│  code-reviewer | security-reviewer | QA | ...  │
└────────────────────────────────────────────────┘
```

## Orchestration Layers

### Layer 0: Program Director (Optional)

**Purpose:** Decomposes large projects into independent scopes, reads docs/specs directly, delegates project/code analysis and wave verification to approved subagents, and coordinates multiple Project Leads in iterative waves.
**File:** `.github/agents/Program-Director.agent.md`
**Workflow:** `.github/instructions/program-director-workflow.instructions.md`
**State:** `PROJECT_LEAD_JOURNAL.md` (Task Ledger, File Registry, Context Recovery, Progress Ledger)

Key patterns:

- Scope-based file partitioning (no overlapping files between Project Leads)
- Wave-based iteration (2-4 Project Leads per wave, max 5 waves)
- True batch launch for independent scopes, with sequential fallback only for dependency-constrained work
- Docs/spec self-study by Program Director plus delegated project/code analysis and post-wave verification via approved subagents
- Stall detection (2 consecutive zero-progress waves → termination)
- Structured handoff with identity, scope, and context recovery instructions

### Layer 1: Project Lead

**Purpose:** Orchestrates the full development pipeline for a single task or assigned scope.
**File:** `.github/agents/Project-Lead.agent.md`
**Workflow:** `.github/instructions/project-lead-workflow.instructions.md`
**State:** `PROJECT_LEAD_JOURNAL.md`, `SubAgents-context/subagent-context-{task-name}.instructions.md`

Modes:

- **Single-Project-Lead mode:** Standard operation, full journal control
- **Parallel mode:** Activated by Program Director; name-scoped journal, restricted file access

### Layer 2: Specialized Subagents

20 agents covering: intake, research, planning, implementation, review, security, QA, architecture audit, UI/UX design, test coverage, documentation, and cleanup.

## Components

### Agent Definitions (`.github/agents/`)

**Responsibility:** Define agent roles, tools, workflows, and constraints.
**Format:** `.agent.md` with YAML frontmatter + XML body sections.
**Count:** 20 agents (1 super-orchestrator, 1 orchestrator, 18 specialists).
**Nested orchestration:** constrained by explicit `agents` allowlists and workflow rules. Program Director may delegate only approved research, audit, closure, and Project Lead agents; deeper nested orchestration inside subagents remains limited to the repository's documented exceptions.

### Instructions (`.github/instructions/`)

**Responsibility:** Global rules applied across contexts — pipeline workflow, documentation standards, task marking.
**Format:** `.instructions.md` with YAML frontmatter including `applyTo` patterns.

### Skills (`.github/skills/`)

**Responsibility:** Reusable domain knowledge modules that agents reference for specialized tasks.
**Format:** `SKILL.md` in dedicated subdirectories.

### Task Files (`SubAgents-tasks/`)

**Responsibility:** Task definitions, project backlog, and pipeline stage documentation.
**Key file:** `project-todo.instructions.md` — the only file with `applyTo: '**'` for universal visibility.

### Context Files (`SubAgents-context/`)

**Responsibility:** Persistent current-state coordination between subagent invocations — one owned block per participant plus shared and protected sections.
**Format:** Reusable owned blocks with explicit role attribution, stable participant identity, and limited hygiene/archive exceptions.

### Implementation Plans (`.github/implementations/`)

**Responsibility:** Detailed change plans with phases, task IDs, risk assessment, and verification steps.

## Coordination Mechanisms

| Mechanism | Purpose | Owner |
| --------- | ------- | ----- |
| `PROJECT_LEAD_JOURNAL.md` | Dual-ledger: Task Ledger + File Registry + Progress Ledger | Program Director (ledger), Project Leads (progress) |
| `SubAgents-context/*.instructions.md` | Current-state task coordination between invocations; one owned block per participant, plus protected/shared sections | Pipeline participants (owned blocks), Project Lead (mid-task hygiene), implementation-completion-reporter (closure archive) |
| `SubAgents-tasks/task-*.instructions.md` | Immutable task definitions (Source/Goal) | task-creator |
| `project-todo.instructions.md` | Global task queue visible to all agents | User, task-creator (mode B) |
| `Required Documentation` section (in task + context files) | Curated list of documentation relevant to the task; populated at intake, extended by research agents | task-creator (initial), research agents + web-searcher (append) |
| File Registry (in journal) | Scope ownership: file → Project-Lead mapping | Program Director |

Context freshness rules at the architecture level:

- Each pipeline participant owns one reusable current block per task. Stable identity is the agent or role name by default, and the assigned Project Lead name in parallel mode.
- Repeated invocations and stage transitions update metadata inside the same owned block instead of creating new stage-specific entries.
- `Required Documentation` remains the sole shared-section exception, while `## User Comment` remains user-editable only.
- Non-user participants may detect a non-empty `## User Comment` and propagate only the signal upward. Project Lead must acknowledge the signal, record the reaction, and carry the state through `NEW`, `ACKNOWLEDGED`, `DEFERRED`, and `RESOLVED` without rewriting user text.
- During an active task, Project Lead may compact stale or superseded context only to restore one current owned block per participant while preserving active findings, current implementation status, `Required Documentation`, and the protected user section.
- At closure, `implementation-completion-reporter` owns archive handling. On `READY`, it may compress superseded context into a compact closure summary and transition the file to `ARCHIVE`; on `NOT READY`, it keeps current owned blocks visible and archives only resolved noise.

## Key Decisions

| Decision | Choice | Rationale |
| -------- | ------ | --------- |
| Scope enforcement | Prompt-level only | Industry standard; no platform supports file locking between agents |
| State management | File-based (journal + context) | Agents have no shared memory; files are the only persistent medium |
| Parallel coordination | Dual-ledger journal | Enables named sections per Project Lead, read-all / write-own pattern |
| Stall detection | Wave progress comparison | Project Leads cannot signal issues mid-wave; post-wave review is the only checkpoint |
| Max parallel Project Leads | 2-4 per wave | Balances throughput vs. scope-conflict risk |
| Context recovery | 6-step protocol from journal | Project Leads start with clean context each wave; journal is the recovery source |

## Data Flow

### Single-Task Flow

```text
User Request → task-creator → task file + context file
→ Project Lead reads task/context
→ research subagents (analyze-project, QA)
→ implementation-planning → plan file
→ default subagent → code changes
→ code-reviewer → review findings
→ QA + architect → READY/NOT READY
→ completion-reporter → CHANGELOG + closure
```

### Multi-Project Flow

```text
User Request → Program Director reads docs + todo
→ delegated project/code analysis
→ Scope decomposition → File Registry
→ Wave N: launch Project-Lead-Alpha, Project-Lead-Beta, Project-Lead-Gamma (parallel batch)
→ Each Project Lead runs single-task flow within scope
→ post-wave verification audits → stall detection / continue decision
→ If remaining: next wave with updated scopes
→ If complete: implementation-completion-reporter closure report
```
