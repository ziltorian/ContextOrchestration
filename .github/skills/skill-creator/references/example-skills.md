# Example Agent Skills

Real-world examples from the Anthropic skills repository demonstrating best practices.

## Example 1: PDF Processing Skill

**Use case:** Extract text and tables from PDFs, fill forms, merge documents

**Directory:** `pdf/`

### SKILL.md Structure

```yaml
---
name: pdf
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF documents, extracting data, filling forms, or combining PDFs.
license: Apache-2.0
---

# PDF Processing

Extract text, tables, and images from PDFs. Fill forms, merge documents, and manipulate PDF files.

## Quick Start

Extract text from a PDF:
[code example using pdfplumber]

## Core Capabilities

1. Text Extraction
2. Table Parsing
3. Form Filling
4. PDF Merging
5. Page Manipulation

## References

- See references/REFERENCE.md for complete API documentation
- See references/EXAMPLES.md for common patterns
```

### Key Features

- Focused on one document type (PDFs)
- Clear description with multiple trigger keywords
- Progressive disclosure: quick start in SKILL.md, details in references
- Concrete workflows with code examples

---

## Example 2: DOCX Processing Skill

**Use case:** Create, edit, and analyze Word documents

**Directory:** `docx/`

### SKILL.md Structure

```yaml
---
name: docx
description: Comprehensive document creation, editing, and analysis with support for tracked changes, comments, formatting preservation, and text extraction. Use when working with .docx files.
---

# DOCX Processing

Professional document creation and editing for Word files.

## Core Workflows

### Create New Documents
[step-by-step instructions]

### Edit Existing Documents
[instructions with code examples]

### Extract Content
[extraction patterns]

## Advanced Features

- Tracked changes and comments
- Complex formatting preservation
- Template-based generation

## References

See references/ directory for detailed examples and API documentation.
```

### Key Features

- Comprehensive description covering all use cases
- Structured workflows from simple to advanced
- References external files for detailed documentation

---

## Example 3: PPTX Skill

**Use case:** Create and modify PowerPoint presentations

**Directory:** `pptx/`

### SKILL.md Structure

```yaml
---
name: pptx
description: Create slide decks, pitch decks, presentations. Use when working with .pptx files, slides, decks, or presentation creation.
---

# PowerPoint Processing

Create professional presentations with slides, layouts, and formatting.

## Creating Presentations

### From Scratch
[instructions for new presentations]

### From Templates
[using template files in assets/]

## Modifying Existing

- Add/remove slides
- Update content
- Apply themes
- Insert images and charts

## Best Practices

[guidelines for professional presentations]
```

### Key Features

- Multiple trigger words (pptx, slides, decks, presentations)
- Asset directory for templates
- Both creation and modification workflows

---

## Example 4: GitHub Actions Debugging Skill

**Use case:** Debug failing CI/CD workflows

**Directory:** `github-actions-debugging/`

### SKILL.md Structure

```yaml
---
name: github-actions-debugging
description: Debug failing GitHub Actions workflows. Use when asked to troubleshoot CI/CD failures or analyze workflow runs.
---

# GitHub Actions Debugging

Systematic approach to debugging failing workflows.

## Debugging Process

1. List recent workflow runs
2. Identify failed jobs
3. Analyze failure logs
4. Reproduce locally
5. Fix and verify

## Common Issues

- Dependency conflicts
- Environment variables
- Permission problems
- Timeout errors

## Tools Integration

Uses GitHub MCP Server tools for workflow analysis.
```

### Key Features

- Domain-specific (GitHub Actions)
- Process-oriented workflow
- Integrates with external tools (MCP Server)
- Covers common failure patterns

---

## Example 5: API Integration Skill

**Use case:** Work with REST APIs

**Directory:** `api-integration/`

### SKILL.md Structure

```yaml
---
name: api-integration
description: Work with REST APIs including authentication, request handling, response parsing, and error management. Use for HTTP requests, API calls, or web service integration.
---

# API Integration

Comprehensive REST API interaction patterns.

## Authentication

### API Keys
[implementation examples]

### OAuth 2.0
[OAuth flow examples]

### JWT Tokens
[token handling patterns]

## Request Patterns

- GET requests with parameters
- POST with JSON bodies
- File uploads
- Pagination handling

## Error Handling

[common errors and retry strategies]

## References

See references/API_PATTERNS.md for complete examples.
```

