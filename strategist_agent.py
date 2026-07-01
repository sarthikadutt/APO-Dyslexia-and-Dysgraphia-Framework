
def run_pedagogical_strategist(state: dict) -> dict:
    """Select an intervention route based on the diagnostic payload."""
    payload = state["diagnostic_payload"]
    error_count = len(state.get("detected_errors", []))
    frustration = min(1.0, error_count / 4)
    tier = 1 if frustration > 0.65 else 2 if error_count >= 1 else 3

    category = payload.get("error_category", "Orthographic")
    if category == "Spatial":
        path = ["baseline_grid", "spacing_practice", "guided_copying"]
    elif category == "Kinematic":
        path = ["stroke_direction_arrows", "tracing_overlay", "slow_motion_demo"]
    else:
        path = ["sound_symbol_mapping", "bed_mnemonic", "multisensory_letter_practice"]

    state["learner_frustration_lvl"] = frustration
    state["current_scaffolding_tier"] = tier
    state["pedagogical_path"] = path
    return state
