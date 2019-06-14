#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QDesktopWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.Qt import QButtonGroup
from PyQt5.Qt import QListView
from PyQt5.Qt import QSplashScreen, QDateTime

from GUI.ProprietorWindow.UI.Ui_ProprietorWindow import Ui_ProprietorWindow

class Design_ProprietorWindow(QWidget,Ui_ProprietorWindow):
    def __init__(self, parent=None):
        super(Design_ProprietorWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = Design_ProprietorWindow()

    MainWindow.show()
    MainWindow.move(int((QApplication.desktop().width() - MainWindow.width()) / 2),
                        int((QApplication.desktop().height() - MainWindow.height()) / 2 - 50))
    sys.exit(app.exec_())