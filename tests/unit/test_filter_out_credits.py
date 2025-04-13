from fire import filter_out_credits
from tests.unit.example_rows import ROW_CREDIT_INCOME
from tests.unit.example_rows import ROW_CREDIT_OUTCOME
from tests.unit.example_rows import TRAVEL_ROW


def test_empty():
    result = filter_out_credits.execute([])
    assert [] == result


def test_no_credits():
    result = filter_out_credits.execute([TRAVEL_ROW])
    assert [TRAVEL_ROW] == result


def test_only_income_credits():
    result = filter_out_credits.execute([ROW_CREDIT_INCOME])
    assert [ROW_CREDIT_INCOME] == result


def test_only_outcome_credits():
    result = filter_out_credits.execute([ROW_CREDIT_OUTCOME])
    assert [ROW_CREDIT_OUTCOME] == result


def test_has_income_outcome_credits():
    result = filter_out_credits.execute(
        [ROW_CREDIT_INCOME, TRAVEL_ROW, ROW_CREDIT_OUTCOME]
    )
    assert [TRAVEL_ROW] == result
