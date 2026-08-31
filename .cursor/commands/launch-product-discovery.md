# Launch Product Discovery (agent factory)

Same *shape* as [cursor-fullstack-factory](https://github.com/jxtngx/cursor-fullstack-factory) discovery: questionnaire → technical requirements → architect → scrum.
Questions are about an **agent harness**, not a fullstack web app.

Called from `@init-langchain` after language **and provider** are locked. If those are missing, run `@init-langchain` instead.

## Question sequence

### Q1 — Agent job

Conversational, then lock it:

- One-sentence description (what the agent *does*)
- Problem statement (why a human or a script is not enough)
- Product / agent name

Give two examples first:

- "A repo tutor that answers questions from a fixture corpus and refuses to write the user's homework."
- "A support triage agent that classifies tickets, looks up policy, and interrupts before sending email."

### Q2 — Users

```
Who is the primary operator?
- Individual developer
- Internal team
- End customers (the agent is user-facing)
- Mixed
```

### Q3 — Loop shape

```
What is the default loop? (factory will still use LangChain create_agent / LangGraph)
- Single specialist (create_agent + tools)
- Supervisor + specialists (multi-agent)
- Deep-agent style (planning + filesystem) — only if they accept Deep Agents as a dep
```

### Q4 — Tools (3–7)

Ask them to name tools. For each: must-have vs later, side-effecting (yes/no), HITL before run (yes/no).

### Q5 — Memory

```
- None (stateless invoke)
- Thread memory (checkpointer + thread_id)
- Long-term (store) — later
```

### Q6 — Observability (not optional)

```
LangSmith is on.
- Project name
- Dataset name for golden evals
- Harbor now vs later
```

### Q7 — Model

```
- Provider they already have (OpenAI / Anthropic / other)
- Fake model in CI (always yes)
```

### Q8 — Safety

```
- Interrupt before which tools?
- Max iterations
- What the agent must refuse
```

### Q9 — Repo

- GitHub `owner/repo` for the *generated* product (may be this repo if they are transforming it in place)
- Sprint plan filename suggestion: `<slug>-sprint.plan.md`

## Write the spec

Use [technical-requirements-template.md](../templates/technical-requirements-template.md).
Fill language, knobs, LangSmith project, Harbor flags.

Do not implement.
Hand back to `@init-agent` step 3 (review) if you were invoked from there; otherwise hand off to `@chief-architect` yourself.
