#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *

from GUI.CEOWindow import Design_CEOWindow
import sys
from Controllers import CEOControl


class CEOWindow(Design_CEOWindow):
    def __init__(self,ID, parent=None):
        super().__init__(parent)
        self.__ID = ID
        self.__control = CEOControl(ID)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = CEOWindow("sa")

    MainWindow.show()

    sys.exit(app.exec_())

