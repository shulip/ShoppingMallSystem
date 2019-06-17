# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_CEOWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CEOWindow(object):
    def setupUi(self, CEOWindow):
        CEOWindow.setObjectName("CEOWindow")
        CEOWindow.resize(1092, 730)
        CEOWindow.setStyleSheet("font: 10pt \"黑体\";")
        self.frame = QtWidgets.QFrame(CEOWindow)
        self.frame.setGeometry(QtCore.QRect(20, 20, 1000, 600))
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
        self.btnMyShop = QtWidgets.QToolButton(self.widgetBtn)
        self.btnMyShop.setGeometry(QtCore.QRect(0, 50, 150, 50))
        self.btnMyShop.setObjectName("btnMyShop")
        self.btnAllShop = QtWidgets.QToolButton(self.widgetBtn)
        self.btnAllShop.setGeometry(QtCore.QRect(0, 0, 150, 50))
        self.btnAllShop.setStyleSheet(" border-top-left-radius:0px;\n"
"    border-top-right-radius:0px;")
        self.btnAllShop.setObjectName("btnAllShop")
        self.btnInf = QtWidgets.QToolButton(self.widgetBtn)
        self.btnInf.setGeometry(QtCore.QRect(0, 100, 150, 50))
        self.btnInf.setObjectName("btnInf")
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
        self.stackedWidgetShop.setGeometry(QtCore.QRect(0, 70, 850, 500))
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
        self.firstFloorShop.setGeometry(QtCore.QRect(20, 20, 400, 470))
        self.firstFloorShop.setStyleSheet("#firstFloorShop\n"
"{\n"
"    background:white;\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"")
        self.firstFloorShop.setObjectName("firstFloorShop")
        self.firstFloorInf = QtWidgets.QWidget(self.firstFloorShop)
        self.firstFloorInf.setGeometry(QtCore.QRect(0, 0, 400, 41))
        self.firstFloorInf.setStyleSheet("QWidget\n"
"{\n"
"    background:rgb(165, 200, 255);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"")
        self.firstFloorInf.setObjectName("firstFloorInf")
        self.widget_2 = QtWidgets.QWidget(self.firstFloorShop)
        self.widget_2.setGeometry(QtCore.QRect(10, 60, 151, 401))
        self.widget_2.setStyleSheet("background: rgb(255, 255, 255);")
        self.widget_2.setObjectName("widget_2")
        self.pushButtonShop_12 = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonShop_12.setGeometry(QtCore.QRect(95, 9, 45, 370))
        self.pushButtonShop_12.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButtonShop_12.setObjectName("pushButtonShop_12")
        self.pushButtonShop_11 = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonShop_11.setGeometry(QtCore.QRect(10, 210, 70, 170))
        self.pushButtonShop_11.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButtonShop_11.setObjectName("pushButtonShop_11")
        self.pushButtonShop_01 = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonShop_01.setGeometry(QtCore.QRect(10, 10, 70, 70))
        self.pushButtonShop_01.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButtonShop_01.setObjectName("pushButtonShop_01")
        self.pushButtonShop_04 = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonShop_04.setGeometry(QtCore.QRect(10, 90, 70, 45))
        self.pushButtonShop_04.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButtonShop_04.setObjectName("pushButtonShop_04")
        self.pushButtonShop_08 = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonShop_08.setGeometry(QtCore.QRect(10, 150, 70, 41))
        self.pushButtonShop_08.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButtonShop_08.setObjectName("pushButtonShop_08")
        self.widget_3 = QtWidgets.QWidget(self.firstFloorShop)
        self.widget_3.setGeometry(QtCore.QRect(160, 320, 231, 141))
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
        self.pushButtonShop_10.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
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
        self.pushButtonShop_06.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
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
        self.pushButtonShop_05.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButtonShop_05.setObjectName("pushButtonShop_05")
        self.pushButtonShop_07 = QtWidgets.QPushButton(self.widget_4)
        self.pushButtonShop_07.setGeometry(QtCore.QRect(160, 85, 65, 40))
        self.pushButtonShop_07.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButtonShop_07.setObjectName("pushButtonShop_07")
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
        self.widget_6.setGeometry(QtCore.QRect(10, 60, 151, 401))
        self.widget_6.setStyleSheet("background: rgb(255, 255, 255);")
        self.widget_6.setObjectName("widget_6")
        self.pushButtonShop_18 = QtWidgets.QPushButton(self.widget_6)
        self.pushButtonShop_18.setGeometry(QtCore.QRect(95, 9, 45, 371))
        self.pushButtonShop_18.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButtonShop_18.setObjectName("pushButtonShop_18")
        self.pushButtonShop_14 = QtWidgets.QPushButton(self.widget_6)
        self.pushButtonShop_14.setGeometry(QtCore.QRect(10, 210, 70, 171))
        self.pushButtonShop_14.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButtonShop_14.setObjectName("pushButtonShop_14")
        self.pushButtonShop_17 = QtWidgets.QPushButton(self.widget_6)
        self.pushButtonShop_17.setGeometry(QtCore.QRect(10, 10, 70, 70))
        self.pushButtonShop_17.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButtonShop_17.setObjectName("pushButtonShop_17")
        self.pushButtonShop_21 = QtWidgets.QPushButton(self.widget_6)
        self.pushButtonShop_21.setGeometry(QtCore.QRect(10, 90, 70, 45))
        self.pushButtonShop_21.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButtonShop_21.setObjectName("pushButtonShop_21")
        self.pushButtonShop_ = QtWidgets.QPushButton(self.widget_6)
        self.pushButtonShop_.setGeometry(QtCore.QRect(10, 150, 70, 41))
        self.pushButtonShop_.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButtonShop_.setObjectName("pushButtonShop_")
        self.widget_7 = QtWidgets.QWidget(self.secondFloorShop)
        self.widget_7.setGeometry(QtCore.QRect(160, 320, 231, 141))
        self.widget_7.setStyleSheet("background: rgb(255, 255, 255);")
        self.widget_7.setObjectName("widget_7")
        self.pushButtonShop_24 = QtWidgets.QPushButton(self.widget_7)
        self.pushButtonShop_24.setGeometry(QtCore.QRect(10, 10, 210, 40))
        self.pushButtonShop_24.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButtonShop_24.setObjectName("pushButtonShop_24")
        self.pushButtonShop_16 = QtWidgets.QPushButton(self.widget_7)
        self.pushButtonShop_16.setGeometry(QtCore.QRect(10, 80, 210, 40))
        self.pushButtonShop_16.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButtonShop_16.setObjectName("pushButtonShop_16")
        self.widget_8 = QtWidgets.QWidget(self.secondFloorShop)
        self.widget_8.setGeometry(QtCore.QRect(160, 60, 231, 141))
        self.widget_8.setStyleSheet("background: rgb(255, 255, 255);")
        self.widget_8.setObjectName("widget_8")
        self.pushButtonShop_19 = QtWidgets.QPushButton(self.widget_8)
        self.pushButtonShop_19.setGeometry(QtCore.QRect(5, 10, 91, 41))
        self.pushButtonShop_19.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(60,192,192);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_19.setObjectName("pushButtonShop_19")
        self.pushButtonShop_23 = QtWidgets.QPushButton(self.widget_8)
        self.pushButtonShop_23.setGeometry(QtCore.QRect(75, 85, 81, 40))
        self.pushButtonShop_23.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButtonShop_23.setObjectName("pushButtonShop_23")
        self.pushButtonShop_20 = QtWidgets.QPushButton(self.widget_8)
        self.pushButtonShop_20.setGeometry(QtCore.QRect(100, 10, 125, 40))
        self.pushButtonShop_20.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(60,192,192);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_20.setObjectName("pushButtonShop_20")
        self.pushButtonShop_22 = QtWidgets.QPushButton(self.widget_8)
        self.pushButtonShop_22.setGeometry(QtCore.QRect(10, 85, 61, 40))
        self.pushButtonShop_22.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButtonShop_22.setObjectName("pushButtonShop_22")
        self.pushButtonShop_15 = QtWidgets.QPushButton(self.widget_8)
        self.pushButtonShop_15.setGeometry(QtCore.QRect(160, 85, 65, 40))
        self.pushButtonShop_15.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButtonShop_15.setObjectName("pushButtonShop_15")
        self.stackedWidgetShop.addWidget(self._2f)
        self.contractInf = QtWidgets.QWidget(self.AllShop)
        self.contractInf.setGeometry(QtCore.QRect(440, 250, 380, 311))
        self.contractInf.setStyleSheet("#contractInf\n"
"{\n"
"        background:white;\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
" border-bottom-left-radius:10px;\n"
"    border-bottom-right-radius:10px;\n"
"\n"
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
        self.label_15.setGeometry(QtCore.QRect(20, 15, 101, 20))
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
        self.contractInfomation.setGeometry(QtCore.QRect(120, 230, 201, 71))
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
        self.shopInfomation.setStyleSheet("QLineEdit\n"
"{\n"
"  background:transparent;\n"
"    padding-left:5px ;\n"
"    padding-top:1px ;\n"
"    border-bottom-left-radius:6px;\n"
"    border-bottom-right-radius:6px;\n"
"    border: 1px solid rgb(123 ,123 , 123);\n"
"}\n"
"#shopInfomation\n"
"{\n"
"        background:white;\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
" border-bottom-left-radius:10px;\n"
"    border-bottom-right-radius:10px;\n"
"\n"
"}")
        self.shopInfomation.setObjectName("shopInfomation")
        self.widget_12 = QtWidgets.QWidget(self.shopInfomation)
        self.widget_12.setGeometry(QtCore.QRect(0, 0, 380, 41))
        self.widget_12.setStyleSheet("QWidget\n"
"{\n"
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
        self.oweWaterFee.setObjectName("oweWaterFee")
        self.oweElectricFee = QtWidgets.QCheckBox(self.shopInfomation)
        self.oweElectricFee.setGeometry(QtCore.QRect(180, 80, 50, 20))
        self.oweElectricFee.setStyleSheet("background:transparent;\n"
"font-size:14px")
        self.oweElectricFee.setCheckable(False)
        self.oweElectricFee.setObjectName("oweElectricFee")
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
        self.label_12 = QtWidgets.QLabel(self.AllShop)
        self.label_12.setGeometry(QtCore.QRect(320, 350, 54, 12))
        self.label_12.setStyleSheet("font-size:18px;\n"
"background:transparent;")
        self.label_12.setObjectName("label_12")
        self.label_7 = QtWidgets.QLabel(self.AllShop)
        self.label_7.setGeometry(QtCore.QRect(40, 100, 90, 30))
        self.label_7.setStyleSheet("font-size:22px;\n"
"background:transparent;")
        self.label_7.setObjectName("label_7")
        self.pushButton_15 = QtWidgets.QPushButton(self.AllShop)
        self.pushButton_15.setGeometry(QtCore.QRect(230, 105, 20, 20))
        self.pushButton_15.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(60,192,192);\n"
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
        self.pushButton_13.setGeometry(QtCore.QRect(150, 105, 20, 20))
        self.pushButton_13.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(171, 146,196);\n"
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
        self.myShop.setGeometry(QtCore.QRect(15, 15, 101, 30))
        self.myShop.setStyleSheet("font-size:22px")
        self.myShop.setObjectName("myShop")
        self.widget_24 = QtWidgets.QWidget(self.MyShop)
        self.widget_24.setGeometry(QtCore.QRect(0, 70, 850, 500))
        self.widget_24.setStyleSheet("#widget_24\n"
"{\n"
"    background:rgb(226, 232, 255);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}")
        self.widget_24.setObjectName("widget_24")
        self.widget_9 = QtWidgets.QWidget(self.widget_24)
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
        self.label_23 = QtWidgets.QLabel(self.widget_9)
        self.label_23.setGeometry(QtCore.QRect(20, 90, 101, 20))
        self.label_23.setObjectName("label_23")
        self.residualAuditNum = QtWidgets.QLabel(self.widget_9)
        self.residualAuditNum.setGeometry(QtCore.QRect(130, 90, 61, 20))
        self.residualAuditNum.setText("")
        self.residualAuditNum.setObjectName("residualAuditNum")
        self.label_25 = QtWidgets.QLabel(self.widget_9)
        self.label_25.setGeometry(QtCore.QRect(20, 140, 81, 20))
        self.label_25.setObjectName("label_25")
        self.residualAudit = QtWidgets.QComboBox(self.widget_9)
        self.residualAudit.setGeometry(QtCore.QRect(100, 140, 140, 20))
        self.residualAudit.setObjectName("residualAudit")
        self.widget_14 = QtWidgets.QWidget(self.widget_9)
        self.widget_14.setGeometry(QtCore.QRect(0, 0, 251, 40))
        self.widget_14.setStyleSheet("QWidget\n"
"{\n"
"    background:rgb(165, 200, 255);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"")
        self.widget_14.setObjectName("widget_14")
        self.label_35 = QtWidgets.QLabel(self.widget_14)
        self.label_35.setGeometry(QtCore.QRect(20, 15, 111, 20))
        self.label_35.setStyleSheet("font-size:20px")
        self.label_35.setObjectName("label_35")
        self.widget_10 = QtWidgets.QWidget(self.widget_24)
        self.widget_10.setGeometry(QtCore.QRect(20, 270, 251, 200))
        self.widget_10.setStyleSheet("QLabel{\n"
"  background:transparent;\n"
"font-size:16px;\n"
"}\n"
"\n"
"#widget_10\n"
"{\n"
"            background:white;\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
" border-bottom-left-radius:10px;\n"
"    border-bottom-right-radius:10px;\n"
"}")
        self.widget_10.setObjectName("widget_10")
        self.label_32 = QtWidgets.QLabel(self.widget_10)
        self.label_32.setGeometry(QtCore.QRect(20, 90, 100, 20))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.widget_10)
        self.label_33.setGeometry(QtCore.QRect(20, 140, 80, 20))
        self.label_33.setObjectName("label_33")
        self.quantityAudited = QtWidgets.QComboBox(self.widget_10)
        self.quantityAudited.setGeometry(QtCore.QRect(100, 140, 140, 20))
        self.quantityAudited.setObjectName("quantityAudited")
        self.quantityAuditedNum = QtWidgets.QLabel(self.widget_10)
        self.quantityAuditedNum.setGeometry(QtCore.QRect(130, 90, 61, 20))
        self.quantityAuditedNum.setStyleSheet("background:transparent;")
        self.quantityAuditedNum.setText("")
        self.quantityAuditedNum.setObjectName("quantityAuditedNum")
        self.widget_15 = QtWidgets.QWidget(self.widget_10)
        self.widget_15.setGeometry(QtCore.QRect(0, 0, 251, 40))
        self.widget_15.setStyleSheet("QWidget\n"
"{\n"
"    background:rgb(165, 200, 255);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"")
        self.widget_15.setObjectName("widget_15")
        self.label_17 = QtWidgets.QLabel(self.widget_15)
        self.label_17.setGeometry(QtCore.QRect(20, 15, 111, 20))
        self.label_17.setStyleSheet("font-size:20px")
        self.label_17.setObjectName("label_17")
        self.widget = QtWidgets.QWidget(self.widget_24)
        self.widget.setGeometry(QtCore.QRect(290, 20, 551, 451))
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
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setGeometry(QtCore.QRect(20, 20, 91, 21))
        self.label_16.setStyleSheet("font-size:20px")
        self.label_16.setObjectName("label_16")
        self.contractContent = QtWidgets.QTextEdit(self.widget)
        self.contractContent.setGeometry(QtCore.QRect(20, 70, 511, 311))
        self.contractContent.setStyleSheet("QTextEdit\n"
"{\n"
" background:transparent;\n"
"    padding-left:5px ;\n"
"    padding-top:1px ;\n"
"    border-bottom-left-radius:9px;\n"
"    border-bottom-right-radius:9px;\n"
"    border: 1px solid rgb(123 ,123 , 123);\n"
"}")
        self.contractContent.setObjectName("contractContent")
        self.label_26 = QtWidgets.QLabel(self.widget)
        self.label_26.setGeometry(QtCore.QRect(200, 390, 90, 20))
        self.label_26.setObjectName("label_26")
        self.label_28 = QtWidgets.QLabel(self.widget)
        self.label_28.setGeometry(QtCore.QRect(30, 390, 71, 20))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.widget)
        self.label_29.setGeometry(QtCore.QRect(30, 420, 90, 20))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.widget)
        self.label_30.setGeometry(QtCore.QRect(270, 420, 91, 20))
        self.label_30.setObjectName("label_30")
        self.shopNun = QtWidgets.QLineEdit(self.widget)
        self.shopNun.setGeometry(QtCore.QRect(100, 390, 71, 20))
        self.shopNun.setReadOnly(True)
        self.shopNun.setObjectName("shopNun")
        self.contractConfirm = QtWidgets.QCheckBox(self.widget)
        self.contractConfirm.setGeometry(QtCore.QRect(120, 420, 51, 20))
        self.contractConfirm.setStyleSheet("background:transparent;")
        self.contractConfirm.setCheckable(True)
        self.contractConfirm.setObjectName("contractConfirm")
        self.rentTime = QtWidgets.QLineEdit(self.widget)
        self.rentTime.setGeometry(QtCore.QRect(290, 390, 71, 20))
        self.rentTime.setReadOnly(True)
        self.rentTime.setObjectName("rentTime")
        self.auditConfirmation = QtWidgets.QPushButton(self.widget)
        self.auditConfirmation.setGeometry(QtCore.QRect(170, 420, 80, 20))
        self.auditConfirmation.setStyleSheet("QPushButton\n"
"{\n"
" border-radius:5px;font-size:16px;background:rgb(200, 222,255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background:rgb(142, 182, 255)\n"
"}")
        self.auditConfirmation.setObjectName("auditConfirmation")
        self.ceoSignature = QtWidgets.QLineEdit(self.widget)
        self.ceoSignature.setGeometry(QtCore.QRect(360, 420, 81, 20))
        self.ceoSignature.setObjectName("ceoSignature")
        self.signatureConfirmation = QtWidgets.QPushButton(self.widget)
        self.signatureConfirmation.setGeometry(QtCore.QRect(450, 420, 80, 20))
        self.signatureConfirmation.setStyleSheet("QPushButton\n"
"{\n"
" border-radius:5px;font-size:16px;background:rgb(200, 222,255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background:rgb(142, 182, 255)\n"
"}")
        self.signatureConfirmation.setObjectName("signatureConfirmation")
        self.widget_11 = QtWidgets.QWidget(self.widget)
        self.widget_11.setGeometry(QtCore.QRect(0, 0, 551, 40))
        self.widget_11.setStyleSheet("QWidget\n"
"{\n"
"    background:rgb(165, 200, 255);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"")
        self.widget_11.setObjectName("widget_11")
        self.label_24 = QtWidgets.QLabel(self.widget_11)
        self.label_24.setGeometry(QtCore.QRect(20, 15, 91, 20))
        self.label_24.setStyleSheet("font-size:20px;")
        self.label_24.setObjectName("label_24")
        self.label_34 = QtWidgets.QLabel(self.widget)
        self.label_34.setGeometry(QtCore.QRect(20, 50, 91, 20))
        self.label_34.setObjectName("label_34")
        self.stackedWidget.addWidget(self.MyShop)
        self.MyInformation = QtWidgets.QWidget()
        self.MyInformation.setObjectName("MyInformation")
        self.myInformation = QtWidgets.QLabel(self.MyInformation)
        self.myInformation.setGeometry(QtCore.QRect(15, 15, 120, 20))
        self.myInformation.setStyleSheet("font-size:22px")
        self.myInformation.setObjectName("myInformation")
        self.widget_25 = QtWidgets.QWidget(self.MyInformation)
        self.widget_25.setGeometry(QtCore.QRect(0, 70, 850, 500))
        self.widget_25.setStyleSheet("#widget_25\n"
"{\n"
"    background:rgb(226, 232, 255);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}")
        self.widget_25.setObjectName("widget_25")
        self.widget_16 = QtWidgets.QWidget(self.widget_25)
        self.widget_16.setGeometry(QtCore.QRect(50, 210, 361, 231))
        self.widget_16.setStyleSheet("#widget_14\n"
"{\n"
"    background:white;\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"\n"
"\n"
"QLabel\n"
"{    \n"
"background:transparent;\n"
"font-size:16px;\n"
"}")
        self.widget_16.setObjectName("widget_16")
        self.label_31 = QtWidgets.QLabel(self.widget_16)
        self.label_31.setGeometry(QtCore.QRect(20, 10, 54, 20))
        self.label_31.setStyleSheet("font-size:20px;")
        self.label_31.setObjectName("label_31")
        self.label_36 = QtWidgets.QLabel(self.widget_16)
        self.label_36.setGeometry(QtCore.QRect(30, 50, 81, 21))
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.widget_16)
        self.label_37.setGeometry(QtCore.QRect(100, 120, 111, 21))
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.widget_16)
        self.label_38.setGeometry(QtCore.QRect(70, 90, 54, 12))
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.widget_16)
        self.label_39.setGeometry(QtCore.QRect(40, 160, 121, 20))
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.widget_16)
        self.label_40.setGeometry(QtCore.QRect(160, 160, 31, 20))
        self.label_40.setStyleSheet("\n"
"font-size:30px;")
        self.label_40.setObjectName("label_40")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_16)
        self.pushButton_5.setGeometry(QtCore.QRect(190, 20, 151, 91))
        self.pushButton_5.setStyleSheet("QPushButton\n"
"{\n"
"background:transparent;\n"
"image:url(:/icon/晴.png)；\n"
"}")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.stackedWidget.addWidget(self.MyInformation)
        self.label = QtWidgets.QLabel(CEOWindow)
        self.label.setGeometry(QtCore.QRect(30, 20, 70, 31))
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 15pt \"华文中宋\";")
        self.label.setObjectName("label")

        self.retranslateUi(CEOWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidgetShop.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CEOWindow)

    def retranslateUi(self, CEOWindow):
        _translate = QtCore.QCoreApplication.translate
        CEOWindow.setWindowTitle(_translate("CEOWindow", "Form"))
        self.btnMyShop.setText(_translate("CEOWindow", "审核合同"))
        self.btnAllShop.setText(_translate("CEOWindow", "全部店铺"))
        self.btnInf.setText(_translate("CEOWindow", "我的信息"))
        self.allShop.setText(_translate("CEOWindow", "全部店铺"))
        self.pushButtonShop_12.setText(_translate("CEOWindow", "12"))
        self.pushButtonShop_11.setText(_translate("CEOWindow", "11"))
        self.pushButtonShop_01.setText(_translate("CEOWindow", "01"))
        self.pushButtonShop_04.setText(_translate("CEOWindow", "04"))
        self.pushButtonShop_08.setText(_translate("CEOWindow", "08"))
        self.pushButtonShop_09.setText(_translate("CEOWindow", "09"))
        self.pushButtonShop_10.setText(_translate("CEOWindow", "10"))
        self.pushButtonShop_02.setText(_translate("CEOWindow", "02"))
        self.pushButtonShop_06.setText(_translate("CEOWindow", "06"))
        self.pushButtonShop_03.setText(_translate("CEOWindow", "03"))
        self.pushButtonShop_05.setText(_translate("CEOWindow", "05"))
        self.pushButtonShop_07.setText(_translate("CEOWindow", "07"))
        self.pushButtonShop_18.setText(_translate("CEOWindow", "18"))
        self.pushButtonShop_14.setText(_translate("CEOWindow", "14"))
        self.pushButtonShop_17.setText(_translate("CEOWindow", "17"))
        self.pushButtonShop_21.setText(_translate("CEOWindow", "21"))
        self.pushButtonShop_.setText(_translate("CEOWindow", "13"))
        self.pushButtonShop_24.setText(_translate("CEOWindow", "24"))
        self.pushButtonShop_16.setText(_translate("CEOWindow", "16"))
        self.pushButtonShop_19.setText(_translate("CEOWindow", "19"))
        self.pushButtonShop_23.setText(_translate("CEOWindow", "23"))
        self.pushButtonShop_20.setText(_translate("CEOWindow", "20"))
        self.pushButtonShop_22.setText(_translate("CEOWindow", "22"))
        self.pushButtonShop_15.setText(_translate("CEOWindow", "15"))
        self.label_15.setText(_translate("CEOWindow", "合同信息"))
        self.label_3.setText(_translate("CEOWindow", "状态："))
        self.label_5.setText(_translate("CEOWindow", "签订时长："))
        self.label_6.setText(_translate("CEOWindow", "业主签字;"))
        self.label_8.setText(_translate("CEOWindow", "总经理签字："))
        self.label_9.setText(_translate("CEOWindow", "合同事项："))
        self.label_10.setText(_translate("CEOWindow", "总经理确认情况："))
        self.label_18.setText(_translate("CEOWindow", "店铺编号："))
        self.ceoConfirm.setText(_translate("CEOWindow", "已确认"))
        self.userSignature.setText(_translate("CEOWindow", "已签字"))
        self.ceoSingature.setText(_translate("CEOWindow", "已签字"))
        self.label_14.setText(_translate("CEOWindow", "店铺信息"))
        self.label_19.setText(_translate("CEOWindow", "已缴水费："))
        self.label_20.setText(_translate("CEOWindow", "已缴电费："))
        self.label_21.setText(_translate("CEOWindow", "已缴物业费："))
        self.label_22.setText(_translate("CEOWindow", "已缴保证金："))
        self.oweWaterFee.setText(_translate("CEOWindow", "欠费"))
        self.oweElectricFee.setText(_translate("CEOWindow", "欠费"))
        self.owePropertyFee.setText(_translate("CEOWindow", "欠费"))
        self.oweGuaranteePaid.setText(_translate("CEOWindow", "欠费"))
        self.label_12.setText(_translate("CEOWindow", "1f"))
        self.label_7.setText(_translate("CEOWindow", "楼层信息"))
        self.label_13.setText(_translate("CEOWindow", "楼层："))
        self.label_2.setText(_translate("CEOWindow", "已租店铺"))
        self.label_4.setText(_translate("CEOWindow", "可租店铺"))
        self.label_11.setText(_translate("CEOWindow", "当前楼层："))
        self.myShop.setText(_translate("CEOWindow", "审核合同"))
        self.label_23.setText(_translate("CEOWindow", "剩余审核数量："))
        self.label_25.setText(_translate("CEOWindow", "审核合同："))
        self.label_35.setText(_translate("CEOWindow", "待审核合同"))
        self.label_32.setText(_translate("CEOWindow", "待签数量："))
        self.label_33.setText(_translate("CEOWindow", "待签合同："))
        self.label_17.setText(_translate("CEOWindow", "待签字合同"))
        self.label_16.setText(_translate("CEOWindow", "租赁合同"))
        self.label_26.setText(_translate("CEOWindow", "签订年份："))
        self.label_28.setText(_translate("CEOWindow", "店铺号："))
        self.label_29.setText(_translate("CEOWindow", "审核确认："))
        self.label_30.setText(_translate("CEOWindow", "确认签字："))
        self.contractConfirm.setText(_translate("CEOWindow", "确认"))
        self.auditConfirmation.setText(_translate("CEOWindow", "确认审核"))
        self.signatureConfirmation.setText(_translate("CEOWindow", "签字确认"))
        self.label_24.setText(_translate("CEOWindow", "合同信息"))
        self.label_34.setText(_translate("CEOWindow", "合同内容："))
        self.myInformation.setText(_translate("CEOWindow", "我的信息"))
        self.label_31.setText(_translate("CEOWindow", "无锡"))
        self.label_36.setText(_translate("CEOWindow", "当前天气"))
        self.label_37.setText(_translate("CEOWindow", "温度：26-32℃"))
        self.label_38.setText(_translate("CEOWindow", "27℃"))
        self.label_39.setText(_translate("CEOWindow", "实时空气质量："))
        self.label_40.setText(_translate("CEOWindow", "34"))
        self.label.setText(_translate("CEOWindow", "JOJO"))

