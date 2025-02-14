from typing import Dict
from typing import List
from decimal import Decimal

from fire.entities import CleanBankRow


def execute(bank_rows: List[CleanBankRow]) -> Dict:
    """

    :param bank_rows:
    :return: report as a simple dictionary that is serializable
    """
    income, outcome = _get_income_outcome(bank_rows)
    print("Income:", income)
    print("Outcome:", outcome)

    report = {}
    total = Decimal(0)
    for row in bank_rows:
        category = str(row.category)
        if category in report:
            report[category] = report[category] + Decimal(row.amount)
        else:
            report[category] = Decimal(row.amount)
        total += Decimal(row.amount)

    print("\n# Report for", bank_rows[0].date)
    sorted_report = dict(sorted(report.items(), key=lambda item: item[1]))
    for key, value in sorted_report.items():
        print(f"    {key}: {value}")
        sorted_report[key] = str(value)
    print(f"    total: {total}")
    return sorted_report


def _get_income_outcome(bank_rows: List[CleanBankRow]) -> (float, float):
    income = 0
    outcome = 0
    for row in bank_rows:
        amount = row.get_float_amount()
        if amount < 0:
            outcome += amount
        else:
            income += amount

    return income, outcome
