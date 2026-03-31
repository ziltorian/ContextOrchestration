# Agent YAML Reference

Complete reference for `.agent.md` frontmatter fields.
Source: [VS Code Custom Agents Docs](https://code.visualstudio.com/docs/copilot/customization/custom-agents)

---

## File Format

```
---
<YAML frontmatter>
---

<Markdown body — agent instructions>
```

Extension: `.agent.md`  
Locations: `.github/agents/` (workspace), user profile folder (global), configurable via `chat.agentFilesLocations` setting.

---

## All Frontmatter Fields

### Core Fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `name` | string | filename | Agent display name in dropdown |
| `description` | string | — | Placeholder text in chat input; shown to user when agent is active |
| `argument-hint` | string | — | Optional hint guiding user on how to interact with this agent |

### Tools & Agents

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `tools` | string[] | — | Available tools for this agent. Built-in, MCP, extension-contributed. Use `<server name>/*` for all tools of an MCP server |
| `agents` | string[] \| `"*"` \| `[]` | `*` | Subagents allowed to be invoked. `*` = all, `[]` = none, list = explicit allowlist. **Requires `agent` in `tools`**. Applies at every nesting level. |

#### Built-in Tool Names
`agent`, `codebase`, `editFiles`, `fetch`, `findTestFiles`, `githubRepo`, `new`, `problems`, `read`, `references`, `runCommands`, `runTests`, `search`, `terminalLastCommand`, `usages`, `vscodeAPI`

### Model

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `model` | string \| string[] | current picker selection | Model(s) to use. Array = priority fallback list. Format: `Model Name (vendor)` |

**Model name examples:**
```yaml
model: Claude Sonnet 4.5 (copilot)
model: ['Claude Opus 4.5 (copilot)', 'GPT-5.2 (copilot)']  # fallback order
model: Claude Haiku 4.5 (copilot)   # fast/cheap for worker agents
```

### Visibility & Invocation Control

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `user-invocable` | boolean | `true` | Show in agents dropdown. Set `false` for subagent-only agents |
| `disable-model-invocation` | boolean | `false` | Prevent being used as subagent by other agents |
| `infer` | boolean | `true` | **Deprecated** — use `user-invocable` + `disable-model-invocation` instead |

### Deployment

| Field | Type | Description |
|-------|------|-------------|
| `target` | `"vscode"` \| `"github-copilot"` | Deployment context |
| `mcp-servers` | object[] | MCP server config for `target: github-copilot` agents |

### Handoffs

Used to create sequential workflows between agents. Handoff buttons appear after a response completes.

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `handoffs` | object[] | — | List of next-step transitions |
| `handoffs[].label` | string | — | Button text shown to user |
| `handoffs[].agent` | string | — | Target agent identifier |
| `handoffs[].prompt` | string | — | Pre-filled prompt for target agent |
| `handoffs[].send` | boolean | `false` | Auto-submit the prompt |
| `handoffs[].model` | string | — | Model for handoff execution. Format: `Model Name (vendor)` |

### Hooks (Preview)

Scoped hooks that run only when this agent is active (user-invoked or as a subagent).  
Requires VS Code setting: `chat.useCustomAgentHooks: true`

| Field | Type | Description |
|-------|------|-------------|
| `hooks` | object | Hook commands following the same format as hook configuration files |

---

## VS Code Settings for Subagents

| Setting | Default | Description |
|---------|---------|-------------|
| `chat.subagents.allowInvocationsFromSubagents` | `false` | Allows a subagent to invoke itself (self-referential / recursive agents). Required for an agent that lists itself in `agents`. |
| `chat.useCustomAgentHooks` | `false` | Enables the `hooks` frontmatter field in agent files. |
| `chat.agentFilesLocations` | — | Additional locations for VS Code to discover `.agent.md` files. |
| `chat.useCustomizationsInParentRepositories` | `false` | Discover agents from the parent repository root in monorepos. |
| `github.copilot.chat.organizationCustomAgents.enabled` | `false` | Enable discovery of organization-level custom agents. |

---

## Complete Examples

### User-Facing Agent with Handoff
```yaml
---
name: Planner
description: Generate an implementation plan for new features or refactoring.
tools: ['fetch', 'githubRepo', 'search', 'usages', 'read']
model: ['Claude Opus 4.5 (copilot)', 'GPT-5.2 (copilot)']
handoffs:
  - label: Start Implementation
    agent: agent
    prompt: Implement the plan outlined above.
    send: false
---
```

### Coordinator Agent (manages subagents)
```yaml
---
name: Feature Builder
description: Build features end-to-end using specialized subagents.
tools: ['agent', 'read', 'search', 'editFiles']
agents: ['Researcher', 'Implementer', 'Reviewer']
model: Claude Sonnet 4.5 (copilot)
---
```

### Nested Worker (worker that spawns its own subagents)
```yaml
---
name: Lead Researcher
description: Coordinate domain-specific research by orchestrating sub-researchers.
tools: ['agent', 'read', 'search']
agents: ['API Researcher', 'DB Researcher']
user-invocable: false
model: Claude Sonnet 4.5 (copilot)
---
Run API Researcher and DB Researcher in parallel. Synthesize findings.
```

### Subagent-Only (hidden from dropdown)
```yaml
---
name: Researcher
description: Research codebase patterns and gather context for other agents.
tools: ['codebase', 'fetch', 'usages', 'read', 'search']
user-invocable: false
model: Claude Sonnet 4.5 (copilot)
---
```

### Lightweight Worker Subagent
```yaml
---
name: Implementer
description: Implement code changes following TDD. Called by coordinator agents.
tools: ['editFiles', 'runCommands', 'runTests', 'terminalLastCommand', 'read']
user-invocable: false
model: Claude Haiku 4.5 (copilot)
---
```

### Protected Subagent (accessible only to specific coordinator)
```yaml
---
name: SecurityReviewer
description: Perform deep security analysis. Only invocable by ThoroughReviewer.
tools: ['read', 'search', 'codebase', 'problems']
user-invocable: false
disable-model-invocation: true   # blocked by default
---
# Note: coordinator must explicitly list this in `agents:` to override
```

### Self-Referential Recursive Agent
```yaml
---
name: RecursivePlanner
description: Break down complex tasks recursively until each subtask is atomic.
tools: ['agent', 'read', 'search']
agents: ['RecursivePlanner']     # self-referential — requires chat.subagents.allowInvocationsFromSubagents
---
If the task is complex, break it into subtasks and spawn an instance of yourself
for each. Stop recursing when the task is atomic (one file, one function, one change).
Return your subtask results merged into a single structured output.
```

---

## Claude Format (`.claude/agents/`)

For cross-tool compatibility with Claude Code, use plain `.md` files in `.claude/agents/`:

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Required. Agent name |
| `description` | string | What the agent does |
| `tools` | string | Comma-separated tool names, e.g. `"Read, Grep, Glob, Bash"` |
| `disallowedTools` | string | Comma-separated tools to block |

VS Code maps Claude tool names to VS Code equivalents automatically.

```markdown
---
name: Researcher
description: Read-only research agent for codebase analysis.
tools: Read, Grep, Glob, Bash(find:*)
---
```

---

## Key Rules & Notes

1. **`agents` requires `agent` in `tools`** — at every nesting level. A worker that omits `agent` from `tools` cannot call sub-workers, even if `agents` is set.
2. **`agents` applies recursively** — each agent in the chain enforces its own `agents` allowlist independently.
3. **Explicit `agents` list overrides `disable-model-invocation: true`** — use this to protect agents from general use while allowing specific coordinators.
4. **`user-invocable: false` + no `disable-model-invocation`** = subagent only (not in picker, but any agent can call it — including nested workers).
5. **`disable-model-invocation: true`** = visible in picker, but no agent can call it as subagent (unless explicitly listed in caller's `agents`).
6. **Self-referential agents** require `chat.subagents.allowInvocationsFromSubagents: true` in VS Code settings.
7. **Model array** = first available model wins. Useful for cost optimization (try expensive model, fall back to cheaper).
8. **Ignored tools** — if a tool is unavailable, it's silently ignored (no error).
9. **Workspace vs. user scope** — `.github/agents/` is workspace-scoped; user profile folder is global across workspaces.
10. **Context isolation per level** — each subagent has its own context window. Only the final result bubbles up to the caller.