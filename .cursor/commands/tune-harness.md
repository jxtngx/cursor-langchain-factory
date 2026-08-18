# Tune Harness

Sweep **prompt / tools / middleware** via Harbor + LangSmith.
Do not rewrite `make_graph` unless a knob cannot be expressed in `harness/knobs.yaml`.

## Usage

```
@tune-harness
```

## MUST

1. Confirm `make_graph` is implemented (not `NotImplementedError`)
2. Confirm `langgraph.json` points at the chosen language
3. Propose a small sweep (2–4 prompt variants, or tool on/off, or one middleware)
4. Show the Harbor-shaped command (do not invent flags — use official Harbor docs):

```
# shape — verify against https://harborframework.com/ and the LangChain Harbor blog
harbor run --agent langgraph --plugin langsmith --model <id>
```

5. Map results to a LangSmith experiment / dataset named in `knobs.yaml`
6. Write findings in `.cursor/plans/project-init/<slug>-harness-results.md`
7. Recommend the winning knob set. Ask before changing the default `knobs.yaml`

## MUST NOT

- Change tools' business logic in a "tune" pass
- Disable LangSmith
- Claim a score you did not run
