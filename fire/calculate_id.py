from fire import utils
from fire.entities import RawBankRow


def execute(row: RawBankRow) -> str:
    input_string = " ".join(
        [row.account_name, row.date, row.payment_to, row.amount, row.description]
    )
    return utils.sha256(input_string)
