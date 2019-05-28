#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from GUI.LoginWindow import *

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *

from .LoginWindow import Design_LoginWindow

class LoginWindow(Design_LoginWindow):
    def __init__(self, parent=None):
        super().__init__(parent)