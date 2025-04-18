# Fire

[![unit tests](https://github.com/KasparPeterson/fire/actions/workflows/unit_tests.yml/badge.svg)](https://github.com/KasparPeterson/fire/actions/workflows/unit_tests.yml)

Simple personal app to analyse my spendings based on my bank statements. Combines multiple .csv outputs from multiple different Estonian banks. Supports adding manual rules for categorisation. What is not being categorised by python will be categorised by an LLM.

Python backend for categorisation and providing a structured json.
Frontend for visualisation and charts.

### Setup

```shell
pip install -r requirements.txt
```

### Usage

Export bank statements into ```data/raw``` as csv.

```shell
python main.py
```

### Frontend

See [frontend/README.md](frontend/README.md)


### TODO:

- [x] filter out credit payments before
- [x] use AI to categorise unknowns
- [ ] ignore duplicates in data ingestion
- [x] add tests and get to TDD
- [ ] add Rest API
- [ ] add monthly trends per category
- [ ] each category needs to be the same color on every graph
- [ ] click on a category to see all transactions in that category
- [ ] use UI to categorize and save mappings
