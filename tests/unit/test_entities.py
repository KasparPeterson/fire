from fire.entities import Category
from fire.entities import CleanBankRow


def test_category_from_dict():
    result = CleanBankRow.from_dict(
        {
            "id": "id1",
            "account_name": "account_name1",
            "date": "date1",
            "payment_to": "payment_to1",
            "amount": "amount1",
            "description": "description1",
            "category": "groceries",
        }
    )
    assert result == CleanBankRow(
        id="id1",
        account_name="account_name1",
        date="date1",
        payment_to="payment_to1",
        amount="amount1",
        description="description1",
        category=Category.GROCERIES,
    )


def test_category_from_dict_invalid_category():
    result = CleanBankRow.from_dict(
        {
            "id": "id1",
            "account_name": "account_name1",
            "date": "date1",
            "payment_to": "payment_to1",
            "amount": "amount1",
            "description": "description1",
            "category": "abc",
        }
    )
    assert result == CleanBankRow(
        id="id1",
        account_name="account_name1",
        date="date1",
        payment_to="payment_to1",
        amount="amount1",
        description="description1",
        category=Category.UNCATEGORIZED,
    )
