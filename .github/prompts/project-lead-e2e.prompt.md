---
name: project-lead-e2e
description: "Project Lead workflow for sequential live e2e test execution with backend health-check and log/artifact audit via subagents."
argument-hint: "e2e group scope, task/context file, backend command, test list"
---

Run research and sequential execution of live e2e tests only for the user-selected group.

<inputs>
- Target e2e test scope: ${input:test_scope}
- Task file: ${input:task_file}
- Context file: ${input:context_file}
- Backend start command: ${input:backend_start_command}
- Health endpoint: ${input:health_endpoint}
- List of target tests or selection pattern: ${input:test_targets}
</inputs>

<goal>
Orchestrate live e2e research so that Project Lead preserves its own context: scenarios, long logs, and file artifacts are studied by subagents, while Project Lead manages the step order, makes decisions on cycle continuation, and logs issues in PROJECT_LEAD_JOURNAL.md.
</goal>

<constraints>
- This instruction supplements but does not override other workflow instructions for task/context files, handoff, and subagent management.
- If the current testing policy requires delegating backend launch, health-check, or pytest to default subagent or QA subagent, maintain that order. What matters is the phase order, not the specific executor of the terminal command.
- Do not run e2e tests in batch. One cycle = one test.
- Do not switch to other e2e groups if the user explicitly selected only one group.
- Project Lead does not read long logs or scan directories recursively on its own. Always use subagents for this.
- By default, use the minimum sufficient number of subagents.
- If QA already returned READY, do not launch additional research subagents for that test.
- Launch additional subagents for root cause investigation only after a problem is identified, and if investigation directions are independent, they can be launched in parallel.
</constraints>

<available-subagents>
- analyze-project: factual analysis of test files, helper contracts, health-check, and artifact structure.
- product-qa-scenario-analyst: expected path vs actual path, compliance with product idea, specifications, and project documentation.
- compliance-gap-auditor: additional gap analysis if QA has already identified discrepancies with specifications.
- test-coverage-lead: use only if after a series of runs a coverage audit, false-positive detection, or verification gap assessment is needed.
- default subagent: factual breakdown of long logs, test output contents, and file artifacts, if not covered by a specialized subagent.
</available-subagents>

<workflow>
  <phase id="1" name="research-scenarios">
    <step id="1.1">
      Open task/context files from input parameters and verify they correspond to the current e2e test group.
      If the task/context file is missing, first follow the current Project Lead workflow to prepare it, then return to this instruction.
    </step>
    <step id="1.2">
      Identify only the e2e tests that belong to the selected scope. Do not include other groups.
      Use the list ${input:test_targets}, and if incomplete, refine it with a quick factual query to analyze-project on target files and helper modules.
    </step>
    <step id="1.3">
      Preliminary research should be brief. Its goal: for Project Lead to quickly understand what application behavior is expected during testing and what questions to ask the subagent investigating run results later.
      Do not turn this phase into a deep audit of logs, artifacts, or code.
    </step>
    <step id="1.4">
      Launch product-qa-scenario-analyst as the primary and usually sufficient subagent for this phase, so it quickly maps selected tests to project specifications and documentation.
      Require brief output: what scenarios are expected, what signs of correct behavior to check later, what questions to ask during post-run analysis. The result should be recorded in ${input:context_file}.
    </step>
    <step id="1.5">
      Connect analyze-project only if without it the test composition or expected technical traces cannot be quickly determined. If context is already sufficient, proceed to backend launch without extra checks.
      After completing step 1, Project Lead uses only brief subagent summaries. Do not re-read long test files and documentation without necessity.
    </step>
  </phase>

  <phase id="2" name="start-backend">
    <step id="2.1">
      Start the backend using the command ${input:backend_start_command} following current instructions for terminal, virtual environment, and UTF-8.
      Do not create multiple competing backend processes for the same research session.
    </step>
    <step id="2.2">
      Wait for the launch result through standard terminal tools. After any backend launch, always verify availability of ${input:health_endpoint}.
    </step>
    <step id="2.3">
      If the backend is unavailable, perform a brief root cause analysis, restart the backend if needed, and repeat the health-check.
      Do not proceed to test launch until the health-check succeeds or the user explicitly prohibits further actions.
    </step>
  </phase>

  <phase id="3" name="single-test-cycle">
    <step id="3.1">
      Before EACH next test, re-verify backend availability via ${input:health_endpoint}.
      If after code changes the backend restarted, crashed, or hung, first restore backend availability, then proceed to the test.
    </step>
    <step id="3.2">
      Select only one next test from the target group and run only it.
      Do not combine multiple files and do not run the entire e2e suite at once.
    </step>
    <step id="3.3">
      If the user selectively rejected the test launch command, do not treat this as no effect.
      Immediately proceed to the post-run-audit phase: the test may have partially executed, the backend may have received the request, and artifacts and logs may have appeared.
    </step>
    <step id="3.4">
      If the terminal reported that the test was not executed, also proceed to post-run-audit and verify actual execution traces through subagents.
    </step>
  </phase>

  <phase id="4" name="post-run-audit">
    <step id="4.1">
      First launch only product-qa-scenario-analyst to analyze results of one specific test.
      It should independently check test logs, file artifacts, expected path vs actual path, and compliance with scenarios.
      Require a brief verdict with ${input:context_file} update as an append-only block.
    </step>
    <step id="4.2">
      If product-qa-scenario-analyst returned READY, consider the post-run check sufficient and immediately proceed to the next test.
      If it returned a problem, launch additional subagents to find the exact cause. If investigation directions are independent, they can be launched in parallel.
      Basic directions for additional investigation:
      1. Logs of the specific e2e test in test output directories.
      2. File artifacts in output/data directories.
      3. Technical helper contracts, backend health traces, and API signals.
      4. Additional spec-gap analysis if QA has already pointed to a conflict with scenarios or documentation.
    </step>
    <step id="4.3">
      Use additional subagents only as a diagnosis branch after a problem:
      - default subagent: detailed factual breakdown of long logs and artifacts.
      - analyze-project: verification of test code, helper modules, and backend contracts.
      - compliance-gap-auditor: gap analysis against specifications and docs.
      Do not launch them if QA already returned READY.
    </step>
    <step id="4.4">
      Any found problems must be logged by Project Lead in PROJECT_LEAD_JOURNAL.md in a separate chapter for issues requiring resolution.
      For each issue specify: test, brief symptom, user impact, evidence source, required follow-up action.
    </step>
    <step id="4.5">
      Project Lead itself does not read long logs in full. It uses only brief summaries and verdicts from ${input:context_file} and from subagent responses.
    </step>
  </phase>

  <phase id="5" name="repeat-until-scope-finished">
    <step id="5.1">
      After completing phases 3-4, proceed to the next test from the selected group and repeat the cycle.
    </step>
    <step id="5.2">
      Before each new test, perform the backend health-check again.
    </step>
    <step id="5.3">
      Stop only when all e2e tests belonging to the user-selected scope are completed.
      Do not touch other e2e groups without separate user instruction.
    </step>
  </phase>
