"""Harbor / LangGraph entry: make_graph(config) -> compiled graph.

Reads harness/knobs.yaml and honors config['configurable'] overrides
so a Harbor trial can change prompt, tools, or model without a code edit.
The Agent Engineer fills this in after the spec is approved.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[4]


def load_knobs() -> dict[str, Any]:
    path = _repo_root() / "harness" / "knobs.yaml"
    text = path.read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore

        return yaml.safe_load(text)
    except ImportError:
        return {"raw": text}


def make_graph(config: dict[str, Any] | None = None):
    """Return a compiled LangGraph app.

    Harbor calls this via langgraph.json. Until the spec is implemented,
    this raises so nobody ships the stub by accident.
    """
    _ = load_knobs()
    configurable = (config or {}).get("configurable") or {}
    _ = configurable.get("model")
    raise NotImplementedError(
        "make_graph: implement after @init-agent spec is approved "
        "(create_agent + knobs + LangSmith)."
    )
