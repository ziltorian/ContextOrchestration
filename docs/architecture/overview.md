# Architecture Overview

## High-Level Diagram

```text
{Replace with your actual architecture}

┌──────────┐     ┌──────────┐     ┌──────────┐
│  Client   │────▶│   API    │────▶│ Database │
└──────────┘     └────┬─────┘     └──────────┘
                      │
                      ▼
                ┌──────────┐
                │ Services │
                └──────────┘
```

## Components

### {Component 1}

**Responsibility:** {What this component does}  
**Location:** `{path/to/code}`  
**Depends on:** {Other components}

### {Component 2}

**Responsibility:** {What this component does}  
**Location:** `{path/to/code}`  
**Depends on:** {Other components}

## Key Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| {e.g., Database} | {e.g., PostgreSQL} | {e.g., Complex queries, ACID compliance} |
| {e.g., Auth} | {e.g., JWT} | {e.g., Stateless, works with microservices} |

## Data Flow

{Describe how data moves through the system for key operations.}
