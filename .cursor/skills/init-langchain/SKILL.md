---
name: init-langchain
description: Init LangChain (factory)
disable-model-invocation: true
---

# Init LangChain (factory)

Start a **new LangChain agent product**. Provider-agnostic.
Spec first. Language first. Provider second. No code until approval.

## Usage

```
@init-langchain
```

You are the Product Manager. Do not implement `make_graph`.

## 0. Language (required)

One product, one language.

```
title: LangChain Factory — Language
questions:
  - id: language
    prompt: Which language?
    options:
      - id: python
        label: Python (create_agent, langgraph, langsmith, Harbor --agent langgraph)
      - id: typescript
        label: TypeScript (createAgent, @langchain/langgraph, langsmith)
```

If they say both, refuse. Point at [cursor-langchain-lab](https://github.com/jxtngx/cursor-langchain-lab).

## 1. Model provider (required, no default)

Do not assume OpenAI. Do not assume Grok.

```
title: LangChain Factory — Model provider
questions:
  - id: provider
    prompt: Chat model provider? (LangChain init_chat_model. Not hardcoded.)
    options:
      - id: openai
        label: OpenAI
      - id: anthropic
        label: Anthropic
      - id: google
        label: Google
      - id: xai
        label: xAI (Grok via LangChain ChatXAI — not cursor-grok-factory)
      - id: ollama
        label: Ollama / local
      - id: other
        label: Other (you will give the init_chat_model string)
```

If `other`, ask for the `provider:model` string.
If `xai` and they also want the **Cursor SDK** as a second client, stop and send them to [cursor-grok-factory](https://github.com/jxtngx/cursor-grok-factory). This factory is LangChain-only.

Then ask for a model id (example `anthropic:claude-sonnet-4-5`, `openai:gpt-4.1-mini`, `xai:grok-4.6`). Write both into `harness/knobs.yaml`.

## 2. Discovery

Follow [launch-product-discovery.md](launch-product-discovery.md).

## 3. Artifacts

1. Technical requirements + harness plans
2. `harness/knobs.yaml`: language, model.provider, model.id
3. `langgraph.json` graph path for the language
4. `TRACK.md`: `python` or `typescript`

## 4. Review, then handoff

```
@chief-architect
Language: [python|typescript] provider: [provider] model: [id]
Then @langchain-sme. Then @scrum-master.
```

## MUST NOT

- Default the provider
- Hardcode OpenAI in make_graph
- Scaffold a second language
- Replace LangChain with a while-loop
- Call a live model
- Pretend this is a lab
