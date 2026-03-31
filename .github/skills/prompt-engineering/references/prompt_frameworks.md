# Prompt Frameworks: Choosing an Architecture

Named frameworks provide a quick entry point when designing a prompt.
Instead of building structure from scratch every time, choose a suitable template
by task type and fill in the slots.

---

## Framework Selection Table

| Task | Recommended Framework |
|------|----------------------|
| Simple generation / instruction | **RTF** |
| Content task with audience | **CO-STAR** |
| Complex multi-step prompt | **RISEN** |
| Full agent system prompt | **CRISPE** |
| Agent with tools / search | **ReAct** |

---

## RTF — Role · Task · Format

Minimalist skeleton for most single-layer tasks.

```
ROLE:   [What role the model takes on — expert, assistant, tool]
TASK:   [What needs to be done — verb + object + context]
FORMAT: [What the result should look like — length, structure, style]
```

**Example:**
```
ROLE:   You are an experienced technical documentation editor.
TASK:   Rewrite the following fragment, eliminating jargon and passive voice.
FORMAT: Return only the corrected text without comments, preserving the original length.
```

**When to use:** quick transformation tasks, single instructions,
prototyping a prompt before expanding it.

---

## CO-STAR — Context · Objective · Style · Tone · Audience · Response

Optimal for content tasks where brand voice and target audience matter.

```
CONTEXT:   [Background and situation — where the request comes from, why the task arose]
OBJECTIVE: [Specific goal — what should change after execution]
STYLE:     [Literary or communication style — formal, technical, narrative]
TONE:      [Emotional coloring — inspiring, strict, friendly]
AUDIENCE:  [Description of the reader — level, context, pain points]
RESPONSE:  [Exact format — document type, length, structure]
```

**Example:**
```
CONTEXT:   SaaS product for HR, launching in the corporate segment.
OBJECTIVE: Write release notes for the new feature "Auto-onboarding".
STYLE:     Business-like, no buzzwords; concrete action verbs.
TONE:      Confident, neutrally positive.
AUDIENCE:  HR managers, not techies, making subscription renewal decisions.
RESPONSE:  3 paragraphs: what changed, what it gives, how to start. No markdown.
```

**When to use:** email campaigns, release notes, UX copywriting, posts,
any content where audience and tone are critical.

---

## RISEN — Role · Instructions · Steps · End goal · Narrowing

Ideal for complex tasks where the order of step execution matters.

```xml
<role>
[Role and area of expertise of the model]
</role>

<instructions>
[General instruction — what to do at a high level]
</instructions>

<steps>
1. [First step — specific action]
2. [Second step]
3. [Third step]
   After each step, make sure it is completed before moving to the next one.
</steps>

<end_goal>
[Description of the ideal final result — what constitutes success]
</end_goal>

<narrowing>
[Constraints — what NOT to do, boundary conditions, edge cases]
</narrowing>
```

**When to use:** document analysis, multi-stage transformations, research tasks,
any prompt where the sequence of steps matters.

---

## CRISPE — Capacity · Role · Insight · Statement · Personality · Experiment

Full skeleton for agent system prompts. Each slot defines a separate
dimension of behavior.

```
CAPACITY:    [Abilities and knowledge the agent possesses]
ROLE:        [How the agent identifies itself — position, context]
INSIGHT:     [Background knowledge about the user / task that the agent should consider]
STATEMENT:   [Specific task — what the agent should do right now]
PERSONALITY: [Communication style and behavioral character]
EXPERIMENT:  [Output format — response structure, examples]
```

**Example (code review agent):**
```
CAPACITY:    Deep knowledge of Python, design patterns, OWASP Top 10.
ROLE:        Senior security engineer reviewing code before release.
INSIGHT:     The team is young, code review culture is just forming.
             Feedback should be constructive, not demotivating.
STATEMENT:   Review the provided diff. Find vulnerabilities, anti-patterns,
             SOLID principle violations. Each comment — with a fix code sample.
PERSONALITY: Precise and direct, but respectful. Explain "why", not just "what".
EXPERIMENT:  Format: ## Critical / ## Suggestions / ## Positives.
             No more than 5 items in Critical, otherwise split into separate reviews.
```

**When to use:** full system prompts for bots, agents, assistants;
tasks where it's important to control each dimension of behavior separately.

---

## ReAct — Reason · Act (+ Observe loop)

Pattern for agents working with tools. The model explicitly alternates
"reasoning → action → observation" until the goal is achieved.

```xml
<react_loop>
For each step follow the cycle:

THOUGHT:  What do you know? What do you need to find out? Which tool is suitable?
ACTION:   Call the tool with exact parameters. No guessing.
OBSERVE:  What did the tool return? Is it enough for the next step?

Repeat THOUGHT → ACTION → OBSERVE until obtaining the final answer.
Finish only when the task is fully solved — not at the first acceptable result.
</react_loop>

<constraints>
- Never guess tool parameters — read files, explore the structure
- Parallel calls are allowed if there is no data dependency between them
- If results of two tools contradict — request a third source
</constraints>
```

**When to use:** agents with web search, file system, code execution, API;
any task where the model must make decisions based on current data.

---

## Memory Block: preserving context between iterations

In long dialogues or multi-step agent tasks, the model loses context
of key decisions made earlier. Memory Block is a structured block
formed based on session history and inserted at the beginning of the prompt.

**Memory Block Structure:**

```xml
<session_memory>
  <decisions>
    <!-- Recorded architectural and design decisions -->
    - [Decision 1: what was chosen and why]
    - [Decision 2: ...]
  </decisions>

  <agreements>
    <!-- Agreements with the user -->
    - [Agreement 1: format, style, constraints]
  </agreements>

  <progress_stack>
    <!-- LIFO stack: last action on top -->
    - [Last action / response]
    - [Previous action]
  </progress_stack>

  <open_questions>
    <!-- Unresolved uncertainties -->
    - [Question 1: what still needs to be clarified]
  </open_questions>
</session_memory>
```

**Application Rules:**

- Form a Memory Block after 3+ exchanges, when decisions or agreements have accumulated
- Place the block immediately after the system prompt, before the user message
- Update the block with each significant new decision
- Limit the size: no more than 200 tokens — only critically important facts

**Code Application Example:**

```python
def build_prompt(system, memory_block, user_message):
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": f"<session_memory>{memory_block}</session_memory>"},
        {"role": "assistant", "content": "Context accepted."},
        {"role": "user", "content": user_message}
    ]
```

---

## PAC2026: content positioning in long prompts

Transformer models pay uneven "attention" to different parts of a prompt.
The PAC2026 principle defines optimal content distribution by position.

```
[BEGINNING — 30%]  System role, key instructions, critical constraints
[MIDDLE — 55%]     Context, data, examples, documentation
[END — 15%]        Repetition of critical instructions, final task
```

**Practical Rules:**

**① Critical instructions — at the beginning AND at the end:**
```
# At the beginning of the prompt
Return ONLY JSON without markdown wrapping.

# ... large context in the middle ...

# At the end of the prompt
Reminder: the response must be ONLY JSON, without additional text.
```

**② Examples — closer to the end of the middle (position ~70%):**
Examples placed closer to the task better activate the desired pattern.

**③ Don't overload the middle with excessive instructions:**
Detailed rules spread throughout the middle have less effect than
a compact block at the beginning.

**Guidelines for length at which PAC2026 starts to matter:**

| Prompt Length | PAC2026 Application |
|---|---|
| < 1000 tokens | Not critical |
| 1000–4000 tokens | Recommended |
| > 4000 tokens | Mandatory |
