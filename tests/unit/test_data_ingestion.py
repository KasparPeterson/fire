from fire import data_ingestion


def setup_module():
    data_ingestion.RAW_FILES_PATH = "tests/assets/raw"


def test_execute():
    result = data_ingestion.execute()
    assert len(result) == 5
    assert result[0].account_name == "EE010123745607892123"
    assert result[0].date == "2025-01-01"
    assert result[0].payment_to == "OLEREX TALLINN LAAGNA"
    assert result[0].amount == "-8.85"
