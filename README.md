# Fire

[![unit tests](https://github.com/KasparPeterson/fire/actions/workflows/unit_tests.yml/badge.svg)](https://github.com/KasparPeterson/fire/actions/workflows/unit_tests.yml)

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

* use AI to categorise unknowns
* ignore duplicates in data ingestion
* add tests and get to TDD
* add Rest API
* add monthly trends per category
* each category needs to be the same color on every graph
* click on a category to see all transactions in that category
