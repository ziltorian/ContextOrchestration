# Platform-Specific Prompt Techniques

Optimizations and best practices for different AI platforms.

## Claude (Anthropic)

### Model Characteristics

**Claude 4.x models** (Sonnet 4, Opus 4.5):

- Extremely precise instruction following
- Excellent with XML structure
- Supports extended thinking mode
- Response prefilling capability

### XML Structure (Preferred for Claude)

Claude works exceptionally well with XML tags:

```xml
<instructions>
  <task>Primary task description</task>
  
  <constraints>
    <constraint>Don't use markdown lists</constraint>
    <constraint>Keep responses under 500 words</constraint>
  </constraints>
  
  <output_format>
    Return as JSON with fields: result, confidence, reasoning
  </output_format>
</instructions>

<examples>
  <example id="1">
    <input>User query here</input>
    <output>Expected response here</output>
  </example>
</examples>
```

**Why XML works better for Claude:**

- Clear hierarchy and nesting
- Explicit boundaries between sections
- Less ambiguity in complex instructions
- Easier to parse and follow

### Prefilling Response (Unique to Claude)

Start assistant's response to guide output format:

```python
messages = [
    {"role": "user", "content": "Generate JSON with user data"},
    {"role": "assistant", "content": "{"}  # Prefill
]
```

**Use cases:**

- Force JSON output format
- Skip pleasantries ("Sure, I'll help you...")
- Start with specific structure

**Example:**

```python
# Force function call format
{"role": "assistant", "content": "Let me call the"}  # Will complete with tool call
```

### Extended Thinking Mode (Opus 4.5)

Enable deep reasoning for complex tasks:

```xml
<thinking_guidance>
After receiving tool results, carefully analyze their quality and determine 
optimal next steps before proceeding. Use your thinking to plan and iterate 
based on new information.
</thinking_guidance>
```

**When to use:**

- Complex multi-step problems
- Tasks requiring planning
- Code architecture decisions
- Debugging complex issues

**Budget thinking tokens:**

```xml
<thinking_budget>
You have 10,000 tokens for thinking. Use them wisely for planning and analysis.
</thinking_budget>
```

### Claude-Specific Best Practices

**Be extremely explicit:**

```
❌ Don't use markdown
✅ Your response must consist of smoothly flowing prose paragraphs 
   without any markdown formatting whatsoever
```

**Structure complex instructions:**

```xml
<coding_standards>
  <must_do>
    <item>Use type hints for all parameters</item>
    <item>Write docstrings for public functions</item>
  </must_do>
  
  <must_not_do>
    <item>Use mutable default arguments</item>
    <item>Catch bare exceptions</item>
  </must_not_do>
</coding_standards>
```

**Provide context boundaries:**

```xml
<context>
  <project_type>Python backend API</project_type>
  <framework>FastAPI</framework>
  <database>PostgreSQL with SQLAlchemy</database>
</context>
```

## GPT-4.1 (OpenAI)

### Model Characteristics

**GPT-4.1 optimizations:**

- Enhanced agentic workflows
- Better tool use and planning
- Improved multi-turn conversations
- Extended context (1M tokens)

### Agentic Behaviors

**Persistence reminder:**

```xml
<persistence_reminder>
You are an agent. Continue working until fully resolving the user's request 
before ending your turn. Only conclude when certain the problem is solved.
</persistence_reminder>
```

**Tool calling reminder:**

```xml
<tool_calling_reminder>
If you're unsure about file contents or codebase structure, use your tools 
to read files and gather information. DO NOT GUESS or make up answers.
</tool_calling_reminder>
```

**Planning emphasis:**

```xml
<planning_reminder>
You MUST plan extensively before each function call and think deeply about 
results of previous calls. DO NOT perform the entire process only through 
function calls - this can degrade your problem-solving ability.
</planning_reminder>
```

### Tool Use Best Practices

**Always use tools field in API:**

```python
completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=messages,
    tools=[{
        "type": "function",
        "function": {
            "name": "search_code",
            "description": "Search codebase for specific patterns",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query"},
                    "file_pattern": {"type": "string", "description": "File glob pattern"}
                },
                "required": ["query"]
            }
        }
    }]
)
```

**Induce planning before tool calls:**

```
Think carefully step-by-step about which documents are needed to answer 
the query. Then output the NAME and ID of each document. Then format the 
IDs as a list.
```

### Long Context Optimization (1M tokens)

**For large document collections:**

- Place instructions at start AND end of context
- Use structured document format:
  ```
  ID: 1 | TITLE: The Fox | CONTENT: The quick brown fox...
  ID: 2 | TITLE: Data | CONTENT: Analysis shows...
  ```
- Avoid JSON for large collections (harder to parse)
- Use XML or pipe-delimited format

**Instruction placement:**

```xml
<!-- At start of context -->
<instructions>
  [Your instructions here]
</instructions>

<!-- Large document collection here -->

<!-- Repeat at end -->
<instructions>
  [Same instructions repeated]
</instructions>
```

