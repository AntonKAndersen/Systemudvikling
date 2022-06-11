from lxml import etree, objectify
from io import BytesIO
from Elementer import Elementer
from anmodningerList import anmodningerList


class AnmodningerToXml:
    def __init__(self, anmodninger: anmodningerList):
        self.anmodninger = anmodninger

    def write_file(self):

        root = etree.Element("anmodninger")
        for anmodning in self.anmodninger.get_anmodningerList():
            anmodning_element = Elementer.create_anmdoning(anmodning)
            root.append(anmodning_element)

        # rydder op xml-filen - fjerne overflødige elementer
        objectify.deannotate(root)
        etree.cleanup_namespaces(root)

        # laver xml-streng
        parser = etree.XMLParser(remove_blank_text=True)
        objekt = BytesIO(etree.tostring(root))
        tree = etree.parse(objekt, parser)

        # skriver xml-koden ind i filen anmodninger.xml
        try:
            with open("anmodninger.xml", "wb") as xml_writer:
                tree.write(xml_writer, pretty_print=True, encoding='utf-8', xml_declaration=True)
        except IOError:
            pass
