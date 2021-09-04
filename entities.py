import enum
from dataclasses import dataclass


class Category(enum.Enum):
    GROCERIES = "groceries"
    BANK_FEES = "bank_fees"
    SUPPORT_OTHERS = "support_others"
    HEALTH = "health"
    ALCOHOL = "alcohol"
    TAXI = "taxi"
    RESTAURANT = "restaurant"
    SELF = "self"
    TRAVEL = "travel"
    ENTERTAINMENT = "entertainment"
    CASH_OUT = "cash_out"
    CRYPTO = "crypto"
    ELECTRONICS = "electronics"
    TECHNOLOGY = "technology"
    EDUCATION = "education"
    INVESTMENT = "investment"


@dataclass(frozen=True)
class RawBankRow:
    account_name: str
    date: str
    payment_to: str
    amount: str
    description: str


@dataclass(frozen=True)
class CleanBankRow:
    account_name: str
    date: str
    payment_to: str
    amount: str
    description: str
    category: Category
