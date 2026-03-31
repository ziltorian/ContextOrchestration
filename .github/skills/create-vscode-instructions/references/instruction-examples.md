# Custom Instructions Examples

Complete, working examples of custom instructions files for various use cases.

## Example 1: General Python Standards

**File:** `.github/instructions/Python_Standards.instructions.md`

```markdown
---
applyTo: "**/*.py"
name: "Python_Code_Standards"
description: "Python coding standards and best practices for the project"
---

## Python Code Standards

### Mandatory Requirements
- **Update this file**: when Python standards change, update these instructions.

### Code Style
- Use 4 spaces for indentation (not tabs).
- Follow PEP 8 style guide.
- Maximum line length: 100 characters.
- Use type hints for all function parameters and return values.

### Naming Conventions
- `snake_case` for functions and variables.
- `PascalCase` for classes.
- `UPPER_CASE` for constants.
- Prefix private methods with single underscore `_method_name`.

### Documentation
- Write docstrings for all public functions and classes.
- Use Google-style docstring format.
- Include parameter types and return types in docstrings.

### Error Handling
- Use specific exception types.
- Always include error messages with context.
- Log errors before raising exceptions.
- Use custom exceptions from `core.exceptions` module.

### Testing
- Write unit tests for all new functions.
- Maintain minimum 80% code coverage.
- Use `pytest` for test framework.
- Mock external dependencies in tests.

### Imports
- Group imports: standard library, third-party, local.
- Use absolute imports for clarity.
- Avoid wildcard imports (`from module import *`).

### MUST DO
- Run `black` formatter before committing.
- Run `mypy` type checker.
- Run `pylint` and fix all warnings.
- Write tests for bug fixes.

### MUST NOT DO
- Commit code with failing tests.
- Use mutable default arguments.
- Catch bare exceptions without re-raising.
- Leave TODO comments without issue numbers.
```

## Example 2: React/TypeScript Frontend Standards

**File:** `.github/instructions/Frontend_Standards.instructions.md`

```markdown
---
applyTo: "src/**/*.{ts,tsx}"
name: "React_TypeScript_Standards"
description: "React and TypeScript coding standards for frontend"
---

## React and TypeScript Standards

### Mandatory Requirements
- **Update this file**: when frontend standards change, update these instructions.

### TypeScript Guidelines
- Use strict mode (`strict: true` in tsconfig).
- Define interfaces for all data structures.
- Use `type` for unions and intersections.
- Use `interface` for object shapes.
- Avoid `any` type - use `unknown` if type is truly unknown.
- Use optional chaining `?.` and nullish coalescing `??`.

### React Guidelines
- Use functional components with hooks.
- Follow React hooks rules (no conditional hooks).
- Use `React.FC` type for components with children.
- Keep components under 250 lines.
- Extract reusable logic into custom hooks.
- Use CSS modules for component styling.

### Component Structure
```typescript
// Import order: React, third-party, local
import React, { useState, useEffect } from 'react';
import { useQuery } from 'react-query';
import { Button } from '@/components/ui';
import styles from './MyComponent.module.css';

interface MyComponentProps {
  title: string;
  onSubmit?: () => void;
}

export const MyComponent: React.FC<MyComponentProps> = ({ title, onSubmit }) => {
  // Hooks first
  const [value, setValue] = useState('');
  
  // Event handlers
  const handleSubmit = () => {
    onSubmit?.();
  };
  
  // Render
  return (
    <div className={styles.container}>
      <h1>{title}</h1>
    </div>
  );
};
```

### State Management
- Use `useState` for component-local state.
- Use `useReducer` for complex state logic.
- Use Context API for global state.
- Avoid prop drilling beyond 2 levels.

### Performance
- Use `React.memo` for expensive components.
- Use `useMemo` for expensive calculations.
- Use `useCallback` for functions passed to child components.
- Implement virtualization for long lists.

### MUST DO
- Define PropTypes with TypeScript interfaces.
- Handle loading and error states.
- Use semantic HTML elements.
- Implement keyboard navigation.
- Test components with React Testing Library.

### MUST NOT DO
- Mutate state directly.
- Use index as key in lists.
- Put business logic in components.
- Forget to clean up effects.
- Use inline styles for complex styling.
```

