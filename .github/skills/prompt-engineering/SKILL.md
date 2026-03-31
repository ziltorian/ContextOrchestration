---
name: prompt-engineering
description: Guide for creating effective prompts for AI assistants (Claude, GPT-4, GitHub Copilot, Cursor, Windsurf, Aider, and others). Use this skill whenever the user wants to create, improve, debug, or optimize any kind of prompt or system prompt — including agent instructions, instruction files (.instructions.md, SKILL.md), persona definitions, tool-use prompts, or multi-turn conversation starters. Also trigger when the user says "prompt", "system prompt", "instructions for AI", "make Claude do X", or asks why their AI isn't behaving as expected. When in doubt, load this skill — it covers fundamentals, named frameworks, platform specifics, templates, and production best practices.
compatibility: Claude, GPT-4, GitHub Copilot, Cursor, Windsurf, Aider
metadata:
  version: "1.1"
  category: ai-assistant-configuration
  author: ziltorian
---

# Prompt Engineering Guide

Create effective prompts for AI coding assistants across multiple platforms (Claude, GPT-4, GitHub Copilot, Cursor, Windsurf).

## Overview

Master prompt engineering fundamentals, advanced techniques, platform-specific optimizations, and proven templates. Learn to craft prompts that elicit accurate, relevant, and high-quality code and responses.

## When to Use This Skill

- Creating/updating system prompts for AI agents
- Improving prompts producing inconsistent results
- Designing instruction files (.instructions.md, SKILL.md)
- Optimizing agent behavior for specific tasks
- Debugging problematic prompts
- Migrating prompts between platforms

## Before You Write: 9-Dimension Analysis

Before writing any prompt, silently extract these 9 dimensions from the request:

| # | Dimension | Question |
|---|-----------|---------|
| 1 | **Task** | What exactly should the model do? (verb + object) |
| 2 | **Input** | What data/context will the model receive? |
| 3 | **Output** | What should the result look like? (format, length, structure) |
| 4 | **Constraints** | What is forbidden or must be avoided? |
| 5 | **Context** | What background does the model need? |
| 6 | **Audience** | Who will consume the output? |
| 7 | **Memory** | Is there session history that must be preserved? |
| 8 | **Success criteria** | How do we know the prompt worked? |
| 9 | **Examples** | Are there samples of desired input/output? |

Missing dimensions → add reasonable defaults or ask the user before writing.

## Framework Selector

Choose the architecture before writing. See [prompt frameworks](references/prompt_frameworks.md) for full reference.

| Task type | Framework |
|-----------|-----------|
| Simple generation / single instruction | **RTF** (Role · Task · Format) |
| Content with audience and tone | **CO-STAR** |
| Complex multi-step task | **RISEN** |
| Full agent system prompt | **CRISPE** |
| Agent with tools / search | **ReAct** |

## Core Principles

### 1. Clarity and Specificity

Be explicit and unambiguous:

**Poor:**
```
Do something with this text
```

**Good:**
```
Extract all dates, names, and organizations from this text.
Return as JSON with fields: dates[], names[], organizations[]
```

**Rules:**
- Use concrete examples
- Define exact success criteria
- Avoid ambiguity
- Specify output format precisely

### 2. Recommend Structure

```xml
<role>AI role and primary task</role>

<context>Necessary background information</context>

<instructions>
Step-by-step guidelines
1. First step
2. Second step
</instructions>

<output_format>Precise format description</output_format>

<examples>
<example id="1">
<input>Sample input</input>
<output>Expected output</output>
</example>
</examples>

<constraints>Task boundaries and what NOT to do</constraints>
```

### 3. Effective Delimiters

**Markdown** (simple prompts):
```markdown
# Main Instructions
## Section 1
- Point A
- Point B
```

**XML** (complex structures):
```xml
<instructions>
  <task>Main task</task>
  <constraints>
    <constraint>Limitation 1</constraint>
  </constraints>
</instructions>
```

See [prompt engineering fundamentals](references/prompt_engineering_fundamentals.md) for comprehensive theory.

## Core Techniques

### Chain of Thought (CoT)

Encourage step-by-step reasoning:

```
Solve step by step:
1. Analyze input data
2. Identify patterns
3. Formulate hypothesis
4. Test with examples
5. Provide final answer with justification
```

**Use for:** Complex problems, multi-step analysis, debugging, architecture decisions

### Few-Shot Learning

Provide 2-5 examples:

```xml
<examples>
<example id="1">
Input: "Buy iPhone 13"
Output: {"intent": "purchase", "product": "iPhone 13"}
</example>

<example id="2">
Input: "This phone is terrible!"
Output: {"intent": "complaint", "product": "unknown"}
</example>
</examples>

Now process: "Looking for good smartphone under $500"
```

**Use for:** Specific output formats, pattern learning, classification

### Self-Consistency

For critical tasks:

```
Solve using three different methods.
Compare results and choose the most justified answer.
Explain your selection.
```

**Use for:** High-stakes decisions, complex calculations, architecture validation

See [advanced techniques](references/advanced_prompting_techniques.md) for more methods.

## Platform-Specific Notes

- **Claude:** Excels with XML structure, supports prefilling, extended thinking
- **GPT-4.1:** Optimized for agentic workflows, long context (1M tokens), tool use
- **Copilot/Cursor:** Workspace-aware, instruction files, inline suggestions
- **Local models:** Simpler structures, more examples, shorter context

See [platform-specific techniques](references/platform_specific_techniques.md) for detailed optimizations.

## Quick Reference

### Prompt Creation Workflow

1. Define goal clearly
2. Choose structure (markdown/XML)
3. Add examples (1-5)
4. Specify output format
5. Add constraints
6. Test and iterate

### Common Mistakes

- Ambiguous instructions
- Missing output format specification
- Too few/many examples
- Ignoring platform differences
- No constraints specified

### Prompt Length Guidelines

- **Simple tasks:** 100-500 tokens
- **Complex tasks:** 500-2000 tokens  
- **System prompts:** 1000-5000 tokens
- **Max recommended:** 8000 tokens

## Examples Repository

See [comprehensive examples](references/comprehensive_examples.md) for:
- System prompts for agents
- Code generation prompts
- Code review prompts
- Testing prompts
- Documentation prompts
- Refactoring prompts

See [prompt templates](references/prompt_templates.md) for ready-to-use templates.

## Further Reading

- [Prompt Frameworks](references/prompt_frameworks.md) - Named frameworks (RTF, CO-STAR, RISEN, CRISPE, ReAct), Memory Block, PAC2026 positional structure
- [Prompt Engineering Fundamentals](references/prompt_engineering_fundamentals.md) - Theory and principles
- [Advanced Prompting Techniques](references/advanced_prompting_techniques.md) - Expert methods
- [Platform-Specific Techniques](references/platform_specific_techniques.md) - Claude, GPT-4, Copilot optimizations
- [Practical Guidelines](references/practical_guidelines.md) - Real-world best practices
- [Comprehensive Examples](references/comprehensive_examples.md) - Copy-paste ready prompts
- [Prompt Templates](references/prompt_templates.md) - Reusable templates