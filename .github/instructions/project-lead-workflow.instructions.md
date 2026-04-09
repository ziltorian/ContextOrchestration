---
name: "project-lead-workflow"
description: "Mandatory subagent coordination workflow with READY/NOT READY status"
---

## Mandatory workflow for working with subagents

### MUST
- Before planning or implementation, always read both artifacts: SubAgents-tasks/task-{task-name}.instructions.md and SubAgents-context/subagent-context-{task-name}.instructions.md.
- The full user request is stored in SubAgents-tasks/task-{task-name}.instructions.md (Source/Goal). The context file stores the stage log, conclusions, risks, and audit reports.
- Reuse one owned context block per participant: by default the block identity is the role or agent name; in parallel mode, the Project Lead identity is its assigned PL name. Repeated invocations and stage changes update the same owned block.
- When a participant changes status or compacts superseded notes, preserve a concise dated transition note in that owned block instead of silently overwriting the latest prior state.
- After reading the context file, inspect `## User Comment`. If it is non-empty, treat it as a signal, deduplicate repeated sightings of the same unresolved comment, surface the signal upward without rewriting the protected text, and require Project Lead acknowledgment and reaction logging.
- Always perform preliminary research using product-qa-scenario-analyst before planning and coding.
- After significant code changes, first execute the review-gate: `code-reviewer`. If the scope includes Python code, explicitly require a Python-specific pass within the same review in the handoff.
- For changes in auth, API endpoints, user input, database operations, file system, or external services, add `security-reviewer` before the final dual audit.
- If implementation is blocked by a build/test/lint/type/import error, invoke `build-error-resolver` as a service stage for diagnosis and minimal fix before continuing the pipeline.
- After implementation, always perform a dual audit:
  1) product-qa-scenario-analyst
  2) integration-architect-auditor
- Each checkpoint audit must end with READY or NOT READY.
- If NOT READY, perform only targeted fixes and re-run the same audit stage.
- If QA and Architect disagree, make a decision based on the authoritative source (task + specifications + code), apply one agreed-upon fix, re-run both audits.

### FORBIDDEN
- Starting planning/implementation without `SubAgents-tasks/task-{task-name}.instructions.md` and `SubAgents-context/subagent-context-{task-name}.instructions.md`. Exception: when launched by Program Director in parallel mode, the PD handoff prompt itself serves as the task definition if no dedicated task file exists for the assigned scope.
- Closing a task without READY from both mandatory checkpoint audits.
- Running the same set of research subagents consecutively without changing the scope.
- Running tests in parallel by multiple subagents.

## Subagent Categories (RACI)

### 1. Intake and Research
- `task-creator`: input formalization. Mode A creates task/context, Mode B updates SubAgents-tasks/project-todo.instructions.md by direct user request.
- `analyze-project`: factual map of modules, APIs, and dependencies from code (code facts).
- `product-qa-scenario-analyst`: scenario QA audit and concepts, user-impact verdict and analysis of the original idea.
- `compliance-gap-auditor`: specification compliance audit.
- `web-searcher`: external technology clarifications and best-practices.

### 2. Planning and Implementation
- `implementation-planning`: creates/updates the planning file *-implementation.instructions.md, when necessary invokes `integration-architect-auditor`, `security-reviewer`, and `test-coverage-lead` on its own for post-draft plan refinement.
- default subagent (`runSubagent` without `agentName`): complex integrations, separate implementation (backend/frontend/docs-sync), testing of written code, any tasks beyond the scope of subagents.
- `code-reviewer`: mandatory code review after significant code changes and before the final dual audit; produces a severity matrix, Verdict PASS/WARNING/FAIL, and when Python scope is present includes Python-specific findings in the same report.
- `build-error-resolver`: service agent for diagnosis and minimal fix of build/test/lint/import/type errors when the implementation stage is blocked.
- `refactor-cleaner`: service agent for tech debt reporting and cleanup plan; not used as a mandatory stage of active feature development.

