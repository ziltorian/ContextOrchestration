# Advanced Prompt Engineering Techniques

## Model-Specific Features

### Claude (Anthropic) - Specifics

#### Precise Instruction Following

Claude 4.x models follow instructions very precisely:

- Be as explicit as possible in your requirements
- State what to do, not only what to avoid
- The model literally interprets every instruction

**Example:**

```
Bad: "Don't use markdown"
Good: "Your response should consist of smoothly flowing prose paragraphs without markdown formatting"
```

#### XML Tags for Claude

Claude works especially well with XML:

```xml
<instructions>
  <task>Main task</task>
  <constraints>
    <constraint>Constraint 1</constraint>
    <constraint>Constraint 2</constraint>
  </constraints>
  <output_format>
    Required output format
  </output_format>
</instructions>

<examples>
  <example id="1">
    <input>Input data</input>
    <output>Expected result</output>
  </example>
</examples>
```

#### Response Prefilling

A unique Claude capability:

```python
messages = [
    {"role": "user", "content": "Write JSON with user data"},
    {"role": "assistant", "content": "{"}  # Prefilling
]
```

#### Extended Thinking (Claude Opus 4.5)

```
<thinking_guidance>
After receiving tool results, carefully analyze their quality and determine optimal next steps before continuing. Use your thinking for planning and iterating based on new information.
</thinking_guidance>
```

### GPT-4.1 (OpenAI) - Specifics

#### Agentic Workflows

GPT-4.1 is optimized for agentic tasks:

```
<persistence_reminder>
You are an agent. Continue working until the user's request is fully resolved before ending your turn. Only end your turn when you are confident the problem is solved.
</persistence_reminder>

<tool_calling_reminder>
If you are unsure about file content or codebase structure, use your tools to read files and gather information. DO NOT GUESS or make up an answer.
</tool_calling_reminder>

<planning_reminder>
You MUST plan in detail before each function call and reflect in detail on the outcomes of the previous calls. DO NOT perform the entire process solely through function calls — this may impair your ability to solve problems.
</planning_reminder>
```

#### Working with Tools

- ALWAYS use the `tools` field in the API
- Do not manually insert tool descriptions into the prompt
- Give clear names and descriptions to tools
- Use the "description" field for parameters

#### Induced Planning

```
Think carefully step by step about which documents are needed to answer the query. Then output the TITLE and ID of each document. Then format the IDs as a list.
```

#### Long Context (1M tokens)

- Place instructions at the beginning AND at the end of the context
- Use XML or a special format for documents:

  ```
  ID: 1 | TITLE: The Fox | CONTENT: The quick brown fox...
  ```

- Avoid JSON for large document collections

### General Advanced Techniques

## 1. Agentic Behavior

### State Management

```xml
<state_management>
  <current_state>
    {
      "progress": "50%",
      "completed_tasks": ["task1", "task2"],
      "next_steps": ["task3", "task4"],
      "context_summary": "Brief description of the current state"
    }
  </current_state>
</state_management>
```

### Multi-Context Workflows

1. Use different prompts for the first context window
2. Create tests in a structured format (JSON)
3. Configure auxiliary tools (initialization scripts)
4. Use Git for state tracking

### Incremental Progress

```
<incremental_work>
This is a very long task, so it helps to plan the work clearly. It is recommended to spend the entire output context working on the task — just make sure you don't run out of context with significant uncommitted work. Keep working systematically until you complete the task.
</incremental_work>
```

## 2. Tool Use Optimization

### Parallel Tool Calls

```
<parallel_tool_calls>
If you plan to call multiple tools and there are no dependencies between calls, perform all independent calls in parallel. Prioritize simultaneous tool calls wherever actions can be performed in parallel rather than sequentially.

For example, when reading 3 files, launch 3 tool calls in parallel to read all files simultaneously. Maximize the use of parallel calls to increase speed and efficiency.

However, if some calls depend on previous ones for obtaining dependent values such as parameters, DO NOT call those tools in parallel, but call them sequentially. Never use placeholders or guess missing parameters in tool calls.
</parallel_tool_calls>
```

### Verbosity Control

```
<verbosity_control>
After completing a task using tools, provide a brief summary of the work performed.
</verbosity_control>
```

## 3. Output Formatting and Style

### Minimizing Markdown

```
<avoid_excessive_markdown>
When writing reports, documents, technical explanations, analysis, or any long-form content, write in clear, flowing prose using full paragraphs and sentences. Use standard paragraph breaks for organization.

Reserve markdown primarily for:
- `inline code`
- Code blocks (```...```)
- Simple headings (###)

Avoid using **bold** and *italics*.

DO NOT use ordered lists (1. ...) or unordered lists (*) unless:
a) you are presenting truly discrete items where list format is the best option
b) the user explicitly requests a list or ranking

Instead of listing items with bullets or numbers, incorporate them naturally into sentences. NEVER output a series of unnecessarily short bullet points.
</avoid_excessive_markdown>
```

### Matching Prompt Style

Your prompt style can influence the model's response style:

- If you want prose without markdown — use prose in the prompt
- If you need code — show code examples
- The prompt format sets the tone for the output

## 4. Research and Information Gathering

### Structured Research

```
<research_strategy>
Search for this information in a structured manner:

1. Develop several competing hypotheses as you gather data
2. Track confidence levels in progress notes
3. Regularly critique your approach and plan
4. Update the hypothesis tree or research notes file
5. Break down the complex research task systematically

Make sure you verify information from multiple sources.
</research_strategy>
```

### Success Criteria

```
<success_criteria>
Research is considered successful when:
- Answers are obtained from at least 3 independent sources
- Information is consistent or contradictions are explained
- Major aspects of the question are covered
- Knowledge gaps are identified
</success_criteria>
```