## Example 3: Module-Specific Instructions

**File:** `.github/instructions/Database_Module.instructions.md`

```markdown
---
applyTo: "modules/database/**"
name: "Database_Module_Instructions"
description: "Instructions for database module development"
---

## Database Module

### Mandatory Requirements
- **Update this file**: when database structure changes, update these instructions.

### Module Description
Handles all database operations including queries, migrations, and connection management.

### Module Structure
- `connection.py`: Database connection pooling and configuration.
- `models.py`: SQLAlchemy model definitions.
- `queries.py`: Reusable query functions.
- `migrations/`: Alembic migration scripts.

### Database Standards
- Use SQLAlchemy ORM for all database operations.
- Use connection pooling for production.
- Use prepared statements to prevent SQL injection.
- Implement proper transaction handling.

### Query Guidelines
- Use ORM queries instead of raw SQL.
- Index frequently queried columns.
- Use eager loading to avoid N+1 queries.
- Implement pagination for large result sets.
- Add query timeouts to prevent long-running queries.

### Migration Standards
- Create migration for every schema change.
- Write both upgrade and downgrade functions.
- Test migrations on development database first.
- Include meaningful migration messages.

### Error Handling
- Catch `SQLAlchemyError` exceptions.
- Log database errors with query context.
- Implement retry logic for transient failures.
- Use custom exception `DatabaseError` for application errors.

### Testing
- Use in-memory SQLite for unit tests.
- Use test fixtures for common data scenarios.
- Clean up test data after each test.
- Test both successful and error cases.

### MUST DO
- Close database connections in finally blocks.
- Use parameterized queries for dynamic values.
- Validate data before database operations.
- Add indexes for foreign key columns.

### MUST NOT DO
- Execute raw SQL from user input.
- Store sensitive data unencrypted.
- Commit database credentials to repository.
- Use SELECT * in production queries.
```

## Example 4: API Development Standards

**File:** `.github/instructions/API_Standards.instructions.md`

```markdown
---
applyTo: "api/**/*.py"
name: "API_Development_Standards"
description: "REST API development standards and patterns"
---

## API Development Standards

### Mandatory Requirements
- **Update this file**: when API standards change, update these instructions.

### API Design Principles
- Follow REST conventions.
- Use proper HTTP methods (GET, POST, PUT, DELETE).
- Return appropriate status codes.
- Use JSON for request and response bodies.
- Version APIs using URL path (`/api/v1/`).

### Endpoint Structure
```python
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1/users")

class UserCreate(BaseModel):
    email: str
    name: str

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    # Validate input
    # Process request
    # Return response
    return {"id": user_id, "email": user.email}
```

### Request Validation
- Use Pydantic models for request/response schemas.
- Validate all inputs before processing.
- Return `400 Bad Request` for invalid data.
- Include specific error messages.

### Response Format
- Use consistent JSON structure.
- Include metadata (pagination, total count).
- Return errors in standard format:
```json
{
  "error": "Resource not found",
  "code": "NOT_FOUND",
  "details": {}
}
```

### Authentication
- Use JWT tokens for authentication.
- Validate tokens on every protected endpoint.
- Return `401 Unauthorized` for missing/invalid tokens.
- Return `403 Forbidden` for insufficient permissions.

### Error Handling
- Catch all exceptions in endpoints.
- Return appropriate HTTP status codes.
- Log errors with request context.
- Never expose internal error details.

### Performance
- Implement caching for expensive operations.
- Use async/await for I/O operations.
- Add rate limiting to prevent abuse.
- Implement request timeouts.

### Documentation
- Document all endpoints with docstrings.
- Use OpenAPI/Swagger for API documentation.
- Include example requests and responses.
- Document error codes and meanings.

### MUST DO
- Validate all user inputs.
- Use HTTPS in production.
- Implement request logging.
- Add health check endpoint.
- Version breaking changes.

### MUST NOT DO
- Return stack traces in responses.
- Use GET requests for state-changing operations.
- Store tokens in URL parameters.
- Skip authentication checks.
- Return all database fields by default.
```

## Example 5: Documentation Standards

**File:** `.github/instructions/Documentation_Standards.instructions.md`

```markdown
---
applyTo: "docs/**/*.md"
name: "Documentation_Writing_Standards"
description: "Standards for writing project documentation"
---

## Documentation Writing Standards

### Mandatory Requirements
- **Update this file**: when documentation standards change, update these instructions.

### Writing Style
- Use present tense verbs (is, creates, returns).
- Write in second person (you) when addressing readers.
- Use active voice where possible.
- Write short, clear sentences (15-20 words average).
- Use simple words over complex alternatives.

### Grammar Rules
- Start sentences with verbs for instructions.
- Avoid hypotheticals (could, would, should).
- State facts directly without qualifiers.
- Use consistent terminology throughout.

### Structure
- Start with overview paragraph.
- Use headings to organize content (`##`, `###`).
- Include code examples for technical concepts.
- End with related resources or next steps.

### Markdown Formatting
- Use code blocks with language specification.
- Use inline code for `commands`, `variables`, `filenames`.
- Use **bold** for emphasis (sparingly).
- Use tables for structured comparisons.
- Include links to related documentation.

### Code Examples
- Keep examples minimal and focused.
- Include comments for complex logic.
- Show complete, runnable examples.
- Use realistic variable names.

### Technical Accuracy
- Test all code examples before publishing.
- Verify all links work.
- Keep documentation in sync with code.
- Note version-specific features.

### MUST DO
- Include table of contents for long documents.
- Add alt text for images.
- Use consistent heading hierarchy.
- Proofread for spelling and grammar.

### MUST NOT DO
- Use emojis in technical documentation.
- Write from first-person perspective.
- Include outdated screenshots.
- Use jargon without explanation.
```

## Example 6: Test Writing Standards

**File:** `.github/instructions/Test_Standards.instructions.md`

```markdown
---
applyTo: "tests/**/*.py"
name: "Test_Writing_Standards"
description: "Standards for writing unit and integration tests"
---

## Test Writing Standards

### Mandatory Requirements
- **Update this file**: when test standards change, update these instructions.

### Test Organization
- Place unit tests in `tests/unit/`.
- Place integration tests in `tests/integration/`.
- Mirror source directory structure.
- Name test files `test_<module_name>.py`.

### Test Structure
```python
import pytest
from mymodule import calculate_total

class TestCalculateTotal:
    """Tests for calculate_total function."""
    
    def test_calculates_sum_of_positive_numbers(self):
        # Arrange
        numbers = [1, 2, 3]
        
        # Act
        result = calculate_total(numbers)
        
        # Assert
        assert result == 6
    
    def test_handles_empty_list(self):
        result = calculate_total([])
        assert result == 0
```

### Naming Conventions
- Test functions: `test_<what_it_tests>_<expected_behavior>`
- Test classes: `Test<ClassBeingTested>`
- Use descriptive names that document behavior.

### Test Coverage
- Write tests for happy path cases.
- Write tests for edge cases.
- Write tests for error conditions.
- Aim for 80%+ code coverage.

### Fixtures
- Use pytest fixtures for common setup.
- Scope fixtures appropriately (function, class, module).
- Clean up resources in fixtures.

### Mocking
- Mock external dependencies (APIs, databases).
- Mock file system operations.
- Use `unittest.mock` or `pytest-mock`.
- Verify mock calls when testing interactions.

### Assertions
- Use specific assertions (`assertEqual`, `assertRaises`).
- Include descriptive error messages.
- Test one concept per test function.
- Use assertion helpers for complex checks.

### MUST DO
- Write tests before fixing bugs.
- Run tests before committing.
- Keep tests independent of each other.
- Use meaningful test data.

