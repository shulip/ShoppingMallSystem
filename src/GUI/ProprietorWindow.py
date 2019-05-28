#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from GUI.LoginWindow import *

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *

from .ProprietorWindow import Design_ProprietorWindow

class ProprietorWindow(Design_ProprietorWindow):
    def __init__(self, parent=None):
        super().__init__(parent)