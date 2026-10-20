# ETABS Industrial Pipeline

Industrial automation pipeline for structural engineering workflows connecting Revit and ETABS.

## Overview
This project is intended as a production-oriented foundation for:
- exporting structural data from Revit
- validating geometry and metadata
- generating ETABS models
- running structural analyses
- extracting results
- checking drift and utilization
- exporting technical reports

## Requirements
- Windows
- Revit
- ETABS 19+
- Python 3.10+
- pywin32

## Installation
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt