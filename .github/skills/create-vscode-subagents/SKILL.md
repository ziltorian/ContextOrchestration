---
name: create-vscode-subagents
description: Create VS Code Copilot custom agents and subagent orchestration systems. Use when building .agent.md files, designing multi-agent workflows, creating coordinator/worker patterns, setting up subagent delegation, nested subagents (subagents calling subagents), or configuring handoffs between agents in VS Code GitHub Copilot.
compatibility: VS Code with GitHub Copilot extension. Subagents require VS Code 1.106+. Nested subagents require enabling chat.subagents.allowInvocationsFromSubagents.
metadata:
  version: "1.0"
  category: ai-assistant-configuration
  author: ziltorian
---

# VS Code Custom Agents & Subagents

Create `.agent.md` files for GitHub Copilot in VS Code — from simple specialized agents to full multi-level agent orchestration systems.

## When to Use This Skill

- Creating a custom agent with specific tools and instructions
- Building a coordinator agent that delegates to worker subagents
- Designing multi-level pipelines where workers spawn their own sub-workers
- Setting up parallel analysis workflows (code review, audits)
- Configuring TDD development cycle orchestration
- Setting up sequential handoffs between agents

---

## Core Concepts

**Custom Agent** — a `.agent.md` file with YAML frontmatter + Markdown instructions. Defines the agent's persona, tools, and behavior.

**Subagent** — any agent invoked by another agent via the `agent` tool. Gets an isolated context window; returns only its final result to the caller.

**Coordinator** — an agent that uses the `agent` tool to delegate tasks. It routes, it does not implement.

**Worker** — an agent that does specialized work (research, coding, review) and returns a structured result. Workers can also spawn their own subagents.

**Nested Subagent** — a worker agent that itself invokes sub-workers. Enables multi-level orchestration hierarchies (Coordinator → Worker → Sub-worker).

---

## File Structure

### Minimal Agent
```
.github/agents/
└── my-agent.agent.md
```

### Orchestration System (Flat)
```
.github/agents/
├── coordinator.agent.md        # user-facing, manages workers
├── researcher.agent.md         # user-invocable: false
├── implementer.agent.md        # user-invocable: false
└── reviewer.agent.md           # user-invocable: false
```

### Multi-Level Orchestration
```
.github/agents/
├── coordinator.agent.md        # top-level, delegates to workers
├── lead-researcher.agent.md    # worker that spawns sub-researchers
├── sub-researcher-a.agent.md   # leaf worker (read-only)
├── sub-researcher-b.agent.md   # leaf worker (read-only)
└── implementer.agent.md        # leaf worker (write access)
```

### Cross-tool Compatibility
```
.claude/agents/                 # Claude Code format (plain .md)
├── researcher.md
└── implementer.md
```

---

## Step-by-Step: Create an Agent

### 1. Choose the agent's role

Define one clear responsibility. Examples: "plan features", "review security", "research codebase".

### 2. Write the YAML frontmatter

```yaml
---
name: MyAgent
description: Short description shown in the chat input field.
tools: ['read', 'search', 'codebase']
model: Claude Sonnet 4.5 (copilot)
---
```

See [Agent YAML Reference](references/agent-yaml-reference.md) for all fields.

### 3. Write the Markdown body

```markdown
You are a [ROLE] agent. Your task is to [GOAL].

## Workflow
1. [Step 1]
2. [Step 2]
3. Return a structured summary of findings.

## Constraints
- Do NOT [prohibited action]
- Always [required behavior]
```

### 4. Place the file

- **Workspace (team):** `.github/agents/agent-name.agent.md`
- **User profile (personal):** via `Chat: New Custom Agent` → "User profile"
- **Claude format:** `.claude/agents/agent-name.md`

---

## Step-by-Step: Create a Subagent System

### 1. Design the agent graph

```
User → Coordinator
         ├── Researcher (read-only)
         ├── Implementer (write access)
         └── Reviewer (read-only + diagnostics)
```

### 2. Create the coordinator

```yaml
---
name: Coordinator
description: Orchestrate feature development end-to-end.
tools: ['agent', 'read', 'search', 'editFiles']
agents: ['Researcher', 'Implementer', 'Reviewer']
model: Claude Sonnet 4.5 (copilot)
---
You coordinate feature development. Do NOT write code yourself.

1. Use Researcher to gather codebase context.
2. Use Implementer to write the code.
3. Use Reviewer to validate the result.
4. If Reviewer flags issues, send feedback to Implementer and repeat.
```

**Key rules:**
- `agent` must be in `tools` for delegation to work
- `agents` list restricts which subagents this coordinator can use
- Coordinator role = route, not implement

### 3. Create worker subagents

```yaml
---
name: Researcher
description: Analyze codebase and return structured findings.
tools: ['codebase', 'fetch', 'usages', 'read', 'search']
user-invocable: false
model: Claude Sonnet 4.5 (copilot)
---
Research thoroughly using read-only tools.
Work autonomously — do NOT pause for user input.
Return: relevant files, existing patterns, recommendations.
```

```yaml
---
name: Implementer
description: Implement code changes following TDD.
tools: ['editFiles', 'runCommands', 'runTests', 'read']
user-invocable: false
model: Claude Haiku 4.5 (copilot)
---
Follow TDD: write failing tests → confirm failure → write minimal
code → confirm passing tests. Return a summary of changes made.
```

### 4. Configure visibility

| Goal | Configuration |
|------|--------------|
| Subagent-only, any coordinator | `user-invocable: false` |
| Visible, protected from subagent use | `disable-model-invocation: true` |
| Protected but accessible to specific coordinator | `disable-model-invocation: true` + list in coordinator's `agents` |
| Standard user-facing agent | defaults (no flags needed) |

---

## Nested Subagents (Multi-Level Orchestration)

Worker agents can now call their own subagents, enabling deep orchestration hierarchies. This is the key new capability introduced in VS Code 1.109+.

### How It Works

Any agent with `agent` in its `tools` list can invoke subagents — including agents that are themselves running as subagents. The nesting depth is theoretically unlimited.

```
User → Coordinator
         └── Lead Researcher          # worker with agent tool
               ├── API Researcher     # sub-worker (leaf)
               └── DB Researcher      # sub-worker (leaf)
```

### Create a Nested Worker

```yaml
---
name: Lead Researcher
description: Orchestrate domain-specific research using specialized sub-researchers.
tools: ['agent', 'read', 'search']
agents: ['API Researcher', 'DB Researcher']
user-invocable: false
model: Claude Sonnet 4.5 (copilot)
---
You coordinate research across technical domains.
1. Run API Researcher and DB Researcher in parallel.
2. Synthesize their findings into a single structured report.
```

```yaml
---
name: API Researcher
description: Research REST API patterns and integrations.
tools: ['codebase', 'fetch', 'search', 'read']
user-invocable: false
model: Claude Haiku 4.5 (copilot)
---
Research API patterns. Return: endpoints, auth methods, error handling.
```

```yaml
---
name: DB Researcher
description: Research database schemas and query patterns.
tools: ['codebase', 'search', 'read']
user-invocable: false
model: Claude Haiku 4.5 (copilot)
---
Research data models and query patterns. Return: schemas, indexes, relations.
```

### Self-Referential Agents

An agent can list itself in `agents` to call itself recursively. This requires enabling the VS Code setting:

```json
"chat.subagents.allowInvocationsFromSubagents": true
```

Use with caution — guard against infinite recursion with explicit termination conditions in the agent instructions.

```yaml
---
name: RecursivePlanner
description: Break down complex tasks recursively until atomic.
tools: ['agent', 'read', 'search']
agents: ['RecursivePlanner']    # self-referential — requires the VS Code setting
---
If the task is too complex, break it into subtasks and spawn instances
of yourself for each. Stop recursing when the task is atomic.
```

### Nested Subagent Visibility Rules

The same `agents` / `disable-model-invocation` rules apply at every level of the hierarchy:

- A nested worker can only call agents listed in its own `agents` property.
- `disable-model-invocation: true` blocks invocation at ALL levels unless the calling agent explicitly allows it.
- `user-invocable: false` only affects the top-level picker — it does not prevent subagent invocation.

→ Full nested patterns in [Orchestration Patterns](references/orchestration-patterns.md#nested-subagent-patterns)

---

## Common Patterns Quick Reference

### Coordinator / Worker
Best for feature development with distinct phases.
```yaml
# coordinator: tools includes 'agent', agents lists workers
# workers: user-invocable: false, each with appropriate tools
```
→ Full examples in [Orchestration Patterns](references/orchestration-patterns.md#pattern-1--coordinator--worker)

### Parallel Analysis
Best for multi-perspective code review or audits.
```yaml
# single coordinator spawns multiple reviewers simultaneously
# prompt uses "in parallel" to trigger concurrent execution
```
→ Full examples in [Orchestration Patterns](references/orchestration-patterns.md#pattern-2--parallel-analysis)

### TDD Cycle (copilot-orchestra style)
Best for structured development with audit trail and mandatory pauses.
```yaml
# Conductor → PlanningAgent → ImplementAgent → ReviewAgent → user commit
```
→ Full examples in [Orchestration Patterns](references/orchestration-patterns.md#pattern-3--tdd-development-cycle-copilot-orchestra)

### Sequential Handoff
Best for user-controlled plan → implement pipelines.
```yaml
handoffs:
  - label: Start Implementation
    agent: agent
    prompt: Implement the plan above.
    send: false
```
→ Full examples in [Orchestration Patterns](references/orchestration-patterns.md#pattern-4--sequential-handoff-workflow)

### Multi-Level Nested Orchestration
Best for complex, domain-spanning tasks with deep specialization.
```yaml
# Top coordinator → Domain workers (with agent tool) → Leaf workers
# Each level manages its own agents list
```
→ Full examples in [Orchestration Patterns](references/orchestration-patterns.md#nested-subagent-patterns)

---

## Model Assignment Strategy

| Role | Recommended Model | Rationale |
|------|------------------|-----------|
| Coordinator / Planner | `Claude Sonnet 4.5 (copilot)` | Needs reasoning for routing decisions |
| Nested worker / mid-level | `Claude Sonnet 4.5 (copilot)` | Still needs some routing ability |
| Reviewer / Architect | `Claude Sonnet 4.5 (copilot)` | Needs thorough analysis |
| Implementer / Leaf worker | `Claude Haiku 4.5 (copilot)` | Repetitive, focused work — cost efficient |
| Complex reasoning | `['Claude Opus 4.5 (copilot)', 'Claude Sonnet 4.5 (copilot)']` | Fallback array |

---

## Edge Cases

**Nested subagent not being invoked:**
- Check `agent` is in the worker's `tools` list (not just the coordinator's).
- Check the sub-worker is not blocked by `disable-model-invocation: true` without being in the worker's `agents` list.

**Subagent not being invoked (general):**
- Check `agent` is in the coordinator's `tools` list.
- Check the worker is not in `disable-model-invocation: true` without being listed in `agents`.

**Agent not appearing in dropdown:**
- Verify file extension is `.agent.md` (or `.md` in `.github/agents/`).
- Check `user-invocable` is not set to `false`.
- Run `Chat: New Custom Agent` and check diagnostics (right-click Chat → Diagnostics).

**Wrong subagent selected:**
- Use `agents` property in coordinator to restrict to explicit list.
- Ensure agent names are unique and descriptive.

**Context overflow in deep chains:**
- Each nesting level creates its own context window — the parent only receives the final result.
- Instruct workers to return concise summaries, not full conversation history.
- Avoid passing large datasets between levels; use file references instead.

**Infinite recursion (self-referential agents):**
- Always include a termination condition in the agent body.
- Test with simple inputs before enabling in production.

---

## Quick-Start Templates

### Simple Specialized Agent
```markdown
---
name: SecurityReviewer
description: Review code for security vulnerabilities. Use for security audits.
tools: ['read', 'codebase', 'search', 'problems']
model: Claude Sonnet 4.5 (copilot)
---
You are a security-focused code reviewer.

Focus on: input validation, injection risks, auth flaws, data exposure,
secrets in code, dependency vulnerabilities.

Structure your review as:
- Critical issues (must fix)
- Warnings (should fix)  
- Suggestions (nice to have)
```

### Minimal Subagent-Only Worker
```markdown
---
name: DocWriter
description: Write documentation for code. Called by coordinator agents.
tools: ['read', 'editFiles', 'codebase']
user-invocable: false
model: Claude Haiku 4.5 (copilot)
---
Write clear documentation for the provided code.
Return a summary of files modified.
```

### Nested Worker (calls its own subagents)
```markdown
---
name: DomainResearcher
description: Orchestrate deep research across API and data layers.
tools: ['agent', 'read', 'search']
agents: ['APIResearcher', 'DataResearcher']
user-invocable: false
model: Claude Sonnet 4.5 (copilot)
---
You coordinate domain research. Run APIResearcher and DataResearcher
in parallel. Synthesize their findings into one structured report.
Return: combined findings, identified gaps, recommended approach.
```

---

## Default Subagent for Implementation

For actual code writing, call the **default subagent** (no `agentName` in `runSubagent`).
It outperforms specialized implementer agents for general coding because it uses the
coordinator's full model capabilities without persona constraints.

```yaml
# In coordinator instructions:
# "Spawn the default subagent (no agentName) to implement the plan."
#
# The default subagent can use all tools granted by the coordinator.
# Reserve custom implementer agents only for domain-specific code
# (Bicep, Terraform, Kotlin MCP, etc.).
```

---

## Full Project Management Pipeline

A complete multi-phase pipeline for turning rough user to-do items into
verified, documented delivery. See [Project Pipeline Reference](references/project-pipeline.md)
for full details, YAML examples, and the awesome-copilot agent catalog.

### Overview

```
project-todo.instructions.md  (user-owned, read-only for all agents)
       │
       ▼  Phase 1 — Task Expansion
SubAgents-tasks/task-{name}.instructions.md        ← created once by ProjectLead, immutable
SubAgents-context/subagent-context-{task-name}.instructions.md   ← append-only shared memory
       │
       ▼  Phase 2 — Planning + Architecture
.github/implementations/{name}-implementation.instructions.md
       │
       ▼  Phase 3 — Implementation (default subagent, no agentName)
Production code
       │
       ▼  Phase 4 — Verification (QA + Architect in parallel)
Results appended to context file
       │
       ▼  Phase 5 — Completion
CHANGELOG.md, commit message, docs, completion report
```

---

## References

- [Agent YAML Reference](references/agent-yaml-reference.md) — all frontmatter fields, nested subagent settings, constraints
- [Orchestration Patterns](references/orchestration-patterns.md) — coordinator/worker, parallel, TDD cycle, nested patterns
- [Project Pipeline Reference](references/project-pipeline.md) — full pipeline, awesome-copilot agent catalog
- [VS Code Custom Agents Docs](https://code.visualstudio.com/docs/copilot/customization/custom-agents)
- [VS Code Subagents Docs](https://code.visualstudio.com/docs/copilot/agents/subagents)
- [Awesome Copilot](https://github.com/github/awesome-copilot) — community agent catalog