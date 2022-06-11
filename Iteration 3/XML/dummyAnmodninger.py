from Anmodninger import Anmodninger
from anmodningerList import anmodningerList


class dummyObjects:
    """Klassen indeholder dummy værdier, som kan bruges til at lave en xml-fil"""
    @staticmethod
    def create():
        anmodninger = anmodningerList()
        anmodninger.append_anmodning(Anmodninger(1, 'Hugo', 'Systemudvikling - lecture', '13-06-2022','10:15-12:00'))
        anmodninger.append_anmodning(Anmodninger(2, 'Jakob', 'Systemudvikling - theo exercise', '13-06-2022','13:15-15:00'))
        anmodninger.append_anmodning(Anmodninger(3, 'Yaasir', 'Sygdomslære - forelæsning', '15-06-2022', '13:15-15:00'))

        return anmodninger
