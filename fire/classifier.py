from fire.entities import RawBankRow


def is_bank_fees(row: RawBankRow) -> bool:
    if row.description.startswith('Ülekande teenustasu.'):
        return True
    return False
