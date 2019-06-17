# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_ProprietorWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProprietorWindow(object):
    def setupUi(self, ProprietorWindow):
        ProprietorWindow.setObjectName("ProprietorWindow")
        ProprietorWindow.resize(1078, 742)
        ProprietorWindow.setStyleSheet("font: 9pt \"黑体\";")
        self.frame = QtWidgets.QFrame(ProprietorWindow)
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
        self.icon = QtWidgets.QPushButton(self.widgetMenu)
        self.icon.setGeometry(QtCore.QRect(0, 0, 30, 30))
        self.icon.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"background:transparent;\n"
"    \n"
"    image: url(:/icon/5.png);\n"
"}")
        self.icon.setText("")
        self.icon.setIconSize(QtCore.QSize(30, 30))
        self.icon.setObjectName("icon")
        self.label = QtWidgets.QLabel(self.widgetMenu)
        self.label.setGeometry(QtCore.QRect(40, 0, 131, 31))
        self.label.setStyleSheet("font-size:20px")
        self.label.setObjectName("label")
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
        self.btnContract = QtWidgets.QToolButton(self.widgetBtn)
        self.btnContract.setGeometry(QtCore.QRect(0, 150, 150, 50))
        self.btnContract.setObjectName("btnContract")
        self.btnSublease = QtWidgets.QToolButton(self.widgetBtn)
        self.btnSublease.setGeometry(QtCore.QRect(0, 200, 150, 50))
        self.btnSublease.setObjectName("btnSublease")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setGeometry(QtCore.QRect(150, 30, 851, 571))
        self.stackedWidget.setStyleSheet("QWidget{\n"
"    background:rgb(243,244,248);\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.AllShop = QtWidgets.QWidget()
        self.AllShop.setObjectName("AllShop")
        self.allShop = QtWidgets.QLabel(self.AllShop)
        self.allShop.setGeometry(QtCore.QRect(15, 15, 90, 30))
        self.allShop.setStyleSheet("\n"
"font-size:22px;")
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
"        background:white;\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
" border-bottom-left-radius:10px;\n"
"    border-bottom-right-radius:10px;\n"
"}\n"
"")
        self.firstFloorShop.setObjectName("firstFloorShop")
        self.widget = QtWidgets.QWidget(self.firstFloorShop)
        self.widget.setGeometry(QtCore.QRect(0, 0, 400, 40))
        self.widget.setStyleSheet("QWidget\n"
"{\n"
"    background:rgb(165, 200, 255);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.firstFloorShop)
        self.widget_2.setGeometry(QtCore.QRect(10, 60, 151, 391))
        self.widget_2.setStyleSheet("background: rgb(255, 255, 255);")
        self.widget_2.setObjectName("widget_2")
        self.pushButtonShop_12 = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonShop_12.setGeometry(QtCore.QRect(95, 10, 45, 370))
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
        self.widget_3.setGeometry(QtCore.QRect(160, 320, 230, 130))
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
        self.widget_4.setGeometry(QtCore.QRect(160, 60, 231, 131))
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
        self.firstFloorShop_2 = QtWidgets.QWidget(self._2f)
        self.firstFloorShop_2.setGeometry(QtCore.QRect(20, 20, 400, 470))
        self.firstFloorShop_2.setStyleSheet("#firstFloorShop_2\n"
"{\n"
"    background:white;\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"\n"
"")
        self.firstFloorShop_2.setObjectName("firstFloorShop_2")
        self.widget_5 = QtWidgets.QWidget(self.firstFloorShop_2)
        self.widget_5.setGeometry(QtCore.QRect(0, 0, 400, 50))
        self.widget_5.setStyleSheet("QWidget\n"
"{\n"
"    background:rgb(165, 200, 255);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"")
        self.widget_5.setObjectName("widget_5")
        self.widget_6 = QtWidgets.QWidget(self.firstFloorShop_2)
        self.widget_6.setGeometry(QtCore.QRect(10, 60, 151, 391))
        self.widget_6.setStyleSheet("background: rgb(255, 255, 255);")
        self.widget_6.setObjectName("widget_6")
        self.pushButtonShop_13 = QtWidgets.QPushButton(self.widget_6)
        self.pushButtonShop_13.setGeometry(QtCore.QRect(95, 10, 45, 370))
        self.pushButtonShop_13.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButtonShop_13.setObjectName("pushButtonShop_13")
        self.pushButtonShop_14 = QtWidgets.QPushButton(self.widget_6)
        self.pushButtonShop_14.setGeometry(QtCore.QRect(10, 210, 70, 170))
        self.pushButtonShop_14.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButtonShop_14.setObjectName("pushButtonShop_14")
        self.pushButtonShop_ = QtWidgets.QPushButton(self.widget_6)
        self.pushButtonShop_.setGeometry(QtCore.QRect(10, 10, 70, 70))
        self.pushButtonShop_.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButtonShop_.setObjectName("pushButtonShop_")
        self.pushButtonShop_5 = QtWidgets.QPushButton(self.widget_6)
        self.pushButtonShop_5.setGeometry(QtCore.QRect(10, 90, 70, 45))
        self.pushButtonShop_5.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButtonShop_5.setObjectName("pushButtonShop_5")
        self.pushButtonShop_17 = QtWidgets.QPushButton(self.widget_6)
        self.pushButtonShop_17.setGeometry(QtCore.QRect(10, 150, 70, 41))
        self.pushButtonShop_17.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButtonShop_17.setObjectName("pushButtonShop_17")
        self.widget_7 = QtWidgets.QWidget(self.firstFloorShop_2)
        self.widget_7.setGeometry(QtCore.QRect(160, 320, 230, 130))
        self.widget_7.setStyleSheet("background: rgb(255, 255, 255);")
        self.widget_7.setObjectName("widget_7")
        self.pushButtonShop_15 = QtWidgets.QPushButton(self.widget_7)
        self.pushButtonShop_15.setGeometry(QtCore.QRect(10, 10, 210, 40))
        self.pushButtonShop_15.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButtonShop_15.setObjectName("pushButtonShop_15")
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
        self.widget_8 = QtWidgets.QWidget(self.firstFloorShop_2)
        self.widget_8.setGeometry(QtCore.QRect(160, 60, 231, 131))
        self.widget_8.setStyleSheet("background: rgb(255, 255, 255);")
        self.widget_8.setObjectName("widget_8")
        self.pushButtonShop_18 = QtWidgets.QPushButton(self.widget_8)
        self.pushButtonShop_18.setGeometry(QtCore.QRect(10, 85, 61, 41))
        self.pushButtonShop_18.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButtonShop_18.setObjectName("pushButtonShop_18")
        self.pushButtonShop_19 = QtWidgets.QPushButton(self.widget_8)
        self.pushButtonShop_19.setGeometry(QtCore.QRect(75, 85, 81, 40))
        self.pushButtonShop_19.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButtonShop_19.setObjectName("pushButtonShop_19")
        self.pushButtonShop_24 = QtWidgets.QPushButton(self.widget_8)
        self.pushButtonShop_24.setGeometry(QtCore.QRect(100, 10, 125, 40))
        self.pushButtonShop_24.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(60,192,192);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_24.setObjectName("pushButtonShop_24")
        self.pushButtonShop_23 = QtWidgets.QPushButton(self.widget_8)
        self.pushButtonShop_23.setGeometry(QtCore.QRect(10, 10, 81, 40))
        self.pushButtonShop_23.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(60,192,192);\n"
"border-radius:10px;\n"
"}")
        self.pushButtonShop_23.setObjectName("pushButtonShop_23")
        self.pushButtonShop_20 = QtWidgets.QPushButton(self.widget_8)
        self.pushButtonShop_20.setGeometry(QtCore.QRect(160, 85, 65, 40))
        self.pushButtonShop_20.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButtonShop_20.setObjectName("pushButtonShop_20")
        self.stackedWidgetShop.addWidget(self._2f)
        self.applyInf = QtWidgets.QWidget(self.AllShop)
        self.applyInf.setGeometry(QtCore.QRect(440, 230, 380, 331))
        self.applyInf.setStyleSheet("#applyInf\n"
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
        self.applyInf.setObjectName("applyInf")
        self.widget_13 = QtWidgets.QWidget(self.applyInf)
        self.widget_13.setGeometry(QtCore.QRect(0, 0, 380, 40))
        self.widget_13.setStyleSheet("QWidget\n"
"{\n"
"\n"
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
        self.label_51 = QtWidgets.QLabel(self.applyInf)
        self.label_51.setGeometry(QtCore.QRect(40, 100, 61, 25))
        self.label_51.setStyleSheet("background:transparent;\n"
"font-size:16px;")
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.applyInf)
        self.label_52.setGeometry(QtCore.QRect(40, 190, 70, 25))
        self.label_52.setStyleSheet("background:transparent;\n"
"font-size:16px;")
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.applyInf)
        self.label_53.setGeometry(QtCore.QRect(40, 130, 70, 25))
        self.label_53.setStyleSheet("background:transparent;\n"
"font-size:16px;")
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.applyInf)
        self.label_54.setGeometry(QtCore.QRect(40, 160, 70, 25))
        self.label_54.setStyleSheet("background:transparent;\n"
"font-size:16px;")
        self.label_54.setObjectName("label_54")
        self.shopName = QtWidgets.QLineEdit(self.applyInf)
        self.shopName.setGeometry(QtCore.QRect(120, 100, 120, 25))
        self.shopName.setStyleSheet("")
        self.shopName.setObjectName("shopName")
        self.userTel = QtWidgets.QLineEdit(self.applyInf)
        self.userTel.setGeometry(QtCore.QRect(120, 130, 120, 25))
        self.userTel.setStyleSheet("")
        self.userTel.setObjectName("userTel")
        self.shopRentTime = QtWidgets.QLineEdit(self.applyInf)
        self.shopRentTime.setGeometry(QtCore.QRect(120, 160, 120, 25))
        self.shopRentTime.setStyleSheet("")
        self.shopRentTime.setObjectName("shopRentTime")
        self.shopReason = QtWidgets.QTextEdit(self.applyInf)
        self.shopReason.setGeometry(QtCore.QRect(120, 190, 240, 100))
        self.shopReason.setStyleSheet("QTextEdit\n"
"{\n"
" background:transparent;\n"
"    padding-left:5px ;\n"
"    padding-top:1px ;\n"
"    border-bottom-left-radius:9px;\n"
"    border-bottom-right-radius:9px;\n"
"    border: 1px solid rgb(123 ,123 , 123);\n"
"}")
        self.shopReason.setObjectName("shopReason")
        self.immediateApplication = QtWidgets.QPushButton(self.applyInf)
        self.immediateApplication.setGeometry(QtCore.QRect(270, 300, 91, 21))
        self.immediateApplication.setStyleSheet("QPushButton\n"
"{\n"
" border-radius:5px;font-size:16px;background:rgb(200, 222,255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background:rgb(142, 182, 255)\n"
"}")
        self.immediateApplication.setObjectName("immediateApplication")
        self.label_11 = QtWidgets.QLabel(self.applyInf)
        self.label_11.setGeometry(QtCore.QRect(40, 70, 50, 25))
        self.label_11.setStyleSheet("background:transparent;\n"
"font-size:16px;")
        self.label_11.setObjectName("label_11")
        self.shopNum = QtWidgets.QLineEdit(self.applyInf)
        self.shopNum.setGeometry(QtCore.QRect(120, 70, 120, 25))
        self.shopNum.setStyleSheet("")
        self.shopNum.setObjectName("shopNum")
        self.shopInfomation = QtWidgets.QWidget(self.AllShop)
        self.shopInfomation.setGeometry(QtCore.QRect(440, 90, 380, 131))
        self.shopInfomation.setStyleSheet("#shopInfomation\n"
"{\n"
"        background:white;\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
" border-bottom-left-radius:10px;\n"
"    border-bottom-right-radius:10px;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"font-size:16px;\n"
"}")
        self.shopInfomation.setObjectName("shopInfomation")
        self.widget_12 = QtWidgets.QWidget(self.shopInfomation)
        self.widget_12.setGeometry(QtCore.QRect(0, 0, 380, 40))
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
        self.label_14.setGeometry(QtCore.QRect(20, 15, 101, 20))
        self.label_14.setStyleSheet("font-size:22px")
        self.label_14.setObjectName("label_14")
        self.areaCoveredLalel = QtWidgets.QLabel(self.shopInfomation)
        self.areaCoveredLalel.setGeometry(QtCore.QRect(50, 60, 81, 20))
        self.areaCoveredLalel.setObjectName("areaCoveredLalel")
        self.annualRentLabel = QtWidgets.QLabel(self.shopInfomation)
        self.annualRentLabel.setGeometry(QtCore.QRect(50, 90, 61, 20))
        self.annualRentLabel.setObjectName("annualRentLabel")
        self.depositLabel = QtWidgets.QLabel(self.shopInfomation)
        self.depositLabel.setGeometry(QtCore.QRect(230, 60, 61, 20))
        self.depositLabel.setObjectName("depositLabel")
        self.propertyFeeLabel = QtWidgets.QLabel(self.shopInfomation)
        self.propertyFeeLabel.setGeometry(QtCore.QRect(230, 90, 61, 20))
        self.propertyFeeLabel.setObjectName("propertyFeeLabel")
        self.areaCovered = QtWidgets.QLabel(self.shopInfomation)
        self.areaCovered.setGeometry(QtCore.QRect(140, 60, 54, 20))
        self.areaCovered.setText("")
        self.areaCovered.setObjectName("areaCovered")
        self.annualRent = QtWidgets.QLabel(self.shopInfomation)
        self.annualRent.setGeometry(QtCore.QRect(140, 90, 54, 20))
        self.annualRent.setText("")
        self.annualRent.setObjectName("annualRent")
        self.deposit = QtWidgets.QLabel(self.shopInfomation)
        self.deposit.setGeometry(QtCore.QRect(310, 60, 54, 20))
        self.deposit.setText("")
        self.deposit.setObjectName("deposit")
        self.propertyFee = QtWidgets.QLabel(self.shopInfomation)
        self.propertyFee.setGeometry(QtCore.QRect(310, 90, 54, 20))
        self.propertyFee.setText("")
        self.propertyFee.setObjectName("propertyFee")
        self.pushButton_13 = QtWidgets.QPushButton(self.AllShop)
        self.pushButton_13.setGeometry(QtCore.QRect(150, 105, 20, 20))
        self.pushButton_13.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"\n"
