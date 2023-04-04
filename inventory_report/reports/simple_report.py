from collections import Counter
from datetime import date


class SimpleReport:
    @classmethod
    def company_with_most_product(cls, list):
        counter = Counter([d["nome_da_empresa"] for d in list])
        most_commom_company = counter.most_common(1)[0][0]
        return most_commom_company

    @classmethod
    def get_older_date(cls, list):
        older_date = str(date.max)
        for product in list:
            if product["data_de_fabricacao"] <= older_date:
                older_date = product["data_de_fabricacao"]

        return older_date

    @classmethod
    def get_validity(cls, list):
        today = str(date.today())
        validity = str(date.max)
        for product in list:
            if today <= product["data_de_validade"] < validity:
                validity = product["data_de_validade"]

        return validity

    @staticmethod
    def generate(list):
        company = SimpleReport.company_with_most_product(list)
        older_date = SimpleReport.get_older_date(list)
        validity = SimpleReport.get_validity(list)

        return f"""Data de fabricação mais antiga: {older_date}
Data de validade mais próxima: {validity}
Empresa com mais produtos: {company}"""
