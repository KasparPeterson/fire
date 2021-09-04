from typing import List
from decimal import Decimal
import matplotlib.pyplot as plt

from entities import CleanBankRow


def execute(bank_rows: List[CleanBankRow]):
    report = {}
    for row in bank_rows:
        if row.category in report:
            report[row.category] = report[row.category] + Decimal(row.amount)
        else:
            report[row.category] = Decimal(row.amount)

    print("\n# Report for", bank_rows[0].date)
    sorted_report = dict(sorted(report.items(), key=lambda item: item[1]))
    for key, value in sorted_report.items():
        print(f"    {key}: {value}")

    _plot(report)


def _plot(report: dict):
    labels = []
    sizes = []
    for x, y in report.items():
        if y < 0:
            labels.append(x)
            sizes.append(abs(y))

    # Plot
    plt.pie(sizes, labels=labels)
    plt.axis('equal')
    plt.legend()
    plt.show()
