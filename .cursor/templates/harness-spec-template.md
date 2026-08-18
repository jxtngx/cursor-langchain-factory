# Harness spec template

Write to `.cursor/plans/project-init/[slug]-harness.plan.md`.

```markdown
---
name: [slug]-harness
language: [python | typescript]
schema_version: 1
---

# Harness spec

The agent is a factory: `make_graph(config)` + `harness/knobs.yaml`.

## Knobs in scope (Harbor sweep)

| Knob | Default | Variants to try |
| --- | --- | --- |
| prompt | harness/prompts/system.md | |
| tools.enabled | | |
| middleware.max_iterations | 8 | |
| model.id | | Harbor --model |

## LangGraph registry

`langgraph.json` → `graphs.agent` → `make_graph` / `makeGraph`.

## LangSmith

- Project: [name]
- Dataset: [name]
- What a passing example looks like: [one line]

## Harbor

- `--agent langgraph`
- `--plugin langsmith`
- Environment: [local | langsmith sandbox | later]

## Out of scope

Replacing LangChain. Adding a second language. Tuning by editing prompts inside `src/` instead of knobs.
```
