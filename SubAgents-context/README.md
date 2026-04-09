# SubAgents-context

Directory for preserving context between subagent invocations

## Rules

Brief rules for using this subfolder to preserve context between subagent invocations.

- Purpose: store task context as a stage-log and audit trail between subagent invocations.
- File naming: `subagent-context-{task-name}.instructions.md`.
- Format: Markdown; store stage chronology, findings, decisions, risks, and READY/NOT READY statuses.
- Access: only participants working on the task may edit; edit only your own block in `Application Research Stage`; when creating, specify the author and role (e.g., Project Lead / QA / Dev / User).
- Exception for closure stage: `implementation-completion-reporter` may archive resolved findings and compress outdated blocks, provided it preserves active risks, current status, and the `## User Comment` section without changes.
- Lifetime: context is stored until the task is closed; upon completion, transfer important conclusions to the corresponding `docs/` or `*.instructions.md` and mark the file as `ARCHIVE`.
- Usage in workflow: before launching subagents, attach the path to the corresponding file and reference it in `runSubagent` parameters.
- The full user request is stored in `SubAgents-tasks/task-{task-name}.instructions.md` (sections `Source`/`Goal`), not in the context file.
- `SubAgents-context/subagent-context-{task-name}.instructions.md`: all pipeline participants read the file and may only add their own scoped block in append-only format with explicit role indication (append-only: no deletion of others' active blocks); pipeline participants may only edit their own block.

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
<!--Your data below in append-only format. Explicit editing by SubAgents and Agents is allowed. -->

### Code Reviewer

- Date: 2026-03-26
- Author: code-reviewer
- Stage: review-gate
- Status: PASS/WARNING/FAIL
- Brief summary by severity and scope follows

### Product QA / Scenario Analyst - post-run audit

- Date: 2026-03-16
- Author: product-qa-scenario-analyst
- Stage: research-scenarios
- Status: READY/NOT READY
- Subagent response format follows

## Implementation Status
<!--Task overall status section below. Status changes as stages are completed. -->
{Current implementation status report: `READY` or `NOT READY`}

## User Comment
<!--Section below is editable by User only. Mandatory for execution. Editing by other participants, SubAgents, and Agents is prohibited. -->
```

### Parallel Mode Context Conventions

When multiple Project Leads work in parallel (launched by Program Director):

- Each PL uses the same shared context file for the project-level task.
- Each PL writes only to its own named block within the context file (e.g., `### PL-Alpha — implementation`).
- Context files for parallel tasks should use commented-out `applyTo` to prevent auto-loading into all agents:

  ```yaml
  # applyTo: '**'
  ```

  This prevents task-specific context from polluting unrelated agent invocations in large multi-task projects.
- Only `project-todo.instructions.md` retains active `applyTo: '**'` so all agents are aware of the project backlog.
- Task files and context files should be explicitly linked to specific items in `project-todo.instructions.md` rather than relying on auto-attachment.
