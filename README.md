# Cursor Agent Factory

A **factory**, not a lab.

This repo is boilerplate for a new LangChain agent product.
Cursor's team implements from a spec you write in the first session.
If you want to *learn* agents by typing every loop yourself, use [cursor-langchain-lab](https://github.com/jxtngx/cursor-langchain-lab) instead.

> **Lab** = student writes the code. Mentors quiz and review.
> **Factory** = you define requirements. Chief Architect, SME, Scrum, and engineers ship tickets.

Sister factories: [cursor-fullstack-factory](https://github.com/jxtngx/cursor-fullstack-factory) · [cursor-deep-learning-factory](https://github.com/jxtngx/cursor-deep-learning-factory).

This factory is tightly coupled to **LangChain** (`create_agent` / `createAgent`), **LangGraph**, and **LangSmith**.
The harness is modular so you can tune it with **[Harbor](https://harborframework.com/)** (`--agent langgraph`, `--plugin langsmith`) without rewriting the agent.

---

## First command

Open this repo in Cursor and run:

```
@init-agent
```

That command:

1. Asks **Python or TypeScript** (one generated product, one language)
2. Walks the same style of **requirements interview** as fullstack-factory (`@launch-product-discovery`)
3. Writes `.cursor/plans/project-init/<name>-technical-requirements.plan.md`
4. Writes `harness/knobs.yaml` (the parameters Harbor and LangSmith will sweep)
5. Hands off to `@chief-architect` → `@scrum-master` → tickets

Do not ask an engineer to "just scaffold" before the spec exists.
That is the whole point of spec-driven init.

## Opinionated stack (not optional)

| Layer | Choice | Why |
| --- | --- | --- |
| Harness | LangChain `create_agent` / `createAgent` | [Custom harness](https://www.langchain.com/blog/how-to-build-a-custom-agent-harness) |
| Orchestration | LangGraph | Durable graphs, interrupts, Harbor `--agent langgraph` |
| Observe / eval | LangSmith | Traces, datasets, `--plugin langsmith` |
| Tune | Harbor + `langgraph.json` | Sweep prompt / tools / middleware knobs |
| Language | **Python *or* TypeScript** | Chosen in `@init-agent` |

You may add tools, middleware, and checkpointers.
You may not replace LangChain with a homemade loop in this factory.

## Factory pattern (harness knobs)

The generated agent is a **parameterized factory**, not a pile of scripts.

```text
spec  →  harness/knobs.yaml  →  make_graph(config)  →  LangGraph app
                                      ↓
                         Harbor trial  +  LangSmith experiment
```

Knobs you are expected to tune (same three LangChain named in harness engineering):

| Knob | File / key | Harbor |
| --- | --- | --- |
| System prompt | `harness/knobs.yaml` → `prompt` | vary per trial |
| Tools | `harness/knobs.yaml` → `tools[]` | enable/disable |
| Middleware | `harness/knobs.yaml` → `middleware[]` | hooks around model/tool |

`make_graph` in `templates/<lang>/` reads `configurable` from Harbor / LangGraph config so a trial can override the YAML without a code change.

## Team

| Agent | Job |
| --- | --- |
| Product Manager | `@init-agent` / `@launch-product-discovery` — spec only |
| Chief Architect | Feasibility, module map, which knobs exist |
| LangChain SME | Official APIs, LangSmith datasets, Harbor `langgraph.json` |
| Scrum Master | Sprint + tickets from the spec |
| Agent Engineer | Implements `make_graph`, tools, middleware for the chosen language |
| Test Developer | Fake-model unit tests + LangSmith eval stubs |
| Eval Engineer | Harbor jobs, LangSmith experiments, knob sweeps |

Engineers **do** implement here. That is the factory contract.
They implement *the spec*, not a surprise architecture.

## After init (typical)

```
@init-agent
  → approve technical requirements
@chief-architect          # validate + fill agent context
@scrum-master             # sprint plan
@run-ticket-plan          # next ticket
@tune-harness             # later: Harbor + LangSmith sweep
```

## Repo layout (this boilerplate)

```
.cursor/
  commands/     init-agent, launch-product-discovery, run-ticket-plan, tune-harness
  agents/       factory team
  templates/    technical-requirements, harness-spec, sprint guide
  plans/project-init/   generated specs land here
harness/
  knobs.yaml    default knobs (copied into the product)
  README.md     how Harbor sees this factory
langgraph.json  Harbor / LangGraph registry (paths filled at init)
templates/
  python/       make_graph stub
  typescript/   make_graph stub
```

The language you did **not** pick is left in `templates/` as reference and is not the product.

## Accounts

| Service | Required |
| --- | --- |
| [Cursor](https://cursor.com) | yes |
| [GitHub](https://github.com) | yes |
| [LangSmith](https://smith.langchain.com) | yes for traces/evals (factory default) |
| Model provider (OpenAI, Anthropic, …) | yes to run live; tests use a fake model |
| [Harbor](https://harborframework.com) | recommended for harness sweeps |

Copy `.env.example` → `.env`. Never commit keys.

## Related repos

| Repo | Kind |
| --- | --- |
| [cursor-langchain-lab](https://github.com/jxtngx/cursor-langchain-lab) | Lab — you write the agent |
| [cursor-rust-lab](https://github.com/jxtngx/cursor-rust-lab) | Lab — Rust |
| [cursor-fullstack-factory](https://github.com/jxtngx/cursor-fullstack-factory) | Factory — fullstack product |
| [cursor-deep-learning-factory](https://github.com/jxtngx/cursor-deep-learning-factory) | Factory — PyTorch / HF |

## License

Apache-2.0. See [LICENSE](LICENSE).
Not affiliated with LangChain Inc. or Harbor.
