#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from GUI.LoginWindow import *

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *

from .ProprietorWindow import Design_ProprietorWindow
from Controllers import ProprietorControl

class ProprietorWindow(Design_ProprietorWindow):
    def __init__(self,ID, parent=None,):
        print(5)
        super().__init__(parent)
        self.__ID = ID
        print(6)
        self.__control = ProprietorControl(ID)

        self.electricCharge.setText(self.__control.receivable_electric())
        self.guaranteeCharge.setText(self.__control.receivable_guarantee())
        self.propertyFeeCharge.setText(self.__control.receivable_propertyfee())
        self.waterCharge.setText(self.__control.receivable_water())

        self.electricReceivable.setText(self.__control.receipt_electric())
        self.waterReceivable.setText(self.__control.receipt_water())
        self.propertyFeeReceivable.setText(self.__control.receipt_propertyfee())
        self.guaranteeReceivable.setText(self.__control.receipt_guarantee())

