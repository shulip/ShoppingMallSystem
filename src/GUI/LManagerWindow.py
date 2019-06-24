#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from GUI.LoginWindow import *

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *

from GUI.ManagerWindow import Design_ManagerWindow
from Controllers import ManagerControl
import sys
import win32com.client
import threading


class ManagerWindow(Design_ManagerWindow):
    def __init__(self,ID, parent=None):
        super().__init__(parent)
        self.speaker = win32com.client.Dispatch("SAPI.SpVoice")
        self.__ID = ID
        self.__control = ManagerControl(ID)
        self.currentApplication = None      #当前申请
        self.__applications = self.__control.get_applications()
        self.__contracts = self.__control.get_all_contracts()
        self.__receipts = self.__control.get_all_receipts()
        self.__receivables = self.__control.get_all_receivable()
        self.pushButtonShop_01.clicked.connect(lambda: self.set_information(1))
        self.pushButtonShop_02.clicked.connect(lambda: self.set_information(2))
        self.pushButtonShop_03.clicked.connect(lambda: self.set_information(3))
        self.pushButtonShop_04.clicked.connect(lambda: self.set_information(4))
        self.pushButtonShop_05.clicked.connect(lambda: self.set_information(5))
        self.pushButtonShop_06.clicked.connect(lambda: self.set_information(6))
        self.pushButtonShop_07.clicked.connect(lambda: self.set_information(7))
        self.pushButtonShop_08.clicked.connect(lambda: self.set_information(8))
        self.pushButtonShop_09.clicked.connect(lambda: self.set_information(9))
        self.pushButtonShop_10.clicked.connect(lambda: self.set_information(10))
        self.pushButtonShop_11.clicked.connect(lambda: self.set_information(11))
        self.pushButtonShop_12.clicked.connect(lambda: self.set_information(12))

        self.btnApprochHandling.clicked.connect(
            lambda: threading.Thread(target=lambda: self.speaker.Speak("申请处理")).start())
        self.btnInf.clicked.connect(lambda: threading.Thread(target=lambda: self.speaker.Speak("拟定合同")).start())
        self.btnAllShop.clicked.connect(lambda: threading.Thread(target=lambda: self.speaker.Speak("全部商铺")).start())

        self.show_combo()
        self.pendingApplication.currentIndexChanged.connect(self.set_information_current)   # 选择申请选项后对右侧进行相应更新
        self.refuseEntry.clicked.connect(self.del_current_application)              # 删除相应的申请记录
        self.approvingEntry.clicked.connect(self.set_contract)                      # 批准进场同时更新合同部分信息
        self.submitAudit.clicked.connect(self.submit_audit)                         # 提交合同




    # def speack_apply(self):
    #     # self.speaker.Speak("申请处理")
    #     threading.Thread(target=lambda :self.speaker.Speak("申请处理")).start()

    def set_information(self,number):
        currentReceipt = None
        currentContract = None
        currentReceivable = None

        for receipt in self.__receipts:
            if receipt["number"] == int(number):
                currentReceipt = receipt
                break

        for contract in self.__contracts:
            if contract["number"] == int(number):
                currentContract = contract
                break

        for receivable in self.__receivables:
            if receivable["number"] == int(number):
                currentReceivable = receivable
                break

        self.owePropertyFee.setCheckable(True)
        self.oweElectricFee.setCheckable(True)
        self.oweGuaranteePaid.setCheckable(True)
        self.oweWaterFee.setCheckable(True)
        self.ceoConfirm.setCheckable(True)
        self.userSignature.setCheckable(True)
        self.ceoSingature.setCheckable(True)

        if currentReceipt is not None and currentContract is not None and currentReceivable is not None:
            # 店铺信息
            self.propertyFee.setText(str(currentReceipt["receiptPropCharge"]))
            self.guaranteePaid.setText(str(currentReceipt["receiptGuarCharge"]))
            self.waterFeePaid.setText(str(currentReceipt["receiptWaterCharge"]))
            self.electricFeePaid.setText(str(currentReceipt["receiptEleCharge"]))

            # 缴纳状态
            if currentReceivable["receivablePropCharge"] >currentReceipt["receiptPropCharge"]:
                self.owePropertyFee.setChecked(1)
            else:
                self.owePropertyFee.setChecked(False)

            if currentReceivable["receivableEleCharge"] >currentReceipt["receiptEleCharge"]:
                self.oweElectricFee.setChecked(1)
            else:
                self.oweElectricFee.setChecked(False)

            if currentReceivable["receivableGuarCharge"] >currentReceipt["receiptGuarCharge"]:
                self.oweGuaranteePaid.setChecked(1)
            else:
                self.oweGuaranteePaid.setChecked(False)

            if currentReceivable["receivableWaterCharge"] >currentReceipt["receiptWaterCharge"]:
                self.oweWaterFee.setChecked(1)
            else:
                self.oweWaterFee.setChecked(False)

            # 合同信息
            self.shopNumberContract.setText(str(number))
            self.RentStateContract.setText(str(currentContract["contractStatus"]))
            self.rentTimeContract.setText(str(currentContract["contractYear"]))
            print("**************currentContract[contractCeoAffirm]***************")
            print(currentContract["contractCeoAffirm"])
            print(bool(currentContract["contractCeoAffirm"]))
            self.ceoConfirm.setChecked(bool(currentContract["contractCeoAffirm"]))
            print("**************currentContract[contractProprietorSign]***************")
            print(currentContract["contractProprietorSign"])
            self.userSignature.setChecked(bool(currentContract["contractProprietorSign"]))
            self.ceoSingature.setChecked(bool(currentContract["contractCeoSign"]))

            self.contractInfomation.setText(str(currentContract["contractInfo"]))
        else:
            # 店铺信息
            self.shopNumberText.setText(str(number))
            self.propertyFeePaid.setText("")
            self.guaranteePaid.setText("")
            self.waterFeePaid.setText("")
            self.electricFeePaid.setText("")
            self.rentStateText.setText("")

            # 缴纳状态
            self.owePropertyFee.setChecked(False)

            self.oweElectricFee.setChecked(False)

            self.oweGuaranteePaid.setChecked(False)

            self.oweWaterFee.setChecked(False)

            # 合同信息
            self.shopNumberContract.setText(str(number))
            self.RentStateContract.setText("")
            self.rentTimeContract.setText("")
            self.ceoConfirm.setChecked(False)
            self.userSignature.setChecked(False)
            self.ceoSingature.setChecked(False)
            self.contractInfomation.setText("")

    def show_combo(self):
        """
        显示下拉申请菜单
        :return:
        """
        for application in self.__applications:
            self.pendingApplication.addItem(str(application["userName"]))
        return None

    def set_information_current(self):
        """
        选择申请选项后对右侧进行相应更新
        :return:
        """

        for application in self.__applications:
            if str(application["userName"]) == self.pendingApplication.currentText():
                self.currentApplication = application
                break
        self.intentionShopNum.setText(str(self.currentApplication["shopIndex"]))
        self.userTel.setText(str(self.currentApplication["telenumber"]))
        self.userName.setText(str(self.currentApplication["userName"]))
        self.rentTime.setText(str(self.currentApplication["rentTime"]))
        self.rentReason.setText(str(self.currentApplication["rentUsage"]))
        return None

    def del_current_application(self):
        """
        删除相应的申请记录
        :return:
        """
        #TODO:数据库删除相应的申请记录
        return None

    def set_contract(self):
        """
        批准进场同时更新合同部分信息
        :return:
        """
        self.shopNum.setText(self.intentionShopNum.text())
        self.userTelContract.setText(self.userTel.text())
        self.rentTimeManager.setText(self.rentTime.text())
        return None

    def submit_audit(self):
        """
        提交拟定合同
        :return:
        """
        self.__control.create_contract(self.currentApplication["ID"],
                                       self.shopNum.text(),
                                       self.userName.text(),
                                       self.userTelContract.text(),
                                       self.contractInformation.toPlainText(),
                                       self.rentTimeManager.text()
                                       )
        QMessageBox.information(self,
                                "消息",
                                "提交合同成功")
        self.shopNum.setText("")
        self.userTelContract.setText("")
        self.rentTimeManager.setText("")
        self.contractInformation.setText("")
        self.__control.delete_application(self.currentApplication["ID"])
        # self.show_combo()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = ManagerWindow("sa")

    MainWindow.show()

    sys.exit(app.exec_())
