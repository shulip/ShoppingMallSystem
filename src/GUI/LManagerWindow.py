#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from GUI.LoginWindow import *

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *

from GUI.ManagerWindow import Design_ManagerWindow
from Controllers import ManagerControl
import sys

class ManagerWindow(Design_ManagerWindow):
    def __init__(self,ID, parent=None):
        super().__init__(parent)
        self.__ID = ID
        self.__control = ManagerControl(ID)
        self.__applications = self.__control.get_applications()
        self.btnApprochHandling.clicked.connect(self.show_combo)                    # 显示下拉申请菜单
        self.pendingApplication.currentIndexChanged.connect(self.set_information)   # 选择申请选项后对右侧进行相应更新
        self.refuseEntry.clicked.connect(self.del_current_application)              # 删除相应的申请记录
        self.approvingEntry.clicked.connect(self.set_contract)                      # 批准进场同时更新合同部分信息
        self.submitAudit.clicked.connect(self.submit_audit)                         # 提交合同


    def show_combo(self):
        """
        显示下拉申请菜单
        :return:
        """
        for application in self.__applications:
            self.pendingApplication.addItems(str(application["userName"]))
        return None

    def set_information(self):
        """
        选择申请选项后对右侧进行相应更新
        :return:
        """
        currentApplication = None
        for application in self.__applications:
            if str(application["userName"]) == self.pendingApplication.currentText():
                currentApplication = application
                break
        self.intentionShopNum.setText(str(currentApplication["shopIndex"]))
        self.userTel.setText(str(currentApplication["telenumber"]))
        self.userName.setText(str(currentApplication["userName"]))
        self.rentTime.setText(str(currentApplication["rentTime"]))
        self.rentReason.setText(str(currentApplication["rentUsage"]))
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
        self.__control.create_contract(self.shopNum.text(),
                                       self.userName.text(),
                                       self.userTelContract.text(),
                                       self.contractInformation.toPlainText(),
                                       self.rentTimeManager.text()
                                       )


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = ManagerWindow("sa")

    MainWindow.show()

    sys.exit(app.exec_())
