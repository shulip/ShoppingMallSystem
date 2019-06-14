#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from GUI.LoginWindow import *

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *

from .CEOWindow import Design_CEOWindow

class CEOWindow(Design_CEOWindow):
    def __init__(self,ID, parent=None):
        super().__init__(parent)