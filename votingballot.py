# Form implementation generated from reading ui file 'votingballot.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(375, 450)
        MainWindow.setMinimumSize(QtCore.QSize(375, 450))
        MainWindow.setMaximumSize(QtCore.QSize(375, 450))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.idInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.idInput.setGeometry(QtCore.QRect(100, 40, 210, 50))
        self.idInput.setObjectName("idInput")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.janeButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.janeButton.setGeometry(QtCore.QRect(160, 170, 70, 40))
        self.janeButton.setMinimumSize(QtCore.QSize(70, 40))
        self.janeButton.setMaximumSize(QtCore.QSize(70, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.janeButton.setFont(font)
        self.janeButton.setObjectName("janeButton")
        self.johnButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.johnButton.setGeometry(QtCore.QRect(160, 230, 70, 40))
        self.johnButton.setMinimumSize(QtCore.QSize(70, 40))
        self.johnButton.setMaximumSize(QtCore.QSize(70, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.johnButton.setFont(font)
        self.johnButton.setObjectName("johnButton")
        self.candidate = QtWidgets.QLabel(parent=self.centralwidget)
        self.candidate.setGeometry(QtCore.QRect(130, 110, 150, 50))
        self.candidate.setMinimumSize(QtCore.QSize(150, 50))
        self.candidate.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.candidate.setFont(font)
        self.candidate.setObjectName("candidate")
        self.submitButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(110, 280, 170, 50))
        self.submitButton.setMinimumSize(QtCore.QSize(170, 50))
        self.submitButton.setMaximumSize(QtCore.QSize(170, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName("submitButton")
        self.message = QtWidgets.QLabel(parent=self.centralwidget)
        self.message.setGeometry(QtCore.QRect(60, 330, 271, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.message.setFont(font)
        self.message.setObjectName("message")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 375, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ID"))
        self.janeButton.setText(_translate("MainWindow", "Jane"))
        self.johnButton.setText(_translate("MainWindow", "John"))
        self.candidate.setText(_translate("MainWindow", "CANDIDATES"))
        self.submitButton.setText(_translate("MainWindow", "SUBMIT ID"))
        self.message.setText(_translate("MainWindow", "Please enter a 5 digit unique ID."))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
