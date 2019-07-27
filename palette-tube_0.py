# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'palette-tube-gui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 440, 341, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(self.lancer_dl)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 571))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("palette_tube.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(540, 130, 231, 101))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 440, 151, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.lancer_dl)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(696, 540, 81, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 520, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label.raise_()
        self.lineEdit.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Palettetube, l'outil de téléchargement de playlist youtubes, made in palette !"))
        self.lineEdit.setText(_translate("MainWindow", "URL de la playlist"))
        self.label_2.setText(_translate("MainWindow", "Pas du tout plein de virus ! "))
        self.pushButton.setText(_translate("MainWindow", "Télécharges-moi ça !"))
        self.label_3.setText(_translate("MainWindow", "made in palette"))
        self.label_4.setText(_translate("MainWindow", "Dakar RpZ"))
        print('La Palette est fiere de vous presenter son script tout naze de telechargement de playlist youtube ! ')
        print('Toute plainte est a deposer aupres de Aziz')

    def lancer_dl(self):
        #!/usr/bin/env python
        import os, sys, time
        import argparse
        import json

        import pytube  # pip install pytube
        url = self.lineEdit.text()

        # cmd = "youtube-dl -o \"%(title)s-%(id)s.%(ext)s\" --audio-format mp3 --audio-quality 0 --yes-playlist {}".format(args.playlisturl)
        cmd = "youtube-dl -o \"%(title)s.%(ext)s\" --audio-format mp3 --audio-quality 0 --yes-playlist {}".format(url)
        os.system(cmd)
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("MainWindow", "fini !"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
