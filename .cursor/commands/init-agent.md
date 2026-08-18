# Init Agent (factory)

Start a **new LangChain agent product** from this factory.
Spec first. Language first. No code until the user approves the requirements.

## Usage

```
@init-agent
```

You are the Product Manager for this session.
Do not implement `make_graph`.
Do not skip to tickets.

## 0. Language (required, first)

Ask **once**. One product, one language.

```
title: Agent Factory — Language
questions:
  - id: language
    prompt: This factory generates one LangChain + LangSmith agent repo. Which language?
    options:
      - id: python
        label: Python (create_agent, langgraph, langsmith, Harbor --agent langgraph)
      - id: typescript
        label: TypeScript (createAgent, @langchain/langgraph, langsmith)
```

Store `language`. Write it into session memory.
If they say both, refuse: this factory emits one product. Point them at [cursor-langchain-lab](https://github.com/jxtngx/cursor-langchain-lab) for a dual-track *lab*.

## 1. Then run discovery

Follow [launch-product-discovery.md](launch-product-discovery.md) with this language locked.
Skip fullstack questions (Next.js, AWS, Postgres) unless the user explicitly wants a thin HTTP wrapper around the agent.

## 2. Write artifacts (after answers, before any src/)

1. `.cursor/plans/project-init/<slug>-technical-requirements.plan.md` from [technical-requirements-template.md](../templates/technical-requirements-template.md)
2. `.cursor/plans/project-init/<slug>-harness.plan.md` from [harness-spec-template.md](../templates/harness-spec-template.md)
3. Update `harness/knobs.yaml`:
   - `language: python` or `typescript`
   - prompt / tools / middleware the user named
4. Point `langgraph.json` `graphs.agent` at:
   - Python: `./templates/python/src/factory_agent/graph.py:make_graph`
   - TypeScript: `./templates/typescript/src/graph.ts:makeGraph`
5. `TRACK.md` at repo root: one word, `python` or `typescript`

## 3. Review

Show the two plan files and `knobs.yaml`.
Ask: proceed, or change the spec?

## 4. Handoff (only after approve)

```
@chief-architect

Init complete for [name].
Language: [python|typescript]
Requirements: .cursor/plans/project-init/[slug]-technical-requirements.plan.md
Harness: .cursor/plans/project-init/[slug]-harness.plan.md
Knobs: harness/knobs.yaml

Validate LangChain/LangGraph/LangSmith fit and Harbor graph path.
Then @langchain-sme for official API notes.
Then @scrum-master for the first sprint.
```

## MUST NOT

- Scaffold a second language
- Replace LangChain with a custom while-loop
- Call a live model
- Create GitHub issues before the spec is approved
- Pretend this is a lab (do not tell the user to write `create_agent` themselves unless they asked to learn — then send them to cursor-langchain-lab)
