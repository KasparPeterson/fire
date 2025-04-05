import enum
from dataclasses import dataclass
from typing import List, Dict


class Category(enum.Enum):
    GROCERIES = "groceries"
    BANK_FEES = "bank_fees"
    CHARITY = "charity"
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


@dataclass(frozen=False)
class CleanBankRow:
    id: str
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

    @staticmethod
    def from_dict(data: Dict) -> 'CleanBankRow':
        return CleanBankRow(
            id=data["id"],
            account_name=data["account_name"],
            date=data["date"],
            payment_to=data["payment_to"],
            amount=data["amount"],
            description=data["description"],
            category=CleanBankRow._get_category(data["category"]),
        )

    @staticmethod
    def _get_category(category: str) -> Category:
        try:
            return Category(category)
        except ValueError:
            print(f"EXCEPTION, ValueError, invalid category with value: {category}")
            return Category.UNCATEGORIZED


@dataclass(frozen=True)
class MonthlyCleanBankRows:
    month: str
    rows: List[CleanBankRow]


@dataclass(frozen=True)
class MonthlyReport:
    month: str
    income: str
    outcome: str
    spendings: Dict[Category, str]


@dataclass(frozen=True)
class Report:
    reports: List[MonthlyReport]
