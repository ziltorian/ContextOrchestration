---
name: "project-lead-workflow"
description: "Mandatory subagent coordination workflow with READY/NOT READY status"
---

## Mandatory workflow for working with subagents

### MUST
- Before planning or implementation, always read both artifacts: SubAgents-tasks/task-{task-name}.instructions.md and SubAgents-context/subagent-context-{task-name}.instructions.md.
- The full user request is stored in SubAgents-tasks/task-{task-name}.instructions.md (Source/Goal). The context file stores the stage log, conclusions, risks, and audit reports.
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
- Starting planning/implementation without `SubAgents-tasks/task-{task-name}.instructions.md` and `SubAgents-context/subagent-context-{task-name}.instructions.md`.
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
- `document-merger` / `instructions-creator` / `prompt-creator` / `skill-creator`: document and instruction synchronization.

## Artifacts And Ownership

- `task-creator` (Mode A): creates SubAgents-tasks/task-{task-name}.instructions.md and initial SubAgents-context/subagent-context-{task-name}.instructions.md.
- `task-creator` (Mode B): can edit SubAgents-tasks/project-todo.instructions.md only by direct user request.
- `implementation-planning`: creates `*-implementation.instructions.md`.
- `implementation-planning`: owner of the full planning cycle, including internal plan refinement through permitted audit subagents.
- `implementation-completion-reporter`: creates `*-COMPLETED.instructions.md`, updates the `Unreleased` block in `CHANGELOG.md`, marks provably completed tasks in plan/todo, and can archive resolved findings in the context file.

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
- Prompt: "Based on approved plan + changed files + verification evidence + Current task and context `SubAgents-context/subagent-context-{task-name}.instructions.md`, generate `*COMPLETED.instructions.md`, update `CHANGELOG.md` using the template, mark only actually completed tasks in plan/todo, and archive resolved findings in the context file without losing active risks and the user comment section."

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

- Subagents do not launch their own subagents, with the exception of `task-creator`, `implementation-planning`, and `integration-architect-auditor`, which have a permitted list of nested subagents in the `agents` field.
- Any coding task is formulated atomically: module/file/function/boundaries.
- Broad refactoring outside the agreed scope is prohibited.
- Subagents have limited context and do not know the context of previous invocations.
- Context must be explicitly passed between subagents via `SubAgents-context/subagent-context-{task-name}.instructions.md`.
- Infinite fix cycles must be avoided, which can arise from untimely documentation updates: a subagent may create a report based on outdated documentation.
- `refactor-cleaner` is used only by explicit request for tech debt or cleanup-wave and must not substitute the implementation of an active task.
