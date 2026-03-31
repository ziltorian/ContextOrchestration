---
name: 'Mark_Tasks_As_Done'
description: 'Brief instruction: how to properly mark completed tasks in plans and todo files'
---

## Task Marking

### REQUIRED
- Apply these rules to files `.github/implementations/*implementation.instructions.md` and `SubAgents-tasks/project-todo.instructions.md`.
- Before replacing a checkbox with `[x]`, verify sufficient evidence of completion: implemented diff, confirmed verification, and compliance with task criteria.
- For a completed task, replace the checkbox with `[x]` and preserve the original HTML comment with `id`, if present.
- Keep no more than one item in `[/]` state; all other items must be only `[ ]` or `[x]`.
- If a task is cancelled, do not delete it: mark as `[x]` and add `title="cancelled"` to the HTML comment, if a comment is used for the identifier.
- If evidence is insufficient or the task is partially completed, do not mark it as done; keep the current status and explicitly state in the report that the task is not completed and cannot be marked as done.
- When changing the checkbox format or plan structure, update this instruction along with the change.

### FORBIDDEN
- Do not delete tasks from the plan or todo file just to hide their status.
- Do not change or delete `id` in HTML comments of already existing tasks.
- Do not leave multiple active `[/]` items in a single file.

### Commit Message
- Use the commit message: `Plan updated: completed tasks marked`.
