from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        counter = Counter([p["nome_da_empresa"] for p in list])
        simple_report = SimpleReport.generate(list)
        companies = ""

        for company, quantity in counter.items():
            companies += f"- {company}: {quantity}\n"

        return f"""{simple_report}
Produtos estocados por empresa:
{companies}"""
