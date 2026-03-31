# GitHub Copilot Skills Specification

Reference for creating skills compatible with GitHub Copilot coding agent, CLI, and VS Code.

## Overview

GitHub Copilot Skills enhance the ability of Copilot coding agent, GitHub Copilot CLI, and Visual Studio Code to perform specialized tasks. Skills are folders of instructions, scripts, and resources that Copilot can load when relevant.

## Skill Location

Skills must be stored in repository at:

- `.github/skills/` (primary location)
- `.claude/skills/` (also supported)

Each skill has its own subdirectory (e.g., `.github/skills/webapp-testing`).

**Important**: Currently only repository-level skills are supported. Organization and enterprise-level support is coming soon.

## SKILL.md File Structure

Every skill requires a `SKILL.md` file (must be named exactly `SKILL.md`).

### Required YAML Frontmatter

```yaml
---
name: skill-name-here
description: What the skill does and when to use it
---
```

**Field Requirements:**

- `name` (required): Unique identifier, lowercase with hyphens for spaces
- `description` (required): Description of what skill does and when Copilot should use it

### Optional YAML Frontmatter

```yaml
---
name: github-actions-debugging
description: Debug failing GitHub Actions workflows
license: MIT
dependencies: python>=3.8, pandas>=1.5.0
---
```

**Optional Fields:**

- `license`: License information
- `dependencies`: Software packages required by the skill (e.g., `python>=3.8, pandas>=1.5.0`)

### Markdown Body

The body contains instructions for Copilot to follow. No format restrictions - write whatever helps Copilot perform the task effectively.

## Example SKILL.md

**Location**: `.github/skills/github-actions-failure-debugging/SKILL.md`

```markdown
---
name: github-actions-failure-debugging
description: Guide for debugging failing GitHub Actions workflows. Use this when asked to debug failing GitHub Actions workflows.
---

To debug failing GitHub Actions workflows in a pull request, follow this process, using tools provided from the GitHub MCP Server:

1. Use the `list_workflow_runs` tool to look up recent workflow runs for the pull request and their status
2. Use the `summarize_job_log_failures` tool to get an AI summary of the logs for failed jobs, to understand what went wrong without filling your context windows with thousands of lines of logs
3. If you still need more information, use the `get_job_logs` or `get_workflow_run_logs` tool to get the full, detailed failure logs
4. Try to reproduce the failure yourself in your own environment.
5. Fix the failing build. If you were able to reproduce the failure yourself, make sure it is fixed before committing your changes.
```

## Adding Resources

For complex skills, add additional files to the skill directory:

**Reference Files**: Supplemental documentation (e.g., `REFERENCE.md`)

- Reference in SKILL.md to help Copilot decide if it needs to access the resource
- Loaded on-demand when skill is executed

**Scripts**: Executable code files

- Python (pandas, numpy, matplotlib)
- JavaScript/Node.js
- File editing packages
- Visualization tools

**Note**: Copilot and Claude Code can install packages from standard repositories (PyPI, npm) when loading skills. API Skills cannot install packages at runtime - all dependencies must be pre-installed in the container.

## Directory Structure Example

```
.github/skills/
├── webapp-testing/
│   ├── SKILL.md
│   ├── REFERENCE.md
│   └── scripts/
│       └── test_helper.py
└── api-integration/
    ├── SKILL.md
    └── resources/
        └── api_schema.json
```

## How Copilot Uses Skills

1. Copilot reads skill descriptions to determine when to invoke them
2. When a skill is relevant to the prompt, SKILL.md is injected into context
3. Copilot follows the instructions and can use scripts/resources in the directory
4. Multiple skills can be used together automatically

## Best Practices

### Focus

- Create separate skills for different workflows
- Multiple focused skills compose better than one large skill

### Clear Descriptions

- Be specific about when the skill applies
- Copilot uses descriptions to decide when to invoke the skill
- Include relevant keywords and triggers

### Start Simple

- Begin with basic Markdown instructions
- Add scripts later if needed
- Test after each significant change

### Use Examples

- Include example inputs and outputs
- Show what success looks like

### Composability

- Skills can't explicitly reference other skills
- But Copilot can use multiple skills together automatically
- Design each skill to do one thing well

### Follow Open Standard

- Review guidelines at agentskills.io
- Ensures skills work across platforms that adopt the standard

## Security Considerations

- Exercise caution when adding scripts
- Don't hardcode sensitive information (API keys, passwords)
- Review any downloaded skills before enabling
- Use appropriate MCP connections for external service access

## Integration with Custom Instructions

**Use custom instructions for**: Simple instructions relevant to almost every task (e.g., repository coding standards)

**Use skills for**: Detailed instructions that Copilot should access when relevant to specific tasks

Skills and custom instructions work together to teach Copilot how to work in your repository.

## Platform Availability

- GitHub Copilot Pro
- GitHub Copilot Pro+
- GitHub Copilot Business
- GitHub Copilot Enterprise

Available in:

- Copilot coding agent
- GitHub Copilot CLI (public preview with data protection)
- Agent mode in VS Code Insiders
- Stable VS Code support coming soon

## References

- Official docs: <https://docs.github.com/en/copilot/concepts/agents/about-agent-skills>
- Example skills: <https://github.com/github/awesome-copilot>
- Open standard: <https://agentskills.io>
