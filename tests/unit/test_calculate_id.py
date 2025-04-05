from fire import calculate_id
from fire.entities import RawBankRow

ROW = RawBankRow(
    account_name="abc123",
    date="date123",
    payment_to="def456",
    amount="123.45",
    description="ghi789",
)


def test_execute():
    result = calculate_id.execute(ROW)
    assert result == "5673d13de9d5e0a1d90375a441dfb3463e4328cc244953ecb565f3c4351f8ce7"
