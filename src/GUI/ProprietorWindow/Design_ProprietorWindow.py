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

from GUI.UserWindow.Design_UserWindow import Design_UserWindow

class Design_ProprietorWindow(Design_UserWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # 添加启动面
    start = QPixmap("start.png")
    splash = QtWidgets.QSplashScreen(start)
    splash.show()   #

    MainWindow = Design_ProprietorWindow()

    # 关闭启动面
    splash.finish(MainWindow)

    MainWindow.show()
    MainWindow.move(int((QApplication.desktop().width() - MainWindow.width()) / 2),
                        int((QApplication.desktop().height() - MainWindow.height()) / 2 - 50))
    sys.exit(app.exec_())