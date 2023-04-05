from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(path: str):

        Importer.ext_validation(path, "xml")

        with open(path) as xmlfile:
            data = xmltodict.parse(xmlfile.read())
            return data["dataset"]["record"]
