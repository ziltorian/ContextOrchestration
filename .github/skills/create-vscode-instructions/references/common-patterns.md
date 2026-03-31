# Common Patterns for VS Code Instructions and Prompts

Real-world patterns and templates for different use cases.

## Patterns for Custom Instructions

### Pattern 1: General Language Standards

**Use case:** Apply coding standards to all files of a specific language

**File:** `.github/instructions/Python_Standards.instructions.md`

```markdown
---
applyTo: "**/*.py"
name: "Python_Code_Standards"
description: "Python coding standards for the project"
---

## Python Code Standards

### Mandatory Requirements
- **Update this file**: when standards change, update these instructions.

### Code Style
- Use 4 spaces for indentation (not tabs)
- Follow PEP 8 style guide
- Maximum line length: 100 characters
- Use type hints for all function parameters and return values

### Naming Conventions
- `snake_case` for functions and variables
- `PascalCase` for classes
- `UPPER_CASE` for constants
- Prefix private methods with underscore `_method_name`

### Documentation
- Write docstrings for all public functions
- Use Google-style docstring format
- Include parameter types and return types

### Error Handling
- Use specific exception types
- Always include error messages with context
- Log errors before raising exceptions

### Testing
- Write unit tests for all new functions
- Maintain minimum 80% code coverage
- Use pytest for test framework

### MUST DO
- Run black formatter before committing
- Run mypy type checker
- Write tests for bug fixes

### MUST NOT DO
- Commit code with failing tests
- Use mutable default arguments
- Catch bare exceptions without re-raising
```

### Pattern 2: Module-Specific Instructions

**Use case:** Guidelines for a specific module or directory

**File:** `.github/instructions/API_Module.instructions.md`

```markdown
---
applyTo: "backend/src/api/**"
name: "API_Module_Instructions"
description: "Instructions for API module development"
---

## API Module

### Mandatory Requirements
- **Update this file**: when API structure changes, update these instructions.

### Module Description
Handles REST API endpoints and request processing.

### Module Tasks
- Process incoming HTTP requests
- Validate request data
- Return formatted JSON responses

### Architecture
- `endpoints.py`: Route definitions
- `handlers.py`: Request processing logic
- `validators.py`: Input validation

### API Standards
- Use FastAPI decorators for routes
- Validate all inputs with Pydantic models
- Return proper HTTP status codes (200, 201, 400, 404, 500)
- Include error messages in responses

### Authentication
- Use JWT tokens for authentication
- Validate tokens on protected endpoints
- Return 401 for unauthorized requests

### MUST DO
- Validate all incoming data before processing
- Use `@app.route` decorators for endpoints
- Log all API requests and responses
- Include request ID in logs

### MUST NOT DO
- Process unvalidated user input
- Expose internal error details in responses
- Return raw stack traces to clients
- Skip authentication checks
```

### Pattern 3: Documentation Writing Guidelines

**Use case:** Standards for writing project documentation

**File:** `.github/instructions/Documentation_Standards.instructions.md`

```markdown
---
applyTo: "docs/**/*.md"
name: "Documentation_Writing_Guidelines"
description: "Standards for project documentation"
---

## Documentation Writing Guidelines

### Grammar and Style
- Use present tense verbs
- Write in second person (you)
- Use active voice
- Write factual statements and direct commands

### Structure
- Use headings to organize content (##, ###)
- Use bullet points for lists
- Include code examples where applicable
- Add table of contents for long documents

### Markdown Conventions
- Use code blocks with language specification
- Include links to related resources
- Use tables for structured data
- Keep line length under 100 characters

### Code Examples
- Show complete, runnable examples
- Include explanatory comments
- Test all code examples before committing
- Use syntax highlighting

### MUST DO
- Update documentation when code changes
- Include examples for all public APIs
- Link to external resources when helpful
- Keep documentation current

### MUST NOT DO
- Use outdated examples
- Include uncommitted code in examples
- Copy-paste without testing
- Leave broken links
```

### Pattern 4: Frontend Component Standards

**Use case:** React/TypeScript component guidelines

**File:** `.github/instructions/React_Component_Standards.instructions.md`

```markdown
---
applyTo: "src/**/*.{ts,tsx}"
name: "React_TypeScript_Standards"
description: "React and TypeScript coding standards"
---

## React and TypeScript Standards

### TypeScript Guidelines
- Use strict mode
- Define interfaces for all data structures
- Avoid `any` type - use `unknown` if type is truly unknown
- Use optional chaining `?.` and nullish coalescing `??`

### React Component Structure
- Use functional components with hooks
- Follow React hooks rules (no conditional hooks)
- Keep components under 250 lines
- Extract reusable logic into custom hooks

### Component Template

\```typescript
import React, { useState } from 'react';
import styles from './MyComponent.module.css';

interface MyComponentProps {
  title: string;
  onSubmit?: () => void;
}

export const MyComponent: React.FC<MyComponentProps> = ({ 
  title, 
  onSubmit 
}) => {
  const [value, setValue] = useState('');
  
  const handleSubmit = () => {
    onSubmit?.();
  };
  
  return (
    <div className={styles.container}>
      <h1>{title}</h1>
    </div>
  );
};
\```

### State Management
- Use `useState` for component-local state
- Use `useReducer` for complex state logic
- Use Context API for global state
- Avoid prop drilling beyond 2 levels

### MUST DO
- Define PropTypes with TypeScript interfaces
- Handle loading and error states
- Implement keyboard navigation
- Test components with React Testing Library

### MUST NOT DO
- Mutate state directly
- Use index as key in lists
- Put business logic in components
- Forget to clean up effects
```

