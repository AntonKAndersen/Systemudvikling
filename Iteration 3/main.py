from Model.Anmodninger import Anmodninger
from Model.Skema import Skema
from Model.ClassMethods import ClassMethods
from Controller.Database import Database
from PyQt6 import QtWidgets
from Controller.UnderviserGUI import UnderviserGUI
from Controller.SekretarGUI import SekretarGUI
import sys

def main():
    # Indlæser data fra database ind i en liste vha. klassen Anmodninger og metoden add_anmodning fra ClassMethods
    db = Database()
    req = db.showAnmodninger()
    for i in req:
        anmodning = Anmodninger(i[0], i[1], i[2], i[3], i[4])
        ClassMethods.add_anmodning(anmodning)

    bookinger = db.showSkema()
    for i in bookinger:
        skema = Skema(i[0], i[1], i[2], i[3], i[4], i[5])
        ClassMethods.add_skema(skema)

    app = QtWidgets.QApplication(sys.argv)
    Underviser_window = UnderviserGUI()
    Sekretar_window = SekretarGUI()
    app.exec()

if __name__ == '__main__':
    main()