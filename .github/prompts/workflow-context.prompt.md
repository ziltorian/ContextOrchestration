---
name: workflow-context
description: "Short prompt for executing workflow based on .instructions.md and context files"
---

<workflow>
  <tasks>
    <step order="0">
    Open the file in full to study tasks and application concept:
    1. Master plan `.github\implementations\00_MASTER_MVP_PLAN.instructions.md`
    2. Completed plans `*COMPLETED.instructions.md`
    3. Project documentation: `docs/*`
    4. Skills for task execution: `.github/skills/*`
    </step>
    <step order="1">
    Use the file attached to the context: `.github/implementations/*.instructions.md` or the next phase of an incomplete plan as the task source
    </step>
    <step order="2">
    Use the file `*context.md` (if present) as context for task execution
    </step>
    <step order="3">
    Execute tasks in the order they appear, using the provided context
    </step>
    <step order="4">
    Mark completed tasks: replace checkbox with `[x]`, follow rules in `Mark_Tasks_As_Done.instructions.md`
    </step>
    <step order="5">
    After all tasks are complete, create `Phase{id}_COMPLETED.instructions.md`
    </step>
    <step order="6">
    Synchronize project documentation `docs/*` with the implementation.
    </step>
  </tasks>
  <knowledge>
    <source> path="docs/*" Main project documentation, concept, architecture</source>
    <source> path="CHANGELOG.md" Project change log</source>
    <source> path=".github/instructions/Project_structure.instructions.md" Project structure for coding agent context</source>
    <source> path=".github/skills/*" Skills for task execution</source>
    <source> path="mvp-recommendations-and-release.md" MVP recommendations and release notes</source>
  </knowledge>
</workflow>
