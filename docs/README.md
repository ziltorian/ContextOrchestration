# Project Documentation

This folder contains project documentation. Organize it as needed for your project.

## Suggested Structure

```
docs/
├── README.md                  # This file — documentation overview
├── specification/             # Feature specifications and project concept
│   └── project-idea.md        # Project idea and concept description
├── api/                       # API documentation
│   └── endpoints.md           # REST API endpoints reference
└── architecture/              # Architecture decisions and diagrams
    └── overview.md            # High-level architecture overview
```

## How This Integrates with Context Orchestration

The `.github/instructions/Project_Docs_Context.instructions.md` file tells agents to read documentation from this folder before making changes. Update that instruction file to point to your actual documentation paths.

Agents will look here for:
- **Project context** — what the project does and how it works
- **Specifications** — what features should do (source of truth)
- **API contracts** — endpoint formats, request/response shapes
- **Architecture** — how components connect, key decisions and constraints
