# Fire

### Setup

```shell
conda update -f environment.yml
conda activate fire
```

### Usage

Export bank statements into ```data/raw``` as csv.

```shell
python main.py
```

### Frontend

See [frontend/README.md](frontend/README.md)


### TODO:

* ignore duplicates in data ingestion
* add tests and get to TDD
* add Rest API
* add monthly trends per category
* each category needs to be the same color on every graph