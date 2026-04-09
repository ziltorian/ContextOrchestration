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
│PL-Alpha││PL-Beta ││PL-Gamma│   (parallel Project Leads)
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

**Purpose:** Decomposes large projects into independent scopes and coordinates multiple Project Leads in iterative waves.
**File:** `.github/agents/Program-Director.agent.md`
**Workflow:** `.github/instructions/program-director-workflow.instructions.md`
**State:** `PROJECT_LEAD_JOURNAL.md` (Task Ledger, File Registry, Context Recovery, Progress Ledger)

Key patterns:

- Scope-based file partitioning (no overlapping files between PLs)
- Wave-based iteration (2-4 PLs per wave, max 5 waves)
- Stall detection (2 consecutive zero-progress waves → termination)
- Structured handoff with identity, scope, and context recovery instructions

### Layer 1: Project Lead

**Purpose:** Orchestrates the full development pipeline for a single task or assigned scope.
**File:** `.github/agents/Project-Lead.agent.md`
**Workflow:** `.github/instructions/project-lead-workflow.instructions.md`
**State:** `PROJECT_LEAD_JOURNAL.md`, `SubAgents-context/subagent-context-{task-name}.instructions.md`

Modes:

- **Single-PL mode:** Standard operation, full journal control
- **Parallel mode:** Activated by Program Director; name-scoped journal, restricted file access

### Layer 2: Specialized Subagents

20 agents covering: intake, research, planning, implementation, review, security, QA, architecture audit, UI/UX design, test coverage, documentation, and cleanup.

## Components

### Agent Definitions (`.github/agents/`)

**Responsibility:** Define agent roles, tools, workflows, and constraints.
**Format:** `.agent.md` with YAML frontmatter + XML body sections.
**Count:** 20 agents (1 super-orchestrator, 1 orchestrator, 18 specialists).
**Nested orchestration:** allowed only for `task-creator`, `implementation-planning`, `integration-architect-auditor`, and `document-merger`, each with an explicit `agents` allowlist.

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

**Responsibility:** Persistent state between subagent invocations — stage logs, findings, audit results.
**Format:** Append-only blocks with explicit role attribution.

### Implementation Plans (`.github/implementations/`)

**Responsibility:** Detailed change plans with phases, task IDs, risk assessment, and verification steps.

## Coordination Mechanisms

| Mechanism | Purpose | Owner |
| --------- | ------- | ----- |
| `PROJECT_LEAD_JOURNAL.md` | Dual-ledger: Task Ledger + File Registry + Progress Ledger | Program Director (ledger), PLs (progress) |
| `SubAgents-context/*.instructions.md` | Stage-log between subagent invocations | Pipeline participants (append-only) |
| `SubAgents-tasks/task-*.instructions.md` | Immutable task definitions (Source/Goal) | task-creator |
| `project-todo.instructions.md` | Global task queue visible to all agents | User, task-creator (mode B) |
| `Required Documentation` section (in task + context files) | Curated list of documentation relevant to the task; populated at intake, extended by research agents | task-creator (initial), research agents + web-searcher (append) |
| File Registry (in journal) | Scope ownership: file → PL mapping | Program Director |

## Key Decisions

| Decision | Choice | Rationale |
| -------- | ------ | --------- |
| Scope enforcement | Prompt-level only | Industry standard; no platform supports file locking between agents |
| State management | File-based (journal + context) | Agents have no shared memory; files are the only persistent medium |
| Parallel coordination | Dual-ledger journal | Enables named sections per PL, read-all / write-own pattern |
| Stall detection | Wave progress comparison | PLs cannot signal issues mid-wave; post-wave review is the only checkpoint |
| Max parallel PLs | 2-4 per wave | Balances throughput vs. scope-conflict risk |
| Context recovery | 6-step protocol from journal | PLs start with clean context each wave; journal is the recovery source |

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
→ Scope decomposition → File Registry
→ Wave N: launch PL-Alpha, PL-Beta, PL-Gamma (parallel)
→ Each PL runs single-task flow within scope
→ Post-wave review → stall detection
→ If remaining: next wave with updated scopes
→ If complete: closure report
```
