/**
 * Harbor / LangGraph entry: makeGraph(config) -> compiled graph.
 * Knobs live in harness/knobs.yaml. Harbor --model arrives on configurable.model.
 * Agent Engineer implements after the spec is approved.
 */

export type GraphConfig = {
  configurable?: {
    model?: string;
    promptId?: string;
    [key: string]: unknown;
  };
};

export async function makeGraph(_config?: GraphConfig): Promise<never> {
  throw new Error(
    "makeGraph: implement after @init-agent spec is approved (createAgent + knobs + LangSmith).",
  );
}
