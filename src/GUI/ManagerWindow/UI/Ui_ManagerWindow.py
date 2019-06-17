# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_ManagerWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ManagerWindow(object):
    def setupUi(self, ManagerWindow):
        ManagerWindow.setObjectName("ManagerWindow")
        ManagerWindow.resize(1092, 730)
        ManagerWindow.setStyleSheet("font: 9pt \"华文中宋\";")
        self.frame = QtWidgets.QFrame(ManagerWindow)
        self.frame.setGeometry(QtCore.QRect(20, 20, 1000, 600))
        self.frame.setStyleSheet("font: 9pt \"黑体\";")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widgetMenu = QtWidgets.QWidget(self.frame)
        self.widgetMenu.setGeometry(QtCore.QRect(0, 0, 1001, 30))
        self.widgetMenu.setStyleSheet("QWidget\n"
"{\n"
"background:white;\n"
"}")
        self.widgetMenu.setObjectName("widgetMenu")
        self.btnMenu_Close = QtWidgets.QPushButton(self.widgetMenu)
        self.btnMenu_Close.setGeometry(QtCore.QRect(970, 0, 30, 30))
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
        self.btnMenu_Max = QtWidgets.QPushButton(self.widgetMenu)
        self.btnMenu_Max.setGeometry(QtCore.QRect(940, 0, 30, 30))
        self.btnMenu_Max.setStyleSheet("QPushButton:hover\n"
"\n"
"{\n"
"image: url(:/icon/arrow_hover.png);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"image: url(:/icon/arrow_press.png);\n"
"}\n"
"QPushButton\n"
"{\n"
"background:transparent;\n"
"    image: url(:/icon/4.png);\n"
"}")
        self.btnMenu_Max.setText("")
        self.btnMenu_Max.setIconSize(QtCore.QSize(30, 30))
        self.btnMenu_Max.setObjectName("btnMenu_Max")
        self.btnMenu_Min = QtWidgets.QPushButton(self.widgetMenu)
        self.btnMenu_Min.setGeometry(QtCore.QRect(910, 0, 30, 30))
        self.btnMenu_Min.setStyleSheet("QPushButton:hover\n"
"{\n"
"image: url(:/icon/min_hover.bmp);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"image: url(:/icon/min_press.bmp);\n"
"}\n"
"QPushButton\n"
"{\n"
"background:transparent;\n"
"    image: url(:/icon/1.png);\n"
"}")
        self.btnMenu_Min.setText("")
        self.btnMenu_Min.setIconSize(QtCore.QSize(30, 30))
        self.btnMenu_Min.setObjectName("btnMenu_Min")
        self.widgetLeft = QtWidgets.QWidget(self.frame)
        self.widgetLeft.setGeometry(QtCore.QRect(0, 30, 150, 571))
        self.widgetLeft.setObjectName("widgetLeft")
        self.widgetBtn = QtWidgets.QWidget(self.widgetLeft)
        self.widgetBtn.setGeometry(QtCore.QRect(0, 0, 150, 571))
        self.widgetBtn.setStyleSheet("QToolButton\n"
"{    \n"
"color:rgb(255, 255, 255);\n"
"background:#66A5ad;\n"
"border-radius:10px;\n"
"font-size:16px;\n"
"}\n"
"QWidget\n"
"{\n"
"background:#333645;\n"
"}\n"
"\n"
"QToolButton:hover\n"
"{\n"
"    color:rgb(255, 234, 246);\n"
"border-radius:10px;\n"
"    background:#39c0c3;\n"
"}\n"
"\n"
"\n"
"")
        self.widgetBtn.setObjectName("widgetBtn")
        self.btnApprochHandling = QtWidgets.QToolButton(self.widgetBtn)
        self.btnApprochHandling.setGeometry(QtCore.QRect(0, 50, 150, 50))
        self.btnApprochHandling.setObjectName("btnApprochHandling")
        self.btnAllShop = QtWidgets.QToolButton(self.widgetBtn)
        self.btnAllShop.setGeometry(QtCore.QRect(0, 0, 150, 50))
        self.btnAllShop.setStyleSheet(" border-top-left-radius:0px;\n"
"    border-top-right-radius:0px;")
        self.btnAllShop.setObjectName("btnAllShop")
        self.btnInf = QtWidgets.QToolButton(self.widgetBtn)
        self.btnInf.setGeometry(QtCore.QRect(0, 100, 150, 50))
        self.btnInf.setObjectName("btnInf")
        self.btnContract = QtWidgets.QToolButton(self.widgetBtn)
        self.btnContract.setGeometry(QtCore.QRect(0, 150, 150, 50))
        self.btnContract.setObjectName("btnContract")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setGeometry(QtCore.QRect(150, 30, 851, 571))
        self.stackedWidget.setStyleSheet("QWidget{\n"
"    background:rgb(243,244,248);\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.AllShop = QtWidgets.QWidget()
        self.AllShop.setObjectName("AllShop")
        self.allShop = QtWidgets.QLabel(self.AllShop)
        self.allShop.setGeometry(QtCore.QRect(15, 15, 91, 30))
        self.allShop.setStyleSheet("font-size:22px")
        self.allShop.setObjectName("allShop")
        self.stackedWidgetShop = QtWidgets.QStackedWidget(self.AllShop)
        self.stackedWidgetShop.setGeometry(QtCore.QRect(0, 70, 851, 530))
        self.stackedWidgetShop.setStyleSheet("\n"
"#_1f\n"
"{\n"
"    background:rgb(226, 232, 255);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"\n"
"#_2f\n"
"{\n"
"    background:rgb(226, 232, 255);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"")
        self.stackedWidgetShop.setObjectName("stackedWidgetShop")
        self._1f = QtWidgets.QWidget()
        self._1f.setObjectName("_1f")
        self.firstFloorShop = QtWidgets.QWidget(self._1f)
        self.firstFloorShop.setGeometry(QtCore.QRect(20, 20, 401, 471))
        self.firstFloorShop.setStyleSheet("#firstFloorShop\n"
"{\n"
"        background:white;\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
" border-bottom-left-radius:10px;\n"
"    border-bottom-right-radius:10px;\n"
"}\n"
"")
        self.firstFloorShop.setObjectName("firstFloorShop")
        self.firstFloorInf = QtWidgets.QWidget(self.firstFloorShop)
        self.firstFloorInf.setGeometry(QtCore.QRect(0, 0, 401, 40))
        self.firstFloorInf.setStyleSheet("QWidget\n"
"{\n"
"    background:rgb(165, 200, 255);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"")
        self.firstFloorInf.setObjectName("firstFloorInf")
        self.widget_2 = QtWidgets.QWidget(self.firstFloorShop)
        self.widget_2.setGeometry(QtCore.QRect(10, 60, 150, 400))
        self.widget_2.setStyleSheet("background: rgb(255, 255, 255);")
        self.widget_2.setObjectName("widget_2")
        self.pushButtonShop_12 = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonShop_12.setGeometry(QtCore.QRect(95, 9, 45, 380))
        self.pushButtonShop_12.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_12.setObjectName("pushButtonShop_12")
        self.pushButtonShop_11 = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonShop_11.setGeometry(QtCore.QRect(10, 220, 70, 170))
        self.pushButtonShop_11.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_11.setObjectName("pushButtonShop_11")
        self.pushButtonShop_01 = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonShop_01.setGeometry(QtCore.QRect(10, 10, 70, 70))
        self.pushButtonShop_01.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_01.setObjectName("pushButtonShop_01")
        self.pushButtonShop_04 = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonShop_04.setGeometry(QtCore.QRect(10, 90, 70, 45))
        self.pushButtonShop_04.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_04.setObjectName("pushButtonShop_04")
        self.pushButtonShop_08 = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonShop_08.setGeometry(QtCore.QRect(10, 150, 70, 41))
        self.pushButtonShop_08.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_08.setObjectName("pushButtonShop_08")
        self.widget_3 = QtWidgets.QWidget(self.firstFloorShop)
        self.widget_3.setGeometry(QtCore.QRect(160, 329, 230, 131))
        self.widget_3.setStyleSheet("background: rgb(255, 255, 255);")
        self.widget_3.setObjectName("widget_3")
        self.pushButtonShop_09 = QtWidgets.QPushButton(self.widget_3)
        self.pushButtonShop_09.setGeometry(QtCore.QRect(10, 10, 210, 40))
        self.pushButtonShop_09.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(60,192,192);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_09.setObjectName("pushButtonShop_09")
        self.pushButtonShop_10 = QtWidgets.QPushButton(self.widget_3)
        self.pushButtonShop_10.setGeometry(QtCore.QRect(10, 80, 210, 40))
        self.pushButtonShop_10.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_10.setObjectName("pushButtonShop_10")
        self.widget_4 = QtWidgets.QWidget(self.firstFloorShop)
        self.widget_4.setGeometry(QtCore.QRect(160, 60, 231, 141))
        self.widget_4.setStyleSheet("background: rgb(255, 255, 255);")
        self.widget_4.setObjectName("widget_4")
        self.pushButtonShop_02 = QtWidgets.QPushButton(self.widget_4)
        self.pushButtonShop_02.setGeometry(QtCore.QRect(5, 10, 91, 41))
        self.pushButtonShop_02.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(60,192,192);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_02.setObjectName("pushButtonShop_02")
        self.pushButtonShop_06 = QtWidgets.QPushButton(self.widget_4)
        self.pushButtonShop_06.setGeometry(QtCore.QRect(75, 85, 81, 40))
        self.pushButtonShop_06.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_06.setObjectName("pushButtonShop_06")
        self.pushButtonShop_03 = QtWidgets.QPushButton(self.widget_4)
        self.pushButtonShop_03.setGeometry(QtCore.QRect(100, 10, 125, 40))
        self.pushButtonShop_03.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(60,192,192);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_03.setObjectName("pushButtonShop_03")
        self.pushButtonShop_05 = QtWidgets.QPushButton(self.widget_4)
        self.pushButtonShop_05.setGeometry(QtCore.QRect(10, 85, 61, 40))
        self.pushButtonShop_05.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_05.setObjectName("pushButtonShop_05")
        self.pushButtonShop_07 = QtWidgets.QPushButton(self.widget_4)
        self.pushButtonShop_07.setGeometry(QtCore.QRect(160, 85, 65, 40))
        self.pushButtonShop_07.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_07.setObjectName("pushButtonShop_07")
        self.widget_17 = QtWidgets.QWidget(self.widget_4)
        self.widget_17.setGeometry(QtCore.QRect(0, 130, 221, 151))
        self.widget_17.setObjectName("widget_17")
        self.stackedWidgetShop.addWidget(self._1f)
        self._2f = QtWidgets.QWidget()
        self._2f.setObjectName("_2f")
        self.secondFloorShop = QtWidgets.QWidget(self._2f)
        self.secondFloorShop.setGeometry(QtCore.QRect(20, 20, 401, 471))
        self.secondFloorShop.setStyleSheet("#secondFloorShop\n"
"{\n"
"    background:white;\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"")
        self.secondFloorShop.setObjectName("secondFloorShop")
        self.widget_5 = QtWidgets.QWidget(self.secondFloorShop)
        self.widget_5.setGeometry(QtCore.QRect(0, 0, 401, 41))
        self.widget_5.setStyleSheet("QWidget\n"
"{\n"
"    background:rgb(165, 200, 255);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"")
        self.widget_5.setObjectName("widget_5")
        self.widget_6 = QtWidgets.QWidget(self.secondFloorShop)
        self.widget_6.setGeometry(QtCore.QRect(10, 60, 150, 400))
        self.widget_6.setStyleSheet("background: rgb(255, 255, 255);\n"
"\n"
"border-radius:5px;")
        self.widget_6.setObjectName("widget_6")
        self.pushButtonShop_13 = QtWidgets.QPushButton(self.widget_6)
        self.pushButtonShop_13.setGeometry(QtCore.QRect(95, 9, 45, 381))
        self.pushButtonShop_13.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_13.setObjectName("pushButtonShop_13")
        self.pushButtonShop_14 = QtWidgets.QPushButton(self.widget_6)
        self.pushButtonShop_14.setGeometry(QtCore.QRect(10, 220, 70, 171))
        self.pushButtonShop_14.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_14.setObjectName("pushButtonShop_14")
        self.pushButtonShop_2 = QtWidgets.QPushButton(self.widget_6)
        self.pushButtonShop_2.setGeometry(QtCore.QRect(10, 10, 70, 70))
        self.pushButtonShop_2.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_2.setObjectName("pushButtonShop_2")
        self.pushButtonShop_5 = QtWidgets.QPushButton(self.widget_6)
        self.pushButtonShop_5.setGeometry(QtCore.QRect(10, 90, 70, 45))
        self.pushButtonShop_5.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_5.setObjectName("pushButtonShop_5")
        self.pushButtonShop_9 = QtWidgets.QPushButton(self.widget_6)
        self.pushButtonShop_9.setGeometry(QtCore.QRect(10, 150, 70, 41))
        self.pushButtonShop_9.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_9.setObjectName("pushButtonShop_9")
        self.widget_7 = QtWidgets.QWidget(self.secondFloorShop)
        self.widget_7.setGeometry(QtCore.QRect(160, 329, 231, 130))
        self.widget_7.setStyleSheet("background: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.widget_7.setObjectName("widget_7")
        self.pushButtonShop_15 = QtWidgets.QPushButton(self.widget_7)
        self.pushButtonShop_15.setGeometry(QtCore.QRect(10, 10, 210, 40))
        self.pushButtonShop_15.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(60,192,192);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_15.setObjectName("pushButtonShop_15")
        self.pushButtonShop_16 = QtWidgets.QPushButton(self.widget_7)
        self.pushButtonShop_16.setGeometry(QtCore.QRect(10, 80, 210, 40))
        self.pushButtonShop_16.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_16.setObjectName("pushButtonShop_16")
        self.widget_8 = QtWidgets.QWidget(self.secondFloorShop)
        self.widget_8.setGeometry(QtCore.QRect(160, 60, 231, 141))
        self.widget_8.setStyleSheet("background: rgb(255, 255, 255);\n"
"\n"
"border-radius:5px;")
        self.widget_8.setObjectName("widget_8")
        self.pushButtonShop_3 = QtWidgets.QPushButton(self.widget_8)
        self.pushButtonShop_3.setGeometry(QtCore.QRect(5, 10, 91, 41))
        self.pushButtonShop_3.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(60,192,192);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_3.setObjectName("pushButtonShop_3")
        self.pushButtonShop_7 = QtWidgets.QPushButton(self.widget_8)
        self.pushButtonShop_7.setGeometry(QtCore.QRect(75, 85, 81, 40))
        self.pushButtonShop_7.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_7.setObjectName("pushButtonShop_7")
        self.pushButtonShop_4 = QtWidgets.QPushButton(self.widget_8)
        self.pushButtonShop_4.setGeometry(QtCore.QRect(100, 10, 125, 40))
        self.pushButtonShop_4.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(60,192,192);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_4.setObjectName("pushButtonShop_4")
        self.pushButtonShop_6 = QtWidgets.QPushButton(self.widget_8)
        self.pushButtonShop_6.setGeometry(QtCore.QRect(10, 85, 61, 40))
        self.pushButtonShop_6.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_6.setObjectName("pushButtonShop_6")
        self.pushButtonShop_8 = QtWidgets.QPushButton(self.widget_8)
        self.pushButtonShop_8.setGeometry(QtCore.QRect(160, 85, 65, 40))
        self.pushButtonShop_8.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_8.setObjectName("pushButtonShop_8")
        self.stackedWidgetShop.addWidget(self._2f)
        self.contractInf = QtWidgets.QWidget(self.AllShop)
        self.contractInf.setGeometry(QtCore.QRect(440, 250, 380, 311))
        self.contractInf.setStyleSheet("#contractInf\n"
"\n"
"{\n"
"        background:white;\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
" border-bottom-left-radius:10px;\n"
"    border-bottom-right-radius:10px;\n"
"}\n"
"QLineEdit\n"
"{\n"
"  background:transparent;\n"
"    padding-left:5px ;\n"
"    padding-top:1px ;\n"
"    border-bottom-left-radius:6px;\n"
"    border-bottom-right-radius:6px;\n"
"    border: 1px solid rgb(123 ,123 , 123);\n"
"}\n"
"\n"
"")
        self.contractInf.setObjectName("contractInf")
        self.widget_13 = QtWidgets.QWidget(self.contractInf)
        self.widget_13.setGeometry(QtCore.QRect(0, 0, 380, 40))
        self.widget_13.setStyleSheet("QWidget\n"
"{\n"
"    background:rgb(165, 200, 255);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"")
        self.widget_13.setObjectName("widget_13")
        self.label_15 = QtWidgets.QLabel(self.widget_13)
        self.label_15.setGeometry(QtCore.QRect(15, 15, 101, 20))
        self.label_15.setStyleSheet("font-size:22px")
        self.label_15.setObjectName("label_15")
        self.label_3 = QtWidgets.QLabel(self.contractInf)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 60, 20))
        self.label_3.setStyleSheet("background:transparent;\n"
"font-size:14px")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.contractInf)
        self.label_5.setGeometry(QtCore.QRect(30, 120, 70, 20))
        self.label_5.setStyleSheet("background:transparent;\n"
"font-size:14px")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.contractInf)
        self.label_6.setGeometry(QtCore.QRect(30, 180, 70, 20))
        self.label_6.setStyleSheet("background:transparent;\n"
"font-size:14px")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.contractInf)
        self.label_8.setGeometry(QtCore.QRect(30, 210, 80, 20))
        self.label_8.setStyleSheet("background:transparent;\n"
"font-size:14px")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.contractInf)
        self.label_9.setGeometry(QtCore.QRect(30, 240, 70, 20))
        self.label_9.setStyleSheet("background:transparent;\n"
"font-size:14px")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.contractInf)
        self.label_10.setGeometry(QtCore.QRect(30, 150, 120, 20))
        self.label_10.setStyleSheet("background:transparent;\n"
"font-size:14px")
        self.label_10.setObjectName("label_10")
        self.label_18 = QtWidgets.QLabel(self.contractInf)
        self.label_18.setGeometry(QtCore.QRect(30, 60, 70, 20))
        self.label_18.setStyleSheet("background:transparent;\n"
"font-size:14px")
        self.label_18.setObjectName("label_18")
        self.ceoConfirm = QtWidgets.QCheckBox(self.contractInf)
        self.ceoConfirm.setGeometry(QtCore.QRect(150, 150, 71, 16))
        self.ceoConfirm.setStyleSheet("background:transparent;")
        self.ceoConfirm.setCheckable(False)
        self.ceoConfirm.setObjectName("ceoConfirm")
        self.userSignature = QtWidgets.QCheckBox(self.contractInf)
        self.userSignature.setGeometry(QtCore.QRect(110, 180, 71, 16))
        self.userSignature.setStyleSheet("background:transparent;")
        self.userSignature.setCheckable(False)
        self.userSignature.setObjectName("userSignature")
        self.ceoSingature = QtWidgets.QCheckBox(self.contractInf)
        self.ceoSingature.setGeometry(QtCore.QRect(120, 210, 71, 16))
        self.ceoSingature.setStyleSheet("background:transparent;")
        self.ceoSingature.setCheckable(False)
        self.ceoSingature.setObjectName("ceoSingature")
        self.rentTimeContract = QtWidgets.QLineEdit(self.contractInf)
        self.rentTimeContract.setGeometry(QtCore.QRect(110, 120, 113, 20))
        self.rentTimeContract.setReadOnly(True)
        self.rentTimeContract.setObjectName("rentTimeContract")
        self.RentStateContract = QtWidgets.QLineEdit(self.contractInf)
        self.RentStateContract.setGeometry(QtCore.QRect(80, 90, 113, 20))
        self.RentStateContract.setReadOnly(True)
        self.RentStateContract.setObjectName("RentStateContract")
        self.shopNumberContract = QtWidgets.QLineEdit(self.contractInf)
        self.shopNumberContract.setGeometry(QtCore.QRect(100, 60, 113, 20))
        self.shopNumberContract.setReadOnly(True)
        self.shopNumberContract.setObjectName("shopNumberContract")
        self.contractInfomation = QtWidgets.QTextEdit(self.contractInf)
        self.contractInfomation.setGeometry(QtCore.QRect(120, 230, 231, 71))
        self.contractInfomation.setStyleSheet("QTextEdit\n"
"{\n"
" background:transparent;\n"
"    padding-left:5px ;\n"
"    padding-top:1px ;\n"
"    border-bottom-left-radius:9px;\n"
"    border-bottom-right-radius:9px;\n"
"    border: 1px solid rgb(123 ,123 , 123);\n"
"}")
        self.contractInfomation.setReadOnly(True)
        self.contractInfomation.setObjectName("contractInfomation")
        self.shopInfomation = QtWidgets.QWidget(self.AllShop)
        self.shopInfomation.setGeometry(QtCore.QRect(440, 90, 380, 151))
        self.shopInfomation.setStyleSheet("#shopInfomation\n"
"{\n"
"        background:white;\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
" border-bottom-left-radius:10px;\n"
"    border-bottom-right-radius:10px;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"  background:transparent;\n"
"    padding-left:5px ;\n"
"    padding-top:1px ;\n"
"    border-bottom-left-radius:6px;\n"
"    border-bottom-right-radius:6px;\n"
"    border: 1px solid rgb(123 ,123 , 123);\n"
"}\n"
"")
        self.shopInfomation.setObjectName("shopInfomation")
        self.widget_12 = QtWidgets.QWidget(self.shopInfomation)
        self.widget_12.setGeometry(QtCore.QRect(0, 0, 380, 41))
        self.widget_12.setStyleSheet("QWidget\n"
"{\n"
"\n"
"    background:rgb(165, 200, 255);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"")
        self.widget_12.setObjectName("widget_12")
        self.label_14 = QtWidgets.QLabel(self.widget_12)
        self.label_14.setGeometry(QtCore.QRect(15, 15, 101, 20))
        self.label_14.setStyleSheet("font-size:22px")
        self.label_14.setObjectName("label_14")
        self.label_19 = QtWidgets.QLabel(self.shopInfomation)
        self.label_19.setGeometry(QtCore.QRect(15, 60, 60, 20))
        self.label_19.setStyleSheet("background:transparent;\n"
"font-size:14px")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.shopInfomation)
        self.label_20.setGeometry(QtCore.QRect(15, 80, 60, 20))
        self.label_20.setStyleSheet("background:transparent;\n"
"font-size:14px")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.shopInfomation)
        self.label_21.setGeometry(QtCore.QRect(15, 100, 75, 20))
        self.label_21.setStyleSheet("background:transparent;\n"
"font-size:14px")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.shopInfomation)
        self.label_22.setGeometry(QtCore.QRect(15, 120, 75, 20))
        self.label_22.setStyleSheet("background:transparent;\n"
"font-size:14px")
        self.label_22.setObjectName("label_22")
        self.oweWaterFee = QtWidgets.QCheckBox(self.shopInfomation)
        self.oweWaterFee.setGeometry(QtCore.QRect(180, 60, 50, 20))
        self.oweWaterFee.setStyleSheet("background:transparent;\n"
"font-size:14px")
        self.oweWaterFee.setCheckable(False)
        self.oweWaterFee.setChecked(False)
        self.oweWaterFee.setObjectName("oweWaterFee")
        self.checkBox_8 = QtWidgets.QCheckBox(self.shopInfomation)
        self.checkBox_8.setGeometry(QtCore.QRect(180, 80, 50, 20))
        self.checkBox_8.setStyleSheet("background:transparent;\n"
"font-size:14px")
        self.checkBox_8.setCheckable(False)
        self.checkBox_8.setObjectName("checkBox_8")
        self.owePropertyFee = QtWidgets.QCheckBox(self.shopInfomation)
        self.owePropertyFee.setGeometry(QtCore.QRect(180, 100, 50, 20))
        self.owePropertyFee.setStyleSheet("background:transparent;\n"
"font-size:14px")
        self.owePropertyFee.setCheckable(False)
        self.owePropertyFee.setObjectName("owePropertyFee")
        self.oweGuaranteePaid = QtWidgets.QCheckBox(self.shopInfomation)
        self.oweGuaranteePaid.setGeometry(QtCore.QRect(180, 120, 50, 20))
        self.oweGuaranteePaid.setStyleSheet("background:transparent;\n"
"font-size:14px")
        self.oweGuaranteePaid.setCheckable(False)
        self.oweGuaranteePaid.setObjectName("oweGuaranteePaid")
        self.waterFeePaid = QtWidgets.QLineEdit(self.shopInfomation)
        self.waterFeePaid.setGeometry(QtCore.QRect(100, 60, 70, 20))
        self.waterFeePaid.setReadOnly(True)
        self.waterFeePaid.setObjectName("waterFeePaid")
        self.electricFeePaid = QtWidgets.QLineEdit(self.shopInfomation)
        self.electricFeePaid.setGeometry(QtCore.QRect(100, 80, 70, 20))
        self.electricFeePaid.setReadOnly(True)
        self.electricFeePaid.setObjectName("electricFeePaid")
        self.propertyFee = QtWidgets.QLineEdit(self.shopInfomation)
        self.propertyFee.setGeometry(QtCore.QRect(100, 100, 70, 20))
        self.propertyFee.setReadOnly(True)
        self.propertyFee.setObjectName("propertyFee")
        self.guaranteePaid = QtWidgets.QLineEdit(self.shopInfomation)
        self.guaranteePaid.setGeometry(QtCore.QRect(100, 120, 70, 20))
        self.guaranteePaid.setReadOnly(True)
        self.guaranteePaid.setObjectName("guaranteePaid")
        self.curFloor = QtWidgets.QLabel(self.AllShop)
        self.curFloor.setGeometry(QtCore.QRect(320, 350, 54, 12))
        self.curFloor.setStyleSheet("font-size:18px;\n"
"background:transparent;")
        self.curFloor.setObjectName("curFloor")
        self.label_7 = QtWidgets.QLabel(self.AllShop)
        self.label_7.setGeometry(QtCore.QRect(40, 100, 100, 30))
        self.label_7.setStyleSheet("font-size:22px;\n"
"background:transparent;")
        self.label_7.setObjectName("label_7")
        self.pushButton_15 = QtWidgets.QPushButton(self.AllShop)
        self.pushButton_15.setGeometry(QtCore.QRect(150, 105, 20, 20))
        self.pushButton_15.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}")
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_13 = QtWidgets.QLabel(self.AllShop)
        self.label_13.setGeometry(QtCore.QRect(310, 105, 50, 20))
        self.label_13.setStyleSheet("font-size:15px;\n"
"background:transparent;")
        self.label_13.setObjectName("label_13")
        self.label_2 = QtWidgets.QLabel(self.AllShop)
        self.label_2.setGeometry(QtCore.QRect(170, 105, 61, 20))
        self.label_2.setStyleSheet("background:transparent;")
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.AllShop)
        self.comboBox.setGeometry(QtCore.QRect(350, 100, 60, 25))
        self.comboBox.setObjectName("comboBox")
        self.label_4 = QtWidgets.QLabel(self.AllShop)
        self.label_4.setGeometry(QtCore.QRect(250, 105, 61, 20))
        self.label_4.setStyleSheet("background:transparent;")
        self.label_4.setObjectName("label_4")
        self.pushButton_13 = QtWidgets.QPushButton(self.AllShop)
        self.pushButton_13.setGeometry(QtCore.QRect(230, 105, 20, 20))
        self.pushButton_13.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(60,192,192);\n"
"border-radius:10px;\n"
"}")
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_11 = QtWidgets.QLabel(self.AllShop)
        self.label_11.setGeometry(QtCore.QRect(230, 340, 91, 31))
        self.label_11.setStyleSheet("font-size:18px;\n"
"background:transparent;")
        self.label_11.setObjectName("label_11")
        self.stackedWidget.addWidget(self.AllShop)
        self.MyShop = QtWidgets.QWidget()
        self.MyShop.setObjectName("MyShop")
        self.myShop = QtWidgets.QLabel(self.MyShop)
        self.myShop.setGeometry(QtCore.QRect(15, 15, 101, 31))
        self.myShop.setStyleSheet("font-size:22px")
        self.myShop.setObjectName("myShop")
        self.widget_10 = QtWidgets.QWidget(self.MyShop)
        self.widget_10.setGeometry(QtCore.QRect(0, 70, 850, 500))
        self.widget_10.setStyleSheet("\n"
"\n"
"#widget_10\n"
"{    background:rgb(226, 232, 255);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}")
        self.widget_10.setObjectName("widget_10")
        self.widget_9 = QtWidgets.QWidget(self.widget_10)
        self.widget_9.setGeometry(QtCore.QRect(20, 20, 250, 200))
        self.widget_9.setStyleSheet("QLabel\n"
"{\n"
"  background:transparent;\n"
"font-size:16px;\n"
"}\n"
"\n"
"#widget_9\n"
"{\n"
"            background:white;\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
" border-bottom-left-radius:10px;\n"
"    border-bottom-right-radius:10px;\n"
"}\n"
"")
        self.widget_9.setObjectName("widget_9")
        self.label_34 = QtWidgets.QLabel(self.widget_9)
        self.label_34.setGeometry(QtCore.QRect(40, 90, 110, 20))
        self.label_34.setStyleSheet("")
        self.label_34.setObjectName("label_34")
        self.pendingApplicationNum = QtWidgets.QLabel(self.widget_9)
        self.pendingApplicationNum.setGeometry(QtCore.QRect(150, 90, 80, 20))
        self.pendingApplicationNum.setStyleSheet("")
        self.pendingApplicationNum.setObjectName("pendingApplicationNum")
        self.label_36 = QtWidgets.QLabel(self.widget_9)
        self.label_36.setGeometry(QtCore.QRect(40, 130, 80, 20))
        self.label_36.setObjectName("label_36")
        self.pendingApplication = QtWidgets.QComboBox(self.widget_9)
        self.pendingApplication.setGeometry(QtCore.QRect(120, 130, 80, 20))
        self.pendingApplication.setObjectName("pendingApplication")
        self.widget_14 = QtWidgets.QWidget(self.widget_9)
        self.widget_14.setGeometry(QtCore.QRect(0, 0, 251, 40))
        self.widget_14.setStyleSheet("QWidget\n"
"{\n"
"\n"
"    background:rgb(165, 200, 255);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"")
        self.widget_14.setObjectName("widget_14")
        self.label_37 = QtWidgets.QLabel(self.widget_14)
        self.label_37.setGeometry(QtCore.QRect(15, 15, 151, 20))
        self.label_37.setStyleSheet("font-size:20px")
        self.label_37.setObjectName("label_37")
        self.widget = QtWidgets.QWidget(self.widget_10)
        self.widget.setGeometry(QtCore.QRect(300, 20, 540, 461))
        self.widget.setStyleSheet("QLabel\n"
"{\n"
"  background:transparent;\n"
"font-size:18px;\n"
"\n"
"}\n"
"QLineEdit\n"
"{\n"
"  background:transparent;\n"
"    padding-left:5px ;\n"
"    padding-top:1px ;\n"
"    border-bottom-left-radius:6px;\n"
"    border-bottom-right-radius:6px;\n"
"    border: 1px solid rgb(123 ,123 , 123);\n"
"}\n"
"\n"
"\n"
"#widget\n"
"{\n"
"        background:white;\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
" border-bottom-left-radius:10px;\n"
"    border-bottom-right-radius:10px;\n"
"}\n"
"")
        self.widget.setObjectName("widget")
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setGeometry(QtCore.QRect(310, 60, 100, 20))
        self.label_17.setObjectName("label_17")
        self.label_23 = QtWidgets.QLabel(self.widget)
        self.label_23.setGeometry(QtCore.QRect(30, 90, 100, 20))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.widget)
        self.label_24.setGeometry(QtCore.QRect(310, 90, 100, 20))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.widget)
        self.label_25.setGeometry(QtCore.QRect(30, 120, 91, 20))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.widget)
        self.label_26.setGeometry(QtCore.QRect(30, 60, 91, 20))
        self.label_26.setObjectName("label_26")
        self.approvingEntry = QtWidgets.QPushButton(self.widget)
        self.approvingEntry.setGeometry(QtCore.QRect(360, 430, 75, 23))
        self.approvingEntry.setStyleSheet("QPushButton\n"
"{\n"
" border-radius:5px;font-size:16px;background:rgb(200, 222,255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background:rgb(142, 182, 255)\n"
"}")
        self.approvingEntry.setObjectName("approvingEntry")
        self.refuseEntry = QtWidgets.QPushButton(self.widget)
        self.refuseEntry.setGeometry(QtCore.QRect(450, 430, 75, 23))
        self.refuseEntry.setStyleSheet("QPushButton\n"
"{\n"
" border-radius:5px;font-size:16px;background:rgb(200, 222,255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background:rgb(142, 182, 255)\n"
"}")
        self.refuseEntry.setObjectName("refuseEntry")
        self.rentReason = QtWidgets.QTextEdit(self.widget)
        self.rentReason.setGeometry(QtCore.QRect(30, 150, 491, 271))
        self.rentReason.setStyleSheet("QTextEdit\n"
"{\n"
" background:transparent;\n"
"    padding-left:5px ;\n"
"    padding-top:1px ;\n"
"    border-bottom-left-radius:9px;\n"
"    border-bottom-right-radius:9px;\n"
"    border: 1px solid rgb(123 ,123 , 123);\n"
"}")
        self.rentReason.setReadOnly(True)
        self.rentReason.setObjectName("rentReason")
        self.rentTime = QtWidgets.QLineEdit(self.widget)
        self.rentTime.setGeometry(QtCore.QRect(400, 90, 113, 20))
        self.rentTime.setObjectName("rentTime")
        self.userTel = QtWidgets.QLineEdit(self.widget)
        self.userTel.setGeometry(QtCore.QRect(120, 90, 113, 20))
        self.userTel.setObjectName("userTel")
        self.userName = QtWidgets.QLineEdit(self.widget)
        self.userName.setGeometry(QtCore.QRect(370, 60, 113, 20))
        self.userName.setObjectName("userName")
        self.intentionShopNum = QtWidgets.QLineEdit(self.widget)
        self.intentionShopNum.setGeometry(QtCore.QRect(120, 60, 113, 20))
        self.intentionShopNum.setObjectName("intentionShopNum")
        self.widget_11 = QtWidgets.QWidget(self.widget)
        self.widget_11.setGeometry(QtCore.QRect(0, 0, 541, 40))
        self.widget_11.setStyleSheet("QWidget\n"
"{\n"
"    background:rgb(165, 200, 255);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"")
        self.widget_11.setObjectName("widget_11")
        self.label_30 = QtWidgets.QLabel(self.widget_11)
        self.label_30.setGeometry(QtCore.QRect(15, 15, 141, 20))
        self.label_30.setStyleSheet("font-size:20px;")
        self.label_30.setObjectName("label_30")
        self.stackedWidget.addWidget(self.MyShop)
        self.ApprochHandling = QtWidgets.QWidget()
        self.ApprochHandling.setObjectName("ApprochHandling")
        self.myInformation = QtWidgets.QLabel(self.ApprochHandling)
        self.myInformation.setGeometry(QtCore.QRect(15, 15, 90, 30))
        self.myInformation.setStyleSheet("font-size:22px")
        self.myInformation.setObjectName("myInformation")
        self.widget_15 = QtWidgets.QWidget(self.ApprochHandling)
        self.widget_15.setGeometry(QtCore.QRect(0, 70, 851, 501))
        self.widget_15.setStyleSheet("\n"
"\n"
"#widget_15\n"
"{    background:rgb(226, 232, 255);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}")
        self.widget_15.setObjectName("widget_15")
        self.leaseContract = QtWidgets.QWidget(self.widget_15)
        self.leaseContract.setGeometry(QtCore.QRect(20, 20, 800, 471))
        self.leaseContract.setStyleSheet("#leaseContract\n"
"{\n"
"    background:white;\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"\n"
"\n"
"QLabel\n"
"{\n"
"  background:transparent;\n"
"font-size:18px;\n"
"\n"
"}\n"
"QLineEdit\n"
"{\n"
"  background:transparent;\n"
"    padding-left:5px ;\n"
"    padding-top:1px ;\n"
"    border-bottom-left-radius:6px;\n"
"    border-bottom-right-radius:6px;\n"
"    border: 1px solid rgb(123 ,123 , 123);\n"
"}")
        self.leaseContract.setObjectName("leaseContract")
        self.label_28 = QtWidgets.QLabel(self.leaseContract)
        self.label_28.setGeometry(QtCore.QRect(20, 55, 80, 20))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.leaseContract)
        self.label_29.setGeometry(QtCore.QRect(460, 440, 80, 20))
        self.label_29.setObjectName("label_29")
        self.contractInformation = QtWidgets.QTextEdit(self.leaseContract)
        self.contractInformation.setGeometry(QtCore.QRect(30, 80, 750, 350))
        self.contractInformation.setStyleSheet("QTextEdit\n"
"{\n"
" background:transparent;\n"
"    padding-left:5px ;\n"
"    padding-top:1px ;\n"
"    border-bottom-left-radius:9px;\n"
"    border-bottom-right-radius:9px;\n"
"    border: 1px solid rgb(123 ,123 , 123);\n"
"}")
        self.contractInformation.setObjectName("contractInformation")
        self.rentTimeManager = QtWidgets.QLineEdit(self.leaseContract)
        self.rentTimeManager.setGeometry(QtCore.QRect(550, 440, 113, 20))
        self.rentTimeManager.setReadOnly(True)
        self.rentTimeManager.setObjectName("rentTimeManager")
        self.submitAudit = QtWidgets.QPushButton(self.leaseContract)
        self.submitAudit.setGeometry(QtCore.QRect(680, 440, 101, 20))
        self.submitAudit.setStyleSheet("QPushButton\n"
"{\n"
" border-radius:5px;font-size:16px;background:rgb(200, 222,255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background:rgb(142, 182, 255)\n"
"}")
        self.submitAudit.setObjectName("submitAudit")
        self.label_35 = QtWidgets.QLabel(self.leaseContract)
        self.label_35.setGeometry(QtCore.QRect(40, 440, 54, 20))
        self.label_35.setObjectName("label_35")
        self.shopNum = QtWidgets.QLineEdit(self.leaseContract)
        self.shopNum.setGeometry(QtCore.QRect(100, 440, 80, 20))
        self.shopNum.setReadOnly(True)
        self.shopNum.setObjectName("shopNum")
        self.label_39 = QtWidgets.QLabel(self.leaseContract)
        self.label_39.setGeometry(QtCore.QRect(200, 440, 110, 20))
        self.label_39.setObjectName("label_39")
        self.userTelContract = QtWidgets.QLineEdit(self.leaseContract)
        self.userTelContract.setGeometry(QtCore.QRect(320, 440, 120, 20))
        self.userTelContract.setReadOnly(True)
        self.userTelContract.setObjectName("userTelContract")
        self.widget_16 = QtWidgets.QWidget(self.leaseContract)
        self.widget_16.setGeometry(QtCore.QRect(0, 0, 801, 40))
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
        self.stackedWidget.addWidget(self.ApprochHandling)
        self.MyContract = QtWidgets.QWidget()
        self.MyContract.setObjectName("MyContract")
        self.myContract = QtWidgets.QLabel(self.MyContract)
        self.myContract.setGeometry(QtCore.QRect(15, 15, 91, 31))
        self.myContract.setStyleSheet("font: 15pt \"华文中宋\";")
        self.myContract.setObjectName("myContract")
        self.stackedWidget.addWidget(self.MyContract)
        self.label = QtWidgets.QLabel(ManagerWindow)
        self.label.setGeometry(QtCore.QRect(30, 20, 70, 30))
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 15pt \"华文中宋\";")
        self.label.setObjectName("label")

        self.retranslateUi(ManagerWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidgetShop.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ManagerWindow)

    def retranslateUi(self, ManagerWindow):
        _translate = QtCore.QCoreApplication.translate
        ManagerWindow.setWindowTitle(_translate("ManagerWindow", "Form"))
        self.btnApprochHandling.setText(_translate("ManagerWindow", "申请处理"))
        self.btnAllShop.setText(_translate("ManagerWindow", "全部店铺"))
        self.btnInf.setText(_translate("ManagerWindow", "拟定合同"))
        self.btnContract.setText(_translate("ManagerWindow", "待做功能"))
        self.allShop.setText(_translate("ManagerWindow", "全部店铺"))
        self.pushButtonShop_12.setText(_translate("ManagerWindow", "12"))
        self.pushButtonShop_11.setText(_translate("ManagerWindow", "11"))
        self.pushButtonShop_01.setText(_translate("ManagerWindow", "01"))
        self.pushButtonShop_04.setText(_translate("ManagerWindow", "04"))
        self.pushButtonShop_08.setText(_translate("ManagerWindow", "08"))
        self.pushButtonShop_09.setText(_translate("ManagerWindow", "09"))
        self.pushButtonShop_10.setText(_translate("ManagerWindow", "10"))
        self.pushButtonShop_02.setText(_translate("ManagerWindow", "02"))
        self.pushButtonShop_06.setText(_translate("ManagerWindow", "06"))
        self.pushButtonShop_03.setText(_translate("ManagerWindow", "03"))
        self.pushButtonShop_05.setText(_translate("ManagerWindow", "05"))
        self.pushButtonShop_07.setText(_translate("ManagerWindow", "07"))
        self.pushButtonShop_13.setText(_translate("ManagerWindow", "18"))
        self.pushButtonShop_14.setText(_translate("ManagerWindow", "14"))
        self.pushButtonShop_2.setText(_translate("ManagerWindow", "17"))
        self.pushButtonShop_5.setText(_translate("ManagerWindow", "21"))
        self.pushButtonShop_9.setText(_translate("ManagerWindow", "13"))
        self.pushButtonShop_15.setText(_translate("ManagerWindow", "24"))
        self.pushButtonShop_16.setText(_translate("ManagerWindow", "16"))
        self.pushButtonShop_3.setText(_translate("ManagerWindow", "19"))
        self.pushButtonShop_7.setText(_translate("ManagerWindow", "23"))
        self.pushButtonShop_4.setText(_translate("ManagerWindow", "20"))
        self.pushButtonShop_6.setText(_translate("ManagerWindow", "22"))
        self.pushButtonShop_8.setText(_translate("ManagerWindow", "15"))
        self.label_15.setText(_translate("ManagerWindow", "合同信息"))
        self.label_3.setText(_translate("ManagerWindow", "状态："))
        self.label_5.setText(_translate("ManagerWindow", "签订时长："))
        self.label_6.setText(_translate("ManagerWindow", "业主签字;"))
        self.label_8.setText(_translate("ManagerWindow", "总经理签字："))
        self.label_9.setText(_translate("ManagerWindow", "合同事项："))
        self.label_10.setText(_translate("ManagerWindow", "总经理确认情况："))
        self.label_18.setText(_translate("ManagerWindow", "店铺编号："))
        self.ceoConfirm.setText(_translate("ManagerWindow", "已确认"))
        self.userSignature.setText(_translate("ManagerWindow", "已签字"))
        self.ceoSingature.setText(_translate("ManagerWindow", "已签字"))
        self.label_14.setText(_translate("ManagerWindow", "店铺信息"))
        self.label_19.setText(_translate("ManagerWindow", "已缴水费："))
        self.label_20.setText(_translate("ManagerWindow", "已缴电费："))
        self.label_21.setText(_translate("ManagerWindow", "已缴物业费："))
        self.label_22.setText(_translate("ManagerWindow", "已缴保证金："))
        self.oweWaterFee.setText(_translate("ManagerWindow", "欠费"))
        self.checkBox_8.setText(_translate("ManagerWindow", "欠费"))
        self.owePropertyFee.setText(_translate("ManagerWindow", "欠费"))
        self.oweGuaranteePaid.setText(_translate("ManagerWindow", "欠费"))
        self.curFloor.setText(_translate("ManagerWindow", "1f"))
        self.label_7.setText(_translate("ManagerWindow", "楼层信息"))
        self.label_13.setText(_translate("ManagerWindow", "楼层："))
        self.label_2.setText(_translate("ManagerWindow", "已租店铺"))
        self.label_4.setText(_translate("ManagerWindow", "可租店铺"))
        self.label_11.setText(_translate("ManagerWindow", "当前楼层："))
        self.myShop.setText(_translate("ManagerWindow", "申请处理"))
        self.label_34.setText(_translate("ManagerWindow", "剩余申请数量："))
        self.pendingApplicationNum.setText(_translate("ManagerWindow", "TextLabel"))
        self.label_36.setText(_translate("ManagerWindow", "处理申请："))
        self.label_37.setText(_translate("ManagerWindow", "当月待处理申请"))
        self.label_17.setText(_translate("ManagerWindow", "姓名："))
        self.label_23.setText(_translate("ManagerWindow", "联系方式："))
        self.label_24.setText(_translate("ManagerWindow", "租借时间："))
        self.label_25.setText(_translate("ManagerWindow", "租借用途："))
        self.label_26.setText(_translate("ManagerWindow", "意向店铺："))
        self.approvingEntry.setText(_translate("ManagerWindow", "批准进场"))
        self.refuseEntry.setText(_translate("ManagerWindow", "拒接进场"))
        self.label_30.setText(_translate("ManagerWindow", "当前申请信息"))
        self.myInformation.setText(_translate("ManagerWindow", "合同内容"))
        self.label_28.setText(_translate("ManagerWindow", "合同内容:"))
        self.label_29.setText(_translate("ManagerWindow", "签订年份:"))
        self.submitAudit.setText(_translate("ManagerWindow", "提交审核"))
        self.label_35.setText(_translate("ManagerWindow", "店铺号："))
        self.label_39.setText(_translate("ManagerWindow", "业主联系方式："))
        self.label_31.setText(_translate("ManagerWindow", "租赁合同"))
        self.myContract.setText(_translate("ManagerWindow", "我的合同"))
        self.label.setText(_translate("ManagerWindow", "JOJO"))

