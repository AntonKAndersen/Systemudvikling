from Anmodninger import Anmodninger


class anmodningerList:
    """
    Klassen bruges til at holde anmodninger i en liste
    """

    def __init__(self):
        self.anmodningerList = []

    def append_anmodning(self, anmodning: Anmodninger):
        self.anmodningerList.append(anmodning)

    def get_anmodningerList(self):
        return self.anmodningerList