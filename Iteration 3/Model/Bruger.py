class Bruger:
    def __init__(self, id: int, brugernavn: str, adgangskode: str, brugertype: str):
        self.id = id
        self.brugernavn = brugernavn
        self.adgangskode = adgangskode
        self.brugertype = brugertype

    def get_id(self): return self.id
    def get_brugernavn(self): return self.brugernavn
    def get_adgangskode(self): return self.adgangskode
    def get_brugertype(self): return self.brugertype

    def __str__(self):
        return f"{self.id}, {self.brugernavn}, {self.adgangskode}, {self.brugertype}"