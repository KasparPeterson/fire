import hashlib
from enum import Enum
import json
import dataclasses

from fire.entities import Category
from fire.entities import MonthlyCleanBankRows


def print_stats(monthly_rows: MonthlyCleanBankRows):
    print(f"\n======== Month: {monthly_rows.month} ========\n")
    uncategorised_count = 0
    for row in monthly_rows.rows:
        if row.category == Category.UNCATEGORIZED:
            print(serialize(row), "\n")
            uncategorised_count += 1
    print("total_count:        ", len(monthly_rows.rows))
    print("uncategorised_count:", uncategorised_count)


def sha256(input_string: str) -> str:
    input_bytes = input_string.encode('utf-8')
    hash_object = hashlib.sha256(input_bytes)
    return hash_object.hexdigest()


def serialize(data):
    return json.dumps(data, default=_custom_serializer, indent=2)


def _custom_serializer(obj):
    if isinstance(obj, Enum):
        return obj.value  # Convert Enum to string
    if dataclasses.is_dataclass(obj):
        return dataclasses.asdict(obj)  # Convert dataclass to dictionary
    raise TypeError(f"Type {type(obj)} not serializable")
