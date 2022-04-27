from Model.Skema import Skema
from Model.ClassMethods import ClassMethods
from Controller.Database import Database
from PyQt6 import QtWidgets, uic
db = Database()

for a in ClassMethods.get_anmodninger():
    print(a.get_underviser())

class SekretarGUI(QtWidgets.QWidget):
    def __init__(self):
        super(SekretarGUI, self).__init__()
        #Loader GUI
        uic.loadUi('View/Sekretar.ui', self)
        self.show()

        #Viser anmodninger
        for a in ClassMethods.get_anmodninger():
            self.listRequest.addItem(f"{a.get_id()}, {a.get_underviser()}, {a.get_kursus()}, {a.get_dato()}, {a.get_tid()}")


        #Når der er valgt en anmodning fra listen køres funktionen valgt_foresporgsel
        self.listRequest.itemSelectionChanged.connect(self.valgt_foresporgsel)

        #Tilføjer overskrift til skema med dato
        dato = self.kalenderSekretar.selectedDate().toString("dd-MM-yyyy")
        self.datoValg.setText(f'Planlagte bookinger d. {dato}')

        #Når en ny dato vælges køres funktionen vis_skema
        self.kalenderSekretar.selectionChanged.connect(lambda: self.vis_skema())

        #Når der knappen Afvis trykkes køres funktionen afvis
        self.afvisBooking.clicked.connect(self.afvis)

        #Når der knappen Godkend trykkes køres funktionen godkend
        self.godkendBooking.clicked.connect(self.godkend)

    def vis_skema(self):
        self.listSkema.clear()
        dato = self.kalenderSekretar.selectedDate().toString("dd-MM-yyyy")
        self.datoValg.setText(f'Planlagte bookinger d. {dato}')
        for a in ClassMethods.get_skema():
            if a.get_dato() == dato:
                self.listSkema.addItem(f"{a.get_tid()}:  {a.get_kursus()}, {a.get_lokale()}")

        '''
        for a in ClassMethods.get_skema():
            if a.get_dato == dato:
                self.listSkema.addItem(f"{a.get_dato}, {a.get_tid()}: {a.get_lokale()}, {a.get_kursus()}, {a.get_underviser()}")
            else:
                
        '''




    def valgt_foresporgsel(self):
        valg = [item.text() for item in self.listRequest.selectedItems()]
        primarykey_anmodninger = valg[0][:2]
        return primarykey_anmodninger.strip(',')

    def afvis(self):
        db.delAnmodning(self.valgt_foresporgsel())  # Sletter anmodning i database
        listItems = self.listRequest.selectedItems()
        if not listItems: return
        for item in listItems:
            self.listRequest.takeItem(self.listRequest.row(item))

    def godkend(self):
        #Indhendter variable til databasen
        underviser = ''.join(db.getUnderviser(self.valgt_foresporgsel()))
        kursus = ''.join(db.getKursus(self.valgt_foresporgsel()))
        dato = ''.join(db.getDato(self.valgt_foresporgsel()))
        tid = ''.join(db.getTid(self.valgt_foresporgsel()))
        lokale = self.lokaleDropdown.currentText()

        #Tilføjer booking til Skema tabellen i databasen
        db.addSkema(underviser, kursus, lokale, dato, tid)
        db.delAnmodning(self.valgt_foresporgsel())

        #Tilføjer til skemlisten i ClassMethods, så ændringen kan ses i skema med det samme
        skema = Skema(1, underviser, kursus, lokale, dato, tid)
        ClassMethods.add_skema(skema)

        #Fjerner det godkendte item
        listItems = self.listRequest.selectedItems()
        if not listItems: return
        for item in listItems:
            self.listRequest.takeItem(self.listRequest.row(item))













