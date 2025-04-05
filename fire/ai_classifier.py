import json
import time
from typing import Dict
from typing import List
import os
from openai import OpenAI

from fire import utils
from fire.entities import Category
from fire.entities import CleanBankRow

BATCH_SIZE = 100
PROMPT = """
Given these bank statement lines:
{LINES}

Add category to each item. Maintain the same data format and order.
Allowed categories are:
{CATEGORIES}

Return data as JSON please!
"""


def execute(rows: List[CleanBankRow]) -> List[CleanBankRow]:
    result = []
    for i in range(int(len(rows) / BATCH_SIZE)):
        batch = rows[i * BATCH_SIZE : (i + 1) * BATCH_SIZE]
        result += _handle_batch(batch)
    return result


def _handle_batch(rows: List[CleanBankRow]) -> List[CleanBankRow]:
    print("\nDEBUG, rows for classifying:", len(rows))

    prompt = _generate_prompt(rows)
    # print("\nDEBUG, openai prompt:", prompt)
    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_API_KEY"),
    )
    response = client.responses.create(
        model="gpt-4o",
        instructions="You are financial advisor who is excellent in understanding each "
        "line in a bank statement and to what category it belongs to",
        input=prompt,
    )
    # print("\nDEBUG, openai response:\n", response.output_text, "\n")
    json_data = _markdown_to_json_dict(response.output_text)
    return _json_to_clean_bank_rows(json_data)


def _generate_prompt(rows: List[CleanBankRow]) -> str:
    lines = utils.serialize(rows)
    categories = json.dumps([category.value for category in Category])
    prompt = PROMPT.format(LINES=lines, CATEGORIES=categories)
    return prompt


def _markdown_to_json_dict(text: str) -> Dict:
    text = text.strip()
    if text.startswith("```json"):
        text = text.strip().removeprefix("```json").removesuffix("```").strip()
    print("\ntext:", text)
    return json.loads(text)


def _json_to_clean_bank_rows(json_data: Dict) -> List[CleanBankRow]:
    result = []
    for data in json_data:
        result.append(CleanBankRow.from_dict(data))
    return result


if __name__ == "__main__":
    ROWS = [
        CleanBankRow(
            id="id1",
            account_name="EE757700771003840208",
            date="2024-09-27",
            payment_to="Truebarbers o\u00dc",
            amount="-56.00",
            description="Juuksur",
            category=Category.UNCATEGORIZED,
        ),
        CleanBankRow(
            id="id2",
            account_name="EE757700771003840208",
            date="2024-09-15",
            payment_to="RAHVA RAAMAT AS",
            amount="-16.58",
            description="WT2109605,rahvaraamat.ee",
            category=Category.UNCATEGORIZED,
        ),
    ]
    execute(ROWS)
