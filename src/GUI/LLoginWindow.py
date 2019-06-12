#!/usr/bin/env python 
# -*- coding:utf-8 -*-


from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *

from GUI.LoginWindow import Design_LoginWindow
from Controllers import Login
import sys

class LoginWindow(Design_LoginWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.LOGIN = Login()
        self.logIn.clicked.connect(self.log_in)

    def log_in(self):
        self.LOGIN.run(self.ID.text(),self.Key.text(),self.jobPosition.currentText())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = LoginWindow()

    MainWindow.show()
    MainWindow.move(int((QApplication.desktop().width() - MainWindow.width()) / 2),
                        int((QApplication.desktop().height() - MainWindow.height()) / 2 - 50))
    sys.exit(app.exec_())