# Prompt Templates for Various Task Types

## 1. System Prompt for a Chatbot / Assistant

```xml
<role>
You are a [role name], specializing in [area of expertise].
</role>

<capabilities>
Your main capabilities:
- [capability 1]
- [capability 2]
- [capability 3]
</capabilities>

<communication_style>
Communication style:
- [style characteristic 1]
- [style characteristic 2]
- Tone: [formal/friendly/professional]
- Response length: [brief/detailed/adaptive]
</communication_style>

<guidelines>
Guidelines:
1. Always [required behavior 1]
2. Never [forbidden behavior 1]
3. When [condition] do [action]
</guidelines>

<response_format>
Response structure:
1. [structure element 1]
2. [structure element 2]
3. [structure element 3]
</response_format>

<examples>
<example id="1">
<user_query>Example user query</user_query>
<assistant_response>Example ideal response</assistant_response>
</example>
</examples>
```

## 2. Prompt for Data Analysis

```xml
<task>
Analyze the provided data and deliver a comprehensive report.
</task>

<input_data>
[Data for analysis]
</input_data>

<analysis_framework>
Perform analysis along the following dimensions:

1. Descriptive Statistics
   - Key metrics (mean, median, mode)
   - Data distribution
   - Outliers and anomalies

2. Patterns and Trends
   - Temporal trends
   - Correlations between variables
   - Seasonality (if applicable)

3. Segmentation
   - Grouping by key characteristics
   - Comparative segment analysis

4. Anomalies
   - Identification of unusual patterns
   - Potential data quality issues

5. Insights and Recommendations
   - Key findings
   - Practical recommendations
   - Next steps
</analysis_framework>

<output_format>
Structure the report as follows:

# Executive Summary
[2-3 sentences with main conclusions]

# Key Metrics
[Table with main indicators]

# Detailed Analysis
[Paragraphs with analysis for each dimension]

# Visualizations
[Description of recommended charts and diagrams]

# Conclusions and Recommendations
[Bulleted list of actions]
</output_format>
```

## 3. Prompt for Code Generation

```xml
<task>
Create a [type of application/component/function] with the following requirements:
</task>

<requirements>
Functional requirements:
- [requirement 1]
- [requirement 2]
- [requirement 3]

Technical requirements:
- Language: [programming language]
- Framework: [if applicable]
- Patterns: [architectural patterns]
- Standards: [coding standards]
</requirements>

<code_quality_standards>
Ensure the code meets the following standards:
1. Readability: clear variable and function names
2. Modularity: separation into logical components
3. Error handling: proper exception handling
4. Documentation: comments for complex logic
5. Testability: code should be easy to test
6. Performance: optimal algorithms and data structures
</code_quality_standards>

<deliverables>
Provide:
1. Main code with comments
2. Usage examples
3. Tests (unit tests)
4. README with installation and usage instructions
</deliverables>

<example_usage>
# Example of expected usage
[Usage code example]
</example_usage>
```

## 4. Prompt for Content Creation / Copywriting

```xml
<content_brief>
Content type: [article/post/description/etc.]
Topic: [main topic]
Target audience: [audience description]
Goal: [inform/persuade/entertain/etc.]
Tone: [professional/friendly/authoritative/etc.]
Length: [word count or paragraphs]
</content_brief>

<key_points>
Must include the following points:
1. [key point 1]
2. [key point 2]
3. [key point 3]
</key_points>

<seo_keywords>
SEO keywords (use naturally):
- [keyword 1]
- [keyword 2]
- [keyword 3]
</seo_keywords>

<structure>
Content structure:

1. Title (engaging and informative)
2. Introduction (hook + topic overview)
3. Main content (3-5 sections with subheadings)
4. Practical examples or case studies
5. Conclusion (summary + call to action)
</structure>

<writing_guidelines>
- Use active voice
- Short paragraphs (2-4 sentences)
- Specific examples instead of abstractions
- Transitions between sections
- Avoid clichés and overused phrases
</writing_guidelines>
```

## 5. Prompt for Data Extraction and Structuring

```xml
<task>
Extract structured data from the following unstructured text.
</task>

<input_text>
[Unstructured text]
</input_text>

<extraction_schema>
Extract the following information:

{
  "entities": {
    "people": ["names of people"],
    "organizations": ["organization names"],
    "locations": ["geographic locations"],
    "dates": ["dates in YYYY-MM-DD format"]
  },
  "facts": [
    {
      "subject": "what/whom the fact is about",
      "predicate": "what is stated",
      "confidence": "high/medium/low"
    }
  ],
  "relationships": [
    {
      "entity1": "first entity",
      "relation_type": "type of relationship",
      "entity2": "second entity"
    }
  ],
  "sentiment": {
    "overall": "positive/neutral/negative",
    "aspects": [
      {
        "aspect": "topic aspect",
        "sentiment": "sentiment"
      }
    ]
  }
}
</extraction_schema>

<extraction_rules>
1. Extract only explicitly mentioned information
2. Do not make assumptions or inferences
3. In case of ambiguity, indicate low confidence
4. Normalize dates to YYYY-MM-DD format
5. Preserve original spelling of proper names
</extraction_rules>

<output_format>
Return the result ONLY in JSON format, without additional text or markdown wrapping.
</output_format>
```

## 6. Prompt for Summarization

```xml
<task>
Create a brief summary of the following text.
</task>

<source_text>
[Text for summarization]
</source_text>

<summarization_parameters>
- Target length: [% of original or word count]
- Summary type: [abstractive/extractive/mixed]
- Focus: [general overview/key points/practical conclusions]
- Audience: [audience expertise level]
</summarization_parameters>

<summarization_approach>
Use the following approach:

1. Main Topic Identification
   - Determine the main thesis of the document
   - Highlight key subtopics

2. Critical Information Extraction
   - Author's main arguments
   - Key facts and figures
   - Important conclusions

3. Summary Structuring
   - Logical sequence of ideas
   - Coherence between points
   - Context preservation

4. Language Optimization
   - Removing redundancy
   - Preserving terminology accuracy
   - Clear and concise formulations
</summarization_approach>

<quality_criteria>
The summary must:
- Accurately reflect the original content
- Be self-contained (understandable without the original)
- Not contain distortions or interpretations
- Preserve the tone and style of the original
- Highlight the most important information
</quality_criteria>
```

## 7. Prompt for Creative Writing

```xml
<creative_brief>
Genre: [science fiction/detective/drama/etc.]
Format: [short story/screenplay/dialogue/etc.]
Length: [word count]
Topic: [main topic]
Mood: [atmosphere of the work]
</creative_brief>

<story_elements>
Required elements:

Characters:
- [character 1]: [brief description]
- [character 2]: [brief description]

Setting:
- Time: [when the action takes place]
- Place: [where the action takes place]

Conflict:
- [description of central conflict]

Required moments:
- [key event 1]
- [key event 2]
</story_elements>

<writing_style>
Writing style:
- Point of view: [first/third person]
- Tense: [present/past]
- Descriptiveness: [minimalist/detailed]
- Dialogue: [much/little/moderate]
- Pace: [fast/measured/variable]
</writing_style>

<structure>
Narrative structure:

1. Exposition (10-15%)
   - Introduction of characters and setting
   - Establishing normal state

2. Rising Action (25-30%)
   - Introducing the conflict
   - Building tension

3. Climax (15-20%)
   - Peak of the conflict
   - Turning point

4. Falling Action (25-30%)
   - Conflict resolution
   - Consequences of events

5. Conclusion (10-15%)
   - New state of the world/characters
   - Final impression
</structure>

<creative_constraints>
Constraints and requirements:
- Avoid: [clichés, tropes, stylistics]
- Must use: [literary devices]
- Target audience: [age group, interests]
</creative_constraints>
```

## 8. Prompt for Debugging and Problem Solving

```xml
<problem_description>
[Detailed problem description]

Symptoms:
- [symptom 1]
- [symptom 2]

Context:
- Environment: [operating system, versions, etc.]
- Code: [relevant code or link]
- Expected behavior: [what should happen]
- Actual behavior: [what happens]
</problem_description>

<debugging_approach>
Use a systematic approach for diagnosis:

Stage 1: Reproduce the Problem
- Determine the minimal reproducible example
- Isolate factors affecting the problem

Stage 2: Gather Information
- Logs and error messages
- System state when the problem occurs
- Sequence of actions leading to the problem

Stage 3: Formulate Hypotheses
- Possible causes (from most likely)
- For each hypothesis: method of verification

Stage 4: Test Hypotheses
- Test hypotheses by priority
- Document test results

Stage 5: Solution
- Proposed fix
- Explanation of why this solves the problem
- Potential side effects
</debugging_approach>

<solution_format>
Provide the solution in the following format:

# Diagnosis
[Exact cause of the problem]

# Solution
[Specific steps to fix]

# Code
```[language]
[Fixed code with comments]
```

# Explanation

[Why this works]

# Prevention

[How to avoid similar problems in the future]

# Testing

[How to verify the problem is resolved]
</solution_format>

```

## 9. Prompt for Teaching and Explaining Concepts