</workflow>

<handoff-templates>
  <template id="research-analyze-project">
    Agent: analyze-project
    Task: Use this handoff only if product-qa-scenario-analyst could not quickly clarify the test composition or expected technical traces. Study the tests themselves, helper modules, health-check/artifacts, and related API contracts. Return: test list -> expected technical signals -> expected output artifacts. Update ${input:context_file}. Format: factual summary, maximum 80 lines, no long listings.
  </template>

  <template id="research-qa">
    Agent: product-qa-scenario-analyst
    Task: Based on ${input:task_file}, ${input:context_file}, and relevant project specifications and documentation, quickly determine what application behavior is expected for tests ${input:test_targets} in scope ${input:test_scope}. Return: scenarios, signs of correct behavior, key questions for post-run analysis. Update ${input:context_file}. Format: brief and without deep audit.
  </template>

  <template id="postrun-factual">
    Agent: default subagent
    Task: Use this handoff only after product-qa-scenario-analyst has already returned a problem. Investigate results of ONE test from scope ${input:test_scope}. Check test output logs, related output files, and backend health traces. Return only a brief factual summary: what appeared, what changed, what artifacts and what errors or confirmations were found. Update ${input:context_file} with append-only block. Do not provide full long logs.
  </template>

  <template id="postrun-qa">
    Agent: product-qa-scenario-analyst
    Task: This is the primary and mandatory handoff after each individual e2e run. Check expected path vs actual path, compliance with project specifications and documentation. Use test output logs and artifacts but do not copy long logs into the response. If verdict READY, no additional subagents are needed. If verdict NOT READY, explicitly list diagnostic directions that can be delegated to other subagents in parallel. Update ${input:context_file}.
  </template>
</handoff-templates>

<journal-rules>
- If a bug, regression, scenario mismatch, or suspected false-positive/false-negative test is found, add an entry to PROJECT_LEAD_JOURNAL.md in a separate chapter for issues requiring resolution.
- Do not replace the subagent context file with this entry. The context file stores stage evidence; the Project Lead journal stores management decisions and follow-up.
</journal-rules>

<forbidden>
- Do not run multiple e2e tests in a single command.
- Do not read long integration logs on your own if this can be delegated to a subagent.
- Do not analyze irrelevant e2e groups outside the user-selected scope.
- Do not skip health-check before each test.
- Do not consider the user's rejection of a command as a guarantee that the test definitely did not start.
- Do not overwrite others' blocks in ${input:context_file}; only append-only scoped updates.
</forbidden>