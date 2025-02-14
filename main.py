import json
from typing import Dict
from typing import List

from fire import analyse
from fire import generate_report
from fire import sort_by_month
from fire.entities import Category
from fire.entities import CleanBankRow
from fire import data_ingestion
from fire.entities import MonthlyCleanBankRows


def main():
    # TODO: read all files and combine!
    rows: List[CleanBankRow] = data_ingestion.execute()
    rows_by_month: List[MonthlyCleanBankRows] = sort_by_month.execute(rows)
    for monthly_rows in rows_by_month:
        _print_stats(monthly_rows)
        report = generate_report.execute(monthly_rows.rows)
        _dump_to_json(report)


def _print_stats(monthly_rows: MonthlyCleanBankRows):
    print(f"\n======== Month: {monthly_rows.month} ========")
    uncategorised_count = 0
    for row in monthly_rows.rows:
        if row.category == Category.UNCATEGORIZED:
            print(row, "\n")
            uncategorised_count += 1
    print("total_count:        ", len(monthly_rows.rows))
    print("uncategorised_count:", uncategorised_count)

    # save_bank_rows.execute(clean_bank_rows)
    # analyse.execute(monthly_rows.rows)


def _dump_to_json(report: Dict):
    print("\nREPORT:", report)
    with open("report.json", "w") as file:
        file.write(json.dumps(report))


if __name__ == '__main__':
    main()
