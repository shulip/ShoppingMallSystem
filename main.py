#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from GUI import LoginWindow
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QDesktopWidget


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = LoginWindow()

    MainWindow.show()
    MainWindow.move(int((QApplication.desktop().width() - MainWindow.width()) / 2),
                    int((QApplication.desktop().height() - MainWindow.height()) / 2 - 50))
    sys.exit(app.exec_())