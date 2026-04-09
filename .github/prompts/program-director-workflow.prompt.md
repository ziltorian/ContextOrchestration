---
name: program-director-workflow
description: "Program Director orchestration: decompose a project into scopes, launch parallel Project Leads, and iterate waves until completion."
argument-hint: "project goal, docs path, max PLs per wave, done criteria"
agent: "Program-Director"
---

Launch Program Director to orchestrate parallel Project Lead agents for full multi-scope project delivery.

<inputs>
- Project goal: ${input:project_goal}
- Documentation root: ${input:docs_root:docs/}
- Max parallel PLs per wave: ${input:max_pls:3}
- Done criteria: ${input:done_criteria}
- Task file (optional): ${input:task_file}
- Context file (optional): ${input:context_file}
</inputs>

<goal>
Orchestrate full project delivery through iterative waves of parallel Project Leads. Each wave decomposes remaining work into independent scopes, assigns named PLs with strict file registries, launches them in parallel, reviews results, and continues until all tasks are complete or stall is detected.
</goal>

<constraints>
- Each PL gets a unique name (PL-Alpha, PL-Beta, etc.) and an explicit file scope.
- PLs work independently — they cannot communicate with each other during a wave.
- Program Director cannot interrupt or redirect a PL mid-wave.
- Maximum 5 waves before forced termination with a status report.
- Stall detection: if 2 consecutive waves show zero progress, terminate with STALL status.
- File scope conflicts must be resolved before launching a wave, not during.
</constraints>

<workflow>
  <phase id="1" name="pre-flight">
    <step id="1.1">Read project documentation from ${input:docs_root} to understand the project scope and architecture.</step>
    <step id="1.2">Read PROJECT_LEAD_JOURNAL.md to check for prior wave history. If fresh start, initialize the Task Ledger.</step>
    <step id="1.3">Identify or read the task file and context file (if provided).</step>
  </phase>

  <phase id="2" name="scope-decomposition">
    <step id="2.1">List all remaining tasks from project-todo, task files, and documentation gaps.</step>
    <step id="2.2">Group tasks into independent scopes with no overlapping files.</step>
    <step id="2.3">Assign each scope to a named PL. Write the File Registry to PROJECT_LEAD_JOURNAL.md.</step>
    <step id="2.4">Update Context Recovery section with current project state summary.</step>
  </phase>

  <phase id="3" name="wave-execution">
    <step id="3.1">Launch up to ${input:max_pls} Project Leads in parallel using runSubagent with agentName: Project-Lead.</step>
    <step id="3.2">Each PL handoff includes: assigned name, scope, file registry, forbidden actions, context recovery instructions, journal protocol, and wave number.</step>
    <step id="3.3">Wait for all PLs to complete and collect their summaries.</step>
  </phase>

  <phase id="4" name="post-wave-review">
    <step id="4.1">Read PROJECT_LEAD_JOURNAL.md Progress Ledger to assess each PL's outcome.</step>
    <step id="4.2">Verify file changes against the File Registry for scope violations.</step>
    <step id="4.3">Update Task Ledger with completed items and remaining work.</step>
    <step id="4.4">Run stall detection: compare progress against previous wave.</step>
  </phase>

  <phase id="5" name="continue-or-terminate">
    <step id="5.1">If all tasks complete → proceed to closure.</step>
    <step id="5.2">If remaining tasks exist and no stall → return to phase 2 for next wave.</step>
    <step id="5.3">If stall detected → terminate with STALL status and remaining items list.</step>
  </phase>

  <phase id="6" name="closure">
    <step id="6.1">Write final wave summary to PROJECT_LEAD_JOURNAL.md Task Ledger.</step>
    <step id="6.2">Delegate closure to a Project Lead in the final wave, or write CHANGELOG entry directly.</step>
    <step id="6.3">Report READY status with delivery summary.</step>
  </phase>
</workflow>