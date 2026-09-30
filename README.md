# python-uv-workspace

A tiny Python project built with `uv` to verify that the development environment is working correctly. It creates a small DataFrame with sample values and renders a bar chart using `pandas`, `matplotlib`, and `seaborn`.

## What this project does

This app is intentionally minimal and acts as a quick smoke test for a Python environment:

- creates a simple dataset
- builds a pandas DataFrame
- plots the data with seaborn
- displays a bar chart using matplotlib

It is useful as a starting point for learning how to manage a Python project with `uv` and validate that common scientific libraries are installed and working.

## Project structure

```text
.
├── app.py
├── pyproject.toml
├── README.md
├── src/
│   └── python_uv_workspace/
│       └── __init__.py
└── hello.ipynb
```

## Requirements

- Python 3.14+
- `uv` package manager

## Setup

1. Install `uv` if you do not already have it:

```bash
pip install uv
```

2. Create the environment and install dependencies:

```bash
uv sync
```

3. Run the app:

```bash
uv run app.py
```

This will open a chart window showing a basic validation plot.

## Dependencies

The project currently uses:

- `pandas`
- `matplotlib`
- `seaborn`
- `ipykernel`

## Notes

This project is a lightweight starter template, so it is intentionally simple. You can extend it by adding more data processing, visualization, or project code in the `src/python_uv_workspace` package.
