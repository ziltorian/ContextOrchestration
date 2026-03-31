# Comprehensive Prompt Examples

Real-world, copy-paste ready prompts for common development tasks.

## System Prompts for Agents

### Expert Coding Assistant

```markdown
<role>
You are an expert software engineer and code reviewer with deep knowledge of:
- Software architecture and design patterns
- Multiple programming languages and frameworks
- Testing strategies and best practices  
- Performance optimization
- Security best practices
</role>

<behavior>
- Provide clear, well-reasoned explanations
- Show code examples when helpful
- Suggest best practices and alternatives
- Point out potential issues or edge cases
- Ask clarifying questions when requirements are unclear
</behavior>

<output_style>
- Use markdown formatting for code blocks
- Include type hints and documentation
- Explain your reasoning
- Keep responses focused and concise
- Provide working, tested code
</output_style>

<constraints>
- Never invent APIs or features that don't exist
- Always validate inputs and handle errors
- Follow language-specific conventions
- Consider performance and security
- Prioritize code readability
</constraints>
```

### Code Review Agent

```markdown
<role>
Senior code reviewer focused on quality, maintainability, and best practices.
</role>

<review_checklist>
<code_quality>
- Clear naming conventions
- Appropriate function/class sizes
- Proper error handling
- Code duplication
- Complexity management
</code_quality>

<security>
- Input validation
- Authentication/authorization
- Data sanitization
- Secrets management
- Dependency security
</security>

<performance>
- Algorithm efficiency
- Database query optimization
- Memory usage
- Caching opportunities
- Network request minimization
</performance>

<testing>
- Test coverage
- Edge case handling
- Mock usage
- Test quality
</testing>
</review_checklist>

<output_format>
Provide feedback in this structure:

## Summary
[Overall assessment in 2-3 sentences]

## Critical Issues
[Must-fix issues with specific locations]

## Suggestions
[Improvements with examples]

## Positive Aspects
[What's done well]
</output_format>
```

### Documentation Writer

```markdown
<role>
Technical documentation specialist creating clear, comprehensive documentation.
</role>

<documentation_principles>
- Write for your audience (developers, users, contributors)
- Use clear, concise language
- Provide concrete examples
- Include code samples that work
- Structure content logically
- Keep documentation up-to-date
</documentation_principles>

<structure>
Every documentation should include:
1. **Overview**: What it is and why it exists  
2. **Getting Started**: Quick start guide
3. **Usage**: Common use cases with examples
4. **API Reference**: Detailed technical docs
5. **Troubleshooting**: Common issues and solutions
6. **Contributing**: How to contribute (if applicable)
</structure>

<style>
- Use present tense
- Use active voice
- Use "you" for user instructions
- Use imperative mood for commands ("Click the button", not "The user should click")
- Keep paragraphs short (3-5 sentences)
</style>
```

## Task-Specific Prompts

### Generate REST API Endpoint

```markdown
Create a REST API endpoint using FastAPI with the following requirements:

**Endpoint:** POST /api/users

**Purpose:** Create a new user account

**Request Body:**
\```json
{
  "username": "string",
  "email": "string",
  "password": "string",
  "fullName": "string (optional)"
}
\```

**Requirements:**
1. Validate all inputs using Pydantic models
2. Check if username or email already exists
3. Hash password using bcrypt
4. Save user to database
5. Return created user (without password)
6. Return proper HTTP status codes
7. Include error handling

**Response:**Success (201):
\```json
{
  "id": "uuid",
  "username": "string",
  "email": "string",
  "fullName": "string",
  "createdAt": "datetime"
}
\```

Errors:
- 400: Invalid input data
- 409: Username or email already exists
- 500: Server error

**Additional:**
- Include type hints
- Add docstring
- Use async/await
- Follow project conventions
```

### Debug Complex Issue

```markdown
I'm debugging a ${type_of_issue} in ${language/framework}. Here's the context:

**Problem:**
${detailed_problem_description}

**Expected Behavior:**
${what_should_happen}

**Actual Behavior:**
${what_actually_happens}

**Code:**
\```${language}
${relevant_code}
\```

**Error Message:**
\```
${error_message_if_any}
\```

**Environment:**
- ${language}: ${version}
- ${framework}: ${version}
- OS: ${os}

**What I've Tried:**
1. ${attempt_1}
2. ${attempt_2}
3. ${attempt_3}

Please help me:
1. Identify the root cause
2. Explain why it's happening
3. Provide a solution with code
4. Suggest how to prevent this in the future
```

### Refactor Legacy Code

```markdown
Refactor the following legacy code to modern best practices:

**Current Code:**
\```${language}
${legacy_code}
\```

**Issues:**
- ${issue_1}
- ${issue_2}
- ${issue_3}

**Requirements:**
1. Apply SOLID principles
2. Improve readability and maintainability
3. Add type hints/annotations
4. Add error handling
5. Add documentation
6. Keep existing functionality intact
7. Add unit tests

**Constraints:**
- Must be backward compatible
- Cannot change public API
- Keep performance similar or better

**Deliverables:**
1. Refactored code with documentation
2. Unit tests for refactored code
3. Explanation of changes made
4. Migration guide (if API changes)
```

### Architecture Design

```markdown
Design the architecture for a ${type_of_system}:

**Requirements:**
${list_all_functional_requirements}

**Non-Functional Requirements:**
- Scalability: ${scalability_needs}
- Performance: ${performance_requirements}
- Security: ${security_requirements}
- Availability: ${availability_requirements}

**Constraints:**
- Technology Stack: ${preferred_technologies}
- Team Size: ${team_size}
- Timeline: ${timeline}
- Budget: ${budget_constraints}

**Deliverables:**
1. High-level architecture diagram (describe components)
2. Component breakdown with responsibilities
3. Data flow description
4. Technology choices with justifications
5. Potential challenges and mitigation strategies
6. Scalability plan
7. Security considerations

**Format:**
Present as:
- Architecture overview
- Component details
- Database schema (if applicable)
- API design (if applicable)
- Deployment strategy
```

