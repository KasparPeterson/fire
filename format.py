import os
import csv
from typing import List
from typing import Optional

import analyse
import maps
import save_bank_rows
from entities import Category
from entities import CleanBankRow
from entities import RawBankRow

RAW_FILES_PATH = "data/raw"


def main():
    for file in os.listdir(RAW_FILES_PATH):
        file_path = os.path.join(RAW_FILES_PATH, file)
        raw_bank_rows = _read_bank_rows(file_path)
        clean_bank_rows = _clean(raw_bank_rows)

        uncategorised_count = 0
        for row in clean_bank_rows:
            if not row.category:
                print(row, "\n")
                uncategorised_count += 1
        print("uncategorised_count:", uncategorised_count)

        save_bank_rows.execute(clean_bank_rows)
        analyse.execute(clean_bank_rows)


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
            category=_get_category(row)
        ))
    return result


def _get_category(row: RawBankRow) -> Optional[Category]:
    if category := _get_payment_to_match(row):
        return category

    if category := _get_payment_to_starts_with_match(row):
        return category

    if category := _get_description_starts_with_match(row):
        return category

    if _is_bank_fees(row):
        return Category.BANK_FEES


def _is_bank_fees(row: RawBankRow) -> bool:
    if row.description.startswith('Ülekande teenustasu.'):
        return True


def _get_payment_to_match(row: RawBankRow) -> Optional[Category]:
    for key, value in maps.payment_to.items():
        if row.payment_to == key:
            return value


def _get_payment_to_starts_with_match(row: RawBankRow) -> Optional[Category]:
    for key, value in maps.payment_to_starts_with.items():
        if row.payment_to.startswith(key):
            return value


def _get_description_starts_with_match(row: RawBankRow) -> Optional[Category]:
    for key, value in maps.description_starts_with.items():
        if row.description.startswith(key):
            return value


if __name__ == '__main__':
    main()
