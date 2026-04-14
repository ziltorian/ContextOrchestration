# Project Lead Journal

<!-- 
  Dual-Ledger Template for Project Orchestration
  
  This journal serves three purposes:
  1. Coordination backbone for parallel Project Lead agents
  2. Context recovery source for agents starting with clean context
     3. Decision log for single-Project-Lead and multi-Project-Lead orchestration modes
  
  Structure:
     - Task Ledger: project plan, goals, facts (written by Program Director or single Project Lead)
  - File Registry: file/module ownership per wave (written by Program Director)
  - Context Recovery: compact state summary for fresh-context agents
     - Progress Ledger: per-Project-Lead named sections with structured entries (written by Project Leads)
  
  Rules:
     - Each Project Lead writes ONLY to its own named section in the Progress Ledger
     - Task Ledger and File Registry are written ONLY by Program Director (or single Project Lead in solo mode)
  - All entries are append-only within a wave; Program Director may summarize between waves
  - Use structured fields — not freeform prose — for machine-parseable context recovery
-->

---

## Task Ledger

<!-- Written by Program Director (or single Project Lead in solo mode).
     Contains: project goal, known facts, overall plan, done criteria, wave history. -->

### Project

- **Name:** {project name}
- **Goal:** {one-sentence project goal}
- **Done criteria:** {measurable conditions for release quality}

### Known Facts
<!-- Verified facts from project documentation. Update as new facts are discovered. -->
- {fact 1}
- {fact 2}

### Overall Plan
<!-- High-level phase breakdown. Updated by Program Director between waves. -->
1. {phase 1}
2. {phase 2}
3. {phase 3}

### Wave History

#### Wave {N} — Plan

- **Date:** YYYY-MM-DD
- **Scope assignments:** see File Registry below
- **Parallel Project Leads:** {count}
- **Target deliverables:** {list}

#### Wave {N} — Results

- **Tasks completed:** X/Y
- **Verification:** {QA verdict} / {Architecture verdict}
- **Blockers:** {list or "none"}
- **Scope violations:** {list or "none"}
- **Net progress:** HIGH / LOW / ZERO
- **Remaining backlog/spec gaps:** {list or "none"}
- **Decision:** CONTINUE / TERMINATE — {reason tied to verification and remaining work}

---

## File Registry

<!-- Written by Program Director before each wave.
     Maps files/directories to the Project Lead that owns them for the current wave.
     Project Leads MUST check this registry before editing any file. -->

| File / Directory | Owned By | Wave | Notes |
| ---------------- | -------- | ---- | ----- |
| {src/auth/} | {Project-Lead-Alpha} | {1} | {exclusive} |
| {src/frontend/} | {Project-Lead-Beta} | {1} | {exclusive} |
| {README.md} | {Project-Lead-Alpha} | {1} | {shared — designated writer} |

---

## Context Recovery

<!-- Compact summary of current project state.
     Written by Program Director after each wave.
     Purpose: provide enough context for a fresh-context Project Lead to understand
     where the project stands and what its scope means. -->

### Current State (as of Wave {N})

- **Overall progress:** {X of Y tasks complete}
- **Completed areas:** {list of finished modules/features}
- **In-progress areas:** {list of active work}
- **Blocked items:** {list with reasons}
- **Key decisions made:** {list of architectural/design decisions}
- **Known risks:** {list}

---

## Progress Ledger

<!-- Per-Project-Lead named sections. Each Project Lead writes ONLY to its own section.
     Read other sections for awareness — NEVER edit them.
     Append new entries at the bottom of your section. -->

### {Project-Lead-Name} (e.g., Project-Lead-Alpha)

#### YYYY-MM-DD — Wave {N}

- **Current stage:** {intake | research | planning | implementation | verification | closure | blocked}
- **Scope:** {assigned scope description}
- **Active goal:** {what this Project Lead is working on}
- **Delegated scope:** {subagents invoked and their assignments}
- **Decisions and rationale:** {key decisions made and why}
- **Evidence summary:** {files read, specs referenced, audit verdicts}
- **Files changed:** {list of files created/modified}
- **Tasks completed:** {list of completed task IDs or descriptions}
- **Blockers:** {issues requiring attention, especially out-of-scope dependencies}
- **Current status:** IN_PROGRESS | BLOCKED | READY | NOT READY
- **Next action:** {concrete next step}

---

<!-- Single-Project-Lead Mode: If only one Project Lead is active (no Program Director),
     use a single unnamed section in the Progress Ledger with the same field structure.
     The Task Ledger and File Registry sections can be omitted or left as templates. -->