"background:rgb(171, 146,196);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_2 = QtWidgets.QLabel(self.AllShop)
        self.label_2.setGeometry(QtCore.QRect(170, 105, 61, 20))
        self.label_2.setStyleSheet("background:transparent;\n"
"font-size:13px;")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.AllShop)
        self.label_4.setGeometry(QtCore.QRect(250, 105, 61, 20))
        self.label_4.setStyleSheet("background:transparent;\n"
"font-size:13px;")
        self.label_4.setObjectName("label_4")
        self.pushButton_15 = QtWidgets.QPushButton(self.AllShop)
        self.pushButton_15.setGeometry(QtCore.QRect(230, 105, 20, 20))
        self.pushButton_15.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(60,192,192);\n"
"border-radius:10px;\n"
"}")
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_7 = QtWidgets.QLabel(self.AllShop)
        self.label_7.setGeometry(QtCore.QRect(40, 100, 100, 30))
        self.label_7.setStyleSheet("font-size:22px;\n"
"background:transparent;")
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(self.AllShop)
        self.label_3.setGeometry(QtCore.QRect(310, 105, 50, 20))
        self.label_3.setStyleSheet("font-size:15px;\n"
"background:transparent;")
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.AllShop)
        self.comboBox.setGeometry(QtCore.QRect(350, 100, 60, 25))
        self.comboBox.setObjectName("comboBox")
        self.curFloor = QtWidgets.QLabel(self.AllShop)
        self.curFloor.setGeometry(QtCore.QRect(320, 350, 41, 16))
        self.curFloor.setStyleSheet("font-size:20px;\n"
"background:transparent;")
        self.curFloor.setObjectName("curFloor")
        self.label_16 = QtWidgets.QLabel(self.AllShop)
        self.label_16.setGeometry(QtCore.QRect(230, 340, 91, 31))
        self.label_16.setStyleSheet("font-size:20px;\n"
"background:transparent;")
        self.label_16.setObjectName("label_16")
        self.stackedWidget.addWidget(self.AllShop)
        self.MyShop = QtWidgets.QWidget()
        self.MyShop.setObjectName("MyShop")
        self.myShop = QtWidgets.QLabel(self.MyShop)
        self.myShop.setGeometry(QtCore.QRect(15, 15, 90, 31))
        self.myShop.setStyleSheet("\n"
"font-size:22px;")
        self.myShop.setObjectName("myShop")
        self.Receipt = QtWidgets.QWidget(self.MyShop)
        self.Receipt.setGeometry(QtCore.QRect(0, 70, 851, 501))
        self.Receipt.setStyleSheet("font-size:20px;\n"
"background:rgb(226, 232, 255);")
        self.Receipt.setObjectName("Receipt")
        self.widget_19 = QtWidgets.QWidget(self.Receipt)
        self.widget_19.setGeometry(QtCore.QRect(20, 20, 400, 300))
        self.widget_19.setStyleSheet("    background:white;\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
" border-bottom-left-radius:10px;\n"
"    border-bottom-right-radius:10px;")
        self.widget_19.setObjectName("widget_19")
        self.electricCharge = QtWidgets.QLabel(self.widget_19)
        self.electricCharge.setGeometry(QtCore.QRect(160, 40, 80, 30))
        self.electricCharge.setText("")
        self.electricCharge.setObjectName("electricCharge")
        self.waterCharge = QtWidgets.QLabel(self.widget_19)
        self.waterCharge.setGeometry(QtCore.QRect(160, 160, 81, 30))
        self.waterCharge.setText("")
        self.waterCharge.setObjectName("waterCharge")
        self.propertyFeeCharge = QtWidgets.QLabel(self.widget_19)
        self.propertyFeeCharge.setGeometry(QtCore.QRect(160, 120, 80, 30))
        self.propertyFeeCharge.setText("")
        self.propertyFeeCharge.setObjectName("propertyFeeCharge")
        self.PayImmediately = QtWidgets.QPushButton(self.widget_19)
        self.PayImmediately.setGeometry(QtCore.QRect(260, 200, 80, 30))
        self.PayImmediately.setStyleSheet("QPushButton\n"
"{\n"
" border-radius:5px;font-size:16px;background:rgb(200, 222,255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background:rgb(142, 182, 255)\n"
"}")
        self.PayImmediately.setObjectName("PayImmediately")
        self.waterChargeLabel = QtWidgets.QLabel(self.widget_19)
        self.waterChargeLabel.setGeometry(QtCore.QRect(40, 160, 100, 30))
        self.waterChargeLabel.setObjectName("waterChargeLabel")
        self.propertyFeeChargeLabel = QtWidgets.QLabel(self.widget_19)
        self.propertyFeeChargeLabel.setGeometry(QtCore.QRect(40, 120, 110, 30))
        self.propertyFeeChargeLabel.setObjectName("propertyFeeChargeLabel")
        self.electricChargeLabel = QtWidgets.QLabel(self.widget_19)
        self.electricChargeLabel.setGeometry(QtCore.QRect(40, 40, 90, 30))
        self.electricChargeLabel.setObjectName("electricChargeLabel")
        self.guaranteeCharge = QtWidgets.QLabel(self.widget_19)
        self.guaranteeCharge.setGeometry(QtCore.QRect(160, 80, 80, 30))
        self.guaranteeCharge.setText("")
        self.guaranteeCharge.setObjectName("guaranteeCharge")
        self.guaranteeChargeLabel = QtWidgets.QLabel(self.widget_19)
        self.guaranteeChargeLabel.setGeometry(QtCore.QRect(40, 80, 80, 30))
        self.guaranteeChargeLabel.setObjectName("guaranteeChargeLabel")
        self.label_29 = QtWidgets.QLabel(self.Receipt)
        self.label_29.setGeometry(QtCore.QRect(480, 80, 321, 221))
        self.label_29.setStyleSheet("\n"
"    background:white;\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"\n"
"font-size:25px;\n"
"\n"
"")
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.ReceiptCharge = QtWidgets.QPushButton(self.MyShop)
        self.ReceiptCharge.setGeometry(QtCore.QRect(0, 45, 80, 25))
        self.ReceiptCharge.setStyleSheet("QPushButton\n"
"{\n"
" border-radius:5px;font-size:16px;background:white;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background:rgb(142, 182, 255)\n"
"}")
        self.ReceiptCharge.setObjectName("ReceiptCharge")
        self.ReceivableCharge = QtWidgets.QPushButton(self.MyShop)
        self.ReceivableCharge.setGeometry(QtCore.QRect(80, 45, 80, 25))
        self.ReceivableCharge.setStyleSheet("QPushButton\n"
"{\n"
" border-radius:5px;font-size:16px;background:white;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background:rgb(142, 182, 255)\n"
"}")
        self.ReceivableCharge.setObjectName("ReceivableCharge")
        self.Receivable = QtWidgets.QWidget(self.MyShop)
        self.Receivable.setGeometry(QtCore.QRect(0, 70, 851, 501))
        self.Receivable.setStyleSheet("\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"font-size:20px;\n"
"    background:rgb(226, 232, 255);")
        self.Receivable.setObjectName("Receivable")
        self.widget_18 = QtWidgets.QWidget(self.Receivable)
        self.widget_18.setGeometry(QtCore.QRect(40, 40, 400, 300))
        self.widget_18.setStyleSheet("    background:white;\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;")
        self.widget_18.setObjectName("widget_18")
        self.electricReceivable = QtWidgets.QLabel(self.widget_18)
        self.electricReceivable.setGeometry(QtCore.QRect(160, 40, 80, 30))
        self.electricReceivable.setText("")
        self.electricReceivable.setObjectName("electricReceivable")
        self.waterChargeLabel_3 = QtWidgets.QLabel(self.widget_18)
        self.waterChargeLabel_3.setGeometry(QtCore.QRect(40, 80, 80, 30))
        self.waterChargeLabel_3.setObjectName("waterChargeLabel_3")
        self.electricChargeLabel_3 = QtWidgets.QLabel(self.widget_18)
        self.electricChargeLabel_3.setGeometry(QtCore.QRect(40, 40, 90, 30))
        self.electricChargeLabel_3.setObjectName("electricChargeLabel_3")
        self.waterReceivable = QtWidgets.QLabel(self.widget_18)
        self.waterReceivable.setGeometry(QtCore.QRect(160, 80, 81, 30))
        self.waterReceivable.setText("")
        self.waterReceivable.setObjectName("waterReceivable")
        self.propertyFeeReceivable = QtWidgets.QLabel(self.widget_18)
        self.propertyFeeReceivable.setGeometry(QtCore.QRect(160, 120, 80, 30))
        self.propertyFeeReceivable.setText("")
        self.propertyFeeReceivable.setObjectName("propertyFeeReceivable")
        self.propertyFeeChargeLabel_3 = QtWidgets.QLabel(self.widget_18)
        self.propertyFeeChargeLabel_3.setGeometry(QtCore.QRect(40, 120, 110, 30))
        self.propertyFeeChargeLabel_3.setObjectName("propertyFeeChargeLabel_3")
        self.guaranteeChargeLabel_3 = QtWidgets.QLabel(self.widget_18)
        self.guaranteeChargeLabel_3.setGeometry(QtCore.QRect(40, 160, 111, 30))
        self.guaranteeChargeLabel_3.setObjectName("guaranteeChargeLabel_3")
        self.guaranteeReceivable = QtWidgets.QLabel(self.widget_18)
        self.guaranteeReceivable.setGeometry(QtCore.QRect(160, 160, 80, 30))
        self.guaranteeReceivable.setText("")
        self.guaranteeReceivable.setObjectName("guaranteeReceivable")
        self.Receivable.raise_()
        self.Receipt.raise_()
        self.myShop.raise_()
        self.ReceiptCharge.raise_()
        self.ReceivableCharge.raise_()
        self.stackedWidget.addWidget(self.MyShop)
        self.MyInformation = QtWidgets.QWidget()
        self.MyInformation.setObjectName("MyInformation")
        self.myInformation = QtWidgets.QLabel(self.MyInformation)
        self.myInformation.setGeometry(QtCore.QRect(15, 15, 90, 30))
        self.myInformation.setStyleSheet("\n"
"font-size:22px;")
        self.myInformation.setObjectName("myInformation")
        self.label_25 = QtWidgets.QLabel(self.MyInformation)
        self.label_25.setGeometry(QtCore.QRect(480, 170, 191, 31))
        self.label_25.setStyleSheet("QLabel\n"
"{    \n"
"background:transparent;\n"
"font-size:16px;\n"
"}")
        self.label_25.setObjectName("label_25")
        self.widget_16 = QtWidgets.QWidget(self.MyInformation)
        self.widget_16.setGeometry(QtCore.QRect(0, 70, 851, 521))
        self.widget_16.setStyleSheet("    background:rgb(226, 232, 255);")
        self.widget_16.setObjectName("widget_16")
        self.widget_11 = QtWidgets.QWidget(self.widget_16)
        self.widget_11.setGeometry(QtCore.QRect(20, 20, 251, 221))
        self.widget_11.setStyleSheet("#widget_11\n"
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
        self.widget_11.setObjectName("widget_11")
        self.label_18 = QtWidgets.QLabel(self.widget_11)
        self.label_18.setGeometry(QtCore.QRect(20, 90, 81, 16))
        self.label_18.setObjectName("label_18")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_11)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 170, 75, 20))
        self.pushButton_3.setStyleSheet("QPushButton\n"
"{\n"
" border-radius:5px;font-size:16px;background:rgb(200, 222,255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background:rgb(142, 182, 255)\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_11)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 170, 75, 20))
        self.pushButton_4.setStyleSheet("QPushButton\n"
"{\n"
" border-radius:5px;font-size:16px;background:rgb(200, 222,255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background:rgb(142, 182, 255)\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.mFraction = QtWidgets.QLabel(self.widget_11)
        self.mFraction.setGeometry(QtCore.QRect(60, 120, 131, 31))
        self.mFraction.setStyleSheet("\n"
"font-size:30px;")
        self.mFraction.setObjectName("mFraction")
        self.widget_15 = QtWidgets.QWidget(self.widget_11)
        self.widget_15.setGeometry(QtCore.QRect(0, 0, 251, 41))
        self.widget_15.setStyleSheet("QWidget\n"
"{\n"
"    background:rgb(165, 200, 255);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"")
        self.widget_15.setObjectName("widget_15")
        self.label_17 = QtWidgets.QLabel(self.widget_15)
        self.label_17.setGeometry(QtCore.QRect(20, 15, 111, 21))
        self.label_17.setStyleSheet("font-size:22px;")
        self.label_17.setObjectName("label_17")
        self.label_18.raise_()
        self.pushButton_4.raise_()
        self.mFraction.raise_()
        self.widget_15.raise_()
        self.pushButton_3.raise_()
        self.widget_14 = QtWidgets.QWidget(self.widget_16)
        self.widget_14.setGeometry(QtCore.QRect(20, 250, 361, 231))
        self.widget_14.setStyleSheet("#widget_14\n"
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
        self.widget_14.setObjectName("widget_14")
        self.label_19 = QtWidgets.QLabel(self.widget_14)
        self.label_19.setGeometry(QtCore.QRect(20, 10, 54, 20))
        self.label_19.setStyleSheet("font-size:20px;")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.widget_14)
        self.label_20.setGeometry(QtCore.QRect(30, 40, 81, 21))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.widget_14)
        self.label_21.setGeometry(QtCore.QRect(110, 110, 111, 21))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.widget_14)
        self.label_22.setGeometry(QtCore.QRect(80, 80, 54, 12))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.widget_14)
        self.label_23.setGeometry(QtCore.QRect(40, 160, 121, 20))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.widget_14)
        self.label_24.setGeometry(QtCore.QRect(160, 160, 31, 20))
        self.label_24.setStyleSheet("\n"
"font-size:30px;")
        self.label_24.setObjectName("label_24")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_14)
        self.pushButton_5.setGeometry(QtCore.QRect(190, 20, 151, 91))
        self.pushButton_5.setStyleSheet("QPushButton\n"
"{\n"
"background:transparent;\n"
"image:url(:/icon/晴.png)；\n"
"}")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_27 = QtWidgets.QLabel(self.widget_16)
        self.label_27.setGeometry(QtCore.QRect(280, 20, 541, 221))
        self.label_27.setStyleSheet("\n"
"    background:white;\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"\n"
"font-size:25px;\n"
"\n"
"")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.widget_16)
        self.label_28.setGeometry(QtCore.QRect(390, 250, 431, 231))
        self.label_28.setStyleSheet("\n"
"    background:white;\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"\n"
"font-size:25px;\n"
"\n"
"")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.stackedWidget.addWidget(self.MyInformation)
        self.MyContract = QtWidgets.QWidget()
        self.MyContract.setObjectName("MyContract")
        self.myContract = QtWidgets.QLabel(self.MyContract)
        self.myContract.setGeometry(QtCore.QRect(15, 15, 90, 30))
        self.myContract.setStyleSheet("\n"
"font-size:22px;")
        self.myContract.setObjectName("myContract")
        self.widget_17 = QtWidgets.QWidget(self.MyContract)
        self.widget_17.setGeometry(QtCore.QRect(0, 70, 851, 501))
        self.widget_17.setStyleSheet("QWidget\n"
"{\n"
"\n"
"    background:rgb(226, 232, 255);\n"
"}\n"
"QLabel\n"
"{    \n"
"background:transparent;\n"
"font-size:16px;\n"
"}")
        self.widget_17.setObjectName("widget_17")
        self.widget_10 = QtWidgets.QWidget(self.widget_17)
        self.widget_10.setGeometry(QtCore.QRect(580, 20, 251, 211))
        self.widget_10.setStyleSheet("#widget_10\n"
"{\n"
"    background:white;\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"\n"
"\n"
"QLabel\n"
"{    \n"
"font-size:16px;\n"
"}")
        self.widget_10.setObjectName("widget_10")
        self.label_13 = QtWidgets.QLabel(self.widget_10)
        self.label_13.setGeometry(QtCore.QRect(20, 80, 81, 16))
        self.label_13.setObjectName("label_13")
        self.pushButton = QtWidgets.QPushButton(self.widget_10)
        self.pushButton.setGeometry(QtCore.QRect(30, 170, 75, 20))
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
" border-radius:5px;font-size:16px;background:rgb(200, 222,255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background:rgb(142, 182, 255)\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_10)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 170, 75, 20))
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
" border-radius:5px;font-size:16px;background:rgb(200, 222,255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background:rgb(142, 182, 255)\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.fraction = QtWidgets.QLabel(self.widget_10)
        self.fraction.setGeometry(QtCore.QRect(60, 110, 131, 31))
        self.fraction.setStyleSheet("\n"
"font-size:30px;")
        self.fraction.setObjectName("fraction")
        self.widget_20 = QtWidgets.QWidget(self.widget_10)
        self.widget_20.setGeometry(QtCore.QRect(0, 0, 251, 41))
        self.widget_20.setStyleSheet("QWidget\n"
"{\n"
"    background:rgb(165, 200, 255);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"")
        self.widget_20.setObjectName("widget_20")
        self.label_26 = QtWidgets.QLabel(self.widget_20)
        self.label_26.setGeometry(QtCore.QRect(20, 15, 81, 20))
        self.label_26.setObjectName("label_26")
        self.widget_9 = QtWidgets.QWidget(self.widget_17)
        self.widget_9.setGeometry(QtCore.QRect(580, 250, 251, 241))
        self.widget_9.setStyleSheet("#widget_9\n"
"{\n"
"    background:white;\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"\n"
"\n"
"QLabel\n"
"{    \n"
"font-size:16px;\n"
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
        self.widget_9.setObjectName("widget_9")
        self.status = QtWidgets.QLineEdit(self.widget_9)
        self.status.setGeometry(QtCore.QRect(90, 110, 113, 20))
        self.status.setReadOnly(True)
        self.status.setObjectName("status")
        self.label_8 = QtWidgets.QLabel(self.widget_9)
        self.label_8.setGeometry(QtCore.QRect(10, 110, 51, 20))
        self.label_8.setObjectName("label_8")
        self.rentTime = QtWidgets.QLineEdit(self.widget_9)
        self.rentTime.setGeometry(QtCore.QRect(110, 80, 113, 20))
        self.rentTime.setReadOnly(True)
        self.rentTime.setObjectName("rentTime")
        self.label_6 = QtWidgets.QLabel(self.widget_9)
        self.label_6.setGeometry(QtCore.QRect(10, 80, 81, 20))
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.widget_9)
        self.label_9.setGeometry(QtCore.QRect(10, 140, 111, 16))
        self.label_9.setObjectName("label_9")
        self.ceoSignature = QtWidgets.QCheckBox(self.widget_9)
        self.ceoSignature.setGeometry(QtCore.QRect(130, 140, 71, 20))
        self.ceoSignature.setStyleSheet("\n"
"background:transparent;\n"
"")
        self.ceoSignature.setCheckable(False)
        self.ceoSignature.setChecked(False)
        self.ceoSignature.setObjectName("ceoSignature")
        self.label_10 = QtWidgets.QLabel(self.widget_9)
        self.label_10.setGeometry(QtCore.QRect(10, 170, 81, 21))
        self.label_10.setObjectName("label_10")
        self.signatureConfirmation = QtWidgets.QCheckBox(self.widget_9)
        self.signatureConfirmation.setGeometry(QtCore.QRect(100, 170, 71, 20))
        self.signatureConfirmation.setStyleSheet("background:transparent;")
        self.signatureConfirmation.setObjectName("signatureConfirmation")
        self.mySignature = QtWidgets.QLineEdit(self.widget_9)
        self.mySignature.setGeometry(QtCore.QRect(10, 200, 141, 20))
        self.mySignature.setObjectName("mySignature")
        self.confirmSignature = QtWidgets.QPushButton(self.widget_9)
        self.confirmSignature.setGeometry(QtCore.QRect(160, 200, 75, 20))
        self.confirmSignature.setStyleSheet("QPushButton\n"
"{\n"
" border-radius:5px;font-size:16px;background:rgb(200, 222,255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background:rgb(142, 182, 255)\n"
"}")
        self.confirmSignature.setObjectName("confirmSignature")
        self.widget_21 = QtWidgets.QWidget(self.widget_9)
        self.widget_21.setGeometry(QtCore.QRect(0, 0, 251, 41))
        self.widget_21.setStyleSheet("QWidget\n"
"{\n"
"    background:rgb(165, 200, 255);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"")
        self.widget_21.setObjectName("widget_21")
        self.label_12 = QtWidgets.QLabel(self.widget_21)
        self.label_12.setGeometry(QtCore.QRect(20, 10, 80, 25))
        self.label_12.setObjectName("label_12")
        self.ContractWidget = QtWidgets.QWidget(self.widget_17)
        self.ContractWidget.setGeometry(QtCore.QRect(20, 20, 550, 470))
        self.ContractWidget.setStyleSheet("#ContractWidget\n"
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
        self.ContractWidget.setObjectName("ContractWidget")
        self.contractInf = QtWidgets.QTextEdit(self.ContractWidget)
        self.contractInf.setGeometry(QtCore.QRect(19, 70, 511, 391))
        self.contractInf.setStyleSheet("QTextEdit\n"
"{\n"
" background:transparent;\n"
"    padding-left:5px ;\n"
"    padding-top:1px ;\n"
"    border-bottom-left-radius:9px;\n"
"    border-bottom-right-radius:9px;\n"
"    border: 1px solid rgb(123 ,123 , 123);\n"
"}")
        self.contractInf.setReadOnly(True)
        self.contractInf.setObjectName("contractInf")
        self.label_5 = QtWidgets.QLabel(self.ContractWidget)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 81, 31))
        self.label_5.setObjectName("label_5")
        self.widget_22 = QtWidgets.QWidget(self.ContractWidget)
        self.widget_22.setGeometry(QtCore.QRect(0, 0, 551, 41))
        self.widget_22.setStyleSheet("QWidget\n"
"{\n"
"    background:rgb(165, 200, 255);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"")
        self.widget_22.setObjectName("widget_22")
        self.contractInf.raise_()
        self.widget_22.raise_()
        self.label_5.raise_()
        self.stackedWidget.addWidget(self.MyContract)
        self.ApplyForSublease = QtWidgets.QWidget()
        self.ApplyForSublease.setObjectName("ApplyForSublease")
        self.applyForSublease = QtWidgets.QLabel(self.ApplyForSublease)
        self.applyForSublease.setGeometry(QtCore.QRect(30, 20, 54, 12))
        self.applyForSublease.setObjectName("applyForSublease")
        self.stackedWidget.addWidget(self.ApplyForSublease)

        self.retranslateUi(ProprietorWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidgetShop.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ProprietorWindow)

    def retranslateUi(self, ProprietorWindow):
        _translate = QtCore.QCoreApplication.translate
        ProprietorWindow.setWindowTitle(_translate("ProprietorWindow", "Form"))
        self.label.setText(_translate("ProprietorWindow", "JOJO购物中心"))
        self.btnMyShop.setText(_translate("ProprietorWindow", "我的店铺"))
        self.btnAllShop.setText(_translate("ProprietorWindow", "申请进场"))
        self.btnInf.setText(_translate("ProprietorWindow", "我的信息"))
        self.btnContract.setText(_translate("ProprietorWindow", "我的合同"))
        self.btnSublease.setText(_translate("ProprietorWindow", "申请转租"))
        self.allShop.setText(_translate("ProprietorWindow", "申请进场"))
        self.pushButtonShop_12.setText(_translate("ProprietorWindow", "12"))
        self.pushButtonShop_11.setText(_translate("ProprietorWindow", "11"))
        self.pushButtonShop_01.setText(_translate("ProprietorWindow", "01"))
        self.pushButtonShop_04.setText(_translate("ProprietorWindow", "04"))
        self.pushButtonShop_08.setText(_translate("ProprietorWindow", "08"))
        self.pushButtonShop_09.setText(_translate("ProprietorWindow", "09"))
        self.pushButtonShop_10.setText(_translate("ProprietorWindow", "10"))
        self.pushButtonShop_02.setText(_translate("ProprietorWindow", "02"))
        self.pushButtonShop_06.setText(_translate("ProprietorWindow", "06"))
        self.pushButtonShop_03.setText(_translate("ProprietorWindow", "03"))
        self.pushButtonShop_05.setText(_translate("ProprietorWindow", "05"))
        self.pushButtonShop_07.setText(_translate("ProprietorWindow", "07"))
        self.pushButtonShop_13.setText(_translate("ProprietorWindow", "13"))
        self.pushButtonShop_14.setText(_translate("ProprietorWindow", "14"))
        self.pushButtonShop_.setText(_translate("ProprietorWindow", "16"))
        self.pushButtonShop_5.setText(_translate("ProprietorWindow", "17"))
        self.pushButtonShop_17.setText(_translate("ProprietorWindow", "17"))
        self.pushButtonShop_15.setText(_translate("ProprietorWindow", "15"))
        self.pushButtonShop_16.setText(_translate("ProprietorWindow", "16"))
        self.pushButtonShop_18.setText(_translate("ProprietorWindow", "18"))
        self.pushButtonShop_19.setText(_translate("ProprietorWindow", "19"))
        self.pushButtonShop_24.setText(_translate("ProprietorWindow", "24"))
        self.pushButtonShop_23.setText(_translate("ProprietorWindow", "23"))
        self.pushButtonShop_20.setText(_translate("ProprietorWindow", "20"))
        self.label_15.setText(_translate("ProprietorWindow", "申请进场"))
        self.label_51.setText(_translate("ProprietorWindow", "姓名："))
        self.label_52.setText(_translate("ProprietorWindow", "租借用途："))
        self.label_53.setText(_translate("ProprietorWindow", "联系方式："))
        self.label_54.setText(_translate("ProprietorWindow", "租用时间："))
        self.immediateApplication.setText(_translate("ProprietorWindow", "立即申请"))
        self.label_11.setText(_translate("ProprietorWindow", "商铺号："))
        self.label_14.setText(_translate("ProprietorWindow", "店铺信息"))
        self.areaCoveredLalel.setText(_translate("ProprietorWindow", "占地面积："))
        self.annualRentLabel.setText(_translate("ProprietorWindow", "年租金："))
        self.depositLabel.setText(_translate("ProprietorWindow", "保证金："))
        self.propertyFeeLabel.setText(_translate("ProprietorWindow", "物业费："))
        self.label_2.setText(_translate("ProprietorWindow", "已租店铺"))
        self.label_4.setText(_translate("ProprietorWindow", "可租店铺"))
        self.label_7.setText(_translate("ProprietorWindow", "楼层信息"))
        self.label_3.setText(_translate("ProprietorWindow", "楼层："))
        self.curFloor.setText(_translate("ProprietorWindow", "1f"))
        self.label_16.setText(_translate("ProprietorWindow", "当前楼层："))
        self.myShop.setText(_translate("ProprietorWindow", "我的店铺"))
        self.PayImmediately.setText(_translate("ProprietorWindow", "立即缴费"))
        self.waterChargeLabel.setText(_translate("ProprietorWindow", "应缴水费："))
        self.propertyFeeChargeLabel.setText(_translate("ProprietorWindow", "应缴物业费："))
        self.electricChargeLabel.setText(_translate("ProprietorWindow", "应缴电费："))
        self.guaranteeChargeLabel.setText(_translate("ProprietorWindow", "保证金："))
        self.label_29.setText(_translate("ProprietorWindow", "广告位招租"))
        self.ReceiptCharge.setText(_translate("ProprietorWindow", "我的账单"))
        self.ReceivableCharge.setText(_translate("ProprietorWindow", "已缴费用"))
        self.waterChargeLabel_3.setText(_translate("ProprietorWindow", "水费余额："))
        self.electricChargeLabel_3.setText(_translate("ProprietorWindow", "电费余额："))
        self.propertyFeeChargeLabel_3.setText(_translate("ProprietorWindow", "已缴物业费："))
        self.guaranteeChargeLabel_3.setText(_translate("ProprietorWindow", "已缴保证金："))
        self.myInformation.setText(_translate("ProprietorWindow", "我的信息"))
        self.label_25.setText(_translate("ProprietorWindow", "这里应该有东西"))
        self.label_18.setText(_translate("ProprietorWindow", "我的信用："))
        self.pushButton_3.setText(_translate("ProprietorWindow", "晒晒分"))
        self.pushButton_4.setText(_translate("ProprietorWindow", "了解分"))
        self.mFraction.setText(_translate("ProprietorWindow", "TextLabel"))
        self.label_17.setText(_translate("ProprietorWindow", "信用信息："))
        self.label_19.setText(_translate("ProprietorWindow", "无锡"))
        self.label_20.setText(_translate("ProprietorWindow", "当前天气"))
        self.label_21.setText(_translate("ProprietorWindow", "温度：26-32℃"))
        self.label_22.setText(_translate("ProprietorWindow", "27℃"))
        self.label_23.setText(_translate("ProprietorWindow", "实时空气质量："))
        self.label_24.setText(_translate("ProprietorWindow", "34"))
        self.label_27.setText(_translate("ProprietorWindow", "广告位招租"))
        self.label_28.setText(_translate("ProprietorWindow", "广告位招租"))
        self.myContract.setText(_translate("ProprietorWindow", "我的合同"))
        self.label_13.setText(_translate("ProprietorWindow", "我的信用："))
        self.pushButton.setText(_translate("ProprietorWindow", "晒晒分"))
        self.pushButton_2.setText(_translate("ProprietorWindow", "了解分"))
        self.fraction.setText(_translate("ProprietorWindow", "TextLabel"))
        self.label_26.setText(_translate("ProprietorWindow", "信用信息："))
        self.label_8.setText(_translate("ProprietorWindow", "状态:"))
        self.label_6.setText(_translate("ProprietorWindow", "签订年份:"))
        self.label_9.setText(_translate("ProprietorWindow", "CEO签字情况："))
        self.ceoSignature.setText(_translate("ProprietorWindow", "已签字"))
        self.label_10.setText(_translate("ProprietorWindow", "我的签字:"))
        self.signatureConfirmation.setText(_translate("ProprietorWindow", "已签字"))
        self.confirmSignature.setText(_translate("ProprietorWindow", "确认"))
        self.label_12.setText(_translate("ProprietorWindow", "合同状态："))
        self.label_5.setText(_translate("ProprietorWindow", "合同内容："))
        self.applyForSublease.setText(_translate("ProprietorWindow", "申请转租"))

