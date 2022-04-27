class Anmodninger:
    '''
    Klassen indeholder atributter og metoder for anmodninger, så underviserens anmodninger kan håndteres af systemet.
    '''
    def __init__(self, id: int, underviser: str, kursus: str, dato: str, tid: str):
        self.id = id
        self.underviser = underviser
        self.kursus = kursus
        self.dato = dato
        self.tid = tid

    def get_id(self): return self.id
    def get_underviser(self): return self.underviser
    def get_kursus(self): return self.kursus
    def get_dato(self): return self.dato
    def get_tid(self): return self.tid

    def __str__(self):
        return f"{self.id}, {self.underviser}, {self.kursus}, {self.dato}, {self.tid}"


