
def demo_metrics() -> dict:
    """Return sample metrics aligned with the manuscript for demonstration only."""
    return {
        "single_agent_f1": 0.76,
        "apo_f1": 0.92,
        "single_agent_intervention_relevance": 0.68,
        "apo_intervention_relevance": 0.89,
        "single_agent_latency_seconds": 1.4,
        "apo_latency_seconds": 2.3,
        "note": "Illustrative manuscript-aligned values; not recomputed from demo data.",
    }
