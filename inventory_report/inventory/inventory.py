from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xml.etree.ElementTree as ET


class Inventory:
    @classmethod
    def read_file(cls, path: str, file: str):
        ext = path.split(".")[-1]

        if ext == "csv":
            return csv.DictReader(file)

        if ext == "json":
            return json.load(file)

        if ext == "xml":
            tree = ET.parse(path)
            root = tree.getroot()
            return root

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


print(Inventory.import_data("inventory_report/data/inventory.xml", "simples"))
