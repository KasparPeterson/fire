from typing import Optional

from fire.entities import Category
from fire.entities import RawBankRow
from fire import maps


def get_category(row: RawBankRow) -> Category:
    if category := _get_payment_to_match(row):
        return category

    if category := _get_payment_to_starts_with_match(row):
        return category

    if category := _get_description_starts_with_match(row):
        return category

    if _is_bank_fees(row):
        return Category.BANK_FEES

    return Category.UNCATEGORIZED


def _is_bank_fees(row: RawBankRow) -> bool:
    if row.description.startswith('Ülekande teenustasu.'):
        return True
    return False


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
