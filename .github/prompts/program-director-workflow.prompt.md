---
name: program-director-workflow
description: "Program Director orchestration: decompose a project into scopes, launch parallel Project Leads, and iterate waves until completion."
argument-hint: "project goal, docs path, max Project Leads per wave, done criteria"
agent: "Program-Director"
---

Launch Program Director to orchestrate parallel Project Lead agents for full multi-scope project delivery.

<inputs>
- Project goal: ${input:project_goal}
- Documentation root: ${input:docs_root:docs/}
- Max parallel Project Leads per wave: ${input:max_project_leads:3}
- Done criteria: ${input:done_criteria}
- Task file: ${input:task_file}
- Context file: ${input:context_file}
</inputs>

<goal>
Orchestrate full project delivery through iterative waves of parallel Project Leads. Each wave decomposes remaining work into independent scopes, assigns named Project Leads with strict file registries, launches the whole wave in one parallel batch when scopes are independent, verifies results through approved audit subagents, and continues until formal termination conditions are met.
</goal>

<constraints>
- Each Project Lead gets a unique name (Project-Lead-Alpha, Project-Lead-Beta, etc.) and an explicit file scope.
- Project Leads work independently — they cannot communicate with each other during a wave.
- Program Director cannot interrupt or redirect a Project Lead mid-wave.
- Maximum 5 waves before forced termination with a status report.
- Stall detection: if 2 consecutive waves show zero progress, terminate with STALL status.
- File scope conflicts must be resolved before launching a wave, not during.
- Program Director reads repository docs/specs, task/context artifacts, and the journal directly, but delegates broad project/code analysis and post-wave verification to approved read-only subagents.
- Canonical task/context artifacts are mandatory. Input handoff text narrows scope and wave metadata only; it never replaces task/context files.
- Closure artifacts are routed through implementation-completion-reporter rather than a Project Lead or direct CHANGELOG editing in this prompt.
</constraints>

<workflow>
  <phase id="1" name="pre-flight">
    <step id="1.1">Read project documentation from ${input:docs_root} to understand the project scope and architecture.</step>
    <step id="1.2">Read PROJECT_LEAD_JOURNAL.md to check for prior wave history. If fresh start, initialize the Task Ledger.</step>
    <step id="1.3">Read the canonical task file and context file. If either artifact is missing, recover/create it before any wave launch or terminate as BLOCKED.</step>
    <step id="1.4">Use approved research subagents for project/code analysis rather than manually sweeping code files.</step>
  </phase>

  <phase id="2" name="scope-decomposition">
    <step id="2.1">List all remaining tasks from project-todo, task files, and documentation gaps.</step>
    <step id="2.2">Group tasks into independent scopes with no overlapping files.</step>
    <step id="2.3">Assign each scope to a named Project Lead. Write the File Registry to PROJECT_LEAD_JOURNAL.md.</step>
    <step id="2.4">Update Context Recovery section with current project state summary.</step>
  </phase>

  <phase id="3" name="wave-execution">
    <step id="3.1">If multiple independent scopes exist, launch all Project Leads for the current wave in one parallel batch using runSubagent with agentName: Project-Lead. Use sequential launch only for a single remaining scope or a documented dependency chain.</step>
    <step id="3.2">Each Project Lead handoff includes: assigned name, scope, file registry, forbidden actions, context recovery instructions, journal protocol, wave number, and canonical task/context file paths.</step>
    <step id="3.3">Wait for all Project Leads to complete and collect their summaries.</step>
  </phase>

  <phase id="4" name="post-wave-review">
    <step id="4.1">Read PROJECT_LEAD_JOURNAL.md Progress Ledger to assess each Project Lead's outcome.</step>
    <step id="4.2">Run approved verification subagents for the completed wave to assess scope compliance, remaining backlog/spec gaps, and delivery quality.</step>
    <step id="4.3">Update Task Ledger with completed items, verification evidence, and remaining work.</step>
    <step id="4.4">Run stall detection: compare progress against previous wave.</step>
  </phase>

  <phase id="5" name="continue-or-terminate">
    <step id="5.1">If all done criteria are met and verification shows no unfinished backlog/spec work → proceed to closure.</step>
    <step id="5.2">If remaining tasks, unresolved verification findings, or spec gaps exist and no stall is active → return to phase 2 for the next wave.</step>
    <step id="5.3">If stall detected → terminate with STALL status and remaining items list.</step>
  </phase>

  <phase id="6" name="closure">
    <step id="6.1">Write final wave summary to PROJECT_LEAD_JOURNAL.md Task Ledger.</step>
    <step id="6.2">Route closure artifacts through implementation-completion-reporter using the canonical task/context artifacts for the project scope.</step>
    <step id="6.3">Report final status with delivery summary, remaining work, and termination reason.</step>
  </phase>
</workflow>