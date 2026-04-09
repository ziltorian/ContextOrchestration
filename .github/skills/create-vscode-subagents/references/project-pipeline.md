# Project Management Pipeline & Agent Catalog

Structured multi-agent pipeline for professional project execution, plus a curated
catalog of non-implementing agents from [awesome-copilot](https://github.com/github/awesome-copilot).

---

## Recommended Agents by Role

### 🎯 Coordination / Orchestration

| Agent file | Description | Use in pipeline |
|-----------|-------------|-----------------|
| `blueprint-mode.agent.md` | Executes structured workflows (Debug, Express, Main, Loop) with strict correctness; never assumes facts; self-corrects | Main coordinator for complex multi-phase workflows |
| `blueprint-mode-codex.agent.md` | Same philosophy, optimized for Codex-class models | Alternative coordinator with minimal tool policy |
| `custom-agent-foundry.agent.md` | Expert at designing and creating VS Code custom agents with optimal configurations | Meta-agent: build your pipeline's agents |

### 🏗️ Architecture & Design

| Agent file | Description | Use in pipeline |
|-----------|-------------|-----------------|
| `adr-generator.agent.md` | Creates comprehensive Architectural Decision Records (ADRs) with structured formatting optimized for AI and human consumption | Phase 2: enriching implementation plan with ADR references |
| `api-architect.agent.md` | API architect guidance — mentors engineer with patterns, best practices, working code | Phase 2: architecture review for API-heavy tasks |
| `critical-thinking.agent.md` | Challenges assumptions, encourages critical analysis to ensure the best possible solution | Phase 2: sanity-check on plan or architecture |

### 📋 Planning & Analysis

| Agent file | Description | Use in pipeline |
|-----------|-------------|-----------------|
| `prd.agent.md` | Generates PRD in Markdown: user stories, acceptance criteria, technical considerations, metrics | Pre-pipeline: turning a vague idea into a proper task description |
| `implementation-plan.agent.md` | Generates structured implementation plan for new features or refactoring | Phase 2: creating `.github/implementations/*.instructions.md` |
| `tech-debt-remediation-plan.agent.md` | Generates tech debt remediation plans for code, tests, and documentation | Pre-pipeline or Phase 2: understanding what needs cleanup first |
| Spike research agent | Systematically researches and validates technical spike documents through exhaustive investigation and controlled experimentation | Phase 1: research unknown territory before planning |
| Principal-level engineer agent | Provides principal-level software engineering guidance: engineering excellence, technical leadership, pragmatic implementation | Phase 2: high-level design guidance |

### 🔍 QA & Verification

| Agent file | Description | Use in pipeline |
|-----------|-------------|-----------------|
| `qa-subagent.agent.md` *(or similar)* | **Meticulous QA subagent** for test planning, bug hunting, edge-case analysis, and implementation verification | Phase 4: post-implementation verification |
| `debug.agent.md` | Debug your application to find and fix a bug | Phase 4: if QA fails and root cause is unclear |
| `accessibility.agent.md` | Expert assistant for web accessibility (WCAG 2.1/2.2), inclusive UX, and a11y testing | Phase 4: a11y verification for UI changes |
| Application Security agent | Automated security remediation: verifies package compliance, suggests vulnerability fixes using JFrog security intelligence | Phase 4: security audit after implementation |

> **Note on implementation agents:** For actual code changes, the **default subagent** (calling
> `runSubagent` without an `agentName`) outperforms specialized implementer agents in most cases.
> It receives the coordinator's full model capabilities without specialization overhead.
> Reserve custom implementer agents only for domain-specific code (e.g., Bicep, Terraform, Kotlin MCP).

---

## Full Project Management Pipeline

A coordinator agent manages the complete lifecycle from rough to-do to verified, documented delivery.

```
project-todo.instructions.md (user-owned)
    │
    ▼ Phase 1 — Task Expansion (task-creator intake)
SubAgents-tasks/task-{name}.instructions.md         ← written once, read by all
SubAgents-context/subagent-context-{task-name}.instructions.md  ← current-state coordination file with one owned block per participant
    │
    ▼ Phase 2 — Planning + Architecture (Planner + Architect subagents)
.github/implementations/{name}-implementation.instructions.md
    │
    ▼ Phase 3 — Implementation (default subagent)
Production code files
    │
    ▼ Phase 4 — Verification (QA + Architect subagents)
SubAgents-context/subagent-context-{task-name}.instructions.md  ← QA and architect blocks updated in place
    │
    ▼ Phase 5 — Completion (Completion subagent)
Docs, CHANGELOG.md, commit message
```

---

## Phase Details

### Phase 1 — Task Expansion

**Who:** `task-creator` subagent in mode A, or `ProjectLead` only when the user directly assigns a task outside `project-todo.instructions.md`  
**Reads:** `project-todo.instructions.md`, project documentation, existing codebase  
**Creates:**

- `SubAgents-tasks/task-{task-name}.instructions.md` — expanded, professionally formulated task
- `SubAgents-context/subagent-context-{task-name}.instructions.md` — current-state coordination file initialized with one owned block per participant

**Purpose:** Transform a short, poorly worded todo item into a precise technical task with
full project context. The intake owner reads the documentation and codebase before writing
the task file — only `task-creator` in standard intake, or `ProjectLead` on direct user assignment, may create this file.

**Task file is immutable** — once created, it cannot be modified by any agent.

---

### Phase 2 — Planning & Architecture

**Who:** `PlannerAgent` subagent → `ArchitectAgent` subagent  
**Reads:** `task-{name}.instructions.md`, `subagent-context-{task-name}.instructions.md`, codebase, docs  
**Creates:** `.github/implementations/{name}-implementation.instructions.md`

**Workflow:**
1. `PlannerAgent` creates the implementation instructions file with step-by-step tasks,
   acceptance criteria, and file-level breakdown.
2. `ArchitectAgent` reads the plan and enriches it: adds architectural constraints,
   references to ADRs, design patterns to follow, and files **not** to modify.
3. Both agents update their existing owned blocks in `subagent-context-{task-name}.instructions.md`.

---

### Phase 3 — Implementation

**Who:** Default subagent (called via `runSubagent` with no `agentName`)  
**Reads:** `task-{name}.instructions.md`, `subagent-context-{task-name}.instructions.md`,
`{name}-implementation.instructions.md`  
**Writes:** Production code only  

**Rules:**
- Follows the implementation instructions strictly.
- Does NOT modify documentation, reports, or context files outside its own owned block.
- Uses TDD where applicable: write failing tests → implement → pass.

---

### Phase 4 — Verification

**Who:** `QASubagent` + `ArchitectAgent` subagents (parallel)  
**Reads:** `task-{name}.instructions.md`, `subagent-context-{task-name}.instructions.md`,
`{name}-implementation.instructions.md`, changed files  
**Writes:** Updates each participant's owned block in `subagent-context-{task-name}.instructions.md`

**QA checks:** test coverage, edge cases, regression, acceptance criteria from task file.  
**Architect checks:** architectural consistency, pattern adherence, no unintended side effects.

**Verdict:** Each returns `APPROVED / NEEDS_REVISION / FAILED` + structured notes.  
On `NEEDS_REVISION`: coordinator sends targeted feedback to default subagent and reruns Phase 3.  
On `FAILED`: coordinator halts and presents findings to user.

---

### Phase 5 — Completion

**Who:** `CompletionAgent` subagent  
**Reads:** `task-{name}.instructions.md`, `subagent-context-{task-name}.instructions.md`, implementation instructions  
**Creates/Updates:**
- Completion report in `SubAgents-tasks/task-{name}-complete.md`
- `CHANGELOG.md` entry
- Git commit message (written to context file or returned to coordinator)
- Updated documentation files

---

## File Permissions Reference

| File | Creator | Can edit | Read by |
|------|---------|----------|---------|
| `project-todo.instructions.md` | User | User only | All agents (read-only) |
| `SubAgents-tasks/task-{name}.instructions.md` | `task-creator` mode A, or `ProjectLead` on direct assignment | **Nobody** after creation | All agents (mandatory) |
| `SubAgents-context/subagent-context-{task-name}.instructions.md` | `task-creator` mode A, or `ProjectLead` on direct assignment | All agents (own block only; shared/protected sections by contract) | All agents (mandatory) |
| `.github/implementations/{name}-implementation.instructions.md` | PlannerAgent | ArchitectAgent only (enrichment pass) | All agents (mandatory) |
| Production code | Default subagent | Default subagent only | All agents |
| Docs / reports | Default subagent + CompletionAgent | Default + CompletionAgent | All agents |

> **Key rule:** Every subagent must read `task-{name}.instructions.md` and `subagent-context-{task-name}.instructions.md`
> at the start of its execution. The task file is the single source of truth for what needs
> to be done; the context file is the shared memory of what has been learned and decided.

---

## Coordinator Configuration Example

```yaml
---
name: ProjectCoordinator
description: >
  Full project lifecycle coordinator. Reads project-todo.instructions.md and manages the
  complete pipeline: task expansion → planning → architecture → implementation
  → verification → completion. Use when running multi-phase project work.
tools: ['agent', 'read', 'search', 'editFiles']
agents:
    - task-creator
    - PlannerAgent
    - ArchitectAgent
    - QASubagent
    - CompletionAgent
model: Claude Sonnet 4.5 (copilot)
---
You manage the full project lifecycle. For each task in project-todo.instructions.md:

1. Spawn `task-creator` in mode A to research and expand the task, or use `ProjectLead` only when the user directly assigned the task outside `project-todo.instructions.md`.
2. Spawn PlannerAgent to create implementation instructions.
3. Spawn ArchitectAgent to enrich instructions with architectural context.
4. STOP: present task file and plan to user. Await approval.
5. Spawn default subagent (no agentName) to implement.
6. Spawn QASubagent and ArchitectAgent in parallel to verify.
7. If APPROVED by both: spawn CompletionAgent.
8. If NEEDS_REVISION: send feedback to default subagent, repeat from step 5.
9. If FAILED: halt and report to user.

MANDATORY: Every subagent must receive paths to task-{name}.instructions.md and
subagent-context-{task-name}.instructions.md in its prompt.
```

---

## Default Subagent Call Pattern

For implementation tasks, call the default subagent without specifying `agentName`.
This gives access to the coordinator's full model capabilities:

```
// In coordinator instructions:
Spawn the default subagent (no agentName) with this prompt:

"Read these files first:
- SubAgents-tasks/task-{name}.instructions.md
- SubAgents-context/subagent-context-{task-name}.instructions.md
- .github/implementations/{name}-implementation.instructions.md

Then implement all tasks described in the implementation instructions.
Follow the architectural constraints in the instructions file exactly.
After completing, update your existing owned block in:
SubAgents-context/subagent-context-{task-name}.instructions.md"
```

---

## Recommended awesome-copilot Agents to Install

Copy these from [github/awesome-copilot](https://github.com/github/awesome-copilot/tree/main/agents)
into your `.github/agents/` directory as your pipeline subagents:

| File | Role in pipeline |
|------|-----------------|
| `blueprint-mode.agent.md` | Coordinator |
| `adr-generator.agent.md` | Architect (Phase 2) |
| `critical-thinking.agent.md` | Plan review / sanity check |
| `implementation-plan.agent.md` | Planner (Phase 2) |
| `prd.agent.md` | Pre-pipeline task definition |
| `tech-debt-remediation-plan.agent.md` | Tech debt tasks |
| `debug.agent.md` | QA fallback (Phase 4) |
| `accessibility.agent.md` | A11y verification (Phase 4) |

Use them as-is or adapt their instructions for your project conventions.
