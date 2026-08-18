# Run Ticket Plan

Implement the **next** ticket from the current sprint plan.
Factory engineers write code. They implement the spec, not a new architecture.

## Usage

```
@run-ticket-plan
```

## MUST

1. Read `TRACK.md` and `harness/knobs.yaml`
2. Read `.cursor/plans/project-init/*-technical-requirements.plan.md` and the sprint plan
3. Pick the first open ticket
4. Implement **only** that ticket in the chosen language
5. Tests: fake model, no key required
6. Keep `make_graph` / `makeGraph` as the Harbor entry
7. Stop and summarize the diff

## MUST NOT

- Skip the spec
- Add the other language
- Replace LangChain
- Sweep Harbor in this command (that is `@tune-harness`)
- Commit secrets
