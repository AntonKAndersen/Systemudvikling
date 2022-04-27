from Controller.Database import Database
from PyQt6 import QtWidgets, uic

class UnderviserGUI(QtWidgets.QWidget):
    def __init__(self):
        super(UnderviserGUI, self).__init__()
        uic.loadUi('View/UnderviserV2.ui', self)
        self.lavForsporgselButton.clicked.connect(self.forsporgsel_pressed)
        self.show()

    def forsporgsel_pressed(self):
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
        db.addAnmodninger('Jakob Andersen', kursus, dato, f'{start_tid}-{slut_tid}')

