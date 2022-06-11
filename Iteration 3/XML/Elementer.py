from lxml import objectify
from Anmodninger import Anmodninger

class Elementer:
    """
    Elementer bruges til at definerer hvilke elementer xml-filen skal indeholde
    """
    @staticmethod
    def create_anmdoning(anmodninger_obj: Anmodninger):
        anmodning = objectify.Element("anmodning")
        anmodning.id = anmodninger_obj.get_id()
        anmodning.underviser = anmodninger_obj.get_underviser()
        anmodning.kursus = anmodninger_obj.get_kursus()
        anmodning.dato = anmodninger_obj.get_dato()
        anmodning.tid = anmodninger_obj.get_tid()
        return anmodning