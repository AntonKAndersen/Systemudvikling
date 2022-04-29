from Model.ClassMethods import ClassMethods
from Controller.Database import Database
from PyQt6 import QtWidgets, uic

class UnderviserGUI(QtWidgets.QWidget):
    def __init__(self):
        super(UnderviserGUI, self).__init__()
        uic.loadUi('View/UnderviserV2.ui', self)

        #Når der trykkes Lav forespørgsel, så køres funktionen forsporgsel_pressed
        self.lavForsporgselButton.clicked.connect(self.forsporgsel_pressed)
        self.show()

        #Tilføjer overskrift til skema med dato
        dato = self.kalenderUnderviser.selectedDate().toString("dd-MM-yyyy")
        self.datoValg.setText(f'Planlagte bookinger d. {dato}')

        #Når en ny dato vælges køres funktionen vis_skema
        self.kalenderUnderviser.selectionChanged.connect(lambda: self.vis_skema())

    def vis_skema(self):
        '''
        Funktionen vis_skema bruges til når der vælges en ny dato i kalenderen - skemaet opdateres så det passer til den valgte dato.
        '''
        self.listSkema.clear() #Starter med at rydde skema
        #Indlæser dato fra kalenderen i variablen dato
        dato = self.kalenderUnderviser.selectedDate().toString("dd-MM-yyyy")
        #Tilføjer overskrift til skema med dato
        self.datoValg.setText(f'Planlagte bookinger d. {dato}')
        #For hvert element i list_skema fra ClassMethods som har samme dato som den valgte
        for a in ClassMethods.get_skema():
            if a.get_dato() == dato:
                #Tilføjes der et item(lektion/booking) til QListWidget(skemaet)
                self.listSkema.addItem(f"{a.get_tid()}:  {a.get_kursus()}, {a.get_lokale()}")

    def forsporgsel_pressed(self):
        '''Funktionen indhenter de indsatte oplysninger, dato, tid, kursus og tilføjer det til tabellen Anmodninger i databasen'''
        print('OK')
        dato = self.kalenderUnderviser.selectedDate().toString("dd-MM-yyyy")
        print(dato)
        start_tid = self.forsporgselStartTid.text()
        print(start_tid)
        slut_tid = self.forsporgselSlutTid.text()
        print(slut_tid)
        kursus = self.kursusDropdownForporgsel.currentText()
        print(kursus)

        db = Database()
        #get_login indsæter brugernavnet på den bruger som er logget in
        db.addAnmodninger(ClassMethods.get_login()[-1], kursus, dato, f'{start_tid}-{slut_tid}')

        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Forespørgsel")
        msg.setText("Din forespørgsel er nu afsendt!")
        msg.exec()

