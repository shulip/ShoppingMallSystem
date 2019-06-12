# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_UserWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UserWindow(object):
    def setupUi(self, UserWindow):
        UserWindow.setObjectName("UserWindow")
        UserWindow.resize(1104, 820)
        self.frame = QtWidgets.QFrame(UserWindow)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1051, 791))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widgetMenu = QtWidgets.QWidget(self.frame)
        self.widgetMenu.setGeometry(QtCore.QRect(160, 10, 871, 50))
        self.widgetMenu.setObjectName("widgetMenu")
        self.btnMenu_Close = QtWidgets.QPushButton(self.widgetMenu)
        self.btnMenu_Close.setGeometry(QtCore.QRect(840, 0, 30, 30))
        self.btnMenu_Close.setObjectName("btnMenu_Close")
        self.btnMenu_Max = QtWidgets.QPushButton(self.widgetMenu)
        self.btnMenu_Max.setGeometry(QtCore.QRect(810, 0, 30, 30))
        self.btnMenu_Max.setObjectName("btnMenu_Max")
        self.btnMenu_Min = QtWidgets.QPushButton(self.widgetMenu)
        self.btnMenu_Min.setGeometry(QtCore.QRect(780, 0, 30, 30))
        self.btnMenu_Min.setObjectName("btnMenu_Min")
        self.widgetLeft = QtWidgets.QWidget(self.frame)
        self.widgetLeft.setGeometry(QtCore.QRect(12, 10, 150, 768))
        self.widgetLeft.setObjectName("widgetLeft")
        self.widgetBtn = QtWidgets.QWidget(self.widgetLeft)
        self.widgetBtn.setGeometry(QtCore.QRect(0, 50, 150, 720))
        self.widgetBtn.setStyleSheet("QToolButton\n"
"{    \n"
"color:rgb(255, 255, 255);\n"
"background:#66A5ad;\n"
"border-radius:10px;\n"
"\n"
"}\n"
"QWidget\n"
"{\n"
"background:rgb(67, 66, 58)\n"
"}\n"
"\n"
"QToolButton:hover\n"
"{\n"
"    color:rgb(255, 234, 246);\n"
"    borderr-radius:10px;\n"
"    background:#07575B;\n"
"}\n"
"\n"
"")
        self.widgetBtn.setObjectName("widgetBtn")
        self.btnMyShop = QtWidgets.QToolButton(self.widgetBtn)
        self.btnMyShop.setGeometry(QtCore.QRect(0, 50, 150, 50))
        self.btnMyShop.setObjectName("btnMyShop")
        self.btnAllShop = QtWidgets.QToolButton(self.widgetBtn)
        self.btnAllShop.setGeometry(QtCore.QRect(0, 0, 150, 50))
        self.btnAllShop.setStyleSheet("")
        self.btnAllShop.setObjectName("btnAllShop")
        self.btnInf = QtWidgets.QToolButton(self.widgetBtn)
        self.btnInf.setGeometry(QtCore.QRect(0, 100, 150, 50))
        self.btnInf.setObjectName("btnInf")
        self.btnContract = QtWidgets.QToolButton(self.widgetBtn)
        self.btnContract.setGeometry(QtCore.QRect(0, 150, 150, 50))
        self.btnContract.setObjectName("btnContract")
        self.btnSublease = QtWidgets.QToolButton(self.widgetBtn)
        self.btnSublease.setGeometry(QtCore.QRect(0, 200, 150, 50))
        self.btnSublease.setObjectName("btnSublease")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setGeometry(QtCore.QRect(161, 60, 871, 720))
        self.stackedWidget.setStyleSheet("QWidget{\n"
"background:rgb(167, 167, 167);\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.AllShop = QtWidgets.QWidget()
        self.AllShop.setObjectName("AllShop")
        self.allShop = QtWidgets.QLabel(self.AllShop)
        self.allShop.setGeometry(QtCore.QRect(0, 0, 54, 41))
        self.allShop.setObjectName("allShop")
        self.stackedWidget.addWidget(self.AllShop)
        self.MyShop = QtWidgets.QWidget()
        self.MyShop.setObjectName("MyShop")
        self.myShop = QtWidgets.QLabel(self.MyShop)
        self.myShop.setGeometry(QtCore.QRect(30, 20, 54, 12))
        self.myShop.setObjectName("myShop")
        self.stackedWidget.addWidget(self.MyShop)
        self.MyInformation = QtWidgets.QWidget()
        self.MyInformation.setObjectName("MyInformation")
        self.myInformation = QtWidgets.QLabel(self.MyInformation)
        self.myInformation.setGeometry(QtCore.QRect(20, 20, 54, 12))
        self.myInformation.setObjectName("myInformation")
        self.stackedWidget.addWidget(self.MyInformation)
        self.MyContract = QtWidgets.QWidget()
        self.MyContract.setObjectName("MyContract")
        self.myContract = QtWidgets.QLabel(self.MyContract)
        self.myContract.setGeometry(QtCore.QRect(40, 30, 54, 12))
        self.myContract.setObjectName("myContract")
        self.stackedWidget.addWidget(self.MyContract)
        self.ApplyForSublease = QtWidgets.QWidget()
        self.ApplyForSublease.setObjectName("ApplyForSublease")
        self.applyForSublease = QtWidgets.QLabel(self.ApplyForSublease)
        self.applyForSublease.setGeometry(QtCore.QRect(30, 20, 54, 12))
        self.applyForSublease.setObjectName("applyForSublease")
        self.stackedWidget.addWidget(self.ApplyForSublease)

        self.retranslateUi(UserWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(UserWindow)

    def retranslateUi(self, UserWindow):
        _translate = QtCore.QCoreApplication.translate
        UserWindow.setWindowTitle(_translate("UserWindow", "Form"))
        self.btnMenu_Close.setText(_translate("UserWindow", "×"))
        self.btnMenu_Max.setText(_translate("UserWindow", "×"))
        self.btnMenu_Min.setText(_translate("UserWindow", "×"))
        self.btnMyShop.setText(_translate("UserWindow", "我的店铺"))
        self.btnAllShop.setText(_translate("UserWindow", "全部店铺"))
        self.btnInf.setText(_translate("UserWindow", "我的信息"))
        self.btnContract.setText(_translate("UserWindow", "我的合同"))
        self.btnSublease.setText(_translate("UserWindow", "申请转租"))
        self.allShop.setText(_translate("UserWindow", "全部店铺"))
        self.myShop.setText(_translate("UserWindow", "我的店铺"))
        self.myInformation.setText(_translate("UserWindow", "我的信息"))
        self.myContract.setText(_translate("UserWindow", "我的合同"))
        self.applyForSublease.setText(_translate("UserWindow", "申请转租"))

