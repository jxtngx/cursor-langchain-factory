# Handoff: Product Manager → Chief Architect

Required attachments:

1. `.cursor/plans/project-init/<slug>-technical-requirements.plan.md`
2. `.cursor/plans/project-init/<slug>-harness.plan.md`
3. Updated `harness/knobs.yaml` (`language` set)
4. `TRACK.md`
5. User approval in the thread

Architect rejects the handoff if language is unset, LangSmith is off, or the entrypoint is not `make_graph` / `makeGraph`.
