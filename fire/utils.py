from fire.entities import Category
from fire.entities import MonthlyCleanBankRows


def print_stats(monthly_rows: MonthlyCleanBankRows):
    print(f"\n======== Month: {monthly_rows.month} ========\n")
    uncategorised_count = 0
    for row in monthly_rows.rows:
        if row.category == Category.UNCATEGORIZED:
            print(row, "\n")
            uncategorised_count += 1
    print("total_count:        ", len(monthly_rows.rows))
    print("uncategorised_count:", uncategorised_count)