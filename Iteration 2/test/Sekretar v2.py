# Form implementation generated from reading ui file 'C:\Users\anton\Documents\GitHub\Systemudvikling\GUI - XML\Sekretar v2.ui'
#
# Created by: PyQt6 View code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1045, 595)
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.kalenderSekretar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.kalenderSekretar.setGeometry(QtCore.QRect(0, 60, 541, 281))
        self.kalenderSekretar.setObjectName("kalenderSekretar")
        self.datovalg_2 = QtWidgets.QLabel(self.centralwidget)
        self.datovalg_2.setGeometry(QtCore.QRect(30, 0, 701, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.datovalg_2.setFont(font)
        self.datovalg_2.setObjectName("datovalg_2")
        self.lokaleDropdown = QtWidgets.QComboBox(self.centralwidget)
        self.lokaleDropdown.setGeometry(QtCore.QRect(570, 370, 451, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lokaleDropdown.setFont(font)
        self.lokaleDropdown.setAutoFillBackground(False)
        self.lokaleDropdown.setStyleSheet("")
        self.lokaleDropdown.setCurrentText("")
        self.lokaleDropdown.setObjectName("lokaleDropdown")
        self.lokaleDropdown.addItem("")
        self.lokaleDropdown.addItem("")
        self.lokaleDropdown.addItem("")
        self.lokaleDropdown.addItem("")
        self.lokaleDropdown.addItem("")
        self.tidstart = QtWidgets.QTimeEdit(self.centralwidget)
        self.tidstart.setGeometry(QtCore.QRect(570, 400, 451, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tidstart.setFont(font)
        self.tidstart.setObjectName("tidstart")
        self.bookLokale = QtWidgets.QPushButton(self.centralwidget)
        self.bookLokale.setGeometry(QtCore.QRect(570, 490, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.bookLokale.setFont(font)
        self.bookLokale.setMouseTracking(True)
        self.bookLokale.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(250, 250, 250);\n"
"}")
        self.bookLokale.setObjectName("bookLokale")
        self.kursusDropdown = QtWidgets.QComboBox(self.centralwidget)
        self.kursusDropdown.setGeometry(QtCore.QRect(570, 460, 451, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.kursusDropdown.setFont(font)
        self.kursusDropdown.setAutoFillBackground(False)
        self.kursusDropdown.setStyleSheet("")
        self.kursusDropdown.setCurrentText("")
        self.kursusDropdown.setObjectName("kursusDropdown")
        self.kursusDropdown.addItem("")
        self.kursusDropdown.addItem("")
        self.kursusDropdown.addItem("")
        self.kursusDropdown.addItem("")
        self.kursusDropdown.addItem("")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(30, 360, 511, 191))
        self.splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter.setObjectName("splitter")
        self.datoValgS = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.datoValgS.setFont(font)
        self.datoValgS.setObjectName("datoValgS")
        self.datoIndholdS = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.datoIndholdS.setFont(font)
        self.datoIndholdS.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.datoIndholdS.setWordWrap(True)
        self.datoIndholdS.setObjectName("datoIndholdS")
        self.listRequest = QtWidgets.QListWidget(self.centralwidget)
        self.listRequest.setGeometry(QtCore.QRect(570, 101, 451, 201))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listRequest.setFont(font)
        self.listRequest.setObjectName("listRequest")
        item = QtWidgets.QListWidgetItem()
        self.listRequest.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listRequest.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listRequest.addItem(item)
        self.datoValgS_2 = QtWidgets.QLabel(self.centralwidget)
        self.datoValgS_2.setGeometry(QtCore.QRect(570, 44, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.datoValgS_2.setFont(font)
        self.datoValgS_2.setObjectName("datoValgS_2")
        self.godkendBooking = QtWidgets.QPushButton(self.centralwidget)
        self.godkendBooking.setGeometry(QtCore.QRect(810, 310, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.godkendBooking.setFont(font)
        self.godkendBooking.setMouseTracking(True)
        self.godkendBooking.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(250, 250, 250);\n"
"}")
        self.godkendBooking.setObjectName("godkendBooking")
        self.afvisBooking = QtWidgets.QPushButton(self.centralwidget)
        self.afvisBooking.setGeometry(QtCore.QRect(570, 310, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.afvisBooking.setFont(font)
        self.afvisBooking.setMouseTracking(True)
        self.afvisBooking.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(250, 250, 250);\n"
"}")
        self.afvisBooking.setObjectName("afvisBooking")
        self.tidslut = QtWidgets.QTimeEdit(self.centralwidget)
        self.tidslut.setGeometry(QtCore.QRect(570, 430, 451, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tidslut.setFont(font)
        self.tidslut.setObjectName("tidslut")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1045, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.datovalg_2.setText(_translate("MainWindow", "Login for administration"))
        self.lokaleDropdown.setPlaceholderText(_translate("MainWindow", "V??lg lokale"))
        self.lokaleDropdown.setItemText(0, _translate("MainWindow", "Und.lokale - A102, HC??"))
        self.lokaleDropdown.setItemText(1, _translate("MainWindow", "Und.lokale - A105, HC??"))
        self.lokaleDropdown.setItemText(2, _translate("MainWindow", "Aud. - Lille UP1, DIKU"))
        self.lokaleDropdown.setItemText(3, _translate("MainWindow", "Aud. - Niels K. Jerne, Panum"))
        self.lokaleDropdown.setItemText(4, _translate("MainWindow", "Und.lokale - 13.1.83, Panum"))
        self.tidstart.setSpecialValueText(_translate("MainWindow", "V??lg start tidspunkt"))
        self.bookLokale.setText(_translate("MainWindow", "Book"))
        self.kursusDropdown.setPlaceholderText(_translate("MainWindow", "V??lg kursus"))
        self.kursusDropdown.setItemText(0, _translate("MainWindow", "Systemudvikling - Theo exercise"))
        self.kursusDropdown.setItemText(1, _translate("MainWindow", "Systemudvikling - Lecture"))
        self.kursusDropdown.setItemText(2, _translate("MainWindow", "Sygedomsl??re - Forel??sning"))
        self.kursusDropdown.setItemText(3, _translate("MainWindow", "Sygedomsl??re - SAU"))
        self.kursusDropdown.setItemText(4, _translate("MainWindow", "Sygedomsl??re - Caf??"))
        self.datoValgS.setText(_translate("MainWindow", "{lokale}: Planlagte bookinger d. 21. marts 2022"))
        self.datoIndholdS.setText(_translate("MainWindow", "<html><head/><body><p>09 - 12: Systemudvikling - Theo exercise - Und.lokale - A105, HC??</p><p>15 - 17: Systemudvikling - Lecture - Und.lokale - A105, HC??</p></body></html>"))
        __sortingEnabled = self.listRequest.isSortingEnabled()
        self.listRequest.setSortingEnabled(False)
        item = self.listRequest.item(0)
        item.setText(_translate("MainWindow", "09 - 12: Systemudvikling - Theo exercise - Und.lokale - A105, HC??"))
        item = self.listRequest.item(1)
        item.setText(_translate("MainWindow", "15 - 17: Systemudvikling - Lecture - Aud. - Lille UP1, DIKU"))
        item = self.listRequest.item(2)
        item.setText(_translate("MainWindow", "09 - 12: Sygdomsl??re - Forel??sning - Niels K. Jerne, Panum"))
        self.listRequest.setSortingEnabled(__sortingEnabled)
        self.datoValgS_2.setText(_translate("MainWindow", "Liste over foresp??rgsler fra undervisere"))
        self.godkendBooking.setText(_translate("MainWindow", "Godkend"))
        self.afvisBooking.setText(_translate("MainWindow", "Afvis"))
        self.tidslut.setSpecialValueText(_translate("MainWindow", "V??lg slut tidspunkt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
