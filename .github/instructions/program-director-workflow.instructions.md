---
name: "program-director-workflow"
description: "Orchestration loop lifecycle, scope decomposition, wave management, and stall detection for Program Director agent."
---

## Program Director Workflow Rules

### Orchestration Loop Lifecycle

The Program Director operates in a finite loop:

```
Project Understanding → [Analyze State → Decompose Scopes →
  Launch PLs → Collect Results → Evaluate]* → Closure
```

Each iteration of the bracketed section is called a **wave**. The loop continues
until termination conditions are met.

### Scope Decomposition Guidelines

1. **Partition by module boundaries**: prefer directory-level splits (e.g., `src/auth/` vs `src/frontend/`).
2. **No overlapping file ownership**: every file edited in a wave must belong to exactly one PL.
3. **Shared files rule**: files like README.md, CHANGELOG.md, project-todo that multiple PLs might need are assigned to ONE designated PL per wave, or updated by Program Director between waves.
4. **Dependency sequencing**: if scope A produces output that scope B consumes, place them in sequential waves, not the same wave.
5. **Balanced effort**: if one scope has 5x the work of another, split it or merge the smaller scope with documentation tasks.
6. **Maximum parallelism**: 2-4 PLs per wave. More than 4 increases coordination overhead without proportional benefit.

### Wave Management

- **Wave numbering**: sequential starting from 1.
- **Before each wave**: update Task Ledger with wave plan, update File Registry with scope assignments.
- **After each wave**: read all PL Progress Ledger sections, update Task Ledger with results, update Context Recovery block.
- **Between waves**: resolve conflicts, adjust scopes, compress journal if needed.

### Stall Detection Algorithm

```
stall_counter = 0

after each wave:
  net_progress = tasks_completed + files_meaningfully_changed
  if net_progress == 0:
    stall_counter += 1
  else:
    stall_counter = 0
  
  if stall_counter >= 2:
    TERMINATE with reason STALL
  elif stall_counter == 1:
    re-analyze blockers, adjust scope decomposition
```

### Termination Conditions

Program Director MUST terminate when ANY condition is true:

| Condition | Reason Code | Action |
| --------- | ----------- | ------ |
| All done criteria met | SUCCESS | Report completion to user |
| 2 consecutive zero-progress waves | STALL | Report blocking issues to user |
| Wave count reaches cap (default: 5) | MAX_WAVES | Report progress and remaining work |
| Unresolvable blocker requiring user input | BLOCKED | Report blocker and ask user |

### PL Launch Protocol

Every Project Lead launched by Program Director MUST receive:

1. **Identity**: unique name (PL-Alpha, PL-Beta, etc.) and wave number
2. **Scope**: explicit description + file/directory list
3. **Forbidden actions**: editing files outside scope
4. **Context recovery instructions**: read journal first, find own section
5. **Task description**: specific deliverables for this scope
6. **Journal protocol**: write only to own named section
7. **Done criteria**: scope-specific success conditions
8. **Relevant file paths**: task file, context file, journal path

### Post-Wave Review Checklist

After collecting all PL completion summaries:

- [ ] Read full Progress Ledger — verify each PL wrote a structured entry
- [ ] Spot-check 2-3 changed files for scope compliance
- [ ] Count tasks completed vs. planned
- [ ] List blockers reported by any PL
- [ ] Identify scope violations (if any)
- [ ] Update Task Ledger with wave results
- [ ] Update Context Recovery with current state
- [ ] Decide: CONTINUE or TERMINATE

### Constraints

- Program Director does NOT write code or perform reviews.
- Program Director does NOT edit Progress Ledger sections (those belong to PLs).
- Program Director does NOT launch subagents other than Project Lead (no direct use of code-reviewer, etc.).
- Each Project Lead retains full subagent orchestration privileges when launched by Program Director (nested orchestrator exception).
- Program Director communicates with user at wave boundaries — not during PL execution.
