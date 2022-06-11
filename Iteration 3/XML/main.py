from lxml import etree
from dummyAnmodninger import dummyObjects
from AnmodningerToXml import AnmodningerToXml
from XmlToAnmodninger import XmlToAnmodninger


if __name__ == "__main__":
    # Laver 2 dummy anmodninger, som kan bruges til at teste med
    print("Opretter dummy anmodninger")
    anmodningList = dummyObjects.create()

    print("\nListe med dummy anmodninger skrives til anmodninger.xml")
    AnmodningerToXml(anmodningList).write_file()

    print("\nxml filen indlæses og gemmes i variablen anmodningList")
    anmodningList=XmlToAnmodninger('anmodninger.xml').parseXML()

    print("\nListen af anmodninger er af typen:", type(anmodningList))
    anmodninger=anmodningList.get_anmodningerList()

    print("\nOg anmodninger er af typen:",type(anmodninger))

    print("\nHerunder ses anmodningerne fra xml-filen:")
    for a in anmodninger:
        print(a)

    print("\nTjekker xml-filen opmod (Document Type Definition) dtd-filen:")
    dtd = etree.DTD(open('anmodninger.dtd'))
    print("Validering af anmodninger.xml er ok: ",dtd.validate(etree.parse('anmodninger.xml')))