## Data Analysis Prompts

### Data Analysis Task

```markdown
Analyze this dataset and provide insights:

**Dataset:**
\```
${data_sample_or_description}
\```

**Context:**
${business_context}

**Questions:**
1. ${question_1}
2. ${question_2}
3. ${question_3}

**Requirements:**
1. Perform exploratory data analysis
2. Identify patterns and trends
3. Find anomalies or outliers
4. Provide statistical summary
5. Create visualizations (describe or provide code)
6. Make actionable recommendations

**Output Format:**
## Executive Summary
[3-4 key findings]

## Detailed Analysis
### Finding 1
- Observation
- Evidence
- Implication

### Finding 2
[...]

## Visualizations
[Describe or provide code for charts]

## Recommendations
[Actionable next steps]
```

### SQL Query Generation

```markdown
Generate SQL queries for the following database analysis:

**Database Schema:**
\```sql
${schema_definition}
\```

**Requirements:**
${analysis_requirements}

**Specific Queries Needed:**
1. ${query_description_1}
2. ${query_description_2}  
3. ${query_description_3}

**Constraints:**
- Optimize for performance (explain indexes needed)
- Handle NULL values appropriately
- Include comments explaining complex logic
- Use CTEs for readability where appropriate
- Ensure queries are safe from SQL injection

**Output:**
For each query provide:
1. The SQL query
2. Expected output columns
3. Performance considerations
4. Index recommendations (if any)
```

## Testing Prompts

### Comprehensive Test Suite

```markdown
Generate comprehensive test suite for:

**Code to Test:**
\```${language}
${code_to_test}
\```

**Test Requirements:**
1. **Happy Path Tests:** Normal operation with valid inputs
2. **Edge Cases:** Boundary values, empty inputs, special characters
3. **Error Cases:** Invalid inputs, exceptions, error conditions
4. **Integration:** Interaction with dependencies (mock them)

**Test Framework:** ${framework_name}

**Coverage Requirements:**
- Line coverage: >80%
- Branch coverage: >75%
- All public methods tested

**Test Structure:**
\```${language}
class Test${ClassName}:
    def setup_method(self):
        # Setup before each test
        
    def test_${method}_happy_path(self):
        # Arrange, Act, Assert
        
    def test_${method}_edge_case_${scenario}(self):
        # Test edge case
        
    def test_${method}_error_${error_type}(self):
        # Test error handling
        
    def teardown_method(self):
        # Cleanup after each test
\```

**Deliverables:**
1. Complete test file with all tests
2. Fixtures/mocks needed
3. Test data setup
4. Coverage report interpretation
```

## Prompt Improvement Prompts

### Prompt Critique

```markdown
Analyze and improve this prompt:

**Current Prompt:**
\```
${current_prompt}
\```

**Issues I'm Experiencing:**
- ${issue_1}
- ${issue_2}

**Goals:**
${what_prompt_should_achieve}

**Please:**
1. Identify weaknesses in current prompt
2. Suggest specific improvements
3. Provide revised prompt
4. Explain what makes the revision better

**Consider:**
- Clarity and specificity
- Structure and organization
- Examples and constraints
- Output format specification
- Edge case handling
```

## Multi-Turn Conversation Starters

### Iterative Development

```markdown
Let's build ${feature_name} iteratively:

**Overall Goal:**
${high_level_description}

**User Story:**
As a ${user_type}, I want to ${action}, so that ${benefit}.

**Acceptance Criteria:**
- ${criterion_1}
- ${criterion_2}
- ${criterion_3}

**Process:**
1. First, let's design the API/interface
2. Then implement core functionality  
3. Add error handling
4. Write tests
5. Add documentation

Let's start with step 1. Show me your proposed API design and explain your reasoning.

[After each step, I'll review and we'll proceed to the next]
```

### Code Review Session

```markdown
I'd like your help reviewing this pull request:

**PR Description:**
${pr_description}

**Changed Files:**
${list_of_changed_files}

**Let's review systematically:**

**Round 1 - Architecture:**
Look at the overall changes. Do they make sense architecturally? Any concerns?

[Wait for response]

**Round 2 - Code Quality:**
Now let's look at specific files. Review for:
- Code clarity
- Naming conventions
- Function complexity
- Duplication

[Wait for response]

**Round 3 - Testing:**
Are there adequate tests? What's missing?

[Wait for response]

**Round 4 - Security & Performance:**
Any security or performance concerns?

[Wait for response]

**Final Summary:**
Summarize findings and provide overall recommendation (approve/request changes/needs discussion).
```

## Usage Tips

### Customizing Prompts

1. **Replace placeholders** (${variable}) with actual values
2. **Adjust detail level** based on complexity
3. **Add/remove sections** as needed for your use case
4. **Include context** specific to your project

### Improving Results

If outputs aren't good enough:

1. **Add examples** of desired output
2. **Be more specific** about requirements
3. **Add constraints** to guide behavior
4. **Break into steps** for complex tasks
5. **Iterate** - refine prompt based on results

### Testing Prompts

1. **Start with simple cases** to validate basic functionality
2. **Test edge cases** to ensure robustness
3. **Try with different inputs** to verify consistency
4. **Compare results** across different AI models
5. **Keep track** of what works well

## Contributing

To add your own effective prompt:

1. Use clear section headers
2. Include context about when to use it
3. Provide complete, working examples
4. Explain placeholders
5. Add usage notes if helpful
