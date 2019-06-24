#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *

from GUI.CEOWindow import Design_CEOWindow
import sys
from Controllers import CEOControl
import win32com.client
import threading
import random

class CEOWindow(Design_CEOWindow):
    def __init__(self,ID, parent=None):
        super().__init__(parent)
        self.__ID = ID
        self.__control = CEOControl(ID)

        self.speaker = win32com.client.Dispatch("SAPI.SpVoice")

        self.btnAllShop.clicked.connect(lambda: threading.Thread(target=lambda: self.speaker.Speak("全部店铺")).start())
        self.btnMyShop.clicked.connect(lambda: threading.Thread(target=lambda: self.speaker.Speak("审核合同")).start())
        self.btnInf.clicked.connect(lambda: threading.Thread(target=lambda: self.speaker.Speak("我的信息")).start())

        self.__contracts = self.__control.get_all_contracts()
        self.__receipts = self.__control.get_all_receipts()
        self.__receivables = self.__control.get_all_receivable()
        self.pushButtonShop_01.clicked.connect(lambda :self.set_information(1))
        self.pushButtonShop_02.clicked.connect(lambda :self.set_information(2))
        self.pushButtonShop_03.clicked.connect(lambda :self.set_information(3))
        self.pushButtonShop_04.clicked.connect(lambda :self.set_information(4))
        self.pushButtonShop_05.clicked.connect(lambda :self.set_information(5))
        self.pushButtonShop_06.clicked.connect(lambda :self.set_information(6))
        self.pushButtonShop_07.clicked.connect(lambda :self.set_information(7))
        self.pushButtonShop_08.clicked.connect(lambda :self.set_information(8))
        self.pushButtonShop_09.clicked.connect(lambda :self.set_information(9))
        self.pushButtonShop_10.clicked.connect(lambda :self.set_information(10))
        self.pushButtonShop_11.clicked.connect(lambda :self.set_information(11))
        self.pushButtonShop_12.clicked.connect(lambda :self.set_information(12))

        self.show_combo()

        self.auditConfirmation.clicked.connect(self.confirm_contract)
        self.signatureConfirmation.clicked.connect(self.sign_contract_)
        self.residualAudit.currentTextChanged.connect(self.set_confirm_contract)
        self.quantityAudited.currentTextChanged.connect(self.set_affrim_contract)

    def set_confirm_contract(self):
        for contract in self.__contracts:
            if self.residualAudit.currentText() == str(contract["number"]):
                self.contractContent.setText(contract["contractInfo"])
                self.shopNun.setText(str(contract["number"]))
                # self.userTel.setText(random.randint(12031823712,19023912381))
                self.rentTime.setText(str(contract["contractYear"]))
        return None


    def set_affrim_contract(self):
        for contract in self.__contracts:
            if self.quantityAudited.currentText() == str(contract["number"]):
                self.contractContent.setText(contract["contractInfo"])
                self.shopNun.setText(str(contract["number"]))
                # self.userTel.setText(str(random.randint(12031823712,19023912381)))
                self.rentTime.setText(str(contract["contractYear"]))
        return None

    def show_combo(self):
        """
        显示下拉合同菜单
        :return:
        """
        confirmNum = 0
        signNum = 0


        for contract in self.__contracts:
            if contract["contractCeoAffirm"] ==0 and contract["contractCeoSign"] ==0:
                self.residualAudit.addItem(str(contract["number"]))
                confirmNum += 1
            if contract["contractCeoAffirm"] ==1 and contract["contractCeoSign"] ==0:
                # self.quantityAudited.addItem("asas")
                self.quantityAudited.addItem(str(contract["number"]))
                signNum += 1
        self.residualAuditNum.setText(str(confirmNum))
        self.quantityAuditedNum.setText(str(signNum))

        return None

    def set_information_confirm(self):
        """
        选择申请选项后对右侧进行相应更新
        :return:
        """
        currentContract = None
        for contract in self.__contracts:
            if str(contract["number"]) == self.residualAudit.currentText():
                currentContract = contract
                break
        self.shopNun.setText(str(currentContract["number"]))
        # self.userTel.setText(str(currentContract["telenumber"]))
        self.rentTime.setText(str(currentContract["contractYear"]))
        self.contractContent.setText(str(currentContract["contractInfo"]))
        # self.rentReason.setText(str(currentContract["rentUsage"]))
        return None

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

        # self.owePropertyFee.setCheckable(False)
        # self.oweElectricFee.setCheckable(False)
        # self.oweGuaranteePaid.setCheckable(False)
        # self.oweWaterFee.setCheckable(False)
        # self.ceoConfirm.setCheckable(False)
        # self.userSignature.setCheckable(False)
        # self.ceoSingature.setCheckable(False)

    def confirm_contract(self):
        """
        确认合同
        :return:
        """
        if self.contractConfirm.isChecked():
            for contract in self.__contracts:
                if str(contract["number"]) == str(self.shopNun.text()):
                    self.__control.set_contract_ceoaffirm_by_id(contract["ID"],1)
                    break
        QMessageBox.information(self,
                                "消息",
                                "确认成功")
        return None

    def sign_contract_(self):
        """
        签字
        :return:
        """
        if self.ceoSignature.text() !="":
            for contract in self.__contracts:
                if str(contract["number"]) == str(self.shopNun.text()):
                    self.__control.set_contract_ceosign_by_id(contract["ID"],1)
        QMessageBox.information(self,
                                "消息",
                                "签字成功")
        return None


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = CEOWindow("sa")

    MainWindow.show()

    sys.exit(app.exec_())
