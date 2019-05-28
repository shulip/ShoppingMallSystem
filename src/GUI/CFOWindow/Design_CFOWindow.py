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

class Design_CFOWindow(Design_UserWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

