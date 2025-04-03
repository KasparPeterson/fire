import enum
from dataclasses import dataclass
from typing import List, Dict


class Category(enum.Enum):
    GROCERIES = "groceries"
    BANK_FEES = "bank_fees"
    SUPPORT_OTHERS = "support_others"  # TODO: Is it gifts/donations?
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
    INCOME = "income"
    RENT = "rent"
    UTILITIES = "utilities"
    KIDS = "kids"
    CAR = "car"
    HOME = "home"
    SHOPPING = "shopping"
    BEAUTY = "beauty"
    UNCATEGORIZED = "uncategorized"


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

    def get_float_amount(self) -> float:
        try:
            return float(self.amount)
        except:
            print("Failed to convert amount:", self.amount)
        return 0.0


@dataclass(frozen=True)
class MonthlyCleanBankRows:
    month: str
    rows: List[CleanBankRow]


@dataclass(frozen=True)
class MonthlyReport:
    month: str
    spendings: Dict[Category, str]


@dataclass(frozen=True)
class Report:
    reports: List[MonthlyReport]
