# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Pay.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Pay(object):
    def setupUi(self, Pay):
        Pay.setObjectName("Pay")
        Pay.resize(732, 594)
        self.widget = QtWidgets.QWidget(Pay)
        self.widget.setGeometry(QtCore.QRect(30, 20, 651, 491))
        self.widget.setStyleSheet("QWidget\n"
"{\n"
"    background:rgb(226, 232, 255);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 80, 280, 360))
        self.label.setStyleSheet("\n"
"border-image:  url(:/icon/B36AC9D518FCA380A0E56850D2CE2889.jpg);")
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(340, 80, 280, 360))
        self.label_2.setStyleSheet("border-image: url(:/icon/587485E7898F1773A0CF2807D4D4A126.jpg);")
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.widget_16 = QtWidgets.QWidget(self.widget)
        self.widget_16.setGeometry(QtCore.QRect(0, 0, 651, 40))
        self.widget_16.setStyleSheet("QWidget\n"
"{\n"
"    background:rgb(165, 200, 255);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"")
        self.widget_16.setObjectName("widget_16")
        self.label_31 = QtWidgets.QLabel(self.widget_16)
        self.label_31.setGeometry(QtCore.QRect(15, 15, 141, 20))
        self.label_31.setStyleSheet("font-size:20px;")
        self.label_31.setObjectName("label_31")
        self.btnMenu_Close = QtWidgets.QPushButton(self.widget_16)
        self.btnMenu_Close.setGeometry(QtCore.QRect(610, 10, 30, 30))
        self.btnMenu_Close.setStyleSheet("QPushButton\n"
"{\n"
"background:transparent;\n"
"    image: url(:/icon/2.png);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"image: url(:/icon/close_hover.png);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"image: url(:/icon/close_press.png);\n"
"}")
        self.btnMenu_Close.setText("")
        self.btnMenu_Close.setIconSize(QtCore.QSize(30, 30))
        self.btnMenu_Close.setObjectName("btnMenu_Close")

        self.retranslateUi(Pay)
        QtCore.QMetaObject.connectSlotsByName(Pay)

    def retranslateUi(self, Pay):
        _translate = QtCore.QCoreApplication.translate
        Pay.setWindowTitle(_translate("Pay", "Form"))
        self.label_31.setText(_translate("Pay", "租赁合同"))

from GUI.image.image import *