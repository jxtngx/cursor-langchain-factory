# Harness

This directory is the **parameter surface** of the agent factory.

LangChain's own harness-engineering writeup compresses the search space to three knobs: **system prompt**, **tools**, **middleware**.
Harbor runs the graph (`--agent langgraph`) and LangSmith records the trial (`--plugin langsmith`).

```text
knobs.yaml  +  prompts/*.md  +  langgraph.json
        ↓
make_graph(config)     # templates/<lang>/
        ↓
Harbor trial  →  LangSmith experiment
```

## After `@init-agent`

1. `language` is set in `knobs.yaml`
2. `langgraph.json` `graphs.agent` points at the chosen language's `make_graph`
3. Product-specific tools replace the stubs
4. `@tune-harness` sweeps prompt/tools/middleware without rewriting `make_graph`

## Official

- https://www.langchain.com/blog/how-to-build-a-custom-agent-harness
- https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering
- https://www.langchain.com/blog/unified-stack-for-evaluating-agents
- https://harborframework.com/
- https://docs.langchain.com/langsmith/observability
