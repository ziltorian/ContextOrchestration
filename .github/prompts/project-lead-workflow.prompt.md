---
name: project-lead-workflow
description: "Project Lead orchestration: execute a single task through research, planning, implementation, review, and closure."
argument-hint: "delivery goal, task-name, priority, done criteria"
agent: "Project-Lead"
---

Launch Project Lead to orchestrate a single task or feature from intake to closure.

<inputs>
- Delivery goal: ${input:delivery_goal}
- Task name: ${input:task_name}
- Priority: ${input:priority:normal}
- Done criteria: ${input:done_criteria}
- Constraints: ${input:constraints}
- Task file (optional): ${input:task_file}
- Context file (optional): ${input:context_file}
</inputs>

<goal>
Use Project Lead as the primary single-scope orchestrator: formalize the task if needed, perform research, produce or refine an implementation plan, delegate implementation, run the review gate, complete the mandatory audits, and close the task with updated artifacts.
</goal>

<constraints>
- This prompt is for Project Lead orchestration workflow, not for e2e test execution.
- If the task/context files do not exist, first follow the standard Project Lead intake flow to create them.
- Respect the full Project Lead workflow, including preliminary QA research, review gate after significant changes, and final dual audit.
- Keep the task scope atomic. Do not broaden into unrelated refactors.
- Use `project-lead-e2e.prompt.md` instead when the user specifically wants live e2e testing workflow.
</constraints>

<workflow>
  <phase id="1" name="intake-and-artifacts">
    <step id="1.1">Identify whether ${input:task_file} and ${input:context_file} already exist for ${input:task_name}.</step>
    <step id="1.2">If artifacts are missing, create or delegate creation of task/context artifacts before planning or implementation.</step>
    <step id="1.3">Log the delivery goal, priority, and done criteria in PROJECT_LEAD_JOURNAL.md following the current journal policy.</step>
  </phase>

  <phase id="2" name="research-and-planning">
    <step id="2.1">Run preliminary research through product-qa-scenario-analyst and any minimal factual analysis required for the task.</step>
    <step id="2.2">Create or update the implementation plan for ${input:task_name} before any production changes.</step>
    <step id="2.3">Use the plan to define a focused implementation scope and verification approach.</step>
  </phase>

  <phase id="3" name="implementation">
    <step id="3.1">Delegate implementation to the appropriate executor while preserving scope boundaries and required context.</step>
    <step id="3.2">If blocked by build, lint, import, or type failures, route through build-error-resolver for minimal unblock.</step>
    <step id="3.3">Keep the task journal and task context current as evidence accumulates.</step>
  </phase>

  <phase id="4" name="quality-gates">
    <step id="4.1">Run code-reviewer after significant changes.</step>
    <step id="4.2">If the scope is security-sensitive, run security-reviewer before the final audits.</step>
    <step id="4.3">Run the mandatory final dual audit: product-qa-scenario-analyst and integration-architect-auditor.</step>
  </phase>

  <phase id="5" name="closure">
    <step id="5.1">Close the task only after audit verdicts are READY.</step>
    <step id="5.2">Update closure artifacts such as CHANGELOG.md, implementation status, and task tracking files as required by the current workflow.</step>
    <step id="5.3">Report final delivery summary with completed scope, residual risks, and next actions if any remain.</step>
  </phase>
</workflow>