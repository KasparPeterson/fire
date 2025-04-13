from typing import Dict
from typing import List
from decimal import Decimal

from fire import utils
from fire.entities import CleanBankRow
from fire.entities import MonthlyCleanBankRows
from fire.entities import MonthlyReport
from fire.entities import Report


def execute(rows_by_month: List[MonthlyCleanBankRows]) -> Report:
    report = Report(reports=[])
    for monthly_rows in rows_by_month:
        utils.print_stats(monthly_rows)
        monthly_report = _generate_monthly(monthly_rows.rows)
        report.reports.append(monthly_report)
    return report


def _generate_monthly(bank_rows: List[CleanBankRow]) -> MonthlyReport:
    """

    :param bank_rows:
    :return: report as a simple dictionary that is serializable
    """
    income, outcome = _get_income_outcome(bank_rows)
    print("Income:", income)
    print("Outcome:", outcome)

    report = {}
    detailed_spendings = {}
    total = Decimal(0)
    for row in bank_rows:
        category = str(row.category)
        if category in report:
            report[category] = report[category] + Decimal(row.amount)
            detailed_spendings[category].append(row)
        else:
            report[category] = Decimal(row.amount)
            detailed_spendings[category] = [row]
        total += Decimal(row.amount)

    print("\n# Report for", bank_rows[0].date)
    sorted_report = _sort(report)
    print(f"    total: {total}")

    return MonthlyReport(
        month=bank_rows[0].date,
        income=income,
        outcome=outcome,
        spendings=sorted_report,
        detailed_spendings=detailed_spendings,
    )


def _sort(report: Dict):
    result = dict(sorted(report.items(), key=lambda item: item[1]))
    for key, value in result.items():
        print(f"    {key}: {value}")
        result[key] = str(value)

    return result


def _get_income_outcome(bank_rows: List[CleanBankRow]) -> (str, str):
    income = 0
    outcome = 0
    for row in bank_rows:
        amount = row.get_float_amount()
        if amount < 0:
            outcome += amount
        else:
            income += amount

    return f"{income:.2f}", f"{outcome:.2f}"
