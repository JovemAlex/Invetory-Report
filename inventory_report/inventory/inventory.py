from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @classmethod
    def read_file(cls, path: str, file: str):
        ext = path.split(".")[-1]

        if ext == "csv":
            return csv.DictReader(file)

        if ext == "json":
            return json.load(file)

        if ext == "xml":
            with open(path) as xmlfile:
                data = xmltodict.parse(xmlfile.read())
                return data["dataset"]["record"]

    @staticmethod
    def import_data(path: str, type: str):
        inventory = []

        with open(path) as file:
            data = Inventory.read_file(path, file)

            for row in data:
                inventory.append(row)

        if type == "simples":
            return SimpleReport.generate(inventory)
        if type == "completo":
            return CompleteReport.generate(inventory)
