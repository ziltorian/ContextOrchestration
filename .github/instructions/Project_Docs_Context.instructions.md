---
applyTo: "**"
name: "Project_Docs_Context"
description: "Mandatory reading of documentation from docs/ before planning and changing code"
---

## CRITICAL REQUIREMENT

All project documentation is located in the `docs/` folder at the project root with the following structure:

```text
docs/
├── *.md                    # Core documentation (concept, architecture, stack)
├── specification/          # Detailed feature specifications and addenda
├── api/                    # API documentation and specifications
└── architecture/           # Architectural decisions and diagrams
```

**MANDATORY** before planning architecture, writing code, or making changes:
1. Identify relevant documentation files from the list below
2. Open and study their content
3. Use documentation as the primary source of truth about the project

**DO NOT** make technical decisions without first reading the corresponding documentation.

## Documentation Map

### Core documentation `docs/`

- `README.md` — Main project overview: concept, architecture, stack, development priorities. **Must be read first.**
- Relevant `docs/*.md` — Feature lists, user scenarios, architectural diagrams, integration catalogs
- `docs/specification/project-idea.md` — Project idea and concept specification

### API

- `docs/api/endpoints.md` — REST API documentation with request/response formats and error handling

## How to Use

- Before starting a task, determine its goal and select 2-4 relevant documents (must start with: `README.md`).
- Read the selected files in full and highlight key requirements, constraints, and expected results.
- Create a brief action checklist: input data, expected behavior, error scenarios, acceptance criteria.
- For architectural or integration decisions, refer to files in Architecture and corresponding specifications in Specifications.
