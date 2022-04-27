from Ansat import Ansat
class Underviser(Ansat):
    def __init__(self, navn, fakultet, kurser, id):
        self.navn = navn
        self.kurser = kurser
        self.fakultet = fakultet
        self.id = id