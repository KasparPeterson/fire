from fire import generate_report
from fire.entities import Category
from fire.entities import MonthlyCleanBankRows
from fire.entities import MonthlyReport
from fire.entities import Report
from tests.unit.example_rows import INCOME_ROW
from tests.unit.example_rows import TRAVEL_ROW


def test_execute_one_month_one_spending():
    monthly_row = MonthlyCleanBankRows(
        month="2025-03-01",
        rows=[TRAVEL_ROW],
    )
    result = generate_report.execute([monthly_row])
    expected = Report(
        reports=[
            MonthlyReport(
                month="2025-03-01",
                income="0.00",
                outcome="-123.45",
                spendings={str(Category.TRAVEL): "-123.45"},
                detailed_spendings={
                    str(Category.TRAVEL): [TRAVEL_ROW],
                },
            )
        ]
    )
    assert expected == result


def test_execute_one_month_one_spending_one_income():
    monthly_row = MonthlyCleanBankRows(
        month="2025-03-01",
        rows=[TRAVEL_ROW, INCOME_ROW],
    )
    result = generate_report.execute([monthly_row])
    expected = Report(
        reports=[
            MonthlyReport(
                month="2025-03-01",
                income="456.78",
                outcome="-123.45",
                spendings={
                    str(Category.TRAVEL): "-123.45",
                    str(Category.INCOME): "456.78",
                },
                detailed_spendings={
                    str(Category.TRAVEL): [TRAVEL_ROW],
                    str(Category.INCOME): [INCOME_ROW],
                },
            )
        ]
    )
    assert expected == result
