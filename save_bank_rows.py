from typing import List

import numpy as np

from entities import CleanBankRow

"""
    account_name: str
    date: str
    payment_to: str
    amount: str
    description: str
    category: Category
"""


def execute(bank_rows: List[CleanBankRow]):
    columns = _get_columns(bank_rows)
    np.savetxt('data/data.csv', columns, delimiter=',', fmt='%s')


def _get_columns(bank_rows: List[CleanBankRow]):
    result = []
    for row in bank_rows:
        result.append([
            row.account_name,
            row.date,
            row.payment_to,
            row.amount,
            row.description,
            row.category.value
        ])
    return result
