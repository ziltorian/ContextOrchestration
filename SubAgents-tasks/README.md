# General Project Pipeline

`SubAgents-tasks/README.md` is the single source of truth for the subagent-pipeline.

## Canonical Artifacts

- Short task queue: `SubAgents-tasks/project-todo.instructions.md`
- Detailed task: `SubAgents-tasks/task-{task-name}.instructions.md`
- Task context: `SubAgents-context/subagent-context-{task-name}.instructions.md`
- Implementation plan: `.github/implementations/{task-name}-implementation.instructions.md`

## Pipeline Stages and Roles

1. User or `task-creator` (mode B) adds short items to `SubAgents-tasks/project-todo.instructions.md`.
2. `task-creator` (mode A) performs intake/research and creates `SubAgents-tasks/task-{task-name}.instructions.md` + initial `SubAgents-context/subagent-context-{task-name}.instructions.md`.
3. `project-lead` orchestrates research and planning based on `task + context`.
4. `implementation-planning` creates `.github/implementations/{task-name}-implementation.instructions.md`, invoking `integration-architect-auditor`, `security-reviewer` and `test-coverage-lead` as needed to refine the draft plan;
5. Default subagent performs implementation according to the approved plan.
6. After significant code changes, a review-gate is triggered: `code-reviewer`; for Python scope it must include Python-specific findings in the same report.
7. For security-sensitive scope, `security-reviewer` is added before the final audit.
8. Control auditors `product-qa-scenario-analyst` and `integration-architect-auditor` issue `READY` or `NOT READY`.
9. `implementation-completion-reporter` handles closure: completion report, templated `CHANGELOG.md`, verified marking of completed tasks, and context file cleanup.

Service agents as needed:

- `build-error-resolver`: engaged by Project Lead when implementation stage is blocked by a build/test/lint/import/type error; goal is root cause and minimal fix without tailoring tests to the implementation.
- `refactor-cleaner`: used only for separate cleanup/tech-debt scope; in an active feature task it produces a report and plan rather than silently modifying code.

## Mandatory Pre-read

At each stage, agents and subagents must read:

- `SubAgents-tasks/task-{task-name}.instructions.md`
- `SubAgents-context/subagent-context-{task-name}.instructions.md`

Exception:

- `task-creator` in mode A performs pre-read from `SubAgents-tasks/README.md`, `SubAgents-context/README.md`, `SubAgents-tasks/project-todo.instructions.md` and relevant `docs/`, since `task-{task-name}.instructions.md` has not been created yet.

Additionally per task:

- Relevant specifications and architectural documents in `docs/`
- `.github/implementations/{task-name}-implementation.instructions.md` (starting from the implementation stage)
- For review-stage, changed files and corresponding `.github/agents/*.agent.md` for the invoked reviewer/service-agent are also mandatory.

If `SubAgents-tasks/task-{task-name}.instructions.md` is missing, launching planning/implementation/verification is prohibited, stage result: `NOT READY`.

## File Editing Rights

- `SubAgents-tasks/project-todo.instructions.md`: user can always edit; `task-creator` can edit only in mode B and only by direct user request; `implementation-completion-reporter` can mark truly completed items at closure stage only with confirmed evidence.
- `SubAgents-tasks/task-{task-name}.instructions.md`: created only by `task-creator` (mode A) or `project-lead` if user directly assigned a task bypassing project-todo.instructions.md. After Project Lead approval, the file is immutable and cannot be edited.
- `SubAgents-context/subagent-context-{task-name}.instructions.md`: all pipeline participants read the file and can only add their own scoped block with explicit role identification (append-only, without deleting others' current blocks), pipeline participants can edit only their own block; exception — `implementation-completion-reporter`, which at closure stage can archive resolved findings and compress outdated blocks without modifying active issues and the user comment section.
- `.github/implementations/{task-name}-implementation.instructions.md`: owner `implementation-planning`; plan refinement via audit subagents is performed when `implementation-planning` invokes its own subagents.
- Production code: edited only by default subagent.
- `code-reviewer`, `security-reviewer`, `refactor-cleaner`: review-only/report-only participants; they do not modify production code.
- For Python scope, `code-reviewer` combines general review and Python-specific pass.
- `build-error-resolver`: allowed only for minimal fix of a blocking error within the already approved scope; does not modify tests to match implementation and does not expand the task.
- Documentation and completion artifacts: produced at implementation and closure stages by specialized agents.

## Task File Template `task-{task-name}.instructions.md`

```markdown
---
applyTo: '**'
name: '{Task name. Specified by User or Project Lead}'
description: '{Brief contextual summary of the task and current scope boundaries.}'
---

## Source
- Created by: {Project Lead | task-creator | User}
- Date: {YYYY-MM-DD}
- Basis: {reference to user request / todo item}

## Goal
{Clear task goal in 1-3 paragraphs}

## Scope
1. {What is mandatory for the task}
2. {Change boundaries}
3. {Target files/modules}
4. {Resources and dependencies}
5. {Potential problem areas requiring special attention and additional investigation}

## Done Criteria
- {Verifiable criterion 1}
- {Verifiable criterion 2}

## Non-goals
- {What we explicitly do not do}

## Constraints
- {Constraints: security, tests, format, architectural restrictions}

## Additional Subagents
- {List of additional subagents for the task. Format: agent_name - role/task}
```