### 3. Final Verification
- `security-reviewer`: conditional security gate for security-sensitive scope before the final dual audit; does not replace product and architectural audit.
- `product-qa-scenario-analyst`: final QA scenario audit, compliance with the central application idea.
- `integration-architect-auditor`: final architectural/integration audit.
- `test-coverage-lead`: coverage audit and false-positive test result detection.

### 4. Closure and Documentation
- `implementation-completion-reporter`: completion report, templated CHANGELOG.md update, marking of provably completed tasks and controlled cleanup of the context file.
- `document-merger` / `instructions-creator` / `prompt-creator` / `skill-creator`: document and instruction synchronization. `document-merger` also supports multi-stage documentation creation from scratch.

## Artifacts And Ownership

- `task-creator` (Mode A): creates SubAgents-tasks/task-{task-name}.instructions.md and initial SubAgents-context/subagent-context-{task-name}.instructions.md.
- `task-creator` (Mode B): can edit SubAgents-tasks/project-todo.instructions.md only by direct user request.
- `implementation-planning`: creates `*-implementation.instructions.md`.
- `implementation-planning`: owner of the full planning cycle, including internal plan refinement through permitted audit subagents.
- `project-lead`: owns one reusable PL block in the context file, records User Comment signal state and reaction evidence, and may perform mid-task hygiene to compact stale duplicates or superseded notes without altering `Required Documentation`, the protected `## User Comment` section, or another participant's current block.
- `implementation-completion-reporter`: creates `*-COMPLETED.instructions.md`, updates the `Unreleased` block in `CHANGELOG.md`, marks provably completed tasks in plan/todo, and owns final closure/archive compaction in the context file after Project Lead hygiene.

## User Comment Signal Lifecycle

- Detection: any participant that reads a non-empty `## User Comment` section must treat it as a signal and report its presence to its caller without rewriting or quoting the protected text.
- Deduplication: if the same unresolved signal is already recorded in the participant's owned block or in the Project Lead block, update that existing note instead of creating a duplicate escalation entry.
- Acknowledgment: Project Lead records the signal state as `ACKNOWLEDGED` in its own context block and journal after reviewing the comment and deciding the next action.
- Deferral: if the requested reaction is intentionally postponed, Project Lead records `DEFERRED`, keeps the signal active, and records rationale plus next action without rewriting the original user text.
- Resolution: Project Lead records `RESOLVED` only after the requested reaction is completed and the outcome is recorded. The original user text remains untouched.

## Terminal and Tests policy

- By default, only certain subagents can run tests.
- Tests are run only by explicit Project Lead command.
- Tests must always be run by the default subagent after making changes.
- The primary test executor during research and verification: QA branch (`product-qa-scenario-analyst`).
- `integration-architect-auditor` can run tests only in code verification mode and only by explicit command.
- `build-error-resolver` is engaged only to resolve a specific blocking failure and does not replace a full verification run.

## argument-hint Requirements

For each subagent, `argument-hint` must include:
1) target scope (module/files)
2) expected result type (table, matrix, verdict, diff-summary),
3) constraints (no code, no tests, docs-only, etc.),
4) target file `SubAgents-tasks/task-{task-name}.instructions.md` and `SubAgents-context/subagent-context-{task-name}.instructions.md`.

## Handoff Template

- Specify the role, area of responsibility, and analysis boundaries.
- Pass the list of target folders/modules that need to be checked.
- Pass the list of target Skills necessary for completing the task.
- Fix the response format: evidence (files/functions), risks, priorities, conclusion READY/NOT READY (for checkpoint audits).

### Example: specification gap analysis
- `agentName`: `compliance-gap-auditor`
- Prompt: "Compare specifications A/B/C with code X/Y; Current task and context `SubAgents-context/subagent-context-{task-name}.instructions.md`; return Requirement→Implementation→Status, only verifiable facts, no code changes."

### Example: facts from code
- `agentName`: `analyze-project`
- Prompt: "Build a module and contract map for X; Current task and context `SubAgents-context/subagent-context-{task-name}.instructions.md`; return files, classes, functions, dependencies, regression risks; no tests."

### Example: creating an implementation plan
- `agentName`: `implementation-planning`
- Prompt: "Based on the user request and task context in `SubAgents-context/subagent-context-{task-name}.instructions.md`, create a detailed change plan in `*-implementation.instructions.md` format: goal, background, proposed changes (by components, files, methods), tasks with unique ids, verification steps. Do not add code, only structure and change descriptions."

### Example: general code review after implementation
- `agentName`: `code-reviewer`
- Prompt: "Perform a code review on the changed scope X after implementation. Use `SubAgents-context/subagent-context-{task-name}.instructions.md`, read the changed files in full, return severity counts, Verdict PASS/WARNING/FAIL, specific file:line findings and update the task context. If the scope includes Python files, be sure to include Python-specific findings: type hints, Pythonic idioms, Python security, and pytest patterns. Do not make production changes."

### Example: resolving a blocking build/test error
- `agentName`: `build-error-resolver`
- Prompt: "Analyze the blocking failure in scope X using the full stack trace and related files. Find root cause, apply minimal fix, do not modify tests to match implementation, return verification command and update `SubAgents-context/subagent-context-{task-name}.instructions.md`."

### Example: security audit for security-sensitive scope
- `agentName`: `security-reviewer`
- Prompt: "Perform security audit on scope X: auth/API/user input/DB/external services. Return confirmed vulnerabilities with OWASP/CWE classification, severity, file:line, and remediation steps. Use `SubAgents-context/subagent-context-{task-name}.instructions.md`, do not introduce production code, update the task context."

### Example: completion closure
- `agentName`: `implementation-completion-reporter`
- Prompt: "Based on approved plan + changed files + verification evidence + Current task and context `SubAgents-context/subagent-context-{task-name}.instructions.md`, generate `*COMPLETED.instructions.md`, update `CHANGELOG.md` using the template, mark only actually completed tasks in plan/todo, preserve active `NEW`, `ACKNOWLEDGED`, and `DEFERRED` User Comment signals plus Project Lead reaction evidence, and archive resolved findings in the context file without losing active risks, current status, or the user comment section."

### Example: QA scenario audit and application idea analysis
- `agentName`: `product-qa-scenario-analyst`
- Prompt: "Verify implementation compliance with user scenarios: simple request, complex workflow, code-heavy case, media/content, agent enhancement, failed tests, and self-healing. For each: expected path vs actual path, user impact, status (READY/NOT READY). Analyze compliance with the concept from `docs/specification/project-idea.md`, identify gaps, recommendations, citations. Update or create `SubAgents-context/subagent-context-{task-name}.instructions.md` with audit results."

### Example: web search for Microsoft Agent Framework best-practices
- `agentName`: `web-searcher`
- Prompt: "Perform a comprehensive web search on the topic 'Microsoft Agent Framework best practices for integration into Python backend'. Evaluate relevant approaches, architectural patterns, integration examples, risks, and limitations. Generate a report: key findings, applicability to the project, list of sources with annotations. Use the task context from `SubAgents-context/subagent-context-{task-name}.instructions.md`."

## Example Handoff Pipeline

1. Intake: task-creator (if no valid task-{task-name}.instructions.md).
2. Research: product-qa-scenario-analyst + analyze-project (optionally compliance-gap-auditor).
3. Planning: implementation-planning.
4. Implementation: default subagent.
5. Review gate: code-reviewer.
6. Conditional security gate: security-reviewer for security-sensitive changes.
7. Verification: product-qa-scenario-analyst + integration-architect-auditor.
8. Closure: implementation-completion-reporter.

Note: post-draft architect refinement is no longer launched manually by Project Lead. If plan refinement is needed, it is performed by `implementation-planning` through its own orchestration.

## Global Constraints

