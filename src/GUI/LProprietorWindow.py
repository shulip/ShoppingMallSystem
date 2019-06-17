#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from GUI.LoginWindow import *

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
import random


from GUI.ProprietorWindow import Design_ProprietorWindow
from Controllers import ProprietorControl

class ProprietorWindow(Design_ProprietorWindow):
    def __init__(self,ID, parent=None,):
        print(5)
        super().__init__(parent)
        self.__ID = ID
        print(6)
        self.__control = ProprietorControl(ID)



        self.electricCharge.setText(str(self.__control.receivable_electric()))
        self.guaranteeCharge.setText(str(self.__control.receivable_guarantee()))
        self.propertyFeeCharge.setText(str(self.__control.receivable_propertyfee()))
        self.waterCharge.setText(str(self.__control.receivable_water()))

        self.electricReceivable.setText(str(self.__control.receipt_electric()))
        self.waterReceivable.setText(str(self.__control.receipt_water()))
        self.propertyFeeReceivable.setText(str(self.__control.receipt_propertyfee()))
        self.guaranteeReceivable.setText(str(self.__control.receipt_guarantee()))

        self.pushButtonShop_01.clicked.connect(self.set_information)
        self.pushButtonShop_02.clicked.connect(self.set_information)
        self.pushButtonShop_03.clicked.connect(self.set_information)
        self.pushButtonShop_04.clicked.connect(self.set_information)
        self.pushButtonShop_05.clicked.connect(self.set_information)
        self.pushButtonShop_06.clicked.connect(self.set_information)
        self.pushButtonShop_07.clicked.connect(self.set_information)
        self.pushButtonShop_08.clicked.connect(self.set_information)
        self.pushButtonShop_09.clicked.connect(self.set_information)
        self.pushButtonShop_10.clicked.connect(self.set_information)
        self.pushButtonShop_11.clicked.connect(self.set_information)
        self.pushButtonShop_12.clicked.connect(self.set_information)
        # self.immediateApplication.clicked.connect(self.apply_info)


    def set_information(self):
        self.areaCovered.setText(str(random.randint(50,100)))
        self.annualRent.setText(str(random.randint(20000,30000)))
        self.propertyFee.setText(str(12))
        self.deposit.setText(str(random.randint(10000,20000)))

    def apply_info(self):
        """
        提交申请
        :return:None
        """
        #TODO:提交到数据库
        self.shopName.setText("")
        self.userTel.setText("")
        self.shopRentTime.setText("")
        self.shopReason.setText("")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = ProprietorWindow(1)

    MainWindow.show()

    sys.exit(app.exec_())
