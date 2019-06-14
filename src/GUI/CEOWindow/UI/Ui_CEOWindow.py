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
        self.frame = QtWidgets.QFrame(CEOWindow)
        self.frame.setGeometry(QtCore.QRect(20, 20, 1000, 600))
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
        self.btnMenu_Min_2 = QtWidgets.QPushButton(self.widgetMenu)
        self.btnMenu_Min_2.setGeometry(QtCore.QRect(0, 0, 30, 30))
        self.btnMenu_Min_2.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"background:transparent;\n"
"    \n"
"    image: url(:/icon/5.png);\n"
"}")
        self.btnMenu_Min_2.setText("")
        self.btnMenu_Min_2.setIconSize(QtCore.QSize(30, 30))
        self.btnMenu_Min_2.setObjectName("btnMenu_Min_2")
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
        self.allShop.setGeometry(QtCore.QRect(0, 0, 91, 41))
        self.allShop.setStyleSheet("font-size:22px")
        self.allShop.setObjectName("allShop")
        self.stackedWidgetShop = QtWidgets.QStackedWidget(self.AllShop)
        self.stackedWidgetShop.setGeometry(QtCore.QRect(0, 40, 851, 531))
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
        self.firstFloorShop.setGeometry(QtCore.QRect(20, 30, 401, 471))
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
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(150, 10, 141, 31))
        self.label_7.setStyleSheet("font-size:22px")
        self.label_7.setObjectName("label_7")
        self.widget_2 = QtWidgets.QWidget(self.firstFloorShop)
        self.widget_2.setGeometry(QtCore.QRect(10, 60, 151, 361))
        self.widget_2.setStyleSheet("background: rgb(255, 201, 125);")
        self.widget_2.setObjectName("widget_2")
        self.pushButtonShop_12 = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonShop_12.setGeometry(QtCore.QRect(95, 9, 45, 351))
        self.pushButtonShop_12.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_12.setObjectName("pushButtonShop_12")
        self.pushButtonShop_11 = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonShop_11.setGeometry(QtCore.QRect(10, 220, 70, 140))
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
        self.widget_3.setGeometry(QtCore.QRect(160, 300, 231, 121))
        self.widget_3.setStyleSheet("background: rgb(255, 201, 125);")
        self.widget_3.setObjectName("widget_3")
        self.pushButtonShop_09 = QtWidgets.QPushButton(self.widget_3)
        self.pushButtonShop_09.setGeometry(QtCore.QRect(10, 10, 210, 40))
        self.pushButtonShop_09.setStyleSheet("background:rgb(0, 255, 127)")
        self.pushButtonShop_09.setObjectName("pushButtonShop_09")
        self.pushButtonShop_10 = QtWidgets.QPushButton(self.widget_3)
        self.pushButtonShop_10.setGeometry(QtCore.QRect(10, 70, 210, 40))
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
        self.pushButton_13 = QtWidgets.QPushButton(self.firstFloorShop)
        self.pushButton_13.setGeometry(QtCore.QRect(40, 430, 30, 30))
        self.pushButton_13.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_2 = QtWidgets.QLabel(self.firstFloorShop)
        self.label_2.setGeometry(QtCore.QRect(90, 430, 51, 30))
        self.label_2.setStyleSheet("background:transparent;")
        self.label_2.setObjectName("label_2")
        self.pushButton_15 = QtWidgets.QPushButton(self.firstFloorShop)
        self.pushButton_15.setGeometry(QtCore.QRect(240, 430, 30, 30))
        self.pushButton_15.setStyleSheet("background:rgb(0, 255, 127)")
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_4 = QtWidgets.QLabel(self.firstFloorShop)
        self.label_4.setGeometry(QtCore.QRect(280, 430, 50, 30))
        self.label_4.setStyleSheet("background:transparent;")
        self.label_4.setObjectName("label_4")
        self.stackedWidgetShop.addWidget(self._1f)
        self._2f = QtWidgets.QWidget()
        self._2f.setObjectName("_2f")
        self.firstFloorShop_2 = QtWidgets.QWidget(self._2f)
        self.firstFloorShop_2.setGeometry(QtCore.QRect(20, 30, 401, 471))
        self.firstFloorShop_2.setStyleSheet("#firstFloorShop\n"
"{\n"
"    background:white;\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"}\n"
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
        self.label_26 = QtWidgets.QLabel(self.widget_5)
        self.label_26.setGeometry(QtCore.QRect(150, 10, 141, 31))
        self.label_26.setStyleSheet("font-size:22px")
        self.label_26.setObjectName("label_26")
        self.widget_6 = QtWidgets.QWidget(self.firstFloorShop_2)
        self.widget_6.setGeometry(QtCore.QRect(10, 60, 151, 361))
        self.widget_6.setStyleSheet("background: rgb(255, 201, 125);")
        self.widget_6.setObjectName("widget_6")
        self.pushButtonShop_13 = QtWidgets.QPushButton(self.widget_6)
        self.pushButtonShop_13.setGeometry(QtCore.QRect(95, 9, 45, 351))
        self.pushButtonShop_13.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_13.setObjectName("pushButtonShop_13")
        self.pushButtonShop_14 = QtWidgets.QPushButton(self.widget_6)
        self.pushButtonShop_14.setGeometry(QtCore.QRect(10, 220, 70, 140))
        self.pushButtonShop_14.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_14.setObjectName("pushButtonShop_14")
        self.pushButtonShop_2 = QtWidgets.QPushButton(self.widget_6)
        self.pushButtonShop_2.setGeometry(QtCore.QRect(10, 10, 70, 70))
        self.pushButtonShop_2.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_2.setObjectName("pushButtonShop_2")
        self.pushButtonShop_5 = QtWidgets.QPushButton(self.widget_6)
        self.pushButtonShop_5.setGeometry(QtCore.QRect(10, 90, 70, 45))
        self.pushButtonShop_5.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_5.setObjectName("pushButtonShop_5")
        self.pushButtonShop_9 = QtWidgets.QPushButton(self.widget_6)
        self.pushButtonShop_9.setGeometry(QtCore.QRect(10, 150, 70, 41))
        self.pushButtonShop_9.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_9.setObjectName("pushButtonShop_9")
        self.widget_7 = QtWidgets.QWidget(self.firstFloorShop_2)
        self.widget_7.setGeometry(QtCore.QRect(160, 300, 231, 121))
        self.widget_7.setStyleSheet("background: rgb(255, 201, 125);")
        self.widget_7.setObjectName("widget_7")
        self.pushButtonShop_15 = QtWidgets.QPushButton(self.widget_7)
        self.pushButtonShop_15.setGeometry(QtCore.QRect(10, 10, 210, 40))
        self.pushButtonShop_15.setStyleSheet("background:rgb(0, 255, 127)")
        self.pushButtonShop_15.setObjectName("pushButtonShop_15")
        self.pushButtonShop_16 = QtWidgets.QPushButton(self.widget_7)
        self.pushButtonShop_16.setGeometry(QtCore.QRect(10, 70, 210, 40))
        self.pushButtonShop_16.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_16.setObjectName("pushButtonShop_16")
        self.widget_8 = QtWidgets.QWidget(self.firstFloorShop_2)
        self.widget_8.setGeometry(QtCore.QRect(160, 60, 231, 131))
        self.widget_8.setStyleSheet("background: rgb(255, 201, 125);")
        self.widget_8.setObjectName("widget_8")
        self.pushButtonShop_3 = QtWidgets.QPushButton(self.widget_8)
        self.pushButtonShop_3.setGeometry(QtCore.QRect(5, 10, 91, 41))
        self.pushButtonShop_3.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"background:rgb(0, 255, 127)\n"
"}")
        self.pushButtonShop_3.setObjectName("pushButtonShop_3")
        self.pushButtonShop_7 = QtWidgets.QPushButton(self.widget_8)
        self.pushButtonShop_7.setGeometry(QtCore.QRect(75, 85, 81, 40))
        self.pushButtonShop_7.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_7.setObjectName("pushButtonShop_7")
        self.pushButtonShop_4 = QtWidgets.QPushButton(self.widget_8)
        self.pushButtonShop_4.setGeometry(QtCore.QRect(100, 10, 125, 40))
        self.pushButtonShop_4.setStyleSheet("background:rgb(0, 255, 127)")
        self.pushButtonShop_4.setObjectName("pushButtonShop_4")
        self.pushButtonShop_6 = QtWidgets.QPushButton(self.widget_8)
        self.pushButtonShop_6.setGeometry(QtCore.QRect(10, 85, 61, 40))
        self.pushButtonShop_6.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_6.setObjectName("pushButtonShop_6")
        self.pushButtonShop_8 = QtWidgets.QPushButton(self.widget_8)
        self.pushButtonShop_8.setGeometry(QtCore.QRect(160, 85, 65, 40))
        self.pushButtonShop_8.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButtonShop_8.setObjectName("pushButtonShop_8")
        self.pushButton_14 = QtWidgets.QPushButton(self.firstFloorShop_2)
        self.pushButton_14.setGeometry(QtCore.QRect(40, 430, 30, 30))
        self.pushButton_14.setStyleSheet("background:rgb(255, 0, 4);")
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_27 = QtWidgets.QLabel(self.firstFloorShop_2)
        self.label_27.setGeometry(QtCore.QRect(90, 430, 51, 30))
        self.label_27.setStyleSheet("background:transparent;")
        self.label_27.setObjectName("label_27")
        self.pushButton_16 = QtWidgets.QPushButton(self.firstFloorShop_2)
        self.pushButton_16.setGeometry(QtCore.QRect(240, 430, 30, 30))
        self.pushButton_16.setStyleSheet("background:rgb(0, 255, 127)")
        self.pushButton_16.setText("")
        self.pushButton_16.setObjectName("pushButton_16")
        self.label_28 = QtWidgets.QLabel(self.firstFloorShop_2)
        self.label_28.setGeometry(QtCore.QRect(280, 430, 50, 30))
        self.label_28.setStyleSheet("background:transparent;")
        self.label_28.setObjectName("label_28")
        self.stackedWidgetShop.addWidget(self._2f)
        self.contractInf = QtWidgets.QWidget(self.AllShop)
        self.contractInf.setGeometry(QtCore.QRect(440, 230, 380, 311))
        self.contractInf.setStyleSheet("#contractInf\n"
"{\n"
"    background:white;\n"
"     border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"    font-size:14px\n"
"\n"
"}\n"
"")
        self.contractInf.setObjectName("contractInf")
        self.widget_13 = QtWidgets.QWidget(self.contractInf)
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
        self.ceoConfirm.setObjectName("ceoConfirm")
        self.userSignature = QtWidgets.QCheckBox(self.contractInf)
        self.userSignature.setGeometry(QtCore.QRect(110, 180, 71, 16))
        self.userSignature.setObjectName("userSignature")
        self.ceoSingature = QtWidgets.QCheckBox(self.contractInf)
        self.ceoSingature.setGeometry(QtCore.QRect(120, 210, 71, 16))
        self.ceoSingature.setObjectName("ceoSingature")
        self.rentTimeContract = QtWidgets.QLineEdit(self.contractInf)
        self.rentTimeContract.setGeometry(QtCore.QRect(110, 120, 113, 20))
        self.rentTimeContract.setObjectName("rentTimeContract")
        self.RentStateContract = QtWidgets.QLineEdit(self.contractInf)
        self.RentStateContract.setGeometry(QtCore.QRect(80, 90, 113, 20))
        self.RentStateContract.setObjectName("RentStateContract")
        self.shopNumberContract = QtWidgets.QLineEdit(self.contractInf)
        self.shopNumberContract.setGeometry(QtCore.QRect(100, 60, 113, 20))
        self.shopNumberContract.setObjectName("shopNumberContract")
        self.contractInfomation = QtWidgets.QTextEdit(self.contractInf)
        self.contractInfomation.setGeometry(QtCore.QRect(120, 230, 201, 71))
        self.contractInfomation.setObjectName("contractInfomation")
        self.shopInfomation = QtWidgets.QWidget(self.AllShop)
        self.shopInfomation.setGeometry(QtCore.QRect(440, 70, 380, 151))
        self.shopInfomation.setStyleSheet("#shopInfomation\n"
"{\n"
"    background:white;\n"
" border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"\n"
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
        self.shopNumberLabel = QtWidgets.QLabel(self.shopInfomation)
        self.shopNumberLabel.setGeometry(QtCore.QRect(10, 50, 60, 20))
        self.shopNumberLabel.setStyleSheet("background:transparent;\n"
"font-size:14px")
        self.shopNumberLabel.setObjectName("shopNumberLabel")
        self.rentStateLabel = QtWidgets.QLabel(self.shopInfomation)
        self.rentStateLabel.setGeometry(QtCore.QRect(10, 70, 60, 20))
        self.rentStateLabel.setStyleSheet("background:transparent;\n"
"font-size:14px")
        self.rentStateLabel.setObjectName("rentStateLabel")
        self.label_19 = QtWidgets.QLabel(self.shopInfomation)
        self.label_19.setGeometry(QtCore.QRect(10, 90, 60, 20))
        self.label_19.setStyleSheet("background:transparent;\n"
"font-size:14px")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.shopInfomation)
        self.label_20.setGeometry(QtCore.QRect(10, 110, 60, 20))
        self.label_20.setStyleSheet("background:transparent;\n"
"font-size:14px")
        self.label_20.setObjectName("label_20")
        self.shopNumberText = QtWidgets.QLineEdit(self.shopInfomation)
        self.shopNumberText.setGeometry(QtCore.QRect(75, 50, 70, 20))
        self.shopNumberText.setObjectName("shopNumberText")
        self.label_21 = QtWidgets.QLabel(self.shopInfomation)
        self.label_21.setGeometry(QtCore.QRect(160, 50, 75, 16))
        self.label_21.setStyleSheet("background:transparent;\n"
"font-size:14px")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.shopInfomation)
        self.label_22.setGeometry(QtCore.QRect(160, 70, 75, 20))
        self.label_22.setStyleSheet("background:transparent;\n"
"font-size:14px")
        self.label_22.setObjectName("label_22")
        self.checkBox_7 = QtWidgets.QCheckBox(self.shopInfomation)
        self.checkBox_7.setGeometry(QtCore.QRect(160, 90, 50, 20))
        self.checkBox_7.setStyleSheet("background:transparent;\n"
"font-size:14px")
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.shopInfomation)
        self.checkBox_8.setGeometry(QtCore.QRect(160, 110, 50, 20))
        self.checkBox_8.setStyleSheet("background:transparent;\n"
"font-size:14px")
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.shopInfomation)
        self.checkBox_9.setGeometry(QtCore.QRect(325, 50, 50, 20))
        self.checkBox_9.setStyleSheet("background:transparent;\n"
"font-size:14px")
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.shopInfomation)
        self.checkBox_10.setGeometry(QtCore.QRect(325, 70, 50, 20))
        self.checkBox_10.setStyleSheet("background:transparent;\n"
"font-size:14px")
        self.checkBox_10.setObjectName("checkBox_10")
        self.rentStateText = QtWidgets.QLineEdit(self.shopInfomation)
        self.rentStateText.setGeometry(QtCore.QRect(75, 70, 70, 20))
        self.rentStateText.setObjectName("rentStateText")
        self.waterFeePaid = QtWidgets.QLineEdit(self.shopInfomation)
        self.waterFeePaid.setGeometry(QtCore.QRect(75, 90, 70, 20))
        self.waterFeePaid.setObjectName("waterFeePaid")
        self.electricFeePaid = QtWidgets.QLineEdit(self.shopInfomation)
        self.electricFeePaid.setGeometry(QtCore.QRect(75, 110, 70, 20))
        self.electricFeePaid.setObjectName("electricFeePaid")
        self.propertyFee = QtWidgets.QLineEdit(self.shopInfomation)
        self.propertyFee.setGeometry(QtCore.QRect(240, 50, 70, 20))
        self.propertyFee.setObjectName("propertyFee")
        self.guaranteePaid = QtWidgets.QLineEdit(self.shopInfomation)
        self.guaranteePaid.setGeometry(QtCore.QRect(240, 70, 70, 20))
        self.guaranteePaid.setObjectName("guaranteePaid")
        self.stackedWidget.addWidget(self.AllShop)
        self.MyShop = QtWidgets.QWidget()
        self.MyShop.setObjectName("MyShop")
        self.myShop = QtWidgets.QLabel(self.MyShop)
        self.myShop.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.myShop.setStyleSheet("font-size:22px")
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
        self.myInformation.setGeometry(QtCore.QRect(20, 20, 54, 12))
        self.myInformation.setObjectName("myInformation")
        self.stackedWidget.addWidget(self.MyInformation)
        self.MyContract = QtWidgets.QWidget()
        self.MyContract.setObjectName("MyContract")
        self.myContract = QtWidgets.QLabel(self.MyContract)
        self.myContract.setGeometry(QtCore.QRect(20, 20, 54, 12))
        self.myContract.setObjectName("myContract")
        self.stackedWidget.addWidget(self.MyContract)
        self.ApplyForSublease = QtWidgets.QWidget()
        self.ApplyForSublease.setObjectName("ApplyForSublease")
        self.applyForSublease = QtWidgets.QLabel(self.ApplyForSublease)
        self.applyForSublease.setGeometry(QtCore.QRect(30, 20, 54, 12))
        self.applyForSublease.setObjectName("applyForSublease")
        self.stackedWidget.addWidget(self.ApplyForSublease)

        self.retranslateUi(CEOWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidgetShop.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CEOWindow)

    def retranslateUi(self, CEOWindow):
        _translate = QtCore.QCoreApplication.translate
        CEOWindow.setWindowTitle(_translate("CEOWindow", "Form"))
        self.label.setText(_translate("CEOWindow", "Cool购物中心"))
        self.btnMyShop.setText(_translate("CEOWindow", "我的店铺"))
        self.btnAllShop.setText(_translate("CEOWindow", "全部店铺"))
        self.btnInf.setText(_translate("CEOWindow", "我的信息"))
        self.btnContract.setText(_translate("CEOWindow", "我的合同"))
        self.btnSublease.setText(_translate("CEOWindow", "申请转租"))
        self.allShop.setText(_translate("CEOWindow", "全部店铺"))
        self.label_7.setText(_translate("CEOWindow", "楼层信息"))
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
        self.label_2.setText(_translate("CEOWindow", "已租店铺"))
        self.label_4.setText(_translate("CEOWindow", "可租店铺"))
        self.label_26.setText(_translate("CEOWindow", "楼层信息"))
        self.pushButtonShop_13.setText(_translate("CEOWindow", "12"))
        self.pushButtonShop_14.setText(_translate("CEOWindow", "11"))
        self.pushButtonShop_2.setText(_translate("CEOWindow", "01"))
        self.pushButtonShop_5.setText(_translate("CEOWindow", "04"))
        self.pushButtonShop_9.setText(_translate("CEOWindow", "08"))
        self.pushButtonShop_15.setText(_translate("CEOWindow", "09"))
        self.pushButtonShop_16.setText(_translate("CEOWindow", "10"))
        self.pushButtonShop_3.setText(_translate("CEOWindow", "02"))
        self.pushButtonShop_7.setText(_translate("CEOWindow", "06"))
        self.pushButtonShop_4.setText(_translate("CEOWindow", "03"))
        self.pushButtonShop_6.setText(_translate("CEOWindow", "05"))
        self.pushButtonShop_8.setText(_translate("CEOWindow", "07"))
        self.label_27.setText(_translate("CEOWindow", "已租店铺"))
        self.label_28.setText(_translate("CEOWindow", "可租店铺"))
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
        self.shopNumberLabel.setText(_translate("CEOWindow", "店铺编号："))
        self.rentStateLabel.setText(_translate("CEOWindow", "租借状态："))
        self.label_19.setText(_translate("CEOWindow", "已缴水费："))
        self.label_20.setText(_translate("CEOWindow", "已缴电费："))
        self.label_21.setText(_translate("CEOWindow", "已缴物业费："))
        self.label_22.setText(_translate("CEOWindow", "已缴保证金："))
        self.checkBox_7.setText(_translate("CEOWindow", "欠费"))
        self.checkBox_8.setText(_translate("CEOWindow", "欠费"))
        self.checkBox_9.setText(_translate("CEOWindow", "欠费"))
        self.checkBox_10.setText(_translate("CEOWindow", "欠费"))
        self.myShop.setText(_translate("CEOWindow", "我的店铺"))
        self.electricChargeLabel.setText(_translate("CEOWindow", "应缴电费："))
        self.guaranteeChargeLabel.setText(_translate("CEOWindow", "保证金："))
        self.propertyFeeChargeLabel.setText(_translate("CEOWindow", "应缴物业费："))
        self.waterChargeLabel.setText(_translate("CEOWindow", "应缴水费："))
        self.guaranteeCharge.setText(_translate("CEOWindow", "TextLabel"))
        self.electricCharge.setText(_translate("CEOWindow", "TextLabel"))
        self.propertyFeeCharge.setText(_translate("CEOWindow", "TextLabel"))
        self.waterCharge.setText(_translate("CEOWindow", "TextLabel"))
        self.PayImmediately.setText(_translate("CEOWindow", "立即缴费"))
        self.ReceiptCharge.setText(_translate("CEOWindow", "我的账单"))
        self.ReceivableCharge.setText(_translate("CEOWindow", "已缴费用"))
        self.guaranteeReceivable.setText(_translate("CEOWindow", "TextLabel"))
        self.guaranteeChargeLabel_3.setText(_translate("CEOWindow", "已缴保证金："))
        self.electricChargeLabel_3.setText(_translate("CEOWindow", "电费余额："))
        self.waterReceivable.setText(_translate("CEOWindow", "TextLabel"))
        self.propertyFeeReceivable.setText(_translate("CEOWindow", "TextLabel"))
        self.waterChargeLabel_3.setText(_translate("CEOWindow", "水费余额："))
        self.propertyFeeChargeLabel_3.setText(_translate("CEOWindow", "已缴物业费："))
        self.electricReceivable.setText(_translate("CEOWindow", "TextLabel"))
        self.myInformation.setText(_translate("CEOWindow", "我的信息"))
        self.myContract.setText(_translate("CEOWindow", "我的合同"))
        self.applyForSublease.setText(_translate("CEOWindow", "申请转租"))

from GUI.image import *
