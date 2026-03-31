# Practical Recommendations and Checklists

## Checklist: Creating a Prompt from Scratch

### Stage 1: Task Definition

- [ ] End goal is clearly formulated
- [ ] Target audience of the result is defined
- [ ] Success criteria are established (how to evaluate result quality)
- [ ] Input data is identified
- [ ] Desired output format is defined

### Stage 2: Basic Structure

- [ ] AI role is defined (if necessary)
- [ ] Clear instructions are written
- [ ] Necessary context is added
- [ ] Output format is specified
- [ ] Constraints are added (what NOT to do)

### Stage 3: Improvement

- [ ] Examples are added (if the task is complex)
- [ ] Appropriate delimiters are used (XML/Markdown)
- [ ] Terminology consistency is verified
- [ ] Contradictions in instructions are removed
- [ ] Edge cases are added

### Stage 4: Testing

- [ ] Tested on typical examples
- [ ] Tested on edge cases
- [ ] Result consistency is verified
- [ ] Metrics are measured (accuracy, time, cost)
- [ ] Feedback is collected

### Stage 5: Optimization

- [ ] Identified problems are resolved
- [ ] Prompt length is optimized
- [ ] Instruction wording is improved
- [ ] Examples for problematic cases are added
- [ ] Final quality check

---

## Checklist: Debugging a Problematic Prompt

### Problem Diagnosis

- [ ] Problem is precisely identified (what result instead of expected)
- [ ] Examples of incorrect outputs are collected
- [ ] Problem frequency is determined (always/sometimes/rarely)
- [ ] Error consistency is verified

### Systematic Analysis

- [ ] Instructions checked for contradictions
- [ ] Examples checked for alignment with instructions
- [ ] Clarity of wording is assessed
- [ ] Context completeness is verified
- [ ] Output format is clearly defined

### Step-by-Step Improvement

- [ ] Prompt simplified to minimum (basic functionality check)
- [ ] Elements gradually added back
- [ ] Testing after each change
- [ ] Results of each change are documented
- [ ] Only changes that improve results are applied

### Specific Fixes

- [ ] For format issues: format instructions + examples reinforced
- [ ] For hallucinations: constraints on information sources added
- [ ] For inconsistency: specific examples added
- [ ] For context misunderstanding: context restructured or expanded
- [ ] For instruction ignoring: wording reinforced + moved to end of prompt

---

## Prompt Length Recommendations

### Optimal Length for Different Tasks

**Simple tasks (classification, extraction)**

- System prompt: 100-300 tokens
- User prompt: 50-200 tokens
- Examples: 0-2 examples

**Medium complexity (analysis, content generation)**

- System prompt: 300-800 tokens
- User prompt: 100-500 tokens
- Examples: 2-5 examples

**Complex tasks (agents, multi-step)**

- System prompt: 800-2000 tokens
- User prompt: varies
- Examples: 3-10 examples

### How to Reduce Verbose Prompts

1. Remove repeated instructions
2. Combine similar rules
3. Use examples instead of long descriptions
4. Remove obvious instructions
5. Replace wordy explanations with concise formulations

### When to Expand a Prompt

- Results are unpredictable → add examples
- Model ignores instructions → reinforce wording
- Errors in edge cases → add specific instructions
- Wrong format → add detailed format description + example

---

## Common Errors and Solutions

### Error 1: Model Doesn't Follow Instructions

**Problem:** AI ignores parts of the prompt

**Causes:**

- Instructions are too long or convoluted
- Contradictions between different parts of the prompt
- Instructions are vague or ambiguous

**Solutions:**

- Simplify wording
- Check for contradictions
- Use imperative verbs ("Do X", not "You can do X")
- Place critical instructions at the end of the prompt (Claude 4.x)
- Add specific examples of desired behavior

### Error 2: Inconsistent Results

**Problem:** Different results for identical inputs

**Causes:**

- Insufficient instruction specificity
- Lack of examples
- High temperature

**Solutions:**

- Add more specific details
- Use few-shot examples
- Lower temperature to 0.0-0.3
- Specify exact output format
- Use structured outputs (JSON schema)

### Error 3: Hallucinations

**Problem:** Model fabricates information

**Causes:**

- Insufficient context
- Requesting information outside model knowledge
- Lack of instructions about acknowledging ignorance

**Solutions:**

- Explicitly state: "Use only provided information"
- Add: "If you don't know the answer, say 'I don't know'"
- Provide all necessary context
- For facts — use web search or RAG
- Ask the model to cite sources

### Error 4: Wrong Output Format

**Problem:** Output doesn't match desired format

**Causes:**

- Imprecise format description
- Lack of examples
- Conflict between instructions and examples

**Solutions:**

- Show exact format example
- Use structured outputs (JSON schema for GPT)
- Explicitly state: "ONLY JSON, no additional text"
- For Claude: use prefilling to start the desired format
- Add format validation in post-processing

### Error 5: Responses Too Short or Too Long

**Problem:** Response length doesn't match expectations

**Solutions:**

- Specify exact length: "150-200 words" or "3-5 paragraphs"
- Show example of desired length
- For short responses: "Answer as briefly as possible, in one sentence"
- For detailed: "Provide an exhaustive analysis covering all aspects"

### Error 6: Model Too Cautious or Refuses

**Problem:** Model avoids performing a legitimate task

**Solutions:**

- Provide context about task legitimacy
- Rephrase the request more neutrally
- Break the task into smaller steps
- Explicitly state that the task is ethical and legal (if so)

---

## Optimization for Different Metrics

### Accuracy Optimization

