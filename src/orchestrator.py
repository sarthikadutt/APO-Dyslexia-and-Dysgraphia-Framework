from datetime import datetime
from .vision_agent import run_vision_diagnostic_agent
from .strategist_agent import run_pedagogical_strategist
from .scaffolder_agent import run_content_scaffolder


def run_apo_pipeline(image_path: str) -> dict:
    """Run the demo APO pipeline on one image."""
    state = {
        "input_image": image_path,
        "session_history": [],
    }
    state = run_vision_diagnostic_agent(state)
    if state["diagnostic_payload"]["confidence"] < 0.80:
        state = run_vision_diagnostic_agent(state)
    state = run_pedagogical_strategist(state)
    state = run_content_scaffolder(state)
    state["session_history"].append({
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "diagnostic_payload": state["diagnostic_payload"],
        "pedagogical_path": state["pedagogical_path"],
    })
    return state
