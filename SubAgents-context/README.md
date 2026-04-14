# SubAgents-context

Directory for preserving context between subagent invocations

## Rules

Brief rules for using this subfolder to preserve context between subagent invocations.

- Purpose: store current task context and a compact audit trail between participant invocations.
- File naming: `subagent-context-{task-name}.instructions.md`.
- Format: Markdown; store one reusable owned block per participant plus shared status and protected sections.
- Access: only participants working on the task may edit. Each participant owns exactly one reusable block in `Application Research Stage`; when creating or updating it, specify the author and role (e.g., Project Lead / QA / Dev / User).
- Stable identity for owned blocks: use the agent or role name by default (for example, `code-reviewer`); in parallel mode, each Project Lead uses its assigned name (for example, `Project-Lead-Alpha`). Stage changes and repeated invocations update metadata inside the same owned block rather than creating a new block.
- Mutable data inside an owned block: current stage, status, key findings, active risks, decisions, references, concise archive notes for superseded details, and a concise immutable status-transition trail.
- Traceability floor: when a block changes status or compacts superseded notes, keep a dated `Status history` or equivalent transition note instead of silently deleting the latest prior state.
- Project Lead mid-task hygiene: Project Lead may compact stale duplicate or superseded participant material when needed to restore one current owned block per participant, provided it preserves active findings, current status, `Required Documentation`, and the `## User Comment` section, and does not remove another participant's current owned block.
- Exception for closure stage: `implementation-completion-reporter` owns final closure/archive hygiene. On `READY`, it may archive superseded blocks into a compact closure summary and mark the file as `ARCHIVE`; on `NOT READY`, it keeps current owned blocks visible and archives only resolved noise.
- Lifetime: context is stored until the task is closed; upon completion, transfer important conclusions to the corresponding `docs/` or `*.instructions.md` and mark the file as `ARCHIVE`.
- Usage in workflow: before launching subagents, attach the path to the corresponding file and reference it in `runSubagent` parameters.
- The full user request is stored in `SubAgents-tasks/task-{task-name}.instructions.md` (sections `Source`/`Goal`), not in the context file.
- `SubAgents-context/subagent-context-{task-name}.instructions.md`: all pipeline participants read the file and update only their own current owned block, except for the explicit Project Lead hygiene and `implementation-completion-reporter` closure/archive permissions described above.
- `## User Comment` remains user-editable only. Non-user participants may detect a non-empty comment, treat it as a signal, and surface that signal upward without rewriting or quoting the user text.
- User Comment signal lifecycle: `NEW` when first detected, `ACKNOWLEDGED` when Project Lead records a reaction and next action, `DEFERRED` when the requested reaction is intentionally postponed and follow-up remains active, and `RESOLVED` only after Project Lead records the completed outcome. Repeated sightings of the same unresolved comment must be deduplicated by updating the existing owned block rather than adding duplicate entries.

### Required Documentation — Shared Section Exception

- `Required Documentation` is a **shared section** — an exception to the block-scoping rule. Multiple permitted agents may append entries to this single section.
- This exception applies ONLY to `Required Documentation` and does NOT establish a precedent for other shared sections.
- Permitted editors: `task-creator` (initial population), `analyze-project`, `product-qa-scenario-analyst`, `integration-architect-auditor`, `web-searcher`, `document-merger`.
- Entry format: `- [path](path) — description <!-- added by: agent-name, YYYY-MM-DD -->`
- Dedup rule: before appending, check if the relative path already exists in the section; if it does, skip the entry.
- Backward compatibility: if a context file does not contain a `Required Documentation` section, agents skip silently and do not fail.

- The final subagent response (summary returned to the Project Lead context after invocation): no more than 100 lines. Each agent may set a stricter limit in its `<constraints>`.
- Recommended block order after coding stage: implementation → `code-reviewer` (with Python-specific findings within the same block for Python scope) → `security-reviewer` for security-sensitive scope → mandatory final audits.
- `build-error-resolver` records only root cause, minimal fix, and verification command; `refactor-cleaner` records only the report and risk assessment without hidden cleanup.

### Minimal File Template Example

```markdown
---
applyTo: '**'
name: '{Task name. Specified by User or Project Lead}'
description: '{Brief task summary and current scope boundaries. Full task statement source: SubAgents-tasks/task-{task-name}.instructions.md}'
---

## Required Documentation
<!-- Shared section. Permitted editors append entries with attribution. Dedup: check relative path before appending. -->

- [path/to/doc.md](path/to/doc.md) — description <!-- added by: agent-name, YYYY-MM-DD -->

## Application Research Stage
<!--Your data below in single reusable owned blocks. Explicit editing by SubAgents and Agents is allowed only within their current block, except for permitted hygiene/archive actions. -->

When a block is updated after prior runs or stage changes, keep a `- Status history:` field with dated transition notes and compaction reasons.

### Code Reviewer

- Date: 2026-03-26
- Author: code-reviewer
- Block identity: code-reviewer
- Stage: review-gate
- Status: PASS/WARNING/FAIL
- Status history: {YYYY-MM-DD prior status or compaction note, if any}
- Brief summary by severity and scope follows

### Product QA / Scenario Analyst - post-run audit

- Date: 2026-03-16
- Author: product-qa-scenario-analyst
- Block identity: product-qa-scenario-analyst
- Stage: research-scenarios
- Status: READY/NOT READY
- Status history: {YYYY-MM-DD prior status or compaction note, if any}
- Subagent response format follows

## Implementation Status
<!--Task overall status section below. Status changes as stages are completed. -->
{Current implementation status report: `READY` or `NOT READY`}

## User Comment
<!--Section below is editable by User only. Mandatory for execution. Editing by other participants, SubAgents, and Agents is prohibited. -->
```

### Parallel Mode Context Conventions

When multiple Project Leads work in parallel (launched by Program Director):

- Each Project Lead uses the same shared context file for the project-level task.
- Each Project Lead writes only to its own reusable named block within the context file (for example, `### Project-Lead-Alpha`).
- The assigned Project-Lead name is the stable block identity; repeated invocations and stage transitions update that same named block, with stage stored as mutable metadata inside it.
- Context files for parallel tasks should use commented-out `applyTo` to prevent auto-loading into all agents:

  ```yaml
  # applyTo: '**'
  ```

  This prevents task-specific context from polluting unrelated agent invocations in large multi-task projects.
- Only `project-todo.instructions.md` retains active `applyTo: '**'` so all agents are aware of the project backlog.
- Task files and context files should be explicitly linked to specific items in `project-todo.instructions.md` rather than relying on auto-attachment.