### GPT-4.1 Specific Patterns

**Structured output:**

```python
completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=messages,
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "code_analysis",
            "schema": {
                "type": "object",
                "properties": {
                    "issues": {"type": "array"},
                    "complexity": {"type": "number"}
                }
            }
        }
    }
)
```

**Parallel tool calls:**

```xml
<parallel_tool_calls>
When planning to call multiple tools with no dependencies between them, 
make all independent calls in parallel. For example, if reading 3 files, 
make 3 parallel read calls to fetch all simultaneously.

However, if calls depend on previous results, call them sequentially. 
Never use placeholders or guess missing parameters.
</parallel_tool_calls>
```

## GitHub Copilot / Cursor / Windsurf

### Workspace Context

These tools have automatic workspace context. Leverage it:

**Reference workspace files:**

```markdown
Follow coding standards defined in [.github/instructions/Python_Standards.instructions.md]

Use design patterns from [src/utils/patterns.py]
```

**Use workspace-aware prompts:**

```markdown
Analyze the architecture in this workspace and identify:
1. Main entry points
2. Core modules and their responsibilities
3. External dependencies
```

### Instruction Files (.instructions.md)

**Auto-applied instructions:**

```markdown
---
applyTo: "**/*.py"
name: "Python_Standards"
description: "Python coding standards"
---

## Code Style
- Use type hints
- Follow PEP 8
- Write docstrings
```

**Trigger:** Automatically when editing matching files

### Prompt Files (.prompt.md)

**On-demand prompts:**

```markdown
---
name: create-test
description: "Generate test suite"
argument-hint: "module name"
---

Generate comprehensive tests for ${input:moduleName}:

1. Analyze module structure
2. Create test cases
3. Mock dependencies
4. Aim for 80% coverage
```

**Trigger:** Type `/create-test` in chat

### Platform-Specific Features

**Copilot inline suggestions:**

```typescript
// Type comment to guide inline generation
// Create a function that validates email addresses using regex
function validateEmail
```

**Cursor composition:**

```markdown
@workspace Create a new API endpoint for user registration following 
existing patterns in @api/auth.py
```

**Windsurf cascade:**

```markdown
/cascade Create authentication system:
1. Database models
2. API endpoints
3. Frontend forms
4. Tests
```

## Ollama / Local Models

### Model Limitations

**Be aware of:**

- Smaller context windows (4k-32k)
- Less precise instruction following
- May need more examples
- Simpler prompt structures work better

### Optimization Strategies

**Use simpler structures:**

```markdown
# Task
Generate Python function for data validation

# Requirements
- Check for null values
- Validate types
- Return error list

# Example
Input: {"name": null, "age": "invalid"}
Output: ["name is null", "age must be integer"]
```

**Provide more examples:**

```markdown
# Examples

Example 1:
Input: "hello world"
Output: "HELLO WORLD"

Example 2:
Input: "Python Programming"
Output: "PYTHON PROGRAMMING"

Example 3:
Input: "123 test"
Output: "123 TEST"

Now process: "${user_input}"
```

**Break down complex tasks:**

```markdown
Step 1: Extract function names from code
Step 2: For each function, extract parameters
Step 3: For each function, extract return type
Step 4: Format as JSON

After each step, show your work before proceeding.
```

### Model Selection

**For coding tasks:**

- **Qwen2.5-Coder** (3B-32B): Best for code generation
- **DeepSeek-Coder** (6.7B-33B): Strong code understanding
- **CodeLlama** (7B-34B): Good for completion

**For general tasks:**

- **Llama 3.1** (8B-70B): General purpose
- **Mistral** (7B-22B): Fast inference
- **Phi-3** (3.8B-14B): Efficient, good quality

## Summary Table

| Platform | Best Structure | Key Feature | Context Size |
|----------|---------------|-------------|--------------|
| **Claude** | XML tags | Prefilling, extended thinking | 200k tokens |
| **GPT-4.1** | Markdown/XML | Agentic workflows, long context | 1M tokens |
| **Copilot** | Markdown | Workspace context, instruction files | 128k tokens |
| **Local** | Simple markdown | Fast, private, offline | 4k-32k tokens |

## Platform Migration

### Claude → GPT-4

**Changes needed:**

- Keep XML if complex, can simplify to markdown
- Remove prefilling (not supported)
- Add explicit planning reminders
- Adjust for longer context if needed

### GPT-4 → Claude

**Changes needed:**

- Can add XML structure for clarity
- Add prefilling for format control
- Can use extended thinking for complex tasks
- More explicit instructions

### Cloud → Local

**Changes needed:**

- Simplify structure (more markdown, less XML)
- Add more examples (3-5 instead of 1-2)
- Break complex tasks into steps
- Reduce context usage
- More explicit instructions

### Local → Cloud

**Changes needed:**

- Can use more complex structures
- Fewer examples needed (1-2 sufficient)
- Can combine multiple steps
- Leverage longer context
- Can be more concise
