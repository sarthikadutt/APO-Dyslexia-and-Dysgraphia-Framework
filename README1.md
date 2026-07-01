# APO-Dyslexia-Dysgraphia-Framework

Implementation repository for the paper:

**A Multi-Agent Autonomous Framework for Adaptive Scaffolding in Dysgraphia and Dyslexia: An Implementation Study Using Computer Vision and Agentic Orchestration**

This repository provides a reproducible demonstration of the **Agentic Pedagogical Orchestrator (APO)**, a multi-agent framework for handwriting-based diagnostic support and adaptive scaffolding for dyslexia and dysgraphia.

> **Important data and model notice**  
> This public repository does **not** redistribute the full experimental handwriting datasets or large trained model checkpoints. It includes a small synthetic/demo dataset only to verify the code pipeline. The original study refers to IAM handwriting data and disability-specific handwriting samples; access to those datasets must follow their official licensing, consent, privacy, and ethics requirements.

## Repository Contents

```text
APO-Dyslexia-Dysgraphia-Framework/
├── src/                         # APO implementation modules
├── config/                      # Configuration file
├── data/                        # Demo data and data-use notes
├── models/                      # Model/checkpoint notes
├── examples/                    # Runnable demo
├── results/                     # Sample outputs
├── tests/                       # Basic pipeline test
├── docs/                        # Documentation placeholders
├── requirements.txt
├── environment.yml
├── CITATION.cff
├── LICENSE
└── UPLOAD_TO_GITHUB.md
```

## Methodological Alignment with the Paper

The manuscript describes:

- IAM handwriting database as the normative handwriting stream.
- Disability-specific handwriting samples reviewed/labelled under appropriate expert supervision.
- Data augmentation for training, such as affine jitter, small rotation, and elastic distortion.
- ViT/VLM-based feature extraction.
- Multi-agent orchestration involving a Vision Diagnostic Agent, Pedagogical Strategist, and Content Scaffolder.

This repository reflects that structure in code. However, the public package contains **demo-only data**, not the full private/controlled dataset.

## Data Availability Statement

The included files in `data/demo_dataset/` are demo samples created only to demonstrate repository execution. They should not be interpreted as clinical, diagnostic, or experimental data.

For full reproduction of the study, users should:

1. Obtain the IAM Handwriting Database from its official source under its license.
2. Use institutionally approved, consented, and anonymized disability-specific handwriting data.
3. Document ethical approval, labelling protocol, inclusion criteria, and data handling procedures.
4. Train or calibrate the visual model using the configuration provided in this repository.

## Model Availability Statement

Large model checkpoints are not included due to size, licensing, and reproducibility constraints. The implementation is designed for:

- ViT-B/16 or equivalent vision encoder.
- GPT-4o or equivalent Vision-Language Model API.
- EasyOCR or equivalent OCR component.

See `models/pretrained_model_placeholder.md` for details.

## Installation

```bash
pip install -r requirements.txt
```

Optional conda setup:

```bash
conda env create -f environment.yml
conda activate apo-framework
```

## Run Demo

```bash
python examples/run_demo.py
```

Expected output:

```text
APO demo completed successfully.
Output saved to results/sample_output.json
```

## Run Tests

```bash
pytest tests/
```

## Example APO State Object

The pipeline produces a JSON-like state containing:

- input image reference
- diagnostic payload
- detected errors
- learner frustration level
- scaffolding tier
- pedagogical path
- multimodal scaffolding output
- session history

## Disclaimer

This repository is for academic demonstration only. It is not a clinical diagnostic tool and should not be used to label or diagnose children. Any real deployment must involve qualified educators, psychologists, ethics review, informed consent, and privacy-preserving data handling.

## Citation

If this repository supports your work, please cite the accompanying paper and this repository using `CITATION.cff`.
