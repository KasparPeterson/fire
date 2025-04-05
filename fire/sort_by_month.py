from typing import List

from fire.entities import CleanBankRow
from fire.entities import MonthlyCleanBankRows


def execute(rows: List[CleanBankRow]) -> List[MonthlyCleanBankRows]:
    """
    Sorts bank rows by month
    :return:
    """
    months = {}
    for row in rows:
        month = _get_month(row)
        if month in months:
            months[month].append(row)
        else:
            months[month] = [row]

    result = []
    for month, rows in months.items():
        result.append(MonthlyCleanBankRows(month=month, rows=rows))
    return result


def _get_month(row: CleanBankRow) -> str:
    return "-".join(row.date.split("-")[:2])
