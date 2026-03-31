---
name: research-and-sync
description: "Source research and synchronization with target documents. Universal: code→docs, docs→docs, plans→docs."
argument-hint: "optional: short task description"
---

You are about to perform a **research-and-synchronization task**.

## Input Parameters

- **Source for research:** ${input:source_description}
  > Examples: `#folder:backend/src` · `#folder:docs/architecture` · `#folder:.github/implementations`
- **Target (what we update):** ${input:target_description}
  > Examples: `#folder:docs/architecture`, `#folder:docs/specification`, specific file
- **Task type:** ${input:task_type}
  > Examples: `synchronize actual code with documentation`, `update implementation plans according to specification`, `align documentation with other documentation`
- **Maximum characters per document:** ${input:max_chars}
  > For example: `15000`
- **Document language:** ${input:doc_language}
  > For example: `Russian`, `English`

---

<workflow>

  <phase id="1" name="INIT — Initialization and Overview">
    <description>
      Understand the task and build a complete picture of the target documents.
    </description>
    <steps>
      <step>Read the task description: source, target, task type.</step>
      <step>Get the list of all files in the target folder (search tool or list_dir).</step>
      <step>Alternative: launch subagents to search for relevant documents.</step>
      <step>For each found file, determine its topic in one sentence — without fully reading the content.</step>
      <step>If the target folder is empty — that is normal, you will create documents as topics are discovered.</step>
    </steps>
    <subagent_prompt_template>
      Research: {source_path}
      Topic: {topic}
      Question: {specific_question}
      Response format: structured list of facts, maximum 50 lines.
    </subagent_prompt_template>
    <output>List of target files with a brief topic for each.</output>
  </phase>

  <phase id="2" name="PLAN — Creating the Plan (todo list)">
    <description>
      Form a numbered task list. One task = one file/topic.
      Use manage_todo_list to track progress.
    </description>
    <steps>
      <step>For each found target document, create a task like: "Synchronize: {file_name} — {topic}".</step>
      <step>If there are no target documents — create a placeholder task: "Discover topics from source and create documents".</step>
      <step>Record the todo list via manage_todo_list with not-started status.</step>
      <step>Select the first task and mark it as in-progress.</step>
    </steps>
    <output>Current todo list.</output>
  </phase>

  <phase id="3" name="EXECUTE — Execution Cycle (one topic at a time)">
    <description>
      Main work cycle. Execute strictly sequentially — one document at a time.
    </description>
    <constraint>FORBIDDEN to read multiple target documents simultaneously and move to the next before completing the current one.</constraint>
    <steps>
      <step id="3.1">
        <action>Read the current target document (if it exists).</action>
      </step>
      <step id="3.2">
        <action>
          Research the source on the topic of the current document via runSubagent.
          Pass to the subagent: the topic, source path, specific research question.
          The subagent returns only relevant facts — this saves the context window.
        </action>
        <subagent_prompt_template>
          Research source: {source_path}
          Topic: {topic}
          Question: Find all current information on the topic "{topic}" in the source.
          Return: structured list of facts, maximum 3000 characters.
        </subagent_prompt_template>
      </step>
      <step id="3.3">
        <action>
          Based on the subagent results, update via string replacement (or create) the target document.
          Follow the constraints: maximum ${input:max_chars} characters, language: ${input:doc_language}.
          Document structure: title, table of contents (TOC), main sections.
        </action>
      </step>
      <step id="3.4">
        <action>Read the source information in parts yourself, only the relevant sections.</action>
      </step>
      <step id="3.5">
        <action>Mark the current task as completed in manage_todo_list.</action>
      </step>
      <step id="3.6">
        <action>Select the next task from the todo list and mark it as in-progress. Go to step 3.1.</action>
      </step>
    </steps>
    <output>Updated/created target document.</output>
  </phase>

  <phase id="4" name="DISCOVERY — Discovering New Topics">
    <description>
      During source research, the subagent may discover topics for which no target document exists.
      This process runs in parallel with the EXECUTE phase — without interrupting the current task.
    </description>
    <trigger>The subagent returned facts on a topic for which there is no file in the target folder.</trigger>
    <steps>
      <step>Create an empty file with the correct name in the target folder (name = topic in kebab-case, extension .md).</step>
      <step>Add a new task to the todo list: "Create document: {file_name} — {discovered_topic}" with not-started status.</step>
      <step>Continue working on the current task — the new topic will be processed in queue order.</step>
    </steps>
    <constraint>Do not switch to the new topic until the current task is completed.</constraint>
    <output>Empty placeholder file + new task in todo.</output>
  </phase>

  <phase id="5" name="FINALIZE — Completion">
    <description>
      All tasks are completed. Summarize the results.
    </description>
    <steps>
      <step>Ensure all tasks in manage_todo_list are marked as completed.</step>
      <step>Generate a brief report: how many documents were updated, created, which topics were discovered for the first time.</step>
      <step>If critical discrepancies between the source and documentation were found — note them separately.</step>
    </steps>
    <output>Brief change report (no more than 500 characters).</output>
  </phase>

</workflow>

---

## Execution Rules

**REQUIRED:**
- Use `runSubagent` for source research — this saves the agent's context window.
- After `runSubagent` research, open relevant documents to get the full context.
- Work strictly one document at a time (EXECUTE phase).
- Keep the todo list up to date via `manage_todo_list`.
- Create placeholder files immediately upon discovering a new topic.
- Follow the character limit: `${input:max_chars}` per document.
- Write documents in the language: `${input:doc_language}`.

**FORBIDDEN:**
- Reading all target documents at once before starting work.
- Moving to the next topic without completing the current one.
- Skipping placeholder creation upon discovering a new topic.
- Ignoring subagent results and researching the source yourself instead of delegating.
