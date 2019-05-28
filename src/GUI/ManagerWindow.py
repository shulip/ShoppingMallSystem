#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from GUI.LoginWindow import *

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *

from .ManagerWindow import Design_ManagerWindow

class ManagerWindow(Design_ManagerWindow):
    def __init__(self, parent=None):
        super().__init__(parent)