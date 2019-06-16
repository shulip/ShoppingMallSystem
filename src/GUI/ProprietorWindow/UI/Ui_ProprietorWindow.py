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
        ProprietorWindow.resize(1078, 743)
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
"background:rgb(237, 251, 255)\n"
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
"\n"
"font-size:16px;\n"
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
        self.stackedWidget.setGeometry(QtCore.QRect(150, 30, 851, 571))
        self.stackedWidget.setStyleSheet("QWidget{\n"
"background:rgb(234, 234, 234)\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.AllShop = QtWidgets.QWidget()
        self.AllShop.setObjectName("AllShop")
        self.allShop = QtWidgets.QLabel(self.AllShop)
        self.allShop.setGeometry(QtCore.QRect(10, 10, 90, 30))
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
        self.firstFloorShop.setGeometry(QtCore.QRect(20, 20, 400, 471))
        self.firstFloorShop.setStyleSheet("#firstFloorShop\n"
"{\n"
"    background:white;\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"")
        self.firstFloorShop.setObjectName("firstFloorShop")
        self.widget = QtWidgets.QWidget(self.firstFloorShop)
        self.widget.setGeometry(QtCore.QRect(0, 0, 401, 51))
        self.widget.setStyleSheet("QWidget\n"
"{\n"
"    background:rgb(127, 127, 127);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.firstFloorShop)
        self.widget_2.setGeometry(QtCore.QRect(10, 60, 151, 391))
        self.widget_2.setStyleSheet("background: rgb(255, 201, 125);")
        self.widget_2.setObjectName("widget_2")
        self.pushButtonShop_12 = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonShop_12.setGeometry(QtCore.QRect(95, 10, 45, 370))
        self.pushButtonShop_12.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_12.setObjectName("pushButtonShop_12")
        self.pushButtonShop_11 = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonShop_11.setGeometry(QtCore.QRect(10, 210, 70, 170))
        self.pushButtonShop_11.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_11.setObjectName("pushButtonShop_11")
        self.pushButtonShop_01 = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonShop_01.setGeometry(QtCore.QRect(10, 10, 70, 70))
        self.pushButtonShop_01.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_01.setObjectName("pushButtonShop_01")
        self.pushButtonShop_04 = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonShop_04.setGeometry(QtCore.QRect(10, 90, 70, 45))
        self.pushButtonShop_04.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_04.setObjectName("pushButtonShop_04")
        self.pushButtonShop_08 = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonShop_08.setGeometry(QtCore.QRect(10, 150, 70, 41))
        self.pushButtonShop_08.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_08.setObjectName("pushButtonShop_08")
        self.widget_3 = QtWidgets.QWidget(self.firstFloorShop)
        self.widget_3.setGeometry(QtCore.QRect(160, 320, 230, 130))
        self.widget_3.setStyleSheet("background: rgb(255, 201, 125);")
        self.widget_3.setObjectName("widget_3")
        self.pushButtonShop_09 = QtWidgets.QPushButton(self.widget_3)
        self.pushButtonShop_09.setGeometry(QtCore.QRect(10, 10, 210, 40))
        self.pushButtonShop_09.setStyleSheet("background:rgb(0, 255, 127)")
        self.pushButtonShop_09.setObjectName("pushButtonShop_09")
        self.pushButtonShop_10 = QtWidgets.QPushButton(self.widget_3)
        self.pushButtonShop_10.setGeometry(QtCore.QRect(10, 80, 210, 40))
        self.pushButtonShop_10.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_10.setObjectName("pushButtonShop_10")
        self.widget_4 = QtWidgets.QWidget(self.firstFloorShop)
        self.widget_4.setGeometry(QtCore.QRect(160, 60, 231, 131))
        self.widget_4.setStyleSheet("background: rgb(255, 201, 125);")
        self.widget_4.setObjectName("widget_4")
        self.pushButtonShop_02 = QtWidgets.QPushButton(self.widget_4)
        self.pushButtonShop_02.setGeometry(QtCore.QRect(5, 10, 91, 41))
        self.pushButtonShop_02.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"background:rgb(0, 255, 127)\n"
"}")
        self.pushButtonShop_02.setObjectName("pushButtonShop_02")
        self.pushButtonShop_06 = QtWidgets.QPushButton(self.widget_4)
        self.pushButtonShop_06.setGeometry(QtCore.QRect(75, 85, 81, 40))
        self.pushButtonShop_06.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_06.setObjectName("pushButtonShop_06")
        self.pushButtonShop_03 = QtWidgets.QPushButton(self.widget_4)
        self.pushButtonShop_03.setGeometry(QtCore.QRect(100, 10, 125, 40))
        self.pushButtonShop_03.setStyleSheet("background:rgb(0, 255, 127)")
        self.pushButtonShop_03.setObjectName("pushButtonShop_03")
        self.pushButtonShop_05 = QtWidgets.QPushButton(self.widget_4)
        self.pushButtonShop_05.setGeometry(QtCore.QRect(10, 85, 61, 40))
        self.pushButtonShop_05.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_05.setObjectName("pushButtonShop_05")
        self.pushButtonShop_07 = QtWidgets.QPushButton(self.widget_4)
        self.pushButtonShop_07.setGeometry(QtCore.QRect(160, 85, 65, 40))
        self.pushButtonShop_07.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_07.setObjectName("pushButtonShop_07")
        self.stackedWidgetShop.addWidget(self._1f)
        self._2f = QtWidgets.QWidget()
        self._2f.setObjectName("_2f")
        self.firstFloorShop_2 = QtWidgets.QWidget(self._2f)
        self.firstFloorShop_2.setGeometry(QtCore.QRect(20, 20, 401, 471))
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
        self.widget_5.setGeometry(QtCore.QRect(0, 0, 401, 51))
        self.widget_5.setStyleSheet("QWidget\n"
"{\n"
"    background:rgb(127, 127, 127);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"")
        self.widget_5.setObjectName("widget_5")
        self.widget_6 = QtWidgets.QWidget(self.firstFloorShop_2)
        self.widget_6.setGeometry(QtCore.QRect(10, 60, 151, 391))
        self.widget_6.setStyleSheet("background: rgb(255, 201, 125);")
        self.widget_6.setObjectName("widget_6")
        self.pushButtonShop_13 = QtWidgets.QPushButton(self.widget_6)
        self.pushButtonShop_13.setGeometry(QtCore.QRect(95, 10, 45, 370))
        self.pushButtonShop_13.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_13.setObjectName("pushButtonShop_13")
        self.pushButtonShop_14 = QtWidgets.QPushButton(self.widget_6)
        self.pushButtonShop_14.setGeometry(QtCore.QRect(10, 210, 70, 170))
        self.pushButtonShop_14.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_14.setObjectName("pushButtonShop_14")
        self.pushButtonShop_ = QtWidgets.QPushButton(self.widget_6)
        self.pushButtonShop_.setGeometry(QtCore.QRect(10, 10, 70, 70))
        self.pushButtonShop_.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_.setObjectName("pushButtonShop_")
        self.pushButtonShop_5 = QtWidgets.QPushButton(self.widget_6)
        self.pushButtonShop_5.setGeometry(QtCore.QRect(10, 90, 70, 45))
        self.pushButtonShop_5.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_5.setObjectName("pushButtonShop_5")
        self.pushButtonShop_17 = QtWidgets.QPushButton(self.widget_6)
        self.pushButtonShop_17.setGeometry(QtCore.QRect(10, 150, 70, 41))
        self.pushButtonShop_17.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_17.setObjectName("pushButtonShop_17")
        self.widget_7 = QtWidgets.QWidget(self.firstFloorShop_2)
        self.widget_7.setGeometry(QtCore.QRect(160, 320, 231, 130))
        self.widget_7.setStyleSheet("background: rgb(255, 201, 125);")
        self.widget_7.setObjectName("widget_7")
        self.pushButtonShop_15 = QtWidgets.QPushButton(self.widget_7)
        self.pushButtonShop_15.setGeometry(QtCore.QRect(10, 10, 210, 40))
        self.pushButtonShop_15.setStyleSheet("background:rgb(0, 255, 127)")
        self.pushButtonShop_15.setObjectName("pushButtonShop_15")
        self.pushButtonShop_16 = QtWidgets.QPushButton(self.widget_7)
        self.pushButtonShop_16.setGeometry(QtCore.QRect(10, 80, 210, 40))
        self.pushButtonShop_16.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_16.setObjectName("pushButtonShop_16")
        self.widget_8 = QtWidgets.QWidget(self.firstFloorShop_2)
        self.widget_8.setGeometry(QtCore.QRect(160, 60, 231, 131))
        self.widget_8.setStyleSheet("background: rgb(255, 201, 125);")
        self.widget_8.setObjectName("widget_8")
        self.pushButtonShop_18 = QtWidgets.QPushButton(self.widget_8)
        self.pushButtonShop_18.setGeometry(QtCore.QRect(10, 85, 61, 41))
        self.pushButtonShop_18.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"background:rgb(0, 255, 127)\n"
"}")
        self.pushButtonShop_18.setObjectName("pushButtonShop_18")
        self.pushButtonShop_19 = QtWidgets.QPushButton(self.widget_8)
        self.pushButtonShop_19.setGeometry(QtCore.QRect(75, 85, 81, 40))
        self.pushButtonShop_19.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_19.setObjectName("pushButtonShop_19")
        self.pushButtonShop_24 = QtWidgets.QPushButton(self.widget_8)
        self.pushButtonShop_24.setGeometry(QtCore.QRect(100, 10, 125, 40))
        self.pushButtonShop_24.setStyleSheet("background:rgb(0, 255, 127)")
        self.pushButtonShop_24.setObjectName("pushButtonShop_24")
        self.pushButtonShop_23 = QtWidgets.QPushButton(self.widget_8)
        self.pushButtonShop_23.setGeometry(QtCore.QRect(10, 10, 81, 40))
        self.pushButtonShop_23.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_23.setObjectName("pushButtonShop_23")
        self.pushButtonShop_20 = QtWidgets.QPushButton(self.widget_8)
        self.pushButtonShop_20.setGeometry(QtCore.QRect(160, 85, 65, 40))
        self.pushButtonShop_20.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_20.setObjectName("pushButtonShop_20")
        self.stackedWidgetShop.addWidget(self._2f)
        self.applyInf = QtWidgets.QWidget(self.AllShop)
        self.applyInf.setGeometry(QtCore.QRect(440, 230, 380, 331))
        self.applyInf.setStyleSheet("#applyInf_3\n"
"{\n"
"    background:white;\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"\n"
"}\n"
"")
        self.applyInf.setObjectName("applyInf")
        self.widget_13 = QtWidgets.QWidget(self.applyInf)
        self.widget_13.setGeometry(QtCore.QRect(0, 0, 380, 40))
        self.widget_13.setStyleSheet("QWidget\n"
"{\n"
"    background:rgb(127, 127, 127);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"")
        self.widget_13.setObjectName("widget_13")
        self.label_15 = QtWidgets.QLabel(self.widget_13)
        self.label_15.setGeometry(QtCore.QRect(150, 5, 101, 31))
        self.label_15.setStyleSheet("font-size:22px")
        self.label_15.setObjectName("label_15")
        self.label_51 = QtWidgets.QLabel(self.applyInf)
        self.label_51.setGeometry(QtCore.QRect(40, 90, 61, 25))
        self.label_51.setStyleSheet("background:transparent;\n"
"font-size:16px;")
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.applyInf)
        self.label_52.setGeometry(QtCore.QRect(40, 180, 70, 25))
        self.label_52.setStyleSheet("background:transparent;\n"
"font-size:16px;")
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.applyInf)
        self.label_53.setGeometry(QtCore.QRect(40, 120, 70, 25))
        self.label_53.setStyleSheet("background:transparent;\n"
"font-size:16px;")
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.applyInf)
        self.label_54.setGeometry(QtCore.QRect(40, 150, 70, 25))
        self.label_54.setStyleSheet("background:transparent;\n"
"font-size:16px;")
        self.label_54.setObjectName("label_54")
        self.shopName = QtWidgets.QLineEdit(self.applyInf)
        self.shopName.setGeometry(QtCore.QRect(120, 90, 120, 25))
        self.shopName.setStyleSheet("background:rgb(206, 206, 206)")
        self.shopName.setObjectName("shopName")
        self.userTel = QtWidgets.QLineEdit(self.applyInf)
        self.userTel.setGeometry(QtCore.QRect(120, 120, 120, 25))
        self.userTel.setStyleSheet("background:rgb(206, 206, 206)")
        self.userTel.setObjectName("userTel")
        self.shopRentTime = QtWidgets.QLineEdit(self.applyInf)
        self.shopRentTime.setGeometry(QtCore.QRect(120, 150, 120, 25))
        self.shopRentTime.setStyleSheet("background:rgb(206, 206, 206)")
        self.shopRentTime.setObjectName("shopRentTime")
        self.shopReason = QtWidgets.QTextEdit(self.applyInf)
        self.shopReason.setGeometry(QtCore.QRect(120, 180, 240, 100))
        self.shopReason.setObjectName("shopReason")
        self.pushButton = QtWidgets.QPushButton(self.applyInf)
        self.pushButton.setGeometry(QtCore.QRect(290, 290, 75, 23))
        self.pushButton.setStyleSheet("\n"
"font-size:16px;")
        self.pushButton.setObjectName("pushButton")
        self.label_11 = QtWidgets.QLabel(self.applyInf)
        self.label_11.setGeometry(QtCore.QRect(40, 60, 50, 25))
        self.label_11.setStyleSheet("background:transparent;\n"
"font-size:16px;")
        self.label_11.setObjectName("label_11")
        self.shopName_2 = QtWidgets.QLineEdit(self.applyInf)
        self.shopName_2.setGeometry(QtCore.QRect(120, 60, 120, 25))
        self.shopName_2.setStyleSheet("background:rgb(206, 206, 206)")
        self.shopName_2.setObjectName("shopName_2")
        self.shopInfomation = QtWidgets.QWidget(self.AllShop)
        self.shopInfomation.setGeometry(QtCore.QRect(440, 90, 380, 131))
        self.shopInfomation.setStyleSheet("QWidget\n"
"{\n"
"    background:white;\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"font-size:16px;\n"
"}\n"
"")
        self.shopInfomation.setObjectName("shopInfomation")
        self.widget_12 = QtWidgets.QWidget(self.shopInfomation)
        self.widget_12.setGeometry(QtCore.QRect(0, 0, 380, 41))
        self.widget_12.setStyleSheet("QWidget\n"
"{\n"
"    background:rgb(127, 127, 127);\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
"")
        self.widget_12.setObjectName("widget_12")
        self.label_14 = QtWidgets.QLabel(self.widget_12)
        self.label_14.setGeometry(QtCore.QRect(150, 5, 101, 31))
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
        self.label_9 = QtWidgets.QLabel(self.shopInfomation)
        self.label_9.setGeometry(QtCore.QRect(310, 90, 54, 20))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.pushButton_13 = QtWidgets.QPushButton(self.AllShop)
        self.pushButton_13.setGeometry(QtCore.QRect(150, 105, 20, 20))
        self.pushButton_13.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(255, 0, 7);\n"
"border-radius:10px;\n"
"}")
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
"background:rgb(0, 255, 7);\n"
"border-radius:10px;\n"
"}")
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_7 = QtWidgets.QLabel(self.AllShop)
        self.label_7.setGeometry(QtCore.QRect(40, 100, 90, 30))
        self.label_7.setStyleSheet("font-size:22px;\n"
"background:transparent;")
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(self.AllShop)
        self.label_3.setGeometry(QtCore.QRect(310, 105, 50, 20))
        self.label_3.setStyleSheet("font-size:15px;\n"
"background:transparent;")
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.AllShop)
        self.comboBox.setGeometry(QtCore.QRect(360, 105, 40, 20))
        self.comboBox.setObjectName("comboBox")
        self.curFloor = QtWidgets.QLabel(self.AllShop)
        self.curFloor.setGeometry(QtCore.QRect(320, 320, 41, 16))
        self.curFloor.setStyleSheet("font-size:20px;\n"
"background:transparent;")
        self.curFloor.setObjectName("curFloor")
        self.label_16 = QtWidgets.QLabel(self.AllShop)
        self.label_16.setGeometry(QtCore.QRect(230, 310, 91, 31))
        self.label_16.setStyleSheet("font-size:20px;\n"
"background:transparent;")
        self.label_16.setObjectName("label_16")
        self.pushButton_2 = QtWidgets.QPushButton(self.AllShop)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 50, 61, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.AllShop)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 50, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.stackedWidget.addWidget(self.AllShop)
        self.MyShop = QtWidgets.QWidget()
        self.MyShop.setObjectName("MyShop")
        self.myShop = QtWidgets.QLabel(self.MyShop)
        self.myShop.setGeometry(QtCore.QRect(10, 10, 90, 31))
        self.myShop.setStyleSheet("\n"
"font-size:22px;")
        self.myShop.setObjectName("myShop")
        self.Receipt = QtWidgets.QWidget(self.MyShop)
        self.Receipt.setGeometry(QtCore.QRect(0, 100, 521, 471))
        self.Receipt.setStyleSheet("font-size:20px")
        self.Receipt.setObjectName("Receipt")
        self.electricChargeLabel = QtWidgets.QLabel(self.Receipt)
        self.electricChargeLabel.setGeometry(QtCore.QRect(60, 40, 90, 30))
        self.electricChargeLabel.setObjectName("electricChargeLabel")
        self.guaranteeChargeLabel = QtWidgets.QLabel(self.Receipt)
        self.guaranteeChargeLabel.setGeometry(QtCore.QRect(60, 80, 80, 30))
        self.guaranteeChargeLabel.setObjectName("guaranteeChargeLabel")
        self.propertyFeeChargeLabel = QtWidgets.QLabel(self.Receipt)
        self.propertyFeeChargeLabel.setGeometry(QtCore.QRect(60, 120, 110, 30))
        self.propertyFeeChargeLabel.setObjectName("propertyFeeChargeLabel")
        self.waterChargeLabel = QtWidgets.QLabel(self.Receipt)
        self.waterChargeLabel.setGeometry(QtCore.QRect(60, 160, 100, 30))
        self.waterChargeLabel.setObjectName("waterChargeLabel")
        self.guaranteeCharge = QtWidgets.QLabel(self.Receipt)
        self.guaranteeCharge.setGeometry(QtCore.QRect(180, 80, 80, 30))
        self.guaranteeCharge.setObjectName("guaranteeCharge")
        self.electricCharge = QtWidgets.QLabel(self.Receipt)
        self.electricCharge.setGeometry(QtCore.QRect(180, 40, 80, 30))
        self.electricCharge.setObjectName("electricCharge")
        self.propertyFeeCharge = QtWidgets.QLabel(self.Receipt)
        self.propertyFeeCharge.setGeometry(QtCore.QRect(180, 120, 80, 30))
        self.propertyFeeCharge.setObjectName("propertyFeeCharge")
        self.waterCharge = QtWidgets.QLabel(self.Receipt)
        self.waterCharge.setGeometry(QtCore.QRect(180, 160, 81, 30))
        self.waterCharge.setObjectName("waterCharge")
        self.PayImmediately = QtWidgets.QPushButton(self.Receipt)
        self.PayImmediately.setGeometry(QtCore.QRect(300, 220, 80, 30))
        self.PayImmediately.setStyleSheet("font-size:15px;\n"
"background:transparent;\n"
"")
        self.PayImmediately.setObjectName("PayImmediately")
        self.ReceiptCharge = QtWidgets.QPushButton(self.MyShop)
        self.ReceiptCharge.setGeometry(QtCore.QRect(0, 70, 80, 30))
        self.ReceiptCharge.setStyleSheet("\n"
"background:transparent;\n"
"")
        self.ReceiptCharge.setObjectName("ReceiptCharge")
        self.ReceivableCharge = QtWidgets.QPushButton(self.MyShop)
        self.ReceivableCharge.setGeometry(QtCore.QRect(80, 70, 80, 30))
        self.ReceivableCharge.setStyleSheet("\n"
"background:transparent;\n"
"")
        self.ReceivableCharge.setObjectName("ReceivableCharge")
        self.Receivable = QtWidgets.QWidget(self.MyShop)
        self.Receivable.setGeometry(QtCore.QRect(270, 100, 561, 471))
        self.Receivable.setStyleSheet("font-size:20px")
        self.Receivable.setObjectName("Receivable")
        self.guaranteeReceivable = QtWidgets.QLabel(self.Receivable)
        self.guaranteeReceivable.setGeometry(QtCore.QRect(220, 190, 80, 30))
        self.guaranteeReceivable.setObjectName("guaranteeReceivable")
        self.guaranteeChargeLabel_3 = QtWidgets.QLabel(self.Receivable)
        self.guaranteeChargeLabel_3.setGeometry(QtCore.QRect(100, 190, 80, 30))
        self.guaranteeChargeLabel_3.setObjectName("guaranteeChargeLabel_3")
        self.electricChargeLabel_3 = QtWidgets.QLabel(self.Receivable)
        self.electricChargeLabel_3.setGeometry(QtCore.QRect(100, 70, 90, 30))
        self.electricChargeLabel_3.setObjectName("electricChargeLabel_3")
        self.waterReceivable = QtWidgets.QLabel(self.Receivable)
        self.waterReceivable.setGeometry(QtCore.QRect(220, 110, 81, 30))
        self.waterReceivable.setObjectName("waterReceivable")
        self.propertyFeeReceivable = QtWidgets.QLabel(self.Receivable)
        self.propertyFeeReceivable.setGeometry(QtCore.QRect(220, 150, 80, 30))
        self.propertyFeeReceivable.setObjectName("propertyFeeReceivable")
        self.waterChargeLabel_3 = QtWidgets.QLabel(self.Receivable)
        self.waterChargeLabel_3.setGeometry(QtCore.QRect(100, 110, 100, 30))
        self.waterChargeLabel_3.setObjectName("waterChargeLabel_3")
        self.propertyFeeChargeLabel_3 = QtWidgets.QLabel(self.Receivable)
        self.propertyFeeChargeLabel_3.setGeometry(QtCore.QRect(100, 150, 110, 30))
        self.propertyFeeChargeLabel_3.setObjectName("propertyFeeChargeLabel_3")
        self.electricReceivable = QtWidgets.QLabel(self.Receivable)
        self.electricReceivable.setGeometry(QtCore.QRect(220, 70, 80, 30))
        self.electricReceivable.setObjectName("electricReceivable")
        self.myShop.raise_()
        self.ReceiptCharge.raise_()
        self.ReceivableCharge.raise_()
        self.Receipt.raise_()
        self.Receivable.raise_()
        self.stackedWidget.addWidget(self.MyShop)
        self.MyInformation = QtWidgets.QWidget()
        self.MyInformation.setObjectName("MyInformation")
        self.myInformation = QtWidgets.QLabel(self.MyInformation)
        self.myInformation.setGeometry(QtCore.QRect(10, 10, 90, 30))
        self.myInformation.setStyleSheet("\n"
"font-size:22px;")
        self.myInformation.setObjectName("myInformation")
        self.stackedWidget.addWidget(self.MyInformation)
        self.MyContract = QtWidgets.QWidget()
        self.MyContract.setObjectName("MyContract")
        self.myContract = QtWidgets.QLabel(self.MyContract)
        self.myContract.setGeometry(QtCore.QRect(10, 10, 90, 30))
        self.myContract.setStyleSheet("\n"
"font-size:22px;")
        self.myContract.setObjectName("myContract")
        self.ContractWidget = QtWidgets.QWidget(self.MyContract)
        self.ContractWidget.setGeometry(QtCore.QRect(20, 60, 400, 500))
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
"font-size:16px;\n"
"}")
        self.ContractWidget.setObjectName("ContractWidget")
        self.contractInf = QtWidgets.QTextEdit(self.ContractWidget)
        self.contractInf.setGeometry(QtCore.QRect(19, 80, 360, 160))
        self.contractInf.setReadOnly(True)
        self.contractInf.setObjectName("contractInf")
        self.label_5 = QtWidgets.QLabel(self.ContractWidget)
        self.label_5.setGeometry(QtCore.QRect(20, 40, 81, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.ContractWidget)
        self.label_6.setGeometry(QtCore.QRect(20, 250, 81, 21))
        self.label_6.setObjectName("label_6")
        self.rentTime = QtWidgets.QLabel(self.ContractWidget)
        self.rentTime.setGeometry(QtCore.QRect(110, 250, 54, 20))
        self.rentTime.setObjectName("rentTime")
        self.label_8 = QtWidgets.QLabel(self.ContractWidget)
        self.label_8.setGeometry(QtCore.QRect(20, 290, 71, 21))
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.ContractWidget)
        self.label_10.setGeometry(QtCore.QRect(20, 330, 71, 21))
        self.label_10.setObjectName("label_10")
        self.stackedWidget.addWidget(self.MyContract)
        self.ApplyForSublease = QtWidgets.QWidget()
        self.ApplyForSublease.setObjectName("ApplyForSublease")
        self.applyForSublease = QtWidgets.QLabel(self.ApplyForSublease)
        self.applyForSublease.setGeometry(QtCore.QRect(30, 20, 54, 12))
        self.applyForSublease.setObjectName("applyForSublease")
        self.stackedWidget.addWidget(self.ApplyForSublease)

        self.retranslateUi(ProprietorWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidgetShop.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ProprietorWindow)

    def retranslateUi(self, ProprietorWindow):
        _translate = QtCore.QCoreApplication.translate
        ProprietorWindow.setWindowTitle(_translate("ProprietorWindow", "Form"))
        self.label.setText(_translate("ProprietorWindow", "Cool购物中心"))
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
        self.pushButton.setText(_translate("ProprietorWindow", "立即申请"))
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
        self.pushButton_2.setText(_translate("ProprietorWindow", "店铺情况"))
        self.pushButton_3.setText(_translate("ProprietorWindow", "申请查询"))
        self.myShop.setText(_translate("ProprietorWindow", "我的店铺"))
        self.electricChargeLabel.setText(_translate("ProprietorWindow", "应缴电费："))
        self.guaranteeChargeLabel.setText(_translate("ProprietorWindow", "保证金："))
        self.propertyFeeChargeLabel.setText(_translate("ProprietorWindow", "应缴物业费："))
        self.waterChargeLabel.setText(_translate("ProprietorWindow", "应缴水费："))
        self.guaranteeCharge.setText(_translate("ProprietorWindow", "TextLabel"))
        self.electricCharge.setText(_translate("ProprietorWindow", "TextLabel"))
        self.propertyFeeCharge.setText(_translate("ProprietorWindow", "TextLabel"))
        self.waterCharge.setText(_translate("ProprietorWindow", "TextLabel"))
        self.PayImmediately.setText(_translate("ProprietorWindow", "立即缴费"))
        self.ReceiptCharge.setText(_translate("ProprietorWindow", "我的账单"))
        self.ReceivableCharge.setText(_translate("ProprietorWindow", "已缴费用"))
        self.guaranteeReceivable.setText(_translate("ProprietorWindow", "TextLabel"))
        self.guaranteeChargeLabel_3.setText(_translate("ProprietorWindow", "已缴保证金："))
        self.electricChargeLabel_3.setText(_translate("ProprietorWindow", "电费余额："))
        self.waterReceivable.setText(_translate("ProprietorWindow", "TextLabel"))
        self.propertyFeeReceivable.setText(_translate("ProprietorWindow", "TextLabel"))
        self.waterChargeLabel_3.setText(_translate("ProprietorWindow", "水费余额："))
        self.propertyFeeChargeLabel_3.setText(_translate("ProprietorWindow", "已缴物业费："))
        self.electricReceivable.setText(_translate("ProprietorWindow", "TextLabel"))
        self.myInformation.setText(_translate("ProprietorWindow", "我的信息"))
        self.myContract.setText(_translate("ProprietorWindow", "我的合同"))
        self.label_5.setText(_translate("ProprietorWindow", "合同内容："))
        self.label_6.setText(_translate("ProprietorWindow", "签订年份:"))
        self.rentTime.setText(_translate("ProprietorWindow", "TextLabel"))
        self.label_8.setText(_translate("ProprietorWindow", "甲方签字"))
        self.label_10.setText(_translate("ProprietorWindow", "乙方签字"))
        self.applyForSublease.setText(_translate("ProprietorWindow", "申请转租"))

