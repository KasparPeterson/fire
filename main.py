import json
import dataclasses
from typing import List
from enum import Enum

from fire import generate_report
from fire import sort_by_month
from fire.entities import CleanBankRow
from fire import data_ingestion
from fire.entities import MonthlyCleanBankRows
from fire.entities import Report

"""
TODO:
* handle duplicates in data_ingestion
"""


def main():
    rows: List[CleanBankRow] = data_ingestion.execute()
    rows_by_month: List[MonthlyCleanBankRows] = sort_by_month.execute(rows)
    report = generate_report.execute(rows_by_month)
    print("\n\n\nFINAL REPORT:")
    print(report)
    _dump_to_json(report)
    _dump_to_frontend(report)


def custom_serializer(obj):
    if isinstance(obj, Enum):
        return obj.value  # Convert Enum to string
    if dataclasses.is_dataclass(obj):
        return dataclasses.asdict(obj)  # Convert dataclass to dictionary
    raise TypeError(f"Type {type(obj)} not serializable")


def _report_to_json(report: Report):
    return json.dumps(report, default=custom_serializer, indent=2)


def _dump_to_json(report: Report):
    with open("report.json", "w") as file:
        file.write(_report_to_json(report))


def _dump_to_frontend(report: Report):
    tsx_content = f"export const reportData = {_report_to_json(report)};"
    with open("frontend/src/data/reports.ts", "w") as file:
        file.write(tsx_content)


if __name__ == '__main__':
    main()
