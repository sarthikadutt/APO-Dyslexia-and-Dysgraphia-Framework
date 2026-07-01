from .preprocessing import preprocess_image
from .feature_extraction import extract_demo_features


def run_vision_diagnostic_agent(state: dict) -> dict:
    """Demo Vision Diagnostic Agent."""
    img = preprocess_image(state["input_image"])
    features = extract_demo_features(img)
    error_category = "Spatial" if features["SCI"] > 0.35 else "Kinematic" if features["STAS"] > 0.30 else "Orthographic"
    confidence = 0.86
    state["preprocessed_image_available"] = True
    state["transcription"] = state.get("transcription", "demo handwriting")
    state["diagnostic_payload"] = {
        **features,
        "error_category": error_category,
        "confidence": confidence,
    }
    state["detected_errors"] = []
    if features["GRI"]:
        state["detected_errors"].append("possible b/d or p/q reversal pattern")
    if features["SCI"] > 0.35:
        state["detected_errors"].append("letter crowding")
    if features["LTVC"] > 0.25:
        state["detected_errors"].append("tilt variance")
    return state
