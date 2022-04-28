from Model.Anmodninger import Anmodninger
from Model.Skema import Skema
from Model.Bruger import Bruger
from Model.ClassMethods import ClassMethods
from Controller.Database import Database
from PyQt6 import QtWidgets
from Controller.UnderviserGUI import UnderviserGUI
from Controller.SekretarGUI import SekretarGUI
from Controller.LoginGUI import LoginGUI
import sys

def main():
    # Indlæser data fra database ind i en liste vha. klassen Anmodninger og metoden add_anmodning fra ClassMethods
    db = Database()

    bookinger = db.showSkema()
    for i in bookinger:
        skema = Skema(i[0], i[1], i[2], i[3], i[4], i[5])
        ClassMethods.add_skema(skema)

    bruger = db.showBruger()
    for i in bruger:
        bruger = Bruger(i[0], i[1], i[2], i[3])
        ClassMethods.add_bruger(bruger)

    app = QtWidgets.QApplication(sys.argv)
    Login_window = LoginGUI()
    app.exec()

if __name__ == '__main__':
    main()