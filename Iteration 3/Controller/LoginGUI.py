from Controller.UnderviserGUI import UnderviserGUI
from Controller.SekretarGUI import SekretarGUI
from Model.ClassMethods import ClassMethods
from PyQt6 import QtWidgets, uic


class LoginGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginGUI, self).__init__()
        uic.loadUi('View/Loginside.ui', self)
        self.show()
        self.loginButton.clicked.connect(self.login)

    def login(self):
        brugernavn = self.lineEdit_brugernavn.text()
        adgangskode = self.lineEdit_adgangskode.text()
        print(brugernavn)
        print(adgangskode)

        for b in ClassMethods.get_bruger():
            if b.get_brugernavn() == brugernavn and b.get_adgangskode() == adgangskode:
                print('ok')
                if b.get_brugertype() == 'Underviser':
                    ClassMethods.add_login(brugernavn)
                    self.u = UnderviserGUI()
                    self.u.show()
                elif b.get_brugertype() == 'Admin':
                    self.s = SekretarGUI()
                    self.s.show()






