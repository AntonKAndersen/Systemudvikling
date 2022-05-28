from Model.ClassMethods import ClassMethods # importerer class methods
from Model.Anmodninger import Anmodninger # importerer anmodninger
from Model.Skema import Skema
from Model.Bruger import Bruger

def test_add_anmodning(): # tager anmodninger og tester den, sletter self
    anmodning = Anmodninger("10","Bo","Kursus1","100522","10:15") # laver et objekt der er en anmodning
    print(len(ClassMethods.list_anmodninger)) # printer længden af listen af anmodninger
    assert len(ClassMethods.list_anmodninger) == 0 # tester at den er 0
    ClassMethods.add_anmodning(anmodning) # tilføjer en anmodning
    print(len(ClassMethods.list_anmodninger)) # printer længden af list anmodninger
    assert len(ClassMethods.list_anmodninger)==1 # det man forventer, forventer at længden er 1

def test_get_anmodninger(): # tager funktionen der get en anmodninger
    ClassMethods.get_anmodninger() # bruger metoden
    assert len(ClassMethods.list_anmodninger)==1 # ser at listen med anmodninger er 1

def test_add_skema():
    skema = Skema(1, "Bo", "Kursus1", "B2", "100522", "10:15")
    assert len(ClassMethods.list_skema)==0
    ClassMethods.add_skema(skema)
    assert len(ClassMethods.list_skema)==1

def test_get_skema():
    ClassMethods.get_skema()  # bruger metoden
    assert len(ClassMethods.list_skema) == 1  # ser at listen med skema er 1

def test_add_bruger():
    bruger = Bruger(3,"Bo", "Abc123", "Studerende")
    assert len(ClassMethods.list_bruger)==0
    ClassMethods.add_bruger(bruger)
    assert len(ClassMethods.list_bruger)==1

def test_get_bruger():
    ClassMethods.get_bruger()  # bruger metoden
    assert len(ClassMethods.list_bruger) == 1  # ser at listen med bruger er 1

"""def test_add_login():
    assert len(ClassMethods.list_login)==0
    ClassMethods.add_login()
    assert len(ClassMethods.list_login)==1
#def test_get_login(self):
    #assert False """
