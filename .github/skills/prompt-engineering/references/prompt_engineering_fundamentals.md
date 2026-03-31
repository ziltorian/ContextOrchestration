# Prompt Engineering Fundamentals

## Preliminary Analysis: 9 Dimensions of a Prompt

Before writing a prompt, define all 9 dimensions of the task. This takes 30 seconds
and eliminates most causes of non-working prompts.

| # | Dimension | What We Define |
|---|-----------|----------------|
| 1 | **Task** | What does the model do? (verb + object) |
| 2 | **Input** | What data/context does it receive? |
| 3 | **Output** | What does the result look like? (format, length, structure) |
| 4 | **Constraints** | What is forbidden or undesirable? |
| 5 | **Context** | What background context does the model need? |
| 6 | **Audience** | Who consumes the result and what is their level? |
| 7 | **Memory** | Is there session history that needs to be preserved? |
| 8 | **Success** | How to tell if the prompt worked? |
| 9 | **Examples** | Are there examples of desired input/output? |

If a dimension is undefined → add a reasonable default or ask a clarifying question.

---

## Key Principles of Prompt Creation

### 1. Clarity and Specificity

- Formulate instructions clearly and unambiguously
- Avoid ambiguity in wording
- Use specific examples instead of abstract descriptions
- Define exact success criteria for the task

**Bad:** "Do something with this text"
**Good:** "Analyze this text and extract all mentions of dates, names, and organizations. Present the result in JSON format"

### 2. Prompt Structure

Recommended structure:

```
# Role and Purpose
Define the AI role and main task

# Context
Provide necessary background information

# Instructions
Step-by-step directions for task execution

# Output Format
Exact description of the desired result format

# Examples
Specific examples of input data and expected output

# Constraints
What NOT to do, task boundaries
```

### 3. Using Delimiters

Effective types of delimiters:

**Markdown** (recommended for starters):

- Headers: #, ##, ###
- Code: `inline` or ```blocks```
- Lists: ordered and unordered

**XML tags** (excellent for complex structures):

```xml
<context>
  <background>...</background>
  <requirements>...</requirements>
</context>

<examples>
  <example id="1">
    <input>...</input>
    <output>...</output>
  </example>
</examples>
```

**JSON** (for structured data):

- Well understood in code context
- Requires character escaping
- Can be verbose

### 4. Quality Improvement Techniques

#### Chain of Thought (CoT)

Encourage the model to think step by step:

```
Solve this task step by step:
1. First, analyze the source data
2. Identify key patterns
3. Formulate a hypothesis
4. Verify the hypothesis with examples
5. Formulate the final answer
```

#### Few-Shot Learning

Provide 2-5 examples of desired behavior:

```
<examples>
Example 1:
Input: "I want to buy iPhone 13"
Output: {"intent": "purchase", "product": "iPhone 13", "sentiment": "neutral"}

Example 2:
Input: "This phone is terrible!"
Output: {"intent": "complaint", "product": "unknown", "sentiment": "negative"}
</examples>

Now process: "Looking for a good smartphone under $500"
```

#### Self-Consistency

For critically important tasks:

```
Solve this task in three different ways.
Then compare the results and choose the most substantiated answer.
```

### 5. Managing Long Context

For large volumes of data:

- Place instructions at the beginning AND at the end of the context
- Use structured formats (XML, tables)
- Explicitly point to important parts of the context
- Use intermediate summaries for long documents

### 6. Defining a Role (System Prompts)

Effective system prompts include:

```
You are a [specific role] with [specific skills].

Your task: [clear description of the main goal]

Characteristics of your work:
- [key trait 1]
- [key trait 2]
- [key trait 3]

You must always:
- [required behavior 1]
- [required behavior 2]

You must never:
- [forbidden behavior 1]
- [forbidden behavior 2]
```

### 7. Output Formatting

**For structured data:**

```
Return the result ONLY in JSON format without additional text:
{
  "field1": "value",
  "field2": ["item1", "item2"]
}
```

**For text responses:**

```
Response structure:
1. Brief summary (2-3 sentences)
2. Detailed analysis (3-5 paragraphs)
3. Recommendations (bulleted list)
4. Conclusion (1 paragraph)
```

### 8. Iterative Development

Prompt optimization process:

1. Start with a basic version
2. Test on diverse examples
3. Identify error patterns
4. Refine instructions for problematic cases
5. Add examples for edge cases
6. Repeat the process

### 9. Specific Techniques

#### Prefilling (for Claude)

Start the model's response in the desired way:

```
User: Write a short story
Assistant: Of course! Here's a story:

Title:
```

#### Zero-Shot vs Few-Shot

- **Zero-Shot**: For simple, straightforward tasks
- **Few-Shot**: For complex patterns or specific formats

#### Temperature and Parameters

- **Creative tasks**: temperature 0.7-1.0
- **Analytical tasks**: temperature 0.0-0.3
- **Code**: temperature 0.0-0.2

### 10. Anti-patterns (What to Avoid)

- Too general instructions
- Contradictory requirements
- Examples that don't match instructions
- Excessive use of CAPS or emoji
- Assumptions about model knowledge
- Unclear success criteria

### 11. Prompt Quality Check

A good prompt should:

- Be understandable to a person without context
- Produce consistent results
- Contain measurable success criteria
- Include examples for complex cases
- Explicitly define the output format
- Account for edge cases

### 12. Testing Prompts

Create a set of test cases:

- Typical examples (70%)
- Edge cases (20%)
- Potentially problematic inputs (10%)

Evaluation metrics:

- Answer accuracy
- Format consistency
- Execution time
- Cost (tokens)

---

## Patterns That Kill Prompt Quality (Credit-Killing Patterns)

These constructs silently degrade results and waste tokens.
When found in a prompt — fix without comments.

### Group 1: Vague Instructions

| Anti-pattern | Why It's Bad | Replacement |
|-------------|-------------|-------------|
| "Try to be accurate" | No accuracy criterion | "Use only data from the provided context" |
| "Respond well and in detail" | Ambiguous | "Response: 3-5 paragraphs, each — one thesis + justification" |
| "Be a smart assistant" | Empty instruction | Remove, replace with a role |
| "As best as possible..." | No operational meaning | Formulate a specific criterion |

### Group 2: Redundancy

| Anti-pattern | Why It's Bad |
|-------------|-------------|
| Same rule repeated 3+ times | Pollutes context, doesn't strengthen adherence |
| Instructions contradicting examples | Model follows examples, ignoring text |
| "Absolutely make sure you definitely..." | Intensifiers don't affect behavior |
| Explaining the obvious ("you are an AI") | Wastes tokens without benefit |

### Group 3: Dangerous Formulations

| Anti-pattern | Problem | Replacement |
|-------------|---------|-------------|
| "Don't use markdown" | Negative instruction is weaker than positive | "Write in smooth prose without formatting" |
| "Try not to do X" | "Try" leaves a loophole | "Never do X" |
| Mixing languages in instructions | Reduces adherence accuracy | Everything in one language |
| Nested conditions deeper than 2 levels | Model loses branches | Split into separate rules |

### Group 4: Structural Errors

| Anti-pattern | Problem |
|-------------|---------|
| Critical instructions in the middle of a long prompt | Attention decay — see PAC2026 |
| Examples contradict instructions | Model prioritizes examples |
| Output format described in words but not shown | Add a template or output example |
| Role not aligned with the task | "You are a poet. Write a technical report." |