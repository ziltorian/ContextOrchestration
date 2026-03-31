# Prompt File Examples

Complete, working examples of prompt files for various development tasks.

## Example 1: Component Generator

**File:** `.github/prompts/create-component.prompt.md`

```markdown
---
name: create-component
description: "Generate new React component with TypeScript"
argument-hint: "component name and type (functional/class)"
agent: "agent"
model: "GPT-4o"
tools: ["search/codebase", "githubRepo"]
---

Generate a new React component following project patterns.

## Requirements

Component must include:
- TypeScript interface for props
- Proper imports from project structure
- CSS module for styles
- Basic component documentation
- Export statement

## Component Template

Use this structure:

```typescript
import React from 'react';
import styles from './${input:componentName}.module.css';

interface ${input:componentName}Props {
  // Define props here
}

export const ${input:componentName}: React.FC<${input:componentName}Props> = (props) => {
  return (
    <div className={styles.container}>
      {/* Component content */}
    </div>
  );
};
```

## Process

1. Ask user for component name if not provided in ${input:componentName}
2. Search existing components using #tool:search/codebase for patterns
3. Create component file in `src/components/`
4. Create CSS module file
5. Export component from `src/components/index.ts`

## Style Guidelines

- Follow [component guidelines](../docs/component-patterns.md)
- Use functional components with hooks
- Implement proper TypeScript types
- Add PropTypes documentation
```

## Example 2: API Endpoint Generator

**File:** `.github/prompts/create-endpoint.prompt.md`

```markdown
---
name: create-endpoint
description: "Generate new REST API endpoint"
argument-hint: "endpoint path and HTTP method"
agent: "agent"
tools: ["search/codebase"]
---

Create a new REST API endpoint following project conventions.

## Process

1. Determine endpoint path: `/api/v1/${input:resource}`
2. Create request/response Pydantic models
3. Implement endpoint handler with validation
4. Add authentication if required
5. Include error handling
6. Write endpoint tests

## Endpoint Structure

```python
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from .auth import get_current_user
from .models import User

router = APIRouter(prefix="/api/v1")

class ${input:resource}Create(BaseModel):
    # Define request model

class ${input:resource}Response(BaseModel):
    # Define response model

@router.post("/${input:resource}", 
             response_model=${input:resource}Response,
             status_code=status.HTTP_201_CREATED)
async def create_${input:resource}(
    data: ${input:resource}Create,
    current_user: User = Depends(get_current_user)
):
    # Validate input
    # Process request
    # Return response
    pass
```

## Requirements

- Use existing auth patterns from #tool:search/codebase
- Follow error handling conventions
- Include request validation
- Add proper HTTP status codes
- Document with OpenAPI docstrings

## Validation Rules

- Validate all user inputs
- Return 400 for invalid data with specific errors
- Return 401 for authentication failures
- Return 403 for authorization failures
- Return 404 for missing resources
```

## Example 3: Test Suite Generator

**File:** `.github/prompts/generate-tests.prompt.md`

```markdown
---
name: generate-tests
description: "Generate comprehensive test suite for module"
argument-hint: "module path to test"
agent: "agent"
tools: ["search/codebase"]
---

Generate complete test suite for ${input:modulePath}.

## Analysis Process

1. Read module file: ${input:modulePath}
2. Identify all public functions and classes
3. Determine dependencies and side effects
4. Plan test cases for each function

## Test Structure

```python
import pytest
from unittest.mock import Mock, patch
from ${input:modulePath} import ClassName, function_name

class TestClassName:
    """Tests for ClassName."""
    
    @pytest.fixture
    def instance(self):
        """Create test instance."""
        return ClassName()
    
    def test_method_success_case(self, instance):
        """Test method with valid inputs."""
        # Arrange
        input_data = "test"
        
        # Act
        result = instance.method(input_data)
        
        # Assert
        assert result == expected_value
    
    def test_method_handles_error(self, instance):
        """Test method error handling."""
        with pytest.raises(ValueError):
            instance.method(None)

def test_function_name_basic():
    """Test function with basic input."""
    result = function_name("input")
    assert result is not None
```

## Test Coverage Requirements

For each public function/method, create tests for:
1. Happy path with typical inputs
2. Edge cases (empty, null, boundary values)
3. Error conditions (invalid inputs)
4. Integration with dependencies (mocked)

## Mocking Guidelines

- Mock external API calls
- Mock database operations
- Mock file system access
- Mock time-dependent operations

## Test File Location

Create test file at: `tests/unit/${input:modulePath.replace('src/', '')}/test_<filename>.py`

## Verification

After generation:
1. Run tests to verify they pass
2. Check coverage report
3. Ensure all public interfaces tested
```

