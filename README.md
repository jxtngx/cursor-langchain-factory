# Cursor LangChain Factory

A **factory**, not a lab.

Pure **LangChain** product boilerplate. Model **provider-agnostic**.
Cursor's team implements from a spec you write in the first session.

If you want to *learn* LangChain by typing every loop, use
[cursor-langchain-lab](https://github.com/jxtngx/cursor-langchain-lab).

If you want **Grok + Cursor SDK** (paired clients, not LangChain-as-the-spine),
use [cursor-grok-factory](https://github.com/jxtngx/cursor-grok-factory).

> **Lab** = student writes the code. Mentors quiz and review.
> **Factory** = you define requirements. Chief Architect, SME, Scrum, and engineers ship tickets.

This factory is tightly coupled to **LangChain** (`create_agent` / `createAgent`),
**LangGraph**, and **LangSmith**. It is **not** coupled to OpenAI, Anthropic, xAI, or anyone else.
The chat model is `init_chat_model` / `initChatModel` with a provider you pick at `@init-langchain`.

The harness is modular so you can tune it with **[Harbor](https://harborframework.com/)**
(`--agent langgraph`, `--plugin langsmith`) without rewriting the agent.

Commanded by [cursor-factory-command](https://github.com/jxtngx/cursor-factory-command).

---

## First command

```
@init-langchain
```

(`@init-agent` still works; it is the same interview.)

1. **Language** — Python or TypeScript (one product)
2. **Model provider** — required, no default: OpenAI, Anthropic, Google, xAI, Ollama, or other (`init_chat_model` string)
3. Requirements interview
4. Writes plans + `harness/knobs.yaml` + `TRACK.md`
5. Hands off `@chief-architect` → `@langchain-sme` → `@scrum-master` → tickets

Do not ask an engineer to "just scaffold" before the spec exists.

## Opinionated stack (not optional)

| Layer | Choice |
| --- | --- |
| Harness | LangChain `create_agent` / `createAgent` |
| Orchestration | LangGraph |
| Chat model | `init_chat_model("provider:model")` — provider from init |
| Observe | LangSmith tracing always |
| Tune | Harbor + `harness/knobs.yaml` |
| Language | Python *or* TypeScript |

You may not replace LangChain with a homemade loop.
You may not hardcode a vendor in `make_graph`. Harbor may sweep `model.id`.

Grok-only or Grok+Cursor SDK products belong in [cursor-grok-factory](https://github.com/jxtngx/cursor-grok-factory), not here.

## Factory pattern (harness knobs)

```text
spec  →  harness/knobs.yaml  →  make_graph(config)  →  LangGraph app
                                      ↓
                         Harbor trial  +  LangSmith experiment
```

| Knob | File / key |
| --- | --- |
| Provider + model | `harness/knobs.yaml` → `model.provider`, `model.id` |
| System prompt | `prompt` |
| Tools | `tools[]` |
| Middleware | `middleware[]` |

## Team

| Agent | Job |
| --- | --- |
| Product Manager | `@init-langchain` / `@launch-product-discovery` |
| Chief Architect | Feasibility, knobs, provider fit |
| LangChain SME | Official APIs, `init_chat_model`, LangSmith, Harbor |
| Scrum Master | Sprint + tickets |
| Agent Engineer | `make_graph`, tools, middleware |
| Test Developer | Fake-model tests |
| Eval Engineer | Harbor + LangSmith |

## Related

| Repo | Kind |
| --- | --- |
| [cursor-langchain-lab](https://github.com/jxtngx/cursor-langchain-lab) | Lab — you write the agent |
| [cursor-grok-factory](https://github.com/jxtngx/cursor-grok-factory) | Factory — Grok + Cursor SDK |
| [cursor-fullstack-factory](https://github.com/jxtngx/cursor-fullstack-factory) | Factory — fullstack |
| [cursor-deep-learning-factory](https://github.com/jxtngx/cursor-deep-learning-factory) | Factory — PyTorch / HF |

## License

Apache-2.0. See [LICENSE](LICENSE).
Not affiliated with LangChain Inc. or Harbor.
