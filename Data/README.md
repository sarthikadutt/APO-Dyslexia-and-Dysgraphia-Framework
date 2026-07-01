# Data Directory

This directory contains only a demo dataset for running the APO pipeline.

## Important Notice

The full experimental datasets described in the manuscript are **not** redistributed here.

The paper describes two data streams:

1. **IAM Handwriting Database**  
   A real normative handwriting dataset. Users must obtain it from the official IAM source and follow its licensing terms.

2. **Disability-specific handwriting samples**  
   Real handwriting samples associated with dyslexia/dysgraphia indicators. These are not publicly released in this repository because such data may involve privacy, consent, and ethics restrictions.

## Demo Dataset

The `demo_dataset/` folder contains small synthetic/demo records. These are included only to verify that the code executes and produces the expected APO state object.

These demo samples are **not** clinical data and must not be used for diagnostic claims.

## Recommended Full-Study Data Structure

For authorized reproduction, organize approved data as:

```text
data/
├── iam/
│   ├── raw/
│   ├── processed/
│   └── metadata.csv
├── disability_specific/
│   ├── raw/
│   ├── processed/
│   └── labels.csv
└── demo_dataset/
```

