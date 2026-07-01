from pathlib import Path
from src.orchestrator import run_apo_pipeline


def test_pipeline_runs():
    root = Path(__file__).resolve().parents[1]
    result = run_apo_pipeline(str(root / "data" / "sample_images" / "demo_handwriting.png"))
    assert "diagnostic_payload" in result
    assert "scaffolding_output" in result
    assert result["diagnostic_payload"]["confidence"] >= 0.80