## 5. Subagent Orchestration

### Natural Delegation (Claude 4.5)

```
<subagent_orchestration>
Delegate to subagents only when the task clearly benefits from a separate agent with a fresh context window.

Signs a subagent is needed:
- The task requires specialized knowledge
- A fresh context without history is needed
- Parallel processing of independent subtasks
- Isolated execution environment
</subagent_orchestration>
```

## 6. Working with Images and Multimodal

### Crop Tool for Improved Vision

```
<vision_optimization>
When analyzing images with fine details:
1. Use the crop tool to enlarge areas of interest
2. Analyze image sections separately
3. Synthesize results from all regions
4. Verify findings on the full image
</vision_optimization>
```

### Video Processing

```
For video analysis:
1. Break the video into key frames (every N seconds)
2. Analyze each frame separately
3. Track changes between frames
4. Compose a temporal sequence of events
```

## 7. Minimizing Hallucinations

### Verification Before Answering

```
<investigation_before_answering>
Never make assumptions about code you haven't opened. If the user refers to a specific file, you MUST read the file before answering.

Make sure you explore and read relevant files BEFORE answering questions about the codebase. Never make claims about code before investigation, unless you are confident in the correct answer — provide well-founded answers without hallucinations.
</investigation_before_answering>
```

## 8. Frontend and UI Design

### Avoiding "AI Slop" Aesthetics

```
<frontend_aesthetics>
You tend to produce generic output. In frontend design, this creates what users call "AI slop" aesthetics. Avoid this: create creative, distinctive interfaces that surprise and delight.

Focus on:
- **Typography**: Choose beautiful, unique, interesting fonts. Avoid generic fonts like Arial and Inter; choose distinctive options.
- **Color and Theme**: Stick to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly distributed palettes.
- **Motion**: Use animations for effects and micro-interactions. CSS-only solutions for HTML. Motion library for React.
- **Backgrounds**: Create atmosphere and depth instead of solid colors. Layer CSS gradients, geometric patterns, contextual effects.

Avoid:
- Overused fonts (Inter, Roboto, Arial)
- Cliché color schemes (especially purple gradients)
- Predictable layouts and components
- Design without character

Interpret creatively and make unexpected choices. Vary between light and dark themes, different fonts, different aesthetics.
</frontend_aesthetics>
```

## 9. Code Quality

### Avoiding Over-Engineering (Claude Opus 4.5)

```
<avoid_overengineering>
Avoid excessive engineering. Only make requested or clearly necessary changes. Keep solutions simple and focused.

DO NOT add features, refactor code, or make "improvements" beyond what was requested. Fixing a bug does not require cleaning up surrounding code. A simple function does not need additional configurability.

DO NOT add error handling, fallbacks, or validation for scenarios that cannot happen. Trust internal code and framework guarantees. Validate only at system boundaries.

DO NOT create helpers, utilities, or abstractions for one-time operations. DO NOT design for hypothetical future requirements.

The right amount of complexity is the minimum needed for the current task.
</avoid_overengineering>
```

### General Solution vs Hardcoding

```
<general_solutions>
Write high-quality, universal solutions using standard available tools. DO NOT create helper scripts or workarounds.

Implement a solution that works correctly for all valid inputs, not just test cases. DO NOT hardcode values or create solutions that only work for specific test inputs.

Focus on understanding the problem requirements and implementing the correct algorithm. Tests exist for verifying correctness, not for defining the solution.

If the task is infeasible or the tests are incorrect, inform me instead of working around it. The solution should be robust, maintainable, and extensible.
</general_solutions>
```

## 10. Behavior Control

### Proactiveness vs Conservatism

```
<!-- For proactive action -->
<default_to_action>
By default, implement changes rather than only suggesting them. If the user's intent is unclear, infer the most useful likely action and proceed, using tools to discover missing details instead of guessing.
</default_to_action>

<!-- For conservative approach -->
<do_not_act_before_instructions>
DO NOT proceed to implementation or file modification unless explicitly instructed to make changes. When the user's intent is ambiguous, default to providing information, conducting research, and giving recommendations instead of taking action.
</do_not_act_before_instructions>
```

## 11. Special Model Capabilities

### Model Self-Identification

```
<model_identity>
The assistant is Claude, made by Anthropic. The current model is Claude Sonnet 4.5.

When an LLM is needed, default to Claude Sonnet 4.5 unless the user requests otherwise. The exact model string for Claude Sonnet 4.5: claude-sonnet-4-5-20250929
</model_identity>
```

### Sensitivity to "thinking" (Claude Opus 4.5)

```
<!-- Avoid the word "think" when extended thinking is disabled -->
Instead of "think" use: consider, believe, evaluate, analyze, determine
```

---

## 12. Architectural Frameworks

Before writing a prompt, choose a structure by task type.
Full description with examples — in [prompt_frameworks.md](prompt_frameworks.md).

| Task | Framework |
|------|-----------|
| Simple generation | **RTF** — Role · Task · Format |
| Content with audience and tone | **CO-STAR** |
| Multi-step task | **RISEN** |
| Full agent system prompt | **CRISPE** |
| Agent with tools / search | **ReAct** |

---

## 13. PAC2026: Positioning in Long Prompts

For prompts longer than 1000 tokens, use the **30 / 55 / 15** distribution:

```
[BEGINNING 30%]   Role, critical instructions, key constraints
[MIDDLE 55%]      Context, data, documents, examples
[END 15%]         Repeat critical instructions + final task
```

Any instruction whose violation is unacceptable should be duplicated at the beginning and at the end.
Place examples closer to the end of the middle (~70% from the start of the prompt).

Memory Block for preserving context between iterations — in [prompt_frameworks.md](prompt_frameworks.md).