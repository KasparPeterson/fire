from fire.entities import Category
from fire.entities import CleanBankRow

TRAVEL_ROW = CleanBankRow(
    id="id1",
    account_name="name1",
    date="2025-03-01",
    payment_to="abc1",
    amount="-123.45",
    description="desc1",
    category=Category.TRAVEL,
)
INCOME_ROW = CleanBankRow(
    id="id2",
    account_name="name2",
    date="2025-03-01",
    payment_to="abc2",
    amount="456.78",
    description="desc2",
    category=Category.INCOME,
)
SELF_ROW = CleanBankRow(
    id="id3",
    account_name="name3",
    date="2025-03-01",
    payment_to="abc3",
    amount="789.01",
    description="desc3",
    category=Category.SELF,
)
ROW_CREDIT_INCOME = CleanBankRow(
    id="id4",
    account_name="an4",
    date="2025-03-10",
    payment_to="",
    amount="123.45",
    description="P\u00fcsimakse kaardikontole",
    category=Category.SELF,
)
ROW_CREDIT_OUTCOME = CleanBankRow(
    id="id5",
    account_name="an5",
    date="2025-03-10",
    payment_to="",
    amount="-123.45",
    description="P\u00fcsimakse kaardikontole",
    category=Category.SELF,
)
