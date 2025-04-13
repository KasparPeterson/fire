"""
Filters out credit paybacks as they appear as -€X and +€X which introduce
inflated incomes and spendings.

"""

from typing import Dict
from typing import List
from typing import Optional

from fire.entities import CleanBankRow


def execute(rows: List[CleanBankRow]) -> List[CleanBankRow]:
    """
    1. Add all positive incomes to Dict
    2. Check if there is a negative income with the same amount and date
        - if is then add to blacklist
    3. Iterate over the list again and remove blacklisted

    O(n) as little income rows
    """
    positive_incomes = _get_all_positive_incomes(rows)
    # Row id as a key
    blacklisted = set()
    for row in rows:
        match_row = _get_match_for_amount(row, positive_incomes)
        if match_row:
            blacklisted.add(row.id)
            blacklisted.add(match_row.id)

    result = []
    for row in rows:
        if row.id not in blacklisted:
            result.append(row)
        else:
            print("DEBUG, filtering out:", row, "\n")
    return result


def _get_all_positive_incomes(rows: List[CleanBankRow]) -> Dict[str, CleanBankRow]:
    # Row id as a key
    positive_incomes = {}
    for row in rows:
        if float(row.amount) > 0:
            positive_incomes[row.id] = row
    return positive_incomes


def _get_match_for_amount(
    row: CleanBankRow, positive_incomes: Dict[str, CleanBankRow]
) -> Optional[CleanBankRow]:
    for key, value in positive_incomes.items():
        if row.amount == "-" + value.amount and row.date == value.date:
            return value
