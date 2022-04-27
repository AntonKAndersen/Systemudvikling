class Skema:
    def __init__(self, id: int, underviser: str, kursus: str, lokale: str, dato: str, tid: str):
        self.id = id
        self.underviser = underviser
        self.kursus = kursus
        self.lokale = lokale
        self.dato = dato
        self.tid = tid

    def get_id(self): return self.id
    def get_underviser(self): return self.underviser
    def get_kursus(self): return self.kursus
    def get_lokale(self): return self.lokale
    def get_dato(self): return self.dato
    def get_tid(self): return self.tid

    def __str__(self):
        return f"{self.id}, {self.underviser}, {self.kursus}, {self.lokale}, {self.dato}, {self.tid}"