### Key Features

- Multiple authentication methods
- Reusable request patterns
- Error handling guidance
- Detailed reference file

---

## Example 6: Data Analysis Skill

**Use case:** Analyze datasets and generate insights

**Directory:** `data-analysis/`

### SKILL.md Structure

```yaml
---
name: data-analysis
description: Analyze datasets, generate statistics, create visualizations, and extract insights. Use for data exploration, statistical analysis, or when working with CSV/Excel files.
compatibility: Requires Python 3.8+ with pandas, numpy, matplotlib
---

# Data Analysis

Statistical analysis and visualization workflows.

## Data Loading

[examples for CSV, Excel, JSON]

## Common Analyses

1. Descriptive statistics
2. Correlation analysis
3. Trend detection
4. Outlier identification

## Visualization

[chart creation examples]

## Scripts

- scripts/load_data.py - Universal data loader
- scripts/analyze.py - Statistical analysis
- scripts/visualize.py - Chart generation
```

### Key Features

- Explicitly lists dependencies in compatibility field
- Includes ready-to-use scripts
- Progressive complexity (loading → analysis → visualization)

---

## Example 7: Testing Skill

**Use case:** Generate and run tests

**Directory:** `testing/`

### SKILL.md Structure

```yaml
---
name: testing
description: Generate unit tests, integration tests, and test fixtures. Use when creating tests, improving test coverage, or debugging test failures.
---

# Testing Workflows

Comprehensive test generation and execution.

## Unit Tests

### Test Generation
[patterns for different frameworks]

### Mocking
[mock object creation]

### Assertions
[common assertion patterns]

## Integration Tests

[end-to-end test examples]

## Test Fixtures

[fixture creation and management]

## Coverage Analysis

[coverage improvement strategies]
```

### Key Features

- Framework-agnostic patterns
- Multiple test types
- Practical examples for common scenarios

---

## Common Patterns Across Examples

### 1. Clear, Keyword-Rich Descriptions

All examples include:

- What the skill does
- When to use it
- Specific trigger keywords

### 2. Progressive Disclosure

Structure:

- Quick start / common use case first
- Core capabilities outlined
- Detailed documentation in references/

### 3. Concrete Examples

Every skill includes:

- Code examples
- Step-by-step workflows
- Real-world scenarios

### 4. Focused Scope

Each skill does one thing well:

- PDF processing (not "document processing")
- API integration (not "web development")
- Testing (not "quality assurance")

### 5. Supporting Files Organization

**scripts/** - When to use:

- Same code rewritten repeatedly
- Deterministic operations needed
- Complex logic that benefits from pre-testing

**references/** - When to use:

- Detailed API documentation
- Extended examples
- Domain-specific knowledge

**assets/** - When to use:

- Templates for output files
- Boilerplate code structures
- Static resources used in generation

### 6. Universal Applicability

Skills teach:

- ✅ "How to work with PDFs"
- ❌ "How to process our company's invoices"

Skills are project-agnostic and reusable.

## Anti-Patterns to Avoid

### ❌ Overly Broad Skills

```yaml
name: development-helper
description: Helps with coding tasks
```

Too vague - create focused skills instead.

### ❌ Project-Specific Skills

```yaml
name: acme-deployment
description: Deploy to Acme Corp's infrastructure
```

Not reusable - teach platform skills (Kubernetes, Docker) instead.

### ❌ Poor Descriptions

```yaml
description: PDF stuff
```

Missing triggers and specifics.

### ❌ Everything in SKILL.md

Don't put 1000+ lines in SKILL.md - use references/.

### ❌ Hardcoded Values

```python
API_KEY = "sk-1234567890"  # Never do this
BASE_URL = "https://acme.internal"  # Project-specific
```

## Composability Example

Skills work together automatically:

**User request:** "Analyze this PDF invoice and create a summary presentation"

**Skills activated:**

1. `pdf` - Extract data from PDF
2. `data-analysis` - Analyze extracted data
3. `pptx` - Create presentation with findings

Each skill contributes its specialized capability to solve the complete task.

## References

- Full example repository: <https://github.com/anthropics/skills>
- More examples: <https://github.com/github/awesome-copilot>