```xml
<learning_objective>
Explain the concept [concept name] for an audience at [beginner/intermediate/advanced] level.
</learning_objective>

<pedagogical_approach>
Use the following teaching structure:

1. Prior Knowledge Activation
   - Start with what the audience already knows
   - Connect the new concept to familiar ideas

2. Concept Presentation
   - Clear definition
   - Context and importance
   - Applicability boundaries

3. Explanation Through Examples
   - Start with the simplest example
   - Gradually increase complexity
   - Use real-world situations

4. Key Aspects Highlighting
   - Main principles
   - Common misconceptions
   - Subtleties and nuances

5. Practical Application
   - How to use in practice
   - When to apply / not apply
   - Connection to other concepts

6. Understanding Check
   - Self-check questions
   - Practice exercises
</pedagogical_approach>

<explanation_techniques>
Use the following explanation techniques:

Analogies and Metaphors:
- [analogy from everyday life]

Visualization:
- Description of diagrams or charts
- Step-by-step process illustrations

Contrast:
- What it is NOT (debunking myths)
- Differences from similar concepts

Progressive Complexity:
- "Explain it to a 5-year-old" version
- More detailed version
- Full technical version
</explanation_techniques>

<output_structure>
# [Concept Name]

## What Is It?
[Simple one-sentence definition]

## Why Is It Needed?
[Practical value of the concept]

## How Does It Work?
[Detailed explanation of mechanics]

## Examples
[2-3 practical examples with increasing complexity]

## Frequently Asked Questions and Misconceptions
[Q&A format for typical questions]

## Practical Application
[Specific usage scenarios]

## Further Study
[Resources and topics for deeper learning]
</output_structure>
```

## 10. Prompt for Refactoring and Code Improvement

```xml
<refactoring_task>
Analyze and improve the following code.
</refactoring_task>

<current_code>
```[language]
[Code for refactoring]
```

</current_code>

<refactoring_goals>
Improvement priorities:

1. [goal 1: e.g., readability]
2. [goal 2: e.g., performance]
3. [goal 3: e.g., maintainability]
</refactoring_goals>

<analysis_framework>
Analyze the code against the following criteria:

1. Code Smells
   - Long methods (>20 lines)
   - Code duplication
   - Long parameter lists
   - Complex conditional constructs
   - Poor variable/function names

2. SOLID Principles
   - Single Responsibility
   - Open/Closed
   - Liskov Substitution
   - Interface Segregation
   - Dependency Inversion

3. Performance
   - Inefficient algorithms
   - Unnecessary computations
   - Memory issues

4. Security
   - Vulnerabilities
   - Unsafe practices

5. Testability
   - Testing complexity
   - External resource dependencies
</analysis_framework>

<refactoring_deliverables>
Provide:

1. Current Code Analysis
   - Identified issues
   - Severity assessment for each issue

2. Refactored Code

   ```[language]
   [Improved version of code]
   ```

3. Explanation of Changes
   - What was changed and why
   - What problems were resolved
   - Trade-offs of decisions made

4. Metrics Comparison

   | Metric | Before | After |
   |--------|--------|-------|
   | Cyclomatic complexity | X | Y |
   | Lines of code | X | Y |
   | Test coverage | X% | Y% |

5. Recommendations
   - Further improvements
   - Patterns to adopt
   - Tools for quality monitoring
</refactoring_deliverables>

```

## 11. Prompt for Creating Documentation

```xml
<documentation_task>
Create technical documentation for [component/API/system].
</documentation_task>

<documentation_scope>
Target audience: [developers/users/administrators]
Documentation type: [API reference/User guide/Technical spec]
Detail level: [high/medium/overview]
</documentation_scope>

<documentation_structure>
Documentation structure:

## 1. Overview
   - Purpose and goals
   - Key features
   - Requirements and dependencies

## 2. Quick Start
   - Minimal working example
   - Installation and setup
   - First use

## 3. Detailed Description
   
   ### 3.1 Architecture
   - System components
   - Interaction between components
   
   ### 3.2 API Reference
   For each method/function:
   - Signature
   - Parameters (type, description, default value)
   - Return value
   - Exceptions/errors
   - Usage examples
   
   ### 3.3 Configuration
   - Configuration parameters
   - Environment variables
   - Configuration files

## 4. Practical Examples
   - Typical usage scenarios
   - Best practices
   - Anti-patterns

## 5. Troubleshooting
   - Common problems and solutions
   - Debugging
   - FAQ

## 6. Additional
   - Performance and optimization
   - Security
   - Migration and updates
</documentation_structure>

<documentation_standards>
Quality standards:
- Use active voice
- Imperative verbs in headings
- Specific examples for each feature
- Consistent terminology
- Up-to-date code (verifiable examples)
- Clear diagrams (description in text)
</documentation_standards>
```
