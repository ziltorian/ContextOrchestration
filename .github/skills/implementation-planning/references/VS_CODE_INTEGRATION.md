# VS Code Integration Guide

How to integrate the Implementation Planning skill with VS Code custom agents and GitHub Copilot.

## Overview

This skill is designed to work seamlessly with VS Code's custom agent feature, allowing you to create specialized Planning and Implementation agents that follow the two-phase workflow.

## Prerequisites

- **VS Code** version 1.95 or later
- **GitHub Copilot** extension
- **GitHub Copilot Chat** extension
- Custom agents feature enabled (may require Copilot Labs or preview features)

## Setup Instructions

### Step 1: Create Agent Definitions

Create two custom agent files in your workspace:

**File: `.github/agents/planning-agent.agent.md`**

```markdown
---
name: 'Planning Agent'
description: 'Researches and develops multi-step implementation plans'
argument-hint: 'Describe the goal or problem to research and plan'
tools: ['read/*', 'search', 'agent', 'edit/createDirectory', 'edit/createFile', 'edit/editFiles']
handoffs:
  - label: Start Implementation
    agent: implementation-agent
    prompt: Begin implementation following `*-implementation.instructions.md`
---

You are a Planning Agent operating in planning mode.

Your goal is to:
1. Research the codebase thoroughly
2. Design a comprehensive solution
3. Create detailed implementation instructions
4. Present the plan for user review

Load the implementation-planning skill for detailed workflow guidance.

## Workflow

1. Gather context using read-only tools
2. Create `*-implementation.instructions.md` file in `.github/implementations/`
3. Present plan to user for review
4. Iterate based on feedback
5. Hand off to Implementation Agent when approved

## Restrictions

- NEVER modify production code
- ONLY create/edit files in `.github/implementations/`
- Stay in planning mode until plan is approved
```

**File: `.github/agents/implementation-agent.agent.md`**

```markdown
---
name: 'Implementation Agent'
description: 'Executes approved implementation plans'
argument-hint: 'Specify which implementation plan to execute'
tools: ['execute/*', 'read/*', 'edit/*', 'search', 'web']
---

You are an Implementation Agent operating in implementation mode.

Your goal is to:
1. Load the approved implementation plan
2. Execute tasks sequentially
3. Update task status in real-time
4. Verify changes and document results

Load the implementation-planning skill for detailed workflow guidance.

## Workflow

1. Locate `*-implementation.instructions.md` file
2. Execute tasks one by one from the Task section
3. Update task status: `[ ]` → `[/]` → `[x]`
4. Run verification tests
5. Document changes made

## Task Status Markers

- `[ ]` - Not started
- `[/]` - In progress (use when investigating blockers)
- `[x]` - Completed

When encountering blockers:
1. Mark task `[/]`
2. Investigate the issue
3. Update implementation file with findings
4. Report progress to user
```

### Step 2: Enable Custom Agents

1. Open VS Code Settings (`Cmd/Ctrl + ,`)
2. Search for "GitHub Copilot Agent"
3. Enable custom agents feature (if available)
4. Reload VS Code

### Step 3: Use the Agents

**To start planning:**
```
@planning-agent Design a solution for [feature/bug description]
```

**To execute implementation:**
```
@implementation-agent Start implementation following pagination_fix-implementation.instructions.md
```

## Agent Handoff Workflow

The two agents work together through handoffs:

```
User Request
    ↓
Planning Agent
    ├→ Research codebase
    ├→ Design solution
    ├→ Create implementation.instructions.md
    ├→ Present to user
    └→ [User approves]
        ↓
    Hand off to Implementation Agent
        ├→ Load implementation plan
        ├→ Execute tasks
        ├→ Update status
        ├→ Verify changes
        └→ Report completion
```

## File Organization

Recommended workspace structure:

```
project-root/
├── .github/
│   ├── agents/
│   │   ├── planning-agent.agent.md
│   │   └── implementation-agent.agent.md
│   ├── implementations/
│   │   ├── implementation.instructions.md
│   │   ├── feature_x-implementation.instructions.md
│   │   └── bugfix_y-implementation.instructions.md
│   └── instructions/
│       └── project-standards.instructions.md
├── src/
└── tests/
```

## Skill Loading

Both agents should reference the implementation-planning skill:

**Option 1: Auto-load via skill directory**

Place this skill in `.github/skills/implementation-planning/` and it will be auto-discovered.

**Option 2: Explicit reference in agent definition**

```markdown
Load and follow the implementation-planning skill workflow.

Key references:
- Main workflow: implementation-planning skill SKILL.md
- YAML format: references/YAML_FRONTMATTER.md
- Examples: references/EXAMPLES.md
```

## Custom Instructions Integration

You can combine custom instructions with the agent workflow:

**File: `.github/instructions/planning-standards.instructions.md`**

```markdown
---
name: Planning Standards
description: Standards for creating implementation plans
applyTo: ".github/implementations/**"
---

## Planning Standards

When creating implementation plans:

1. **Research First**: Gather 80% context confidence before planning
2. **Be Specific**: Include file names and line numbers
3. **Atomic Tasks**: Each task is a single, clear action
4. **No Duplicates**: Each task appears once with unique ID
5. **Verify**: Always include verification steps
```

This instruction file will automatically apply when the Planning Agent creates or edits implementation files.

## Task Tracking

VS Code can display task status from markdown files. Configure task providers:

**File: `.vscode/tasks.json`**

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Implementation Status",
      "type": "shell",
      "command": "echo",
      "args": ["Checking implementation tasks..."],
      "problemMatcher": [],
      "presentation": {
        "reveal": "always",
        "panel": "new"
      }
    }
  ]
}
```

## Debugging Agent Behavior

### Enable Chat Debug View

1. Open Command Palette (`Cmd/Ctrl + Shift + P`)
2. Run "GitHub Copilot: Show Chat Debug View"
3. Monitor agent tool calls and context

### Check Agent Context

View what files and instructions the agent is using:

1. In Copilot Chat, click the context icon
2. Review attached files and instructions
3. Verify implementation plan is loaded

### Common Issues

**Agent doesn't load skill:**
- Ensure skill is in `.github/skills/` directory
- Check skill `description` field for proper triggers
- Verify agent has `read` tool access

**Agent modifies wrong files:**
- Check `applyTo` pattern in YAML frontmatter
- Ensure agent references correct implementation file
- Review agent's tool permissions

**Tasks not updating:**
- Verify agent has `edit` permission for implementation files
- Check file path in agent invocation
- Ensure markdown checkbox syntax is correct

## Advanced Configuration

### Multiple Planning Agents

Create specialized planning agents for different domains:

```
.github/agents/
├── planning-agent-backend.agent.md    # Backend planning
├── planning-agent-frontend.agent.md   # Frontend planning
└── planning-agent-infra.agent.md      # Infrastructure planning
```

Each can reference the same skill but with different context and tools.

### Automated Plan Review

Create a review workflow:

**File: `.github/workflows/review-implementation-plan.yml`**

```yaml
name: Review Implementation Plan

on:
  push:
    paths:
      - '.github/implementations/**'

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Check Plan Format
        run: |
          for file in .github/implementations/*.md; do
            echo "Checking $file"
            # Add validation logic
          done
```

### Custom Skill Variants

Create project-specific variations:

**File: `.github/skills/planning-custom/SKILL.md`**

```markdown
---
name: planning-custom
description: Custom implementation planning for [Project Name]
---

# Custom Planning Workflow

Extends implementation-planning skill with project-specific requirements:

1. Include security review checklist
2. Require architecture diagram for new features
3. Mandate performance impact analysis

[Rest of customization]
```

## Best Practices

### Planning Agent Best Practices

1. **Always research first** - Don't skip context gathering
2. **Use clear file names** - Name implementation files after module/feature
3. **Keep plans focused** - One plan per module or feature
4. **Present for review** - Always get user approval before handoff

### Implementation Agent Best Practices

1. **Follow the plan** - Don't deviate without updating plan first
2. **Update status** - Mark tasks `[/]` and `[x]` in real-time
3. **Report blockers** - Flag issues immediately
4. **Run tests** - Execute verification before marking complete

### User Best Practices

1. **Review plans carefully** - Check for missing context or edge cases
2. **Provide feedback** - Help refine plans before implementation
3. **Monitor progress** - Watch task status during implementation
4. **Test thoroughly** - Verify results after implementation

## Troubleshooting

### Planning Agent Issues

**Problem:** Agent starts writing code during planning

**Solution:**
- Add explicit "NEVER modify production code" to agent definition
- Reinforce planning mode in custom instructions
- Review agent's tool permissions (should not have execute/edit for src/)

**Problem:** Plans are too vague

**Solution:**
- Add examples to custom instructions
- Reference good plan examples from skill
- Request more specific task breakdowns

### Implementation Agent Issues

**Problem:** Agent doesn't update task status

**Solution:**
- Verify agent has edit permission for `.github/implementations/`
- Check markdown syntax for checkboxes
- Ensure agent references correct implementation file

**Problem:** Agent deviates from plan

**Solution:**
- Strengthen "follow the plan" instruction
- Add verification step to check plan before each task
- Create stricter custom instructions

## Examples

See `references/EXAMPLES.md` for complete examples of:
- Agent definition files
- Implementation instruction files
- Custom instruction files
- Workflow scenarios

## Resources

- [VS Code Custom Agents Documentation](https://code.visualstudio.com/docs/copilot/customization/custom-agents)
- [GitHub Copilot Skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [Custom Instructions Guide](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
- [Agent Skills Specification](https://agentskills.io)

## Summary

This skill integrates with VS Code through:

1. **Custom agent definitions** - Separate planning and implementation agents
2. **Skill auto-discovery** - Place in `.github/skills/` directory
3. **Custom instructions** - Combine with project-specific guidelines
4. **Task tracking** - Markdown checkboxes tracked in VS Code
5. **Agent handoffs** - Smooth transition from planning to implementation

The two-agent approach ensures separation of concerns: planning focuses on design, implementation focuses on execution.
