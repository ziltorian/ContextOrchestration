# Changelog

**Document version:** 0.2
**Date updated:** 2026-04-10
**Status:** Active
**meta:** All notable changes to this project are documented in this file.

Format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
versioning follows the internal development plan [Master Plan](.github/implementations/MASTER-PLAN.instructions.md).

---

## [0.2.0] - 2026-04-10

### 2026-04-10 - Program-Director / Project-Lead Orchestration Loop Hardening

- Scope: Program-Director / Project-Lead orchestration loop hardening
- Summary: Hardened the Program-Director and Project-Lead orchestration contract so parallel mode is additive only, independent scopes launch as true parallel batches, Program-Director reads repository docs/specs directly while delegating broader project/code analysis and post-wave verification to approved subagents, and closure/verification semantics remain aligned across instructions, agents, prompts, skills, canonical pipeline docs, and public mirrors.

### 2026-04-09 - Context File Freshness

- Scope: Context freshness contract migration
- Summary: Migrated repository-wide context-file coordination from append-only participant logs to one reusable owned block per participant, formalized `## User Comment` escalation and Project Lead reaction states, separated Project Lead mid-task hygiene from closure-stage archive ownership, and synchronized canonical docs, agent mirrors, prompt surfaces, and skill references with the refreshed contract.
- Affected files: SubAgents-context/README.md, SubAgents-tasks/README.md, .github/instructions/project-lead-workflow.instructions.md, .github/agents/Project-Lead.agent.md, .github/agents/implementation-completion-reporter.agent.md, .github/agents/analyze-project.agent.md, .github/agents/build-error-resolver.agent.md, .github/agents/code-reviewer.agent.md, .github/agents/compliance-gap-auditor.agent.md, .github/agents/document-merger.agent.md, .github/agents/integration-architect-auditor.agent.md, .github/agents/product-qa-scenario-analyst.agent.md, .github/agents/refactor-cleaner.agent.md, .github/agents/security-reviewer.agent.md, .github/agents/task-creator.agent.md, .github/agents/test-coverage-lead.agent.md, .github/agents/web-searcher.agent.md, .github/prompts/project-lead-e2e.prompt.md, .github/skills/create-vscode-subagents/SKILL.md, .github/skills/create-vscode-subagents/references/project-pipeline.md, README.md, docs/architecture/overview.md, PROJECT_LEAD_JOURNAL.md, SubAgents-tasks/task-context-file-freshness.instructions.md, SubAgents-context/subagent-context-context-file-freshness.instructions.md, .github/implementations/context-file-freshness-implementation.instructions.md
- Verification: Code review PASS after targeted fixes; QA audit READY; architecture audit READY after the final rerun covering `DEFERRED` lifecycle visibility and skill-reference ownership fixes; automated tests not run because no test harness exists in the repository (`package.json`, `pyproject.toml`, `pytest.ini`, and `tests/` were not found).

### 2026-04-09 - Documentation Awareness Pipeline

- Scope: Agent pipeline, documentation propagation
- Summary: Added `Required Documentation` section to task and context file templates. 8 agents now automatically propagate documentation references through the pipeline: task-creator populates at intake, research agents (analyze-project, product-qa-scenario-analyst, integration-architect-auditor) append discovered specs, web-searcher tracks docs/web/ artifacts, document-merger supports multi-stage documentation creation from scratch. Project Lead workflow updated with Documentation Awareness section.
- Affected files: SubAgents-tasks/README.md, SubAgents-context/README.md, task-creator.agent.md, analyze-project.agent.md, product-qa-scenario-analyst.agent.md, integration-architect-auditor.agent.md, web-searcher.agent.md, document-merger.agent.md, project-lead-workflow.instructions.md, implementation-planning.agent.md, docs/architecture/overview.md, Project_Docs_Context.instructions.md
- Verification: Code review PASS (3 issues fixed), QA audit READY (4/4 scenarios), Architecture audit READY (42/42 integration matrix)

### 2026-04-09 - UI/UX Design Toolkit

- Scope: UI/UX design toolkit
- Summary: Added the `ui-ux-designer` agent and the `desktop-ui-ux` skill with dedicated reference guides for typography, color, components, motion, accessibility, anti-patterns, and a contrast-check helper script. This expands the repository beyond orchestration into opinionated desktop and localhost UI design support.
- Affected files: .github/agents/ui-ux-designer.agent.md, .github/skills/desktop-ui-ux/SKILL.md, .github/skills/desktop-ui-ux/references/TYPOGRAPHY.md, .github/skills/desktop-ui-ux/references/COLOR.md, .github/skills/desktop-ui-ux/references/COMPONENTS.md, .github/skills/desktop-ui-ux/references/MOTION.md, .github/skills/desktop-ui-ux/references/ACCESSIBILITY.md, .github/skills/desktop-ui-ux/references/ANTI-PATTERNS.md, .github/skills/desktop-ui-ux/scripts/check-contrast.py
- Verification: Reviewed agent/skill structure, metadata, and supporting references for internal consistency and publication readiness

### 2026-04-09 - Multi-Agent Orchestration

- Scope: Multi-agent orchestration system (Program Director)
- Summary: Added Program Director super-orchestrator agent that decomposes projects into independent scopes and launches multiple Project Leads in parallel waves. Redesigned PROJECT_LEAD_JOURNAL.md as a dual-ledger (Task Ledger + File Registry + Context Recovery + Progress Ledger). Updated Project Lead with parallel mode support (identity, scope boundaries, context recovery, journal protocol). Created program-director-workflow instructions, and updated all pipeline documentation.
- Affected files: .github/agents/Program-Director.agent.md, .github/agents/Project-Lead.agent.md, .github/instructions/program-director-workflow.instructions.md, .github/instructions/project-lead-workflow.instructions.md, .github/prompts/program-director-e2e.prompt.md, .github/prompts/project-lead-e2e.prompt.md, PROJECT_LEAD_JOURNAL.md, SubAgents-tasks/README.md, SubAgents-context/README.md, docs/architecture/overview.md, README.md
- Verification: Structural review of all created/modified files, cross-reference consistency between Program-Director agent, Project-Lead agent, journal template, and workflow instructions
