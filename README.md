# Context Orchestration

A complete toolkit for orchestrating software projects using AI agents, subagents, structured workflows, and context management — built for VS Code with GitHub Copilot.

## Overview

Context Orchestration provides a ready-to-use framework of **20 AI agents**, **7 skills**, **9 prompt templates**, and a structured pipeline for managing any software project through intelligent delegation and quality gates.

Instead of manually coordinating AI assistants, you get a **Project Lead agent** that orchestrates the entire development lifecycle: task intake → research → planning → implementation → review → verification → completion. For larger projects, a **Program Director** agent can orchestrate multiple Project Leads working in parallel on independent scopes.

## Key Features

- **Program Director** — Super-orchestrator that decomposes projects into independent scopes and launches multiple Project Leads in parallel waves
- **Project Lead Agent** — Central coordinator that delegates work to specialized subagents and enforces quality gates
- **20 Agents** — Project orchestration, code review, security audit, implementation planning, UI/UX design, build error resolution, refactoring, QA scenarios, and more
- **Structured Pipeline** — Predictable flow from task creation through dual-audit verification to completion
- **Context Preservation** — Persistent context files that maintain state between agent invocations
- **Task Management** — Formalized task files, implementation plans, and progress tracking
- **Quality Gates** — Mandatory code review, optional security review, and dual-audit (QA + architecture) before closure
- **Skills Library** — Reusable knowledge modules for prompt engineering, UI/UX design, implementation planning, open-source licensing, VS Code instructions, and subagent creation

## Project Structure

```text
.github/
├── agents/                  # 20 agent definitions (.agent.md)
│   ├── Program-Director.agent.md
│   ├── Project-Lead.agent.md
│   ├── code-reviewer.agent.md
│   ├── security-reviewer.agent.md
│   ├── implementation-planning.agent.md
│   ├── build-error-resolver.agent.md
│   ├── task-creator.agent.md
│   ├── ui-ux-designer.agent.md
│   └── ...12 more agents
├── instructions/            # Global instruction files
│   ├── program-director-workflow.instructions.md
│   ├── project-lead-workflow.instructions.md
│   ├── Project_Docs_Context.instructions.md
│   ├── Project_Documentation.instructions.md
│   └── Mark_Tasks_As_Done.instructions.md
├── implementations/         # Implementation plans per task
│   ├── MASTER-PLAN.instructions.md
│   └── example-auth-implementation.instructions.md
├── prompts/                 # Reusable prompt templates (.prompt.md)
│   ├── program-director-workflow.prompt.md
│   ├── project-lead-workflow.prompt.md
│   ├── project-lead-e2e.prompt.md
│   ├── feature-implementation.prompt.md
│   ├── create-technical-specification.prompt.md
│   └── ...4 more prompts
└── skills/                  # Domain knowledge modules
    ├── desktop-ui-ux/
    ├── create-vscode-instructions/
    ├── create-vscode-subagents/
    ├── implementation-planning/
    ├── open-source-licensing/
    ├── prompt-engineering/
    └── skill-creator/

SubAgents-tasks/             # Task definitions and project backlog
├── project-todo.instructions.md   # Task queue
└── README.md                      # Pipeline rules and conventions

SubAgents-context/           # Persistent context between agent calls
└── README.md                # Context file format and rules

docs/                        # Project documentation (templates)
├── README.md                # Documentation overview
├── specification/           # Feature specifications
│   └── project-idea.md
├── api/                     # API documentation
│   └── endpoints.md
└── architecture/            # Architecture decisions
    └── overview.md
PROJECT_LEAD_JOURNAL.md      # Agent decision log (template)
CHANGELOG.md                 # Change history
```

## Pipeline Workflow

All orchestration flows through **Project Lead**, which delegates to specialized subagents. Any agent can also be called directly by the user for standalone tasks. For large projects, **Program Director** orchestrates multiple Project Leads in parallel.

### Multi-Agent Orchestration (via Program Director)

For projects requiring parallel execution, Program Director decomposes work into independent scopes and launches multiple named Project Leads per wave:

```text
 ┌────────────────────────────────────────────────────────┐
 │  USER                                                  │
 │                                                        │
 │  1. Describe project goal or fill project-todo         │
 │  2. Call @Program-Director                             │
 └──────────────────────┬─────────────────────────────────┘
                        │
                        ▼
          ┌──────────────────────────┐
          │    Program Director      │
          │   (super-orchestrator)   │
          └─────┬──────────┬─────────┘
                │          │          (parallel launch)
       ┌────────┘    ┌─────┘   ┌────────────┐
       ▼             ▼         ▼            │
 ┌───────────┐ ┌───────────┐ ┌───────────┐  │
 │ PL-Alpha  │ │ PL-Beta   │ │ PL-Gamma  │  │
 │ (scope A) │ │ (scope B) │ │ (scope C) │  │
 └─────┬─────┘ └──────┬────┘ └─────┬─────┘  │
       │              │            │        │
       └──────────────┴────────────┘        │
                      │                     │
                      ▼                     │
          ┌──────────────────────┐          │
          │  Post-Wave Review    │          │
          │  (stall detection)   │──────────┘
          └──────────────────────┘   (next wave if needed)
```

Each Project Lead runs the full pipeline independently within its assigned scope (see below).

### Full Pipeline (via Project Lead)

The standard flow starts with the user filling `project-todo.instructions.md` with tasks, then invoking Project Lead:

```text
 ┌──────────────────────────────────────────────────────────────────┐
 │  USER                                                            │
 │                                                                  │
 │  1. Fill project-todo with tasks                                 │
 │  2. Call @Project-Lead                                           │
 │     OR call @task-creator to formalize a single task first       │
 └──────────────────────┬───────────────────────────────────────────┘
                        │
                        ▼
          ┌──────────────────────────┐
          │      Project Lead        │
          │     (orchestrator)       │
          └─────┬──────────┬─────────┘
                │          │
       ┌────────┘          └─────────┐
       ▼                             ▼
 ┌────────────┐            ┌──────────────────┐
 │  task-     │            │ analyze-project  │
 │  creator   │            │ (research)       │
 │ (intake)   │            └────────┬─────────┘
 └────────────┘                     │
                                    ▼
                         ┌──────────────────────┐
                         │ implementation-      │
                         │ planning (plan)      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Default subagent     │
                         │ (implementation)     │
                         └──────────┬───────────┘
                                    │
                                    ▼
                        ┌────────────────────────┐
                        │ code-reviewer          │
                        │ security-reviewer      │
                        │ (review gate)          │
                        └──────────┬─────────────┘
                                   │
                                   ▼
                  ┌──────────────────────────────────┐
                  │ product-qa-scenario-analyst      │
                  │ integration-architect-auditor    │
                  │ (dual audit)                     │
                  └────────────────┬─────────────────┘
                                   │
                                   ▼
                  ┌─────────────────────────────────┐
                  │ implementation-completion-      │
                  │ reporter (closure)              │
                  └─────────────────────────────────┘
```

### Direct Agent Access

Any agent can be invoked directly without Project Lead or a pre-filled todo:

```text
 USER ──▶ @Program-Director      (orchestrate full project with parallel PLs)
 USER ──▶ @code-reviewer         (review specific files)
 USER ──▶ @implementation-planning (plan a feature)
 USER ──▶ @build-error-resolver  (fix a failing build)
 USER ──▶ @task-creator          (formalize a task into the backlog)
 USER ──▶ @security-reviewer     (audit for vulnerabilities)
```

Use direct access when:

- You need a quick, focused operation (code review, error fix)
- You want to create a task or plan without running the full pipeline
- You are working on an ad-hoc request that doesn't need formal tracking

## Agents

