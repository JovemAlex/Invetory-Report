from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path: str):
        inventory = []

        Importer.ext_validation(path, "csv")

        with open(path) as csvfile:
            data = csv.DictReader(csvfile)

            for row in data:
                inventory.append(row)

        return inventory
