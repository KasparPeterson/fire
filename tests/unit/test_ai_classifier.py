from fire import ai_classifier
from fire.entities import Category
from fire.entities import CleanBankRow

ROWS = [
    CleanBankRow(
        id="id1",
        account_name="abc1",
        date="date",
        payment_to="def2",
        amount="123.12",
        description="ghi3",
        category=Category.UNCATEGORIZED,
    ),
    CleanBankRow(
        id="id2",
        account_name="abc2",
        date="date",
        payment_to="def3",
        amount="129.33",
        description="ghi4",
        category=Category.UNCATEGORIZED,
    ),
]


def test_generate_prompt():
    result = ai_classifier._generate_prompt(ROWS)
    assert (
        result
        == """
Given these bank statement lines:
[
  {
    "id": "id1",
    "account_name": "abc1",
    "date": "date",
    "payment_to": "def2",
    "amount": "123.12",
    "description": "ghi3",
    "category": "uncategorized"
  },
  {
    "id": "id2",
    "account_name": "abc2",
    "date": "date",
    "payment_to": "def3",
    "amount": "129.33",
    "description": "ghi4",
    "category": "uncategorized"
  }
]

Add category to each item. Maintain the same data format and order.
Allowed categories are:
["groceries", "bank_fees", "charity", "health", "alcohol", "taxi", "restaurant", "self", "travel", "entertainment", "cash_out", "crypto", "electronics", "technology", "education", "investment", "income", "rent", "utilities", "kids", "car", "home", "shopping", "beauty", "uncategorized"]

Return data as JSON please!
"""
    )


def test_markdown_to_json_dict():
    result = ai_classifier._markdown_to_json_dict(
        """
 ```json
[
  {
    "id": "id1",
    "account_name": "EE757700771003840208",
    "date": "2024-09-27",
    "payment_to": "Truebarbers oÜ",
    "amount": "-56.00",
    "description": "Juuksur",
    "category": "beauty"
  }
]
```
    """
    )
    assert result == [
        {
            "id": "id1",
            "account_name": "EE757700771003840208",
            "date": "2024-09-27",
            "payment_to": "Truebarbers oÜ",
            "amount": "-56.00",
            "description": "Juuksur",
            "category": "beauty",
        }
    ]


def test_json_to_clean_bank_rows():
    result = ai_classifier._json_to_clean_bank_rows(
        [
            {
                "id": "id1",
                "account_name": "EE757700771003840208",
                "date": "2024-09-27",
                "payment_to": "Truebarbers oÜ",
                "amount": "-56.00",
                "description": "Juuksur",
                "category": "beauty",
            }
        ]
    )
    assert result == [
        CleanBankRow(
            id="id1",
            account_name="EE757700771003840208",
            date="2024-09-27",
            payment_to="Truebarbers oÜ",
            amount="-56.00",
            description="Juuksur",
            category=Category.BEAUTY,
        )
    ]
