# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginInterface(object):
    def setupUi(self, LoginInterface):
        LoginInterface.setObjectName("LoginInterface")
        LoginInterface.setEnabled(True)
        LoginInterface.resize(717, 526)
        LoginInterface.setStyleSheet("")
        self.frame = QtWidgets.QFrame(LoginInterface)
        self.frame.setGeometry(QtCore.QRect(100, 60, 430, 330))
        self.frame.setStyleSheet("*{\n"
"    font-family:century gothic;\n"
"    font-size:16px\n"
"}\n"
"\n"
"QFrame\n"
"{\n"
"    background:rgb(132, 132, 132);\n"
"    border-radius:15px\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"    color:white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QLineEdit\n"
"{\n"
"background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"border-bottom:1px solid#717072;\n"
"}\n"
"\n"
"QCheckBox\n"
"{\n"
"    color:white;\n"
"}\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.ID = QtWidgets.QLineEdit(self.frame)
        self.ID.setGeometry(QtCore.QRect(150, 110, 141, 31))
        self.ID.setStyleSheet("QLineEdit\n"
"{\n"
"    background:white;\n"
"    padding-left:5px ;\n"
"    padding-top:1px ;\n"
"    border-bottom-left-radius:7px;\n"
"    border-bottom-right-radius:7px;\n"
"    border: 1px solid rgb(209 , 209 , 209);\n"
"    border-top:transparent;\n"
"}\n"
"QLineEdit:hover\n"
"{\n"
"    padding-top:0px ;\n"
"    border: 1px solid rgb(21 , 131 , 221);\n"
"}")
        self.ID.setText("")
        self.ID.setObjectName("ID")
        self.logIn = QtWidgets.QPushButton(self.frame)
        self.logIn.setGeometry(QtCore.QRect(130, 280, 171, 31))
        self.logIn.setStyleSheet("QPushButton\n"
"{\n"
"    color:white;\n"
"    background-color:rgb(14 , 150 , 254);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    color:white;\n"
"    background-color:rgb(44 , 137 , 255);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    color:white;\n"
"    background-color:rgb(14 , 135 , 228);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"")
        self.logIn.setObjectName("logIn")
        self.rememberKey = QtWidgets.QCheckBox(self.frame)
        self.rememberKey.setGeometry(QtCore.QRect(60, 230, 91, 31))
        self.rememberKey.setObjectName("rememberKey")
        self.Key = QtWidgets.QLineEdit(self.frame)
        self.Key.setGeometry(QtCore.QRect(150, 150, 141, 31))
        self.Key.setStyleSheet("QLineEdit\n"
"{\n"
"    background:white;\n"
"    padding-left:5px ;\n"
"    padding-top:1px ;\n"
"    border-bottom-left-radius:7px;\n"
"    border-bottom-right-radius:7px;\n"
"    border: 1px solid rgb(209 , 209 , 209);\n"
"    border-top:transparent;\n"
"}\n"
"QLineEdit:hover\n"
"{\n"
"    padding-top:0px ;\n"
"    border: 1px solid rgb(21 , 131 , 221);\n"
"}")
        self.Key.setText("")
        self.Key.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Key.setObjectName("Key")
        self.userID = QtWidgets.QLabel(self.frame)
        self.userID.setGeometry(QtCore.QRect(60, 110, 71, 41))
        self.userID.setObjectName("userID")
        self.userKey = QtWidgets.QLabel(self.frame)
        self.userKey.setGeometry(QtCore.QRect(60, 150, 61, 31))
        self.userKey.setObjectName("userKey")
        self.autLog = QtWidgets.QCheckBox(self.frame)
        self.autLog.setGeometry(QtCore.QRect(210, 230, 121, 31))
        self.autLog.setObjectName("autLog")
        self.mallName = QtWidgets.QLabel(self.frame)
        self.mallName.setGeometry(QtCore.QRect(130, 30, 161, 61))
        self.mallName.setStyleSheet("QLabel\n"
"{\n"
"    color:white;\n"
"font-size:35px;\n"
"}")
        self.mallName.setObjectName("mallName")
        self.registAccount = QtWidgets.QPushButton(self.frame)
        self.registAccount.setGeometry(QtCore.QRect(310, 110, 91, 31))
        self.registAccount.setStyleSheet("QPushButton\n"
"{\n"
"    color:rgb(222, 255, 253);\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    color:rgb(97 , 179 , 246);\n"
"}\n"
"")
        self.registAccount.setObjectName("registAccount")
        self.forgetPassword = QtWidgets.QPushButton(self.frame)
        self.forgetPassword.setGeometry(QtCore.QRect(310, 150, 91, 31))
        self.forgetPassword.setStyleSheet("QPushButton\n"
"{\n"
"     color:rgb(222, 255, 253);\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    color:rgb(97 , 179 , 246);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    color:rgb(0 , 109 , 176);\n"
"}\n"
"")
        self.forgetPassword.setObjectName("forgetPassword")
        self.closeLogInWindow = QtWidgets.QPushButton(self.frame)
        self.closeLogInWindow.setGeometry(QtCore.QRect(390, 0, 30, 30))
        self.closeLogInWindow.setText("")
        self.closeLogInWindow.setObjectName("closeLogInWindow")
        self.arrowcloseLogInWindow = QtWidgets.QPushButton(self.frame)
        self.arrowcloseLogInWindow.setGeometry(QtCore.QRect(360, 0, 30, 30))
        self.arrowcloseLogInWindow.setText("")
        self.arrowcloseLogInWindow.setObjectName("arrowcloseLogInWindow")
        self.userKey_2 = QtWidgets.QLabel(self.frame)
        self.userKey_2.setGeometry(QtCore.QRect(60, 190, 61, 31))
        self.userKey_2.setObjectName("userKey_2")
        self.jobPosition = QtWidgets.QComboBox(self.frame)
        self.jobPosition.setGeometry(QtCore.QRect(150, 191, 141, 31))
        self.jobPosition.setStyleSheet("QComboBox\n"
"{\n"
"    background:white;\n"
"    padding-left:5px ;\n"
"    border-top-left-radius:3px;\n"
"    border-top-right-radius:3px;\n"
"    border: 1px solid rgb(209 , 209 , 209);\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"    border: 1px solid rgb(21 , 131 , 221);\n"
"}\n"
"QComboBox QAbstractItemView::item\n"
"{\n"
"    height:40px;\n"
"}\n"
"")
        self.jobPosition.setObjectName("jobPosition")

        self.retranslateUi(LoginInterface)
        QtCore.QMetaObject.connectSlotsByName(LoginInterface)

    def retranslateUi(self, LoginInterface):
        _translate = QtCore.QCoreApplication.translate
        LoginInterface.setWindowTitle(_translate("LoginInterface", "LoginInterface"))
        self.ID.setPlaceholderText(_translate("LoginInterface", "账号/手机号"))
        self.logIn.setText(_translate("LoginInterface", "登录"))
        self.rememberKey.setText(_translate("LoginInterface", "记住密码"))
        self.Key.setPlaceholderText(_translate("LoginInterface", "Password"))
        self.userID.setText(_translate("LoginInterface", "用户名："))
        self.userKey.setText(_translate("LoginInterface", "密码："))
        self.autLog.setText(_translate("LoginInterface", "自动登录"))
        self.mallName.setText(_translate("LoginInterface", "购物中心"))
        self.registAccount.setText(_translate("LoginInterface", "注册账号"))
        self.forgetPassword.setText(_translate("LoginInterface", "忘记密码"))
        self.userKey_2.setText(_translate("LoginInterface", "职位："))

