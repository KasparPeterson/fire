from typing import List

from fire import ai_classifier
from fire import filter_out_credits
from fire import generate_report
from fire import sort_by_month
from fire import utils
from fire.entities import Category
from fire.entities import CleanBankRow
from fire import data_ingestion
from fire.entities import MonthlyCleanBankRows
from fire.entities import Report


def main():
    rows: List[CleanBankRow] = data_ingestion.execute()
    print("DEBUG, before filter out credits:", len(rows))
    rows: List[CleanBankRow] = filter_out_credits.execute(rows)
    print("DEBUG, after filter out credits:", len(rows))
    rows: List[CleanBankRow] = _ai_classify_uncategorised(rows)
    rows_by_month: List[MonthlyCleanBankRows] = sort_by_month.execute(rows)

    report = generate_report.execute(rows_by_month)
    print("\n\n\nFINAL REPORT:")
    print(report)
    _dump_to_json(report)
    _dump_to_frontend(report)


def _ai_classify_uncategorised(rows: List[CleanBankRow]) -> List[CleanBankRow]:
    """
    1. create two lists - categorized, uncategorized
    2. categorize the uncatogerized
    3. concatenate the two lists and return
    """
    categorized, uncategorized = [], []
    for row in rows:
        if row.category == Category.UNCATEGORIZED:
            uncategorized.append(row)
        else:
            categorized.append(row)
    print("DEBUG, categorized rows:", len(categorized))
    print("DEBUG, uncategorized rows:", len(uncategorized))
    new_rows = ai_classifier.execute(uncategorized)
    return categorized + new_rows


def _dump_to_json(report: Report):
    with open("report.json", "w") as file:
        file.write(utils.serialize(report))


def _dump_to_frontend(report: Report):
    tsx_content = f"export const reportData = {utils.serialize(report)};"
    with open("frontend/src/data/reports.ts", "w") as file:
        file.write(tsx_content)


if __name__ == "__main__":
    main()
