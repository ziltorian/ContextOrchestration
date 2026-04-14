---
name: "program-director-workflow"
description: "Orchestration loop lifecycle, scope decomposition, wave management, and stall detection for Program Director agent."
---

## Program Director Workflow Rules

### Orchestration Loop Lifecycle

The Program Director operates in a finite loop:

```
Project Understanding (docs/specs self-study + delegated research) →
  [Analyze State → Decompose Scopes → Launch Project Leads batch →
  Collect Results → Verification audits → Evaluate]* → Closure
```

Each iteration of the bracketed section is called a **wave**. The loop continues
until termination conditions are met.

### Scope Decomposition Guidelines

1. **Partition by module boundaries**: prefer directory-level splits (e.g., `src/auth/` vs `src/frontend/`).
2. **No overlapping file ownership**: every file edited in a wave must belong to exactly one Project Lead.
3. **Shared files rule**: files like README.md, CHANGELOG.md, project-todo that multiple Project Leads might need are assigned to ONE designated Project Lead per wave, or updated by Program Director between waves.
4. **Dependency sequencing**: if scope A produces output that scope B consumes, place them in sequential waves, not the same wave.
5. **Balanced effort**: if one scope has 5x the work of another, split it or merge the smaller scope with documentation tasks.
6. **Maximum parallelism**: 2-4 Project Leads per wave. More than 4 increases coordination overhead without proportional benefit.
7. **Canonical artifact continuity**: each scope in a wave must reference a canonical task/context pair. Program Director handoff text narrows scope and wave metadata, but never replaces those artifacts.

### Wave Management

- **Wave numbering**: sequential starting from 1.
- **Before each wave**: read repository docs/specs and backlog artifacts directly, run approved research subagents for project/code analysis as needed, update Task Ledger with wave plan, and update File Registry with scope assignments.
- **Wave launch rule**: if more than one independent scope exists, launch all Project Leads for that wave in one parallel batch. Sequential launch is allowed only when one scope remains or a documented dependency forces serialization.
- **After each wave**: read all Project Lead Progress Ledger sections, run approved verification subagents, update Task Ledger with results and verification evidence, update Context Recovery block, then decide continue vs terminate.
- **Between waves**: resolve conflicts, adjust scopes, and rescan backlog/specification gaps before declaring success.

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
| All done criteria met AND verification confirms no unfinished backlog/spec work remains | SUCCESS | Route formal closure, then report completion to user |
| 2 consecutive zero-progress waves | STALL | Report blocking issues to user |
| Wave count reaches cap (default: 5) | MAX_WAVES | Report progress and remaining work |
| Unresolvable blocker requiring user input | BLOCKED | Report blocker and ask user |

### Project-Lead Launch Protocol

Every Project Lead launched by Program Director MUST receive:

1. **Identity**: unique name (Project-Lead-Alpha, Project-Lead-Beta, etc.) and wave number
2. **Scope**: explicit description + file/directory list
3. **Forbidden actions**: editing files outside scope
4. **Context recovery instructions**: read journal first, find own section
5. **Task description**: specific deliverables for this scope
6. **Journal protocol**: write only to own named section
7. **Done criteria**: scope-specific success conditions
8. **Relevant file paths**: canonical task file, canonical context file, journal path
9. **Artifact rule**: if the canonical task/context files are missing, Program Director must create or recover them before wave launch or terminate that scope as BLOCKED. The handoff prompt never substitutes for those artifacts.

### Post-Wave Review Checklist

After collecting all Project Lead completion summaries:

- [ ] Read full Progress Ledger — verify each Project Lead wrote a structured entry
- [ ] Run approved verification subagents for the completed wave: `product-qa-scenario-analyst` and `integration-architect-auditor`; add `analyze-project` only when factual gaps remain
- [ ] Count tasks completed vs. planned
- [ ] List blockers reported by any Project Lead
- [ ] Identify scope violations (if any)
- [ ] Check remaining backlog items and unimplemented specification requirements before considering `SUCCESS`
- [ ] Update Task Ledger with wave results
- [ ] Record verification evidence and verdicts in the Task Ledger / Context Recovery summary
- [ ] Update Context Recovery with current state
- [ ] Decide: CONTINUE or TERMINATE

### Constraints

- Program Director does NOT write code or perform direct implementation.
- Program Director does NOT edit Progress Ledger sections (those belong to Project Leads).
- Program Director may launch only the approved delegation set for this repository contract: `Project-Lead`, `analyze-project`, `product-qa-scenario-analyst`, `integration-architect-auditor`, and `implementation-completion-reporter`.
- Program Director reads repository docs/specs, task artifacts, context artifacts, and the journal directly, but delegates broad project/code analysis and post-wave verification to the approved research/audit subagents rather than manually sweeping code.
- When editing prompts, instructions, agent files, or skills as part of orchestration work, also consult `.github/skills/prompt-engineering/SKILL.md`.
- Each Project Lead retains full subagent orchestration privileges when launched by Program Director (nested orchestrator exception).
- Program Director communicates with the user at wave boundaries and at formal termination, not in place of the next required wave.
