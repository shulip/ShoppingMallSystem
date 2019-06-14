#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QDesktopWidget,QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.Qt import QButtonGroup
from PyQt5.Qt import QListView
from PyQt5.Qt import QSplashScreen, QDateTime
from GUI.LoginWindow.Ui import *
from GUI.image.image import *


class Design_LoginWindow(QWidget, Ui_LoginInterface):
    def __init__(self, parent=None):
        super(Design_LoginWindow, self).__init__(parent)
        self.setupUi(self)
        infomation = ["业主", "ceo", "cfo",'管理员']
        #self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.jobPosition.addItems(infomation)
        self.logIn.clicked.connect(self.close)
        self.closeLogInWindow.clicked.connect(self.close)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = Design_LoginWindow()

    MainWindow.show()
    MainWindow.move(int((QApplication.desktop().width() - MainWindow.width()) / 2),
                        int((QApplication.desktop().height() - MainWindow.height()) / 2 - 50))
    sys.exit(app.exec_())