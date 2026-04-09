# Changelog

**Document version:** 0.2
**Date updated:** 2026-04-09
**Status:** Active
**meta:** All notable changes to this project are documented in this file.

Format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
versioning follows the internal development plan [Master Plan](.github/implementations/MASTER-PLAN.instructions.md).

---

## [0.2.0] - 2026-04-09

### 2026-04-09 - UI/UX Design Toolkit

- Scope: UI/UX design toolkit
- Summary: Added the `ui-ux-designer` agent and the `desktop-ui-ux` skill with dedicated reference guides for typography, color, components, motion, accessibility, anti-patterns, and a contrast-check helper script. This expands the repository beyond orchestration into opinionated desktop and localhost UI design support.
- Affected files: .github/agents/ui-ux-designer.agent.md, .github/skills/desktop-ui-ux/SKILL.md, .github/skills/desktop-ui-ux/references/TYPOGRAPHY.md, .github/skills/desktop-ui-ux/references/COLOR.md, .github/skills/desktop-ui-ux/references/COMPONENTS.md, .github/skills/desktop-ui-ux/references/MOTION.md, .github/skills/desktop-ui-ux/references/ACCESSIBILITY.md, .github/skills/desktop-ui-ux/references/ANTI-PATTERNS.md, .github/skills/desktop-ui-ux/scripts/check-contrast.py
- Verification: Reviewed agent/skill structure, metadata, and supporting references for internal consistency and publication readiness

### 2026-04-09 - Multi-Agent Orchestration

- Scope: Multi-agent orchestration system (Program Director)
- Summary: Added Program Director super-orchestrator agent that decomposes projects into independent scopes and launches multiple Project Leads in parallel waves. Redesigned PROJECT_LEAD_JOURNAL.md as a dual-ledger (Task Ledger + File Registry + Context Recovery + Progress Ledger). Updated Project Lead with parallel mode support (identity, scope boundaries, context recovery, journal protocol). Created program-director-workflow instructions, and updated all pipeline documentation.
- Affected files: .github/agents/Program-Director.agent.md, .github/agents/Project-Lead.agent.md, .github/instructions/program-director-workflow.instructions.md, .github/instructions/project-lead-workflow.instructions.md, .github/prompts/program-director-e2e.prompt.md, .github/prompts/project-lead-e2e.prompt.md, PROJECT_LEAD_JOURNAL.md, SubAgents-tasks/README.md, SubAgents-context/README.md, docs/architecture/overview.md, README.md
- Verification: Structural review of all created/modified files, cross-reference consistency between PD agent, PL agent, journal template, and workflow instructions