- Subagents do not launch their own subagents, with the exception of `task-creator`, `implementation-planning`, `integration-architect-auditor`, and `document-merger`, which have a permitted list of nested subagents in the `agents` field.
- **Nested orchestrator exception**: Project Lead launched by Program Director retains full subagent orchestration privileges (may call code-reviewer, implementation-planning, etc.) despite being itself a subagent of Program Director.
- Any coding task is formulated atomically: module/file/function/boundaries.
- Broad refactoring outside the agreed scope is prohibited.
- Subagents have limited context and do not know the context of previous invocations.
- Context must be explicitly passed between subagents via `SubAgents-context/subagent-context-{task-name}.instructions.md`.
- Infinite fix cycles must be avoided, which can arise from untimely documentation updates: a subagent may create a report based on outdated documentation.
- `refactor-cleaner` is used only by explicit request for tech debt or cleanup-wave and must not substitute the implementation of an active task.

## Documentation Awareness

### Required Documentation Propagation

- Before planning, verify that the task file and context file contain a `Required Documentation` section.
- When delegating to subagents, remind them to check the `Required Documentation` section in the context file for relevant specifications.
- Research agents may append newly discovered documentation references to the context file's `Required Documentation` section during their analysis.
- `Required Documentation` remains the only shared section in the context file; all other participant updates must stay within owned blocks or the explicit hygiene/archive permissions.

### Documentation Creation (Optional Parallel Track)

- When a task affects a module without stable documentation in `docs/`, PL may invoke `document-merger` in its multi-stage documentation creation mode as a parallel track.
- Documentation creation must NOT block the main implementation pipeline.
- Entry criteria: target module has no existing stable docs, or specification template is unfilled.
- PL controls stage transitions — each stage requires explicit PL decision to proceed.

## Parallel Mode Conventions

These conventions apply when **Program Director** launches multiple Project Lead agents to work in parallel within the same project.

### Identity and Naming

- Each parallel Project Lead receives a unique name from Program Director (e.g., PL-Alpha, PL-Beta).
- The PL MUST use its assigned name in all journal entries and context file updates.
- If no name is assigned, the PL is running in single-PL mode — parallel conventions do not apply.

### Scope Boundaries

#### MUST
- Respect the assigned scope: only edit files/directories listed in the File Registry under your name.
- Before editing any file, verify it appears in your scope in the File Registry section of `PROJECT_LEAD_JOURNAL.md`.
- If you need a file outside your scope, record it as a blocker in your Progress Ledger section — do NOT edit it.

#### FORBIDDEN
- Editing files outside your assigned scope.
- Modifying the Task Ledger or File Registry sections of the journal (owned by Program Director).
- Editing other PLs' sections in the Progress Ledger.
- Running tests in parallel with other Project Leads (test execution conflicts).
- Creating new task files (`task-*.instructions.md`) without scope authorization — use the existing project-level task file.

### Journal Coordination

- Write ONLY to your own named section in the Progress Ledger of `PROJECT_LEAD_JOURNAL.md`.
- Read the full journal (Task Ledger, File Registry, other PLs' sections) for awareness.
- Use all mandatory fields in every journal entry — no freeform prose.
- Append new entries; do not overwrite previous entries within the same wave.

### Context Recovery Protocol

When launched by Program Director with clean context:

1. Read `PROJECT_LEAD_JOURNAL.md` in full.
2. Find the Task Ledger → understand project goal and overall plan.
3. Find the File Registry → identify your assigned scope.
4. Find the Context Recovery section → understand current project state.
5. Find your named section in Progress Ledger → reconstruct your prior work (if any from previous waves).
6. Accept that context recovery may be incomplete — proceed with available information.
7. If critical context is missing, log it as a blocker rather than guessing.

### Scope Conflict Resolution

- If two PLs need the same file, the one NOT listed in the File Registry yields.
- If neither is listed (registry error), both log it as a blocker for Program Director to resolve in the next wave.
- Shared infrastructure files (README, CHANGELOG, project-todo) are handled by the designated PL or by Program Director between waves.

### Partial Completion

- If you complete your scope before other PLs finish, write a READY status to your journal section and terminate.
- If you cannot complete your scope, write a NOT READY or BLOCKED status with details for Program Director to re-assign in the next wave.
