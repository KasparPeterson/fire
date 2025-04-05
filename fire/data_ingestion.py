import os
import csv
from typing import List

from fire import calculate_id
from fire import classifier
from fire.entities import CleanBankRow
from fire.entities import RawBankRow

RAW_FILES_PATH = "data/raw"

FIELD_ALIASES = {
    "account_name": {"Kliendi konto", "Account name", "Account number"},
    "date": {"Kuupäev", "Date"},
    "payment_to": {"Saaja/maksja nimi", "Name", "Recipient name"},
    "amount": {"Summa", "Amount", "Transaction amount"},
    "description": {"Selgitus", "Description", "Details"}
}


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


def normalize_headers(headers):
    normalized = {}
    for idx, header in enumerate(headers):
        for key, aliases in FIELD_ALIASES.items():
            if header.strip() in aliases:
                normalized[key] = header
                break
    return normalized


def _read_bank_rows(file_path: str) -> List[RawBankRow]:
    reader = csv.DictReader(open(file_path, encoding='utf-8-sig'))
    normalized = normalize_headers(reader.fieldnames)

    bank_rows = []
    for row in reader:
        parsed_row = {
            key: row.get(header, "").strip()
            for key, header in normalized.items()
        }

        bank_rows.append(RawBankRow(
            account_name=parsed_row["account_name"],
            date=parsed_row['date'],
            payment_to=parsed_row['payment_to'],
            amount=parsed_row['amount'],
            description=parsed_row['description']
        ))
    return bank_rows


def _clean(raw_bank_rows: List[RawBankRow]) -> List[CleanBankRow]:
    result: List[CleanBankRow] = []
    for row in raw_bank_rows:
        result.append(CleanBankRow(
            id=calculate_id.execute(row),
            account_name=row.account_name,
            date=row.date,
            payment_to=row.payment_to,
            amount=row.amount,
            description=row.description,
            category=classifier.get_category(row)
        ))
    return result


def _get_account_name(row) -> str:
    return row["Kliendi konto"]
