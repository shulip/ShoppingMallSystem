#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from GUI.LoginWindow import *

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
import random
import win32com.client
import threading
from GUI.ProprietorWindow import Design_ProprietorWindow
from Controllers import ProprietorControl

class ProprietorWindow(Design_ProprietorWindow):
    def __init__(self,ID, parent=None,):
        print(5)
        super().__init__(parent)
        self.__ID = ID
        print(6)
        self.__control = ProprietorControl(ID)
        self.speaker = win32com.client.Dispatch("SAPI.SpVoice")

        self.set_up_parameters()

        self.btnAllShop.clicked.connect(lambda :threading.Thread(target=lambda :self.speaker.Speak("申请进场")).start())
        self.btnMyShop.clicked.connect(lambda :threading.Thread(target=lambda :self.speaker.Speak("我的店铺")).start())
        self.btnInf.clicked.connect(lambda :threading.Thread(target=lambda :self.speaker.Speak("我的信息·")).start())
        self.btnContract.clicked.connect(lambda :threading.Thread(target=lambda :self.speaker.Speak("我的合同")).start())
        self.btnSublease.clicked.connect(lambda :threading.Thread(target=lambda :self.speaker.Speak("申请转租")).start())

        self.pushButtonShop_01.clicked.connect(self.set_information)
        self.pushButtonShop_01.clicked.connect(lambda : self.shopNum.setText(str(1)))

        self.pushButtonShop_02.clicked.connect(self.set_information)
        self.pushButtonShop_02.clicked.connect(lambda : self.shopNum.setText(str(2)))

        self.pushButtonShop_03.clicked.connect(self.set_information)
        self.pushButtonShop_03.clicked.connect(lambda : self.shopNum.setText(str(3)))

        self.pushButtonShop_04.clicked.connect(self.set_information)
        self.pushButtonShop_04.clicked.connect(lambda : self.shopNum.setText(str(4)))

        self.pushButtonShop_05.clicked.connect(self.set_information)
        self.pushButtonShop_05.clicked.connect(lambda : self.shopNum.setText(str(5)))

        self.pushButtonShop_06.clicked.connect(self.set_information)
        self.pushButtonShop_06.clicked.connect(lambda : self.shopNum.setText(str(6)))

        self.pushButtonShop_07.clicked.connect(self.set_information)
        self.pushButtonShop_07.clicked.connect(lambda : self.shopNum.setText(str(7)))

        self.pushButtonShop_08.clicked.connect(self.set_information)
        self.pushButtonShop_08.clicked.connect(lambda : self.shopNum.setText(str(8)))

        self.pushButtonShop_09.clicked.connect(self.set_information)
        self.pushButtonShop_09.clicked.connect(lambda : self.shopNum.setText(str(9)))

        self.pushButtonShop_10.clicked.connect(self.set_information)
        self.pushButtonShop_10.clicked.connect(lambda : self.shopNum.setText(str(10)))

        self.pushButtonShop_11.clicked.connect(self.set_information)
        self.pushButtonShop_11.clicked.connect(lambda : self.shopNum.setText(str(11)))

        self.pushButtonShop_12.clicked.connect(self.set_information)
        self.pushButtonShop_12.clicked.connect(lambda : self.shopNum.setText(str(12)))

        self.immediateApplication.clicked.connect(self.apply_info)


    def set_up_parameters(self):
        """
        设置参数
        :return: None
        """

        self.electricCharge.setText(str(self.__control.receivable_electric()))
        self.guaranteeCharge.setText(str(self.__control.receivable_guarantee()))
        self.propertyFeeCharge.setText(str(self.__control.receivable_propertyfee()))
        self.waterCharge.setText(str(self.__control.receivable_water()))

        self.electricReceivable.setText(str(self.__control.receipt_electric()))
        self.waterReceivable.setText(str(self.__control.receipt_water()))
        self.propertyFeeReceivable.setText(str(self.__control.receipt_propertyfee()))
        self.guaranteeReceivable.setText(str(self.__control.receipt_guarantee()))

        self.rentTime.setText(str(self.__control.contract_year()))
        self.contractInf.setText(str(self.__control.contract_information()))
        self.ceoSignature.setCheckState(self.__control.contract_CEOSign())
        self.signatureConfirmation.setCheckState(self.__control.contract_proprietorSign())
        self.fraction.setText(str(random.randint(500,700)))

        return None

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
        self.__control.create_application(self.__ID,
                                          int(self.shopNum.text()),
                                          self.shopName.text(),
                                          self.userTel.text(),
                                          int(self.shopRentTime.text()),
                                          self.shopReason.toPlainText())
        self.shopName.setText("")
        self.userTel.setText("")
        self.shopRentTime.setText("")
        self.shopReason.setText("")
        self.shopNum.setText("")
        QMessageBox.information(self,
                                "消息",
                                "提交申请成功")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = ProprietorWindow(12)

    MainWindow.show()

    sys.exit(app.exec_())
