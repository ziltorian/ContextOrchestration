---
name: feature-implementation
description: "Complex task implementation: subagent research → implementation plan → step-by-step execution with task marking."
argument-hint: "optional: short task description"
---

You are about to **implement a complex task**.

## Input Parameters

- **What to implement:** ${input:task_description}
- **Context (documentation/files for review):** ${input:context_sources}
  > Examples: `docs/specification/*.md`, `backend/src/module/`, `specific_file.md`
- **Where to save the implementation plan:** ${input:plan_path}
  > Example: `.github/implementations/phase_X_feature.instructions.md`

---

<workflow>

  <phase id="1" name="RESEARCH — Subagent Investigation">
    <description>
      Study documentation and current code state using multiple subagents.
      Goal — gather enough information for planning without overflowing the context.
    </description>
    <constraint>Each subagent must return no more than 100 lines — only key facts and directions for changes.</constraint>
    <steps>
      <step id="1.1">
        <action>
          Identify 2–4 independent research areas for the task.
          Typical areas: specification/documentation, current code (target module), adjacent modules and dependencies, tests and configuration.
        </action>
      </step>
      <step id="1.2">
        <action>
          Run subagents sequentially, not in parallel — one per each area.
          For each subagent formulate: what to study, in which files/folders, what question to answer.
          Subagent task template:
        </action>
        <subagent_prompt_template>
          Investigate: {source_path}
          Topic: {topic}
          Question: {specific_question}
          Response format: structured list of facts, maximum 100 lines.
          DO NOT include full code listings — only signatures, class/method names, key patterns.
        </subagent_prompt_template>
      </step>
      <step id="1.3">
        <action>
          Collect results from all subagents.
          Highlight: key dependencies, files to change, architectural constraints, existing patterns.
        </action>
      </step>
    </steps>
    <output>Structured task summary: what exists, what needs to change, where.</output>
  </phase>

  <phase id="2" name="PLAN — Creating the Implementation Plan">
    <description>
      Based on research results, create an implementation plan document (~10,000 characters).
      The document serves as the single source of truth for the duration of the task.
    </description>
    <steps>
      <step id="2.1">
        <action>
          Create a plan file at path ${input:plan_path} with the following structure:
        </action>
        <plan_structure>
          ## Goal
          Brief (2–4 sentences) description of the task and expected outcome.

          ## Background / Context
          Problem description, architectural context, data from subagents.
          Key files, patterns, dependencies, constraints.

          ## Proposed Changes
          Groups of changes by modules/topics.
          Each item marked [NEW] or [CHANGE].
          For each file: path, change type, brief description.

          ## Tasks
          List of tasks grouped by topics.
          Format for each task: `- [ ] task description`
        </plan_structure>
      </step>
      <step id="2.2">
        <action>
          Verify the plan for completeness:
          — Are all dependencies accounted for?
          — Does the task order account for dependencies (base modules first, then high-level)?
          — Are there tasks for tests?
          — Are there tasks for documentation?
        </action>
      </step>
    </steps>
    <output>Implementation plan file at path ${input:plan_path}.</output>
  </phase>

  <phase id="3" name="EXECUTE — Step-by-Step Execution">
    <description>
      Execute tasks from the Tasks section sequentially, one by one.
      After completing each task — immediately mark it as done in the plan file.
    </description>
    <constraint>FORBIDDEN to mark multiple tasks as done at once — only after actual completion of each.</constraint>
    <constraint>FORBIDDEN to proceed to the next task without marking the current one as done.</constraint>
    <steps>
      <step id="3.1">
        <action>
          Read the plan file ${input:plan_path}.
          Find the first task with status `[ ]`.
          Study its context (read necessary files if required).
        </action>
      </step>
      <step id="3.2">
        <action>
          Execute the task: create or modify files, run terminal, write tests — whatever is required.
        </action>
      </step>
      <step id="3.2.5">
        <action>
          If problems arise during execution (test failures, ImportError, unexpected behavior):
          DO NOT read all related files yourself — first run subagents for diagnostics.
        </action>
        <subagent_prompt_template>
          Problem: {error description or behavior}
          Test file / error stack: {error text}
          Investigate: {suspected culprit files}
          Question: find the root cause — method signatures, argument types, API changes.
          Response format: cause + specific lines/methods, maximum 50 lines.
        </subagent_prompt_template>
        <constraint>Subagent works faster and saves context — do not skip this step on errors.</constraint>
      </step>
      <step id="3.3">
        <action>
          Immediately mark the task as done in the plan file:
          `- [ ] description` → `- [x] description`
          Do not change the task text.
        </action>
      </step>
      <step id="3.4">
        <action>Move to the next task `[ ]`. Repeat steps 3.1–3.3.</action>
      </step>
    </steps>
    <output>Completed code changes and updated plan file.</output>
  </phase>

  <phase id="4" name="RECOVERY — Recovery After Context Compression">
    <description>
      If context compression occurred (a summarization section appeared in the system prompt),
      it is necessary to restore task understanding before continuing.
    </description>
    <trigger>A summarization section appeared in the system prompt / context was compressed.</trigger>
    <steps>
      <step>Read the plan file ${input:plan_path} — find incomplete tasks `[ ]` and the last completed `[x]`.</step>
      <step>
        Run subagents to investigate files related to the next incomplete tasks.
        It is critical to study the ACTUAL state of the code — context compression may have cut details of implemented changes.
        Subagent task: read the current state of the module (including already changed files from `[x]` tasks)
        and return key facts (up to 50 lines). DO NOT rely only on the summary — verify the actual state of files.
      </step>
      <step>Continue execution from the first incomplete task (step 3.1 of the EXECUTE phase).</step>
    </steps>
    <output>Restored context and continued execution.</output>
  </phase>

  <phase id="5" name="FINALIZE — Completion">
    <description>
      All tasks are completed. Final verification, tests, and comprehensive documentation update.
    </description>
    <steps>
      <step id="5.1">
        <action>Make sure all tasks in the plan file are marked `[x]`.</action>
      </step>

      <step id="5.2">
        <action>Run tests (if applicable) and make sure there are no errors.
          If tests fail — use diagnostic subagents (step 3.2.5) before manual investigation.
        </action>
      </step>

      <step id="5.3" name="COMPLETED.md report">
        <action>
          Create a file `{plan_dir}/*_COMPLETED.instructions.md` — a detailed implementation report:
          - What was implemented (list of components)
          - What files were created/modified (with paths)
          - Architectural decisions and patterns
          - Known limitations and technical debt
          - What was skipped / deferred to next phases
        </action>
      </step>

      <step id="5.4" name="Search for all affected documentation">
        <action>
          Launch subagents to search for ALL documents that need updating:
        </action>
        <subagent_prompt_template>
          We implemented: {brief description of changes}
          Changed modules/files: {list of key files}
          New components: {list of new classes/modules}

          Review ALL of the following directories and return a list of files that mention affected components
          or need to be updated due to the changes:
          1. `docs/` and all subdirectories (`docs/specification/`, `docs/architecture/`, `docs/api/`)
          2. `.github/implementations/` — future unimplemented phases (find tasks that changed)
          3. `.github/implementations/00_MASTER_MVP_PLAN.instructions.md` — master plan
          4. `.github/instructions/` — agent instructions (Project_Docs_Context, Project_structure)

          For each found file specify: path, what exactly needs to be updated (1-2 lines).
          Maximum 80 lines of response.
        </subagent_prompt_template>
      </step>

      <step id="5.5" name="Documentation update">
        <action>
          Based on subagent results from step 5.4:
          1. Update the status/content of ALL found specifications (`docs/specification/*.md`)
          2. Adjust future phases in `.github/implementations/` — if implementation changed the API
             or architecture that was planned for use in future phases
          3. Update the master plan `.github/implementations/00_MASTER_MVP_PLAN.instructions.md`
          4. If necessary, update `.github/instructions/Project_Docs_Context.instructions.md`
             (document descriptions) and `Project_structure.instructions.md` (module structure)

          If context summarization has already occurred — launch an additional subagent to
          verify the actual state of key changed files before updating docs.
        </action>
      </step>

      <step id="5.6">
        <action>Update `CHANGELOG.md` — add a section describing the implemented phase.</action>
      </step>
    </steps>
    <output>All tests pass, COMPLETED.md report created, all related documents and future phases updated.</output>
  </phase>

</workflow>

---

## Execution Rules

**MANDATORY:**
- Use subagents for research — this saves the context window.
- Create a plan file before starting coding.
- Execute tasks strictly sequentially, one at a time.
- Mark a task as done immediately after its completion.
- On errors and test failures — first run a diagnostic subagent (step 3.2.5), then fix.
- On context compression — re-read the plan, then use subagents to verify the actual state of code.
- After completion, run all project tests.
- Create a COMPLETED.md report.
- Run a subagent to find ALL documents affected by changes and update them.
- Adjust future unimplemented phases in `.github/implementations/` if implementation changed the API or architecture.

**FORBIDDEN:**
- Starting coding without a created plan.
- Marking tasks as done in advance or in batches.
- Modifying the task text when marking — only the checkbox change `[ ]` → `[x]` is allowed.
- Overflowing the context by reading the entire codebase at once — research must be delegated to subagents.
- Updating only one specification — all related documents must be found and updated.
