# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Admin\Desktop\Programação\VS Code\4. Python\QTprojetos\Duas telas\tela4.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(354, 327)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.novonome = QtWidgets.QLineEdit(self.centralwidget)
        self.novonome.setGeometry(QtCore.QRect(80, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.novonome.setFont(font)
        self.novonome.setStyleSheet("color: rgb(81, 81, 81);")
        self.novonome.setText("")
        self.novonome.setObjectName("novonome")
        self.novovalorreal = QtWidgets.QLineEdit(self.centralwidget)
        self.novovalorreal.setGeometry(QtCore.QRect(80, 180, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.novovalorreal.setFont(font)
        self.novovalorreal.setStyleSheet("color: rgb(81, 81, 81);")
        self.novovalorreal.setObjectName("novovalorreal")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(120, 120, 120);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 240, 91, 31))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Admin\\Desktop\\Programação\\VS Code\\4. Python\\QTprojetos\\Duas telas\\Imagens/Editar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(17, 17))
        self.pushButton.setObjectName("pushButton")
        self.datadia = QtWidgets.QLineEdit(self.centralwidget)
        self.datadia.setGeometry(QtCore.QRect(80, 110, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.datadia.setFont(font)
        self.datadia.setStyleSheet("color: rgb(81, 81, 81);")
        self.datadia.setText("")
        self.datadia.setObjectName("datadia")
        self.datames = QtWidgets.QLineEdit(self.centralwidget)
        self.datames.setGeometry(QtCore.QRect(140, 110, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.datames.setFont(font)
        self.datames.setStyleSheet("color: rgb(81, 81, 81);")
        self.datames.setObjectName("datames")
        self.dataano = QtWidgets.QLineEdit(self.centralwidget)
        self.dataano.setGeometry(QtCore.QRect(200, 110, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dataano.setFont(font)
        self.dataano.setStyleSheet("color: rgb(81, 81, 81);")
        self.dataano.setObjectName("dataano")
        self.novovalorcentavo = QtWidgets.QLineEdit(self.centralwidget)
        self.novovalorcentavo.setGeometry(QtCore.QRect(200, 180, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.novovalorcentavo.setFont(font)
        self.novovalorcentavo.setStyleSheet("color: rgb(81, 81, 81);\n"
"color: rgb(81, 81, 81);")
        self.novovalorcentavo.setObjectName("novovalorcentavo")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 90, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(120, 120, 120);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 160, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(120, 120, 120);")
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 354, 21))
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
        self.label.setText(_translate("MainWindow", "*confirme o nome"))
        self.pushButton.setText(_translate("MainWindow", " Concluir"))
        self.label_4.setText(_translate("MainWindow", "*nova data"))
        self.label_5.setText(_translate("MainWindow", "*novo débito"))