from typing import List
import matplotlib.pyplot as plt

from fire.entities import CleanBankRow


def execute(bank_rows: List[CleanBankRow]):
    # _plot(report)
    pass


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
