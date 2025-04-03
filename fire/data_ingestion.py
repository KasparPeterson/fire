import os
import csv
from typing import List

from fire import classifier
from fire.entities import CleanBankRow
from fire.entities import RawBankRow

RAW_FILES_PATH = "data/raw"


def execute() -> List[CleanBankRow]:
    """
    Reads all the raw files and converts to clean bank row which already has the
    category attached so it can be easily used to visualise and aggregate
    :return: list of processed and categories bank rows from bank statement
    """
    result = []
    for file in os.listdir(RAW_FILES_PATH):
        file_path = os.path.join(RAW_FILES_PATH, file)
        raw_bank_rows = _read_bank_rows(file_path)
        clean_bank_rows = _clean(raw_bank_rows)
        result += clean_bank_rows
    return result


def _read_bank_rows(file_path: str) -> List[RawBankRow]:
    input_file = csv.DictReader(open(file_path))
    bank_rows = []
    for row in input_file:
        bank_rows.append(RawBankRow(
            account_name=row['\ufeff"Kliendi konto"'],
            date=row['Kuupäev'],
            payment_to=row['Saaja/maksja nimi'],
            amount=row['Summa'],
            description=row['Selgitus']
        ))
    return bank_rows


def _clean(raw_bank_rows: List[RawBankRow]) -> List[CleanBankRow]:
    result: List[CleanBankRow] = []
    for row in raw_bank_rows:
        result.append(CleanBankRow(
            account_name=row.account_name,
            date=row.date,
            payment_to=row.payment_to,
            amount=row.amount,
            description=row.description,
            category=classifier.get_category(row)
        ))
    return result
