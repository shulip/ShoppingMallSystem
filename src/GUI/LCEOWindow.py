#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *

from GUI.CEOWindow import Design_CEOWindow
import sys
from Controllers import CEOControl


class CEOWindow(Design_CEOWindow):
    def __init__(self,ID, parent=None):
        super().__init__(parent)
        self.__ID = ID
        self.__control = CEOControl(ID)
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

        self.btnMyShop.clicked.connect(self.show_combo)
        self.processingConfirmation.clicked.connect(self.confirm_contract)

    def show_combo(self):
        """
        显示下拉合同菜单
        :return:
        """
        confirmNum = 0
        signNum = 0
        for contract in self.__contracts:
            if contract["contractCeoAffirm"] ==0 and contract["contractCeoSign"] ==0:
                self.residualAudit.addItems(contract["number"])
                confirmNum += 1
            elif contract["contractCeoAffirm"] ==1 and contract["contractCeoSign"] ==0:
                self.residualAudit.addItems(contract["number"])
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

        if currentReceipt is not None and currentContract is not None and currentReceivable is not None:
            # 店铺信息
            self.propertyFee.setText(str(currentReceipt["receiptPropCharge"]))
            self.guaranteePaid.setText(str(currentReceipt["receiptGuarCharge"]))
            self.waterFeePaid.setText(str(currentReceipt["receiptWaterCharge"]))
            self.electricFeePaid.setText(str(currentReceipt["receiptEleCharge"]))

            # 缴纳状态
            if currentReceivable["receivablePropCharge"] >currentReceipt["receiptPropCharge"]:
                self.owePropertyFee.setCheckState(1)

            if currentReceivable["receivableEleCharge"] >currentReceipt["receiptEleCharge"]:
                self.oweElectricFee.setCheckState(1)

            if currentReceivable["receivableGuarCharge"] >currentReceipt["receiptGuarCharge"]:
                self.oweGuaranteePaid.setCheckState(1)

            if currentReceivable["receivableWaterCharge"] >currentReceipt["receiptWaterCharge"]:
                self.oweWaterFee.setCheckState(1)

            # 合同信息
            self.shopNumberContract.setText(str(number))
            self.RentStateContract.setText(str(currentContract["contractStatus"]))
            self.rentTimeContract.setText(str(currentContract["contractYear"]))
            self.ceoConfirm.setCheckState(currentContract["contractCeoAffirm"])
            self.userSignature.setCheckState(currentContract["contractProprietorSign"])
            self.ceoSingature.setCheckState(currentContract["contractCeoSign"])
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
            self.owePropertyFee.setCheckState(0)

            self.oweElectricFee.setCheckState(0)

            self.oweGuaranteePaid.setCheckState(0)

            self.oweWaterFee.setCheckState(0)

            # 合同信息
            self.shopNumberContract.setText(str(number))
            self.RentStateContract.setText("")
            self.rentTimeContract.setText("")
            self.ceoConfirm.setCheckState(0)
            self.userSignature.setCheckState(0)
            self.ceoSingature.setCheckState(0)
            self.contractInfomation.setText("")

    def confirm_contract(self):
        """
        确认合同
        :return:
        """
        if self.contractConfirm.isChecked():


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = CEOWindow("sa")

    MainWindow.show()

    sys.exit(app.exec_())

