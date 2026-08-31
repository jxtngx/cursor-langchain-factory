# Technical Requirements Template (agent factory)

Write to `.cursor/plans/project-init/[slug]-technical-requirements.plan.md`.

```markdown
---
name: [Agent name]
overview: [One sentence]
language: [python | typescript]
model_provider: [openai | anthropic | google | xai | ollama | other]
model_id: [init_chat_model string]
problem_statement: [Why an agent]
loop: [create_agent | supervisor | deep_agent]
github_repo: [owner/repo]
langsmith_project: [name]
langsmith_dataset: [name]
harbor: [now | later]
sprint_plan_file: .cursor/plans/project-init/[slug]-sprint.plan.md
todos:
  - id: spec
    content: Spec approved
    status: pending
  - id: harness
    content: make_graph + knobs
    status: pending
  - id: evals
    content: LangSmith dataset + Harbor smoke
    status: pending
isProject: false
---

# [Agent name] — Technical Requirements

## User Story

As a [operator], I want [agent behavior] so that [benefit].

## Problem Statement

[Pain. Why a script or a single LLM call is not enough.]

## Language

- **Locked**: python | typescript
- **Provider**: openai | anthropic | google | xai | ollama | other (`init_chat_model`)
- **Packages**: langchain, langgraph, langsmith (JS twins if typescript)
- **Entry**: `make_graph` / `makeGraph` for Harbor `--agent langgraph`

## Loop

- Default: LangChain `create_agent` / `createAgent`
- Graph: LangGraph (even when using create_agent)
- Multi-agent / Deep Agents: [yes/no, why]

## Tools (MVP)

| Tool | Side effect | HITL | Must-have |
| --- | --- | --- | --- |
| [name] | yes/no | yes/no | yes |

## Memory

- [stateless | thread checkpointer | later long-term]

## Observability

- LangSmith tracing: on
- Dataset: [name]
- Harbor: `--agent langgraph --plugin langsmith`

## Safety

- Max iterations: [n]
- Interrupt before: [tools]
- Refusals: [list]

## Harness knobs

See sibling `[slug]-harness.plan.md` and `harness/knobs.yaml`.

## Definition of Done (MVP)

- [ ] Spec approved
- [ ] `make_graph` runs with a fake model in tests
- [ ] Live invoke works with .env (not committed)
- [ ] LangSmith shows a trace
- [ ] Harbor path documented
- [ ] HITL paths tested if any

## Next

1. @chief-architect validates
2. @langchain-sme notes official APIs
3. @scrum-master writes sprint
```