| Agent | Purpose |
| ----- | ------- |
| **Program-Director** | Super-orchestrator: decomposes projects into scopes, launches parallel Project Leads |
| **Project-Lead** | Orchestrates task execution through subagent delegation |
| **analyze-project** | Factual code analysis: modules, contracts, dependencies, API |
| **build-error-resolver** | Diagnoses and fixes build, test, and lint errors |
| **code-reviewer** | Code review for quality, security, and maintainability |
| **compliance-gap-auditor** | Gap analysis between implementation and specifications |
| **document-merger** | Merges or creates stable project documentation with code-backed verification and targeted research/review orchestration |
| **implementation-completion-reporter** | Produces closure artifacts: reports, changelog, task status |
| **implementation-planning** | Creates implementation plans with phases, risks, and testing |
| **instructions-creator** | Creates .instructions.md files for GitHub Copilot |
| **integration-architect-auditor** | Architectural audit of integration integrity |
| **product-qa-scenario-analyst** | Validates implementation against user scenarios |
| **prompt-creator** | Creates system prompts for AI agents and workflows |
| **refactor-cleaner** | Dead code cleanup, duplicates, unused dependencies |
| **security-reviewer** | Security vulnerability analysis (OWASP Top 10) |
| **skill-creator** | Creates universal, reusable Agent Skills |
| **task-creator** | Formalizes pipeline tasks and updates project backlog |
| **test-coverage-lead** | Test coverage audit including false-positive detection |
| **ui-ux-designer** | Designs desktop and localhost UI with strong accessibility and visual direction |
| **web-searcher** | In-depth research and information retrieval |

## Getting Started

### Prerequisites

- [VS Code](https://code.visualstudio.com/) with [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) extension
- GitHub Copilot Chat with agent mode enabled

### Installation

1. Copy the `.github/` folder into the root of your project
2. Copy `SubAgents-tasks/`, `SubAgents-context/`, and `PROJECT_LEAD_JOURNAL.md` into your project root
3. Customize the `MASTER-PLAN.instructions.md` for your project
4. Update `Project_Docs_Context.instructions.md` to point to your documentation

### Usage

**Start a task via Project Lead:**

```text
@Project-Lead Create a new REST API endpoint for user authentication
```

**Use a specific agent directly:**

```text
@code-reviewer Review the changes in src/auth/
@implementation-planning Plan the database migration for v2
@build-error-resolver Fix the failing tests in test_api.py
```

**Create a task for the backlog:**

```text
@task-creator Add caching layer for API responses
```

## Customization

### Adding New Agents

Create a new `.agent.md` file in `.github/agents/` following the existing format:

```yaml
---
name: my-agent
description: 'What this agent does'
tools: [list, of, required, tools]
---
```

### Adding New Skills

Create a new folder in `.github/skills/` with a `SKILL.md` file. Skills provide domain-specific knowledge that agents can reference.

### Modifying the Pipeline

Edit `SubAgents-tasks/README.md` to adjust pipeline stages, roles, and rules. Update `.github/instructions/project-lead-workflow.instructions.md` for the Project Lead's orchestration logic.

## Disclaimer

> **This project was entirely created by AI models and agents.** As such, it may itself contain errors, inaccuracies, or suboptimal patterns. It is strongly recommended that you **review and adapt** all materials — agents, instructions, templates, and documentation — to fit your own codebase, security policies, documentation standards, and development patterns before use.
>
> **This project provides AI agent definitions, orchestration templates, and instructions that interact with AI language models.** AI outputs are non-deterministic and may contain errors, inaccuracies, or unexpected results. The use of this project **does not guarantee** any specific outcome, code quality, or fitness for a particular task. The author(s) assume **no responsibility** for any damage, data loss, incorrect code generation, or other issues arising from the use of agents, subagents, instructions, or any other materials included in this project. **Users are solely responsible for reviewing and validating all AI-generated outputs** before applying them to their projects.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Copyright (c) 2026 Ziltorian. This project is licensed under the [MIT License](LICENSE). You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies — just keep the copyright notice and permission notice in any copies or substantial portions.