### MUST NOT DO
- Share state between tests.
- Use real databases or APIs in unit tests.
- Test implementation details.
- Write tests that depend on execution order.
```

## Example 8: Workflow Module (Hybrid XML+Markdown)

**File:** `.github/instructions/Workflow_Module.instructions.md`

````markdown
---
applyTo: "modules/workflow/**"
name: "Workflow_Orchestration_Instructions"
description: "Workflow engine with multi-phase execution and dependencies"
---

## Workflow Module

### Mandatory Requirements
- **Update this file**: when workflow logic changes, update these instructions.

### Module Description
Orchestrates multi-step workflows with state management, error recovery, and dependency tracking.

### Core Components
- `engine.py`: Main workflow execution engine
- `state.py`: State persistence and recovery
- `tasks.py`: Individual task definitions
- `scheduler.py`: Dependency resolution and task scheduling

<workflow_execution>
  <phase id="initialization">
    <step>Load workflow configuration from database</step>
    <step>Validate all required parameters present</step>
    <step>Check preconditions satisfied</step>
    <step>Initialize workflow state object</step>
  </phase>
  
  <phase id="planning" depends-on="initialization">
    <step>Build dependency graph from tasks</step>
    <step>Detect circular dependencies</step>
    <step>Calculate execution order using topological sort</step>
    <step>Estimate total execution time</step>
  </phase>
  
  <phase id="execution" depends-on="planning">
    <step>Execute tasks in dependency order</step>
    <step>Update state after each task completion</step>
    <step>Handle task failures with retry logic (max 3 attempts)</step>
    <step>Skip downstream tasks if dependency fails</step>
  </phase>
  
  <phase id="finalization" depends-on="execution">
    <step>Aggregate all task results</step>
    <step>Generate execution report</step>
    <step>Persist workflow state to database</step>
    <step>Trigger completion notifications</step>
    <step>Cleanup temporary resources</step>
  </phase>
</workflow_execution>

### Error Handling Strategy

<error_handling>
  <recoverable_errors>
    <error type="network_timeout">
      <action>Retry with exponential backoff (30s, 60s, 120s)</action>
    </error>
    <error type="rate_limit">
      <action>Wait for rate limit reset, then retry</action>
    </error>
    <error type="temporary_unavailable">
      <action>Pause workflow, resume when service available</action>
    </error>
  </recoverable_errors>
  
  <non_recoverable_errors>
    <error type="invalid_configuration">
      <action>Fail fast, notify admin, do not retry</action>
    </error>
    <error type="authorization_failed">
      <action>Stop workflow, require manual intervention</action>
    </error>
    <error type="data_validation_failed">
      <action>Fail task, log details, skip to finalization</action>
    </error>
  </non_recoverable_errors>
</error_handling>

### State Management
- Save state after each phase completion
- Implement checkpointing every 10 tasks
- Support workflow pause and resume
- Enable rollback to previous checkpoint

### MUST DO
- Validate workflow configuration before execution
- Save state after each phase completion
- Implement idempotent operations for retry safety
- Log all state transitions with timestamps
- Update progress metrics in real-time

### MUST NOT DO
- Skip state persistence between phases
- Execute dependent tasks before prerequisites complete
- Ignore task timeout configurations
- Run workflows without resource limits
````

## Example 9: Agent System Instructions (Complex XML)

**File:** `.github/instructions/Agent_System.instructions.md`

````markdown
---
applyTo: "modules/agents/**"
name: "Agent_System_Instructions"
description: "Multi-agent orchestration with tool calling and memory management"
---

## Agent System

### Mandatory Requirements
- **Update this file**: when agent architecture changes, update these instructions.

### Module Purpose
Implements multi-agent system with orchestrator, specialized agents, tool calling, and shared memory.

<agent_architecture>
  <orchestrator>
    <role>Coordinates multiple specialized agents</role>
    <responsibilities>
      <item>Route user requests to appropriate agents</item>
      <item>Aggregate results from multiple agents</item>
      <item>Manage conversation context and memory</item>
      <item>Handle tool invocation and result processing</item>
    </responsibilities>
    <tools>
      <tool name="code_analyzer">Analyze code structure and patterns</tool>
      <tool name="file_editor">Edit files with diff preview</tool>
      <tool name="terminal">Execute shell commands</tool>
      <tool name="search">Semantic search in codebase</tool>
    </tools>
  </orchestrator>
  
  <specialized_agents>
    <agent id="code-gen" type="generator">
      <role>Generate code based on specifications</role>
      <capabilities>
        <capability>Create new files from templates</capability>
        <capability>Generate unit tests</capability>
        <capability>Scaffold project structures</capability>
      </capabilities>
      <context_sources>
        <source>Project coding standards</source>
        <source>Existing code patterns</source>
        <source>Framework documentation</source>
      </context_sources>
    </agent>
    
    <agent id="code-review" type="analyzer">
      <role>Review code for quality and issues</role>
      <capabilities>
        <capability>Detect security vulnerabilities</capability>
        <capability>Check code style compliance</capability>
        <capability>Suggest performance improvements</capability>
      </capabilities>
      <tools>
        <tool name="linter">Run static analysis</tool>
        <tool name="security_scanner">Check for vulnerabilities</tool>
      </tools>
    </agent>
    
    <agent id="doc-writer" type="generator">
      <role>Generate and maintain documentation</role>
      <capabilities>
        <capability>Generate API documentation</capability>
        <capability>Create user guides</capability>
        <capability>Update CHANGELOG</capability>
      </capabilities>
    </agent>
  </specialized_agents>
</agent_architecture>

<communication_protocol>
  <message_format>
    <field name="sender_id">Agent UUID</field>
    <field name="receiver_id">Target agent UUID or "orchestrator"</field>
    <field name="message_type">request | response | notification</field>
    <field name="payload">JSON with type-specific data</field>
    <field name="context">Conversation context snapshot</field>
  </message_format>
  
  <routing_rules>
    <rule priority="1">
      <condition>Request contains "generate" or "create"</condition>
      <action>Route to code-gen agent</action>
    </rule>
    <rule priority="2">
      <condition>Request contains "review" or "check"</condition>
      <action>Route to code-review agent</action>
    </rule>
    <rule priority="3">
      <condition>Request contains "document" or "explain"</condition>
      <action>Route to doc-writer agent</action>
    </rule>
    <rule priority="4">
      <condition>No specific agent identified</condition>
      <action>Orchestrator handles directly</action>
    </rule>
  </routing_rules>
</communication_protocol>

<memory_management>
  <working_memory>
    <scope>Current conversation session</scope>
    <max_tokens>100000</max_tokens>
    <eviction_policy>Remove oldest messages when limit reached</eviction_policy>
  </working_memory>
  
  <long_term_memory>
    <storage>Vector database for semantic search</storage>
    <indexed_content>
      <item>Previous conversations</item>
      <item>Code patterns</item>
      <item>User preferences</item>
      <item>Project knowledge base</item>
    </indexed_content>
    <retrieval_strategy>
      <step>Embed user query</step>
      <step>Search for top 5 most relevant memories</step>
      <step>Inject into agent context</step>
    </retrieval_strategy>
  </long_term_memory>
</memory_management>

### Implementation Guidelines
- Use async/await for all agent communication
- Implement timeout handling (30s default, 5min max)
- Log all inter-agent messages for debugging
- Cache tool results to avoid redundant calls

### MUST DO
- Validate all tool parameters before invocation
- Update memory after each agent interaction
- Handle agent failures gracefully with fallbacks
- Implement rate limiting for external tool calls
- Track token usage per agent and conversation

### MUST NOT DO
- Call tools without parameter validation
- Allow infinite loops in agent communication
- Store sensitive data in long-term memory unencrypted
- Exceed context window limits without truncation
- Block event loop with synchronous operations
````
