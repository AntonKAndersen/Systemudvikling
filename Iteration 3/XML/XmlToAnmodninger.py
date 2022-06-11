from lxml import objectify
from anmodningerList import anmodningerList
from Anmodninger import Anmodninger


class XmlToAnmodninger:

    def __init__(self, xml_filename):
        self.xml_filename = xml_filename

    def parseXML(self) -> anmodningerList:
        """Konverterer xml-filen til anmodninger"""
        with open(self.xml_filename, "rb") as f:
            xml = f.read()

        # Gemmer xml-filens indhold i variablen root
        root = objectify.fromstring(xml)

        anmodninger = anmodningerList()

        # For hver anmodning i xml-filen
        for anmodning in root.getchildren():
            # Oprettes der et objekt med anmodningens attributter
            anmodning_obj = Anmodninger(anmodning.id,anmodning.underviser,anmodning.kursus,anmodning.dato,anmodning.tid)
            # Tiløjer anmodningerne til listen
            anmodninger.append_anmodning(anmodning_obj)

        return anmodninger