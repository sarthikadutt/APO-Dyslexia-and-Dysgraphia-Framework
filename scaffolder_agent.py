
def run_content_scaffolder(state: dict) -> dict:
    """Create a structured multimodal scaffolding output."""
    tier = state.get("current_scaffolding_tier", 2)
    path = state.get("pedagogical_path", [])
    instruction = (
        "Trace the letter slowly using the guide, then try once independently."
        if tier == 1 else
        "Use the visual guide, then write the word again with careful spacing."
        if tier == 2 else
        "Write the word independently and check your spacing and letter direction."
    )
    state["scaffolding_output"] = {
        "primary_instruction": instruction,
        "visual_scaffold_spec": {
            "type": "svg_overlay",
            "elements": path,
            "opacity": 0.75 if tier == 1 else 0.45 if tier == 2 else 0.20,
        },
        "verbal_script": "Good effort. Let us use a helpful strategy and try the next attempt calmly.",
    }
    return state