## Example 4: Database Migration Generator

**File:** `.github/prompts/create-migration.prompt.md`

```markdown
---
name: create-migration
description: "Generate database migration script"
argument-hint: "migration description"
agent: "agent"
tools: ["search/codebase"]
---

Create Alembic migration for: ${input:migrationDescription}

## Process

1. Analyze current database schema from models
2. Determine required changes
3. Generate migration with upgrade and downgrade
4. Add appropriate indexes and constraints

## Migration Template

```python
"""${input:migrationDescription}

Revision ID: ${generate_revision_id}
Revises: ${previous_revision}
Create Date: ${current_timestamp}
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers
revision = '${generate_revision_id}'
down_revision = '${previous_revision}'
branch_labels = None
depends_on = None

def upgrade():
    """Apply migration changes."""
    # Add your upgrade logic here
    pass

def downgrade():
    """Revert migration changes."""
    # Add your downgrade logic here
    pass
```

## Requirements

- Include both upgrade and downgrade
- Add indexes for foreign keys
- Maintain referential integrity
- Test migration on development database first

## Common Operations

**Add table:**
```python
op.create_table(
    'table_name',
    sa.Column('id', sa.Integer(), primary_key=True),
    sa.Column('name', sa.String(100), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.func.now())
)
```

**Add column:**
```python
op.add_column('table_name', 
    sa.Column('new_column', sa.String(50), nullable=True)
)
```

**Create index:**
```python
op.create_index('idx_table_column', 'table_name', ['column_name'])
```
```

## Example 5: Code Review Prompt

**File:** `.github/prompts/code-review.prompt.md`

```markdown
---
name: code-review
description: "Perform comprehensive code review"
agent: "ask"
model: "Claude Sonnet 4"
---

Perform thorough code review of ${selection} or ${file}.

## Review Checklist

### Code Quality
- Code follows project style guidelines
- Functions are focused and single-purpose
- Variable and function names are descriptive
- Complex logic includes explanatory comments

### Best Practices
- DRY principle followed (no code duplication)
- SOLID principles applied appropriately
- Proper error handling implemented
- Edge cases handled

### Security
- Input validation on user data
- SQL injection prevention
- XSS prevention in web code
- Sensitive data not hardcoded

### Performance
- No unnecessary loops or operations
- Appropriate data structures used
- Database queries optimized
- Caching used where beneficial

### Testing
- Tests cover main functionality
- Edge cases tested
- Error conditions tested
- Mocks used appropriately

## Output Format

Provide review in this structure:

### Strengths
- List positive aspects

### Issues Found
**Critical:**
- Issue description with line number and fix suggestion

**Important:**
- Issue description with line number and fix suggestion

**Minor:**
- Issue description with line number and fix suggestion

### Suggestions
- General improvement ideas

### Summary
Brief overall assessment and recommendation (Approve/Request Changes/Comment)
```

## Example 6: Documentation Generator

**File:** `.github/prompts/generate-docs.prompt.md`

```markdown
---
name: generate-docs
description: "Generate documentation for code"
argument-hint: "file or function to document"
agent: "agent"
---

Generate comprehensive documentation for ${input:target}.

## Process

1. Analyze code structure and purpose
2. Identify parameters, return values, exceptions
3. Document examples of usage
4. Note any important caveats

## Documentation Format

### For Functions

```python
def function_name(param1: str, param2: int) -> bool:
    """Brief description of what function does.
    
    Longer explanation if needed, describing the purpose
    and any important behavior details.
    
    Args:
        param1: Description of first parameter
        param2: Description of second parameter
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When invalid input provided
        TypeError: When wrong type passed
        
    Examples:
        >>> function_name("test", 42)
        True
        
        >>> function_name("", 0)
        False
    """
```

### For Classes

```python
class ClassName:
    """Brief description of class purpose.
    
    Longer explanation of class responsibilities,
    when to use it, and any important considerations.
    
    Attributes:
        attribute1: Description of attribute
        attribute2: Description of attribute
        
    Examples:
        >>> obj = ClassName()
        >>> obj.method()
        'result'
    """
```

### For Modules

```markdown
# Module Name

Brief description of module purpose.

## Overview

Detailed explanation of module functionality,
when to use it, and how it fits in the system.

## Usage

```python
from module import ClassName

# Example usage
obj = ClassName()
result = obj.method()
```

## Components

- `ClassName`: Description and purpose
- `function_name`: Description and purpose

## Dependencies

- List of required packages
- Version requirements if specific
```

## Requirements

- Follow [documentation standards](../docs/documentation-guide.md)
- Include all parameters and return types
- Provide realistic usage examples
- Note any exceptions that may be raised
```

## Example 7: Refactoring Prompt

**File:** `.github/prompts/refactor-code.prompt.md`

```markdown
---
name: refactor-code
description: "Refactor code following best practices"
agent: "edit"
---

Refactor ${selection} to improve code quality.

## Refactoring Goals

1. **Improve Readability**
   - Extract complex logic into named functions
   - Use descriptive variable names
   - Add explanatory comments for complex sections

2. **Reduce Complexity**
   - Break large functions into smaller ones
   - Reduce nesting depth
   - Eliminate code duplication

3. **Enhance Maintainability**
   - Follow SOLID principles
   - Improve error handling
   - Add type hints (Python) or types (TypeScript)

4. **Optimize Performance**
   - Remove unnecessary operations
   - Use appropriate data structures
   - Minimize database queries

## Refactoring Patterns

### Extract Function
```python
# Before
def process_order(order):
    # Validate
    if not order.items:
        raise ValueError("Empty order")
    # Calculate
    total = sum(item.price * item.quantity for item in order.items)
    # Apply discount
    if total > 100:
        total *= 0.9
    return total

# After
def process_order(order):
    validate_order(order)
    total = calculate_total(order.items)
    return apply_discount(total)

def validate_order(order):
    if not order.items:
        raise ValueError("Empty order")

def calculate_total(items):
    return sum(item.price * item.quantity for item in items)

def apply_discount(total):
    return total * 0.9 if total > 100 else total
```

### Replace Magic Numbers
```python
# Before
if age > 18:
    status = "adult"

# After
ADULT_AGE_THRESHOLD = 18
if age > ADULT_AGE_THRESHOLD:
    status = "adult"
```

### Simplify Conditionals
```python
# Before
def get_price(customer, product):
    if customer.is_premium:
        if product.is_on_sale:
            return product.price * 0.7
        else:
            return product.price * 0.9
    else:
        if product.is_on_sale:
            return product.price * 0.8
        else:
            return product.price

# After
def get_price(customer, product):
    discount = calculate_discount(customer, product)
    return product.price * (1 - discount)

def calculate_discount(customer, product):
    if customer.is_premium and product.is_on_sale:
        return 0.3
    elif customer.is_premium:
        return 0.1
    elif product.is_on_sale:
        return 0.2
    return 0
```

## Requirements

- Maintain existing functionality (no behavior changes)
- Keep or improve performance
- Add tests for refactored code
- Document significant changes
- Follow project coding standards
```

## Example 8: Bug Fix Prompt

**File:** `.github/prompts/fix-bug.prompt.md`

```markdown
---
name: fix-bug
description: "Analyze and fix bug with test"
argument-hint: "bug description"
agent: "agent"
tools: ["search/codebase"]
---

Fix bug: ${input:bugDescription}

## Bug Analysis Process

1. **Reproduce the Bug**
   - Understand expected vs actual behavior
   - Identify conditions that trigger the bug
   - Document steps to reproduce

2. **Locate the Issue**
   - Search codebase using #tool:search/codebase
   - Trace execution flow
   - Identify root cause

3. **Plan the Fix**
   - Determine minimal change needed
   - Consider edge cases
   - Ensure no regression

## Fix Implementation

1. Create failing test that demonstrates bug
2. Implement minimal fix
3. Verify test passes
4. Check for similar issues in codebase
5. Update documentation if needed

## Test Template

```python
def test_bug_${input:bugDescription.replace(' ', '_')}():
    """Test that reproduces bug: ${input:bugDescription}"""
    # Arrange - Set up conditions that trigger bug
    
    # Act - Execute code that should work
    
    # Assert - Verify correct behavior
    assert result == expected_value
```

## Documentation

After fix, document:
- Root cause of bug
- Why fix works
- Any related changes made
- How to prevent similar bugs

## Verification Checklist

- [ ] Bug is reproducible with test
- [ ] Fix resolves the bug
- [ ] Test passes with fix
- [ ] No regression in other tests
- [ ] Edge cases handled
- [ ] Code reviewed for quality
```
