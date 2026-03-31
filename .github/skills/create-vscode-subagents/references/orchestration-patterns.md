# Orchestration Patterns Reference

Patterns for multi-agent coordination in VS Code Copilot.
Sources: [VS Code Subagents Docs](https://code.visualstudio.com/docs/copilot/agents/subagents), [copilot-orchestra](https://github.com/ShepAlderson/copilot-orchestra)

---

## How Subagents Work

- **Synchronous**: main agent waits for subagent result before continuing.
- **Parallel**: multiple subagents can run concurrently when spawned together.
- **Isolated context**: each subagent gets a clean context window; only its final result returns to the parent.
- **Agent-initiated**: the orchestrator decides when to spawn subagents based on task complexity.

The `agent` tool must be in the coordinator's `tools` list to enable subagent delegation.

---

## Pattern 1 — Coordinator / Worker

One coordinator delegates distinct tasks to specialized workers. Each worker has tailored tools and a focused role.

**When to use:** Feature development, multi-step workflows, when different tasks need different permissions (read-only research vs. file editing).

### Coordinator

```yaml
---
name: FeatureBuilder
description: Orchestrate feature development — research, implement, review.
tools: ['agent', 'read', 'search']
agents: ['Researcher', 'Implementer', 'Reviewer']
model: Claude Sonnet 4.5 (copilot)
---
You are a feature development coordinator. For each request:

1. Use the Researcher agent to analyze the codebase and gather context.
2. Use the Implementer agent to write the code for each task.
3. Use the Reviewer agent to validate the implementation.
4. If Reviewer returns issues, send feedback to Implementer and repeat.
```

### Research Worker (read-only)

```yaml
---
name: Researcher
description: Analyze codebase structure and return findings. Subagent only.
tools: ['codebase', 'fetch', 'usages', 'read', 'search']
user-invocable: false
model: Claude Sonnet 4.5 (copilot)
---
Analyze the codebase thoroughly using read-only tools.
Return a structured summary: relevant files, existing patterns,
dependencies, and recommendations.
Work autonomously without pausing for input.
```

### Implementer Worker (write access)

```yaml
---
name: Implementer
description: Write code following TDD. Subagent only.
tools: ['editFiles', 'runCommands', 'runTests', 'terminalLastCommand', 'read']
user-invocable: false
model: Claude Haiku 4.5 (copilot)
---
Implement code changes following existing patterns.
Follow TDD: write failing tests first, then minimal code to pass them.
Make focused, minimal edits. Return a phase summary on completion.
```

### Reviewer Worker (read-only + diagnostics)

```yaml
---
name: Reviewer
description: Review code changes for quality and correctness. Subagent only.
tools: ['read', 'search', 'codebase', 'problems', 'usages']
user-invocable: false
model: Claude Sonnet 4.5 (copilot)
---
Review uncommitted code changes.
Return structured result: Status (APPROVED / NEEDS_REVISION / FAILED),
Summary, Issues found, Recommendations.
Keep feedback concise and actionable.
```

---

## Pattern 2 — Parallel Analysis

Multiple subagents run simultaneously for independent analysis tasks. Results are synthesized by the coordinator.

**When to use:** Code review from multiple angles, multi-perspective audits, comparing implementation options.

### Parallel Reviewer

```yaml
---
name: ThoroughReviewer
description: Review code from multiple perspectives simultaneously.
tools: ['agent', 'read', 'search']
model: Claude Sonnet 4.5 (copilot)
---
Run these subagents in parallel for every review:
- Correctness reviewer: logic errors, edge cases, type issues.
- Security reviewer: input validation, injection risks, data exposure.
- Performance reviewer: bottlenecks, inefficient patterns.
- Code quality reviewer: readability, naming, duplication.

After all complete, synthesize findings into a prioritized summary.
Mark critical issues vs. nice-to-haves. Acknowledge what the code does well.
```

**Prompt pattern for parallel execution:**

```text
Analyze this codebase simultaneously using subagents:
1. Security: check for vulnerabilities and injection risks
2. Performance: identify bottlenecks
3. Accessibility: verify a11y compliance
Compile findings into a prioritized action plan.
```

---

## Pattern 3 — TDD Development Cycle (copilot-orchestra)

Strict Plan → Implement → Review → Commit cycle with mandatory pause points. Based on [copilot-orchestra](https://github.com/ShepAlderson/copilot-orchestra).

**When to use:** Feature development requiring audit trail, enforcing TDD, team workflows.

### Conductor (orchestrator)

```yaml
---
name: Conductor
description: Orchestrate full dev cycle: Plan → Implement → Review → Commit.
tools: ['agent', 'read', 'search', 'editFiles']
agents: ['PlanningAgent', 'ImplementAgent', 'ReviewAgent']
model: Claude Sonnet 4.5 (copilot)
---
You orchestrate the full development lifecycle.
Strictly follow: Planning → Implementation → Review → Commit per phase.

WORKFLOW:
1. Delegate research to PlanningAgent to gather codebase context.
2. Draft a multi-phase plan (3–10 phases). Each phase has: objective,
   files to modify, and tests to write.
3. MANDATORY STOP: present plan to user for approval.
4. Write plan to plans/<task-name>-plan.md.

For each phase:
5. Delegate to ImplementAgent with phase objective + context.
6. Delegate to ReviewAgent to validate implementation.
   - APPROVED → generate commit message, STOP for user to commit.
   - NEEDS_REVISION → send feedback to ImplementAgent, repeat.
   - FAILED → STOP and ask user for guidance.
7. Write phase summary to plans/<task-name>-phase-<N>-complete.md.

CRITICAL: You do NOT write code. You ONLY orchestrate subagents.
```

### Planning Subagent

```yaml
---
name: PlanningAgent
description: Research codebase and return context for plan creation. Subagent only.
tools: ['codebase', 'read', 'search', 'usages', 'fetch']
user-invocable: false
model: Claude Sonnet 4.5 (copilot)
---
Research the codebase comprehensively.
Return structured findings:
- Relevant files and their purposes
- Existing patterns to follow
- Functions/classes to modify
- Testing setup and conventions
Work autonomously without pausing.
```

### Implementation Subagent (TDD)

```yaml
---
name: ImplementAgent
description: Implement one plan phase using TDD. Subagent only.
tools: ['editFiles', 'runCommands', 'runTests', 'terminalLastCommand', 'read', 'search']
user-invocable: false
model: Claude Haiku 4.5 (copilot)
---
Implement the assigned phase following strict TDD:
1. Write failing tests first.
2. Run tests — confirm they fail.
3. Write minimal code to pass the tests.
4. Run tests — confirm they pass.
5. Apply linting and formatting.
Return a phase summary: files changed, functions added, tests written.
```

### Code Review Subagent

```yaml
---
name: ReviewAgent
description: Validate implementation quality and return structured verdict. Subagent only.
tools: ['read', 'search', 'codebase', 'problems', 'usages', 'runCommands']
user-invocable: false
model: Claude Sonnet 4.5 (copilot)
---
Review uncommitted code changes.
Check: test coverage, code quality, best practices, phase objective adherence.
Return exactly:
- Status: APPROVED / NEEDS_REVISION / FAILED
- Summary: what was done
- Issues: list of problems found (empty if APPROVED)
- Recommendations: improvement suggestions
```

---

## Pattern 4 — Sequential Handoff Workflow

User-driven sequential workflow using the `handoffs` frontmatter. Each step requires user confirmation before proceeding.

**When to use:** Planning → implementation pipeline where users review each phase.

### Plan Agent with Handoff

```yaml
---
name: Planner
description: Generate implementation plan. Transitions to implementation on approval.
tools: ['read', 'search', 'fetch', 'codebase']
handoffs:
  - label: Implement This Plan
    agent: agent
    prompt: Implement the plan outlined above, following existing code patterns.
    send: false
---
Generate a detailed implementation plan.
Do NOT write any code.
```

---

## Orchestration Best Practices

**Coordinator design:**

- Coordinator should route, not implement. Keep it thin.
- Use `agents` property to restrict available subagents and prevent unintended delegation.
- Pass only the relevant subtask to each subagent — avoid sending the full conversation history.

**Worker design:**

- Workers should be autonomous: complete their task and return a structured summary.
- Instruct workers explicitly: "Work autonomously without pausing for input."
- Smaller scope = fewer errors and less context waste.

**Model assignment strategy:**

- Coordinator / Planner / Reviewer → capable model (Claude Sonnet 4.5)
- Implementer / repetitive worker → fast/cheap model (Claude Haiku 4.5)
- Complex reasoning tasks → use model array for fallback

**Parallelism hints:**
Use these phrases to trigger parallel subagent execution:

- "Run subagents in parallel to..."
- "Simultaneously analyze..."
- "Run these checks concurrently..."

**Context efficiency:**

- Only the subagent's final result returns to the coordinator's context.
- Exploratory dead-ends in subagents don't pollute the main context window.
- Parallel execution reduces wall-clock time without multiplying coordinator context.

---

## Restricting Subagent Access

Use `agents` and `disable-model-invocation` together for fine-grained control:

```yaml
# agents/security-reviewer.agent.md
---
name: SecurityReviewer
user-invocable: true                    # visible in dropdown
disable-model-invocation: true          # blocked from general subagent use
---
```

```yaml
# agents/audit-conductor.agent.md
---
name: AuditConductor
tools: ['agent', 'read']
agents: ['SecurityReviewer', 'Reviewer'] # explicit override — SecurityReviewer is now accessible
---
```

Explicitly listing an agent in `agents` overrides `disable-model-invocation: true`.

---

## Nested Subagent Patterns

Workers can themselves spawn sub-workers, enabling multi-level orchestration hierarchies.
**Requires:** `agent` in the worker's `tools` list + appropriate `agents` property at each level.

### Pattern: Two-Level Specialization

A coordinator delegates to domain workers, each of which orchestrates leaf specialists.

```
Coordinator
  ├── Frontend Lead    (worker + nested orchestrator)
  │     ├── UI Researcher  (leaf)
  │     └── A11y Checker   (leaf)
  └── Backend Lead     (worker + nested orchestrator)
        ├── API Researcher (leaf)
        └── DB Researcher  (leaf)
```

**coordinator.agent.md**
```yaml
---
name: FullStackBuilder
description: Orchestrate frontend and backend implementation in parallel.
tools: ['agent']
agents: ['FrontendLead', 'BackendLead']
model: Claude Sonnet 4.5 (copilot)
---
For each feature:
1. Run FrontendLead and BackendLead in parallel.
2. Synthesize their results into a unified implementation plan.
3. Identify cross-cutting concerns from both reports.
```

**frontend-lead.agent.md** — mid-level worker (also orchestrates)
```yaml
---
name: FrontendLead
description: Research and plan frontend implementation.
tools: ['agent', 'read', 'search', 'codebase']
agents: ['UIResearcher', 'A11yChecker']
user-invocable: false
model: Claude Sonnet 4.5 (copilot)
---
1. Run UIResearcher to find existing component patterns.
2. Run A11yChecker to verify accessibility requirements.
3. Return: component plan, accessibility constraints, reuse opportunities.
```

**ui-researcher.agent.md** — leaf worker
```yaml
---
name: UIResearcher
description: Research existing UI component patterns in the codebase.
tools: ['codebase', 'search', 'read']
user-invocable: false
model: Claude Haiku 4.5 (copilot)
---
Catalog existing components: props, variants, styling patterns.
Return a structured component inventory with reuse recommendations.
```

---

### Pattern: Recursive Task Decomposition

An agent breaks a task into subtasks and spawns copies of itself to handle each one.

**Requires VS Code setting:** `chat.subagents.allowInvocationsFromSubagents: true`

```yaml
---
name: RecursivePlanner
description: Recursively decompose complex tasks into atomic units.
tools: ['agent', 'read', 'search']
agents: ['RecursivePlanner']    # self-referential
model: Claude Sonnet 4.5 (copilot)
---
## Decomposition Rules
1. Evaluate the task complexity (scope: more than 3 files or 2 modules = complex).
2. If complex: break into 2-4 subtasks and spawn a RecursivePlanner for each.
3. If atomic: complete the task directly and return a structured result.
4. Merge all subtask results into a coherent report before returning.

## Termination Condition (IMPORTANT)
- A task is atomic when it touches exactly one file, one function, or one configuration entry.
- Never spawn a subagent for an atomic task. Implement directly.
```

---

### Nested Subagent Rules Summary

| Rule | Details |
|------|---------|
| `agent` in `tools` required at each level | A worker that omits `agent` cannot spawn sub-workers |
| `agents` allowlist applies at each level independently | Each agent enforces its own `agents` restrictions |
| `disable-model-invocation` blocked at all levels | Unless explicitly overridden by the direct caller's `agents` list |
| Self-referential agents | Require `chat.subagents.allowInvocationsFromSubagents: true` |
| Context isolation per level | Only the final result bubbles up — intermediate work stays private |
| Parallel execution within a level | Prompt the worker to run its sub-workers "in parallel" |

---

## File Location Reference

| Location | Scope | Format |
| -------- | ----- | ------ |
| `.github/agents/*.agent.md` | Workspace only | VS Code format |
| `<user-profile>/prompts/*.agent.md` | All workspaces | VS Code format |
| `.claude/agents/*.md` | Workspace only | Claude format |
| Custom path via `chat.agentFilesLocations` | Configurable | VS Code format |

**Note:** VS Code also detects `.md` files in `.github/agents/` (without explicit `.agent.md` extension). The `.agent.md` extension is recommended for clarity.