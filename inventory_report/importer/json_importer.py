from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path: str):
        inventory = []

        Importer.ext_validation(path, "json")

        with open(path) as csvfile:
            data = json.load(csvfile)

            for row in data:
                inventory.append(row)

        return inventory
