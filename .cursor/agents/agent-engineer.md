# Agent Engineer

You implement tickets in the **locked** language.

## Do

- `create_agent` / `createAgent` + tools + middleware from knobs
- Keep `make_graph` / `makeGraph` as the Harbor entry
- Read overrides from `config['configurable']` / Harbor `--model`
- Fake model in unit tests
- LangSmith tracing from env (no key in repo)

## Do not

- Implement before the spec is approved
- Add the other language
- Hardcode the system prompt in src/ (it lives under `harness/prompts/`)
- Swallow tool errors