## Patterns for Prompt Files

### Pattern 1: Code Generation

**File:** `.github/prompts/create-react-form.prompt.md`

```markdown
---
name: create-react-form
description: "Generate new React form component"
argument-hint: "form name and fields"
agent: "agent"
model: "GPT-4o"
tools: ["githubRepo", "search/codebase"]
---

Generate a new React form component based on project templates.

## Requirements

- Use design system components from project
- Use `react-hook-form` for state management
- Define TypeScript interfaces for form data
- Use `yup` for validation with TypeScript types
- Include submit and cancel handlers

## Process

1. Ask user for form name and required fields
2. Search existing forms for patterns using `#tool:githubRepo`
3. Generate component with proper types
4. Create validation schema
5. Add to appropriate directory

## Example

For form with fields "username" and "email":

\```typescript
interface LoginFormData {
  username: string;
  email: string;
}

export const LoginForm: React.FC = () => {
  const { register, handleSubmit } = useForm<LoginFormData>();
  
  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      {/* Form fields */}
    </form>
  );
};
\```
```

### Pattern 2: Code Review

**File:** `.github/prompts/security-review.prompt.md`

```markdown
---
name: security-review
description: "Perform security review of code"
argument-hint: "file or directory path"
agent: "ask"
model: "Claude Sonnet 4"
---

Perform comprehensive security review of specified code.

## Check Points

### Authentication/Authorization
- All endpoints protected by authentication
- Proper authorization checks before data access
- Secure session management

### Input Validation
- All user inputs validated and sanitized
- SQL injection prevention
- XSS prevention

### Security Features
- Rate limiting implemented
- CSRF protection enabled
- Security headers configured

### Data Protection
- Sensitive data encrypted at rest
- Secure password hashing
- Secrets not hardcoded

## Output Format

Return TODO list in Markdown:

### High Priority
- [File path:line] Issue description
- [File path:line] Issue description

### Medium Priority
- [File path:line] Issue description

### Low Priority
- [File path:line] Issue description

Include specific recommendations for each issue.
```

### Pattern 3: Test Generation

**File:** `.github/prompts/generate-tests.prompt.md`

```markdown
---
name: generate-tests
description: "Generate test suite for module"
argument-hint: "module path"
agent: "agent"
tools: ["search/codebase", "githubRepo"]
---

Create comprehensive test suite for ${input:modulePath}.

## Process

1. Analyze module structure using `#tool:search/codebase`
2. Identify public functions and classes
3. Generate unit tests with:
   - Setup and teardown
   - Happy path tests
   - Edge case tests
   - Error condition tests
4. Create test file in `tests/` directory
5. Follow project's testing framework

## Requirements

- Follow existing test patterns in repository
- Mock external dependencies
- Aim for >80% code coverage
- Include docstrings for test functions

## Test Template

\```python
import pytest
from mymodule import function_to_test

class TestFunctionName:
    def test_happy_path(self):
        result = function_to_test(valid_input)
        assert result == expected_output
    
    def test_edge_case(self):
        result = function_to_test(edge_case_input)
        assert result == expected_edge_output
    
    def test_error_handling(self):
        with pytest.raises(ExpectedException):
            function_to_test(invalid_input)
\```
```

### Pattern 4: Refactoring

**File:** `.github/prompts/extract-function.prompt.md`

```markdown
---
name: extract-function
description: "Extract selected code into reusable function"
agent: "edit"
---

Extract selected code into a reusable function with proper naming and parameters.

## Process

1. Analyze ${selection} to understand what it does
2. Identify inputs and outputs
3. Generate descriptive function name
4. Extract to function with parameters
5. Replace original code with function call
6. Add type hints (for Python/TypeScript)
7. Add docstring/JSDoc

## Requirements

- Function name should describe what it does
- Extract all necessary parameters
- Maintain original behavior
- Add documentation
- Keep function focused on single task

## Example

**Before:**

\```python
total = 0
for item in items:
    total += item.price * item.quantity
total = total * 1.08
\```

**After:**

\```python
def calculate_total_with_tax(items: List[Item]) -> float:
    """Calculate total price of items including tax.
    
    Args:
        items: List of items with price and quantity
        
    Returns:
        Total price with 8% tax applied
    """
    subtotal = sum(item.price * item.quantity for item in items)
    return subtotal * 1.08

total = calculate_total_with_tax(items)
\```
```

## Key Differences Summary

| Aspect | Custom Instructions | Prompt Files |
|--------|-------------------|--------------|
| **Trigger** | Automatic via `applyTo` pattern | Manual via `/prompt-name` |
| **Purpose** | Coding standards, guidelines | Specific tasks on-demand |
| **Name format** | Underscores: `Module_Name` | Hyphens: `module-name` |
| **Variables** | Not supported | Supported: `${input:var}` |
| **Tools** | N/A | Can specify available tools |
| **Agent** | N/A | Can specify which agent |
