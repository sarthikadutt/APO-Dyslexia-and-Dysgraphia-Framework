from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.orchestrator import run_apo_pipeline
from src.utils import write_json


def main():
    image_path = ROOT / "data" / "sample_images" / "demo_handwriting.png"
    output_path = ROOT / "results" / "sample_output.json"
    result = run_apo_pipeline(str(image_path))
    write_json(result, str(output_path))
    print("APO demo completed successfully.")
    print(f"Output saved to {output_path}")


if __name__ == "__main__":
    main()