**Techniques:**

1. Use self-consistency (multiple answers + selection)
2. Add Chain of Thought
3. Increase number of examples
4. Add validation to the prompt ("Check your answer for...")
5. Use ensembling (different prompts → reconciliation)

**Example prompt for self-checking:**

```
After formulating the answer, perform the following checks:
1. Are all requirements accounted for?
2. Are there contradictions in the answer?
3. Is the format correct?
4. Are there factual errors?

If you find problems — fix them before the final answer.
```

### Speed Optimization

**Techniques:**

1. Reduce prompt to the necessary minimum
2. Use faster models for simple tasks
3. Cache repeating parts of the prompt (Claude Prompt Caching)
4. Use batch API for multiple requests
5. Parallel tool calls for independent operations

### Cost Optimization

**Techniques:**

1. Use less expensive models where possible (Haiku instead of Sonnet)
2. Reduce prompt length
3. Use prompt caching for repeating elements
4. Batch processing for non-time-critical tasks
5. Filter inputs before sending to an expensive model

**Cascading strategy:**

```
1. Simple classification → Haiku (cheap)
2. If confidence < 0.8 → Sonnet (medium)
3. If critical task → Opus (expensive)
```

---

## Patterns for Specific Tasks

### Pattern: Structured Data Extraction

```xml
<instructions>
Extract the following data from the text. If information is missing, use null.
</instructions>

<output_schema>
{
  "field1": "type and description",
  "field2": "type and description"
}
</output_schema>

<extraction_rules>
1. Extract only explicit information
2. Do not make assumptions
3. Preserve original wording
4. Use null for missing fields
</extraction_rules>

<examples>
[Minimum 2 examples with different cases]
</examples>

<input>
[Text for processing]
</input>

Return ONLY JSON without additional text.
```

### Pattern: Multi-Step Analysis

```xml
<task>Analyze [object] using the following steps:</task>

<analysis_steps>
Step 1: [first stage of analysis]
- Describe what you see
- Highlight key elements

Step 2: [second stage]
- Analyze relationships
- Identify patterns

Step 3: [third stage]
- Formulate conclusions
- Give recommendations

After each step, pause and make sure you completed it fully before moving to the next.
</analysis_steps>

<output_format>
# Step 1: [name]
[results]

# Step 2: [name]
[results]

# Step 3: [name]
[results]

# Final Conclusions
[final conclusions]
</output_format>
```

### Pattern: Creative Generation with Constraints

```xml
<creative_task>
Create [content type] on the topic [topic]
</creative_task>

<mandatory_elements>
Must include:
- [element 1]
- [element 2]
- [element 3]
</mandatory_elements>

<constraints>
Constraints:
- Do not use: [forbidden elements]
- Style: [desired style]
- Tone: [desired tone]
- Length: [word/paragraph count]
</constraints>

<inspiration>
Be inspired by the following, but create an original work:
[references or style examples]
</inspiration>

<quality_criteria>
The result must be:
- [quality criterion 1]
- [quality criterion 2]
- [quality criterion 3]
</quality_criteria>
```

---

## Prompt Testing

### Creating a Test Set

**Test case categories:**

1. **Happy Path (70%)** - Typical examples
   - Standard inputs
   - Expected usage
   - Medium complexity

2. **Edge Cases (20%)** - Boundary cases
   - Minimum inputs
   - Maximum inputs
   - Empty or null values
   - Unusual but valid combinations

3. **Error Cases (10%)** - Problematic cases
   - Invalid inputs
   - Contradictory information
   - Incomplete data
   - Potentially malicious inputs

### Evaluation Metrics

**Qualitative metrics:**

- Correctness (right answer)
- Completeness (all aspects covered)
- Relevance (alignment with the task)
- Consistency (result stability)
- Format (compliance with requirements)

**Quantitative metrics:**

- Accuracy
- Precision and Recall (for classification)
- F1-score
- Latency (response time)
- Cost (tokens/price)

### A/B Testing Process for Prompts

```
1. Baseline prompt → collect metrics on test set
2. Create a prompt variant with improvement
3. Test on the same set
4. Compare metrics:
   - If improvement ≥ 5% → accept
   - If degradation → rollback
   - If insignificant changes → continue optimization
5. Repeat the process
```

---

## Prompt Versioning and Documentation

### What to Document

```markdown
# Prompt: [Name] v[Version]

## Purpose
[What this prompt is used for]

## Model
- Optimized for: [model and version]
- Tested on: [list of models]

## Parameters
- Temperature: [value]
- Max tokens: [value]
- Top P: [value]
- Other parameters: [values]

## Input Variables
- `{variable1}`: [description, type, constraints]
- `{variable2}`: [description, type, constraints]

## Expected Output Format
[Description or example]

## Known Limitations
- [limitation 1]
- [limitation 2]

## Change History
### v1.2 (2024-01-15)
- Added: [what was added]
- Fixed: [what was fixed]
- Metrics: accuracy 85% → 92%

### v1.1 (2024-01-10)
- Changes and metrics

### v1.0 (2024-01-05)
- Initial version
- Baseline metrics
```

---

## Final Checklist Before Deployment

- [ ] Prompt tested on a representative dataset
- [ ] Quality metrics meet requirements
- [ ] Cost per request is acceptable
- [ ] Latency meets SLA
- [ ] Edge cases are handled
- [ ] Documentation is updated
- [ ] Prompt version is recorded
- [ ] Production monitoring is set up
- [ ] Rollback plan exists (previous prompt version)
- [ ] Team is trained on prompt usage
