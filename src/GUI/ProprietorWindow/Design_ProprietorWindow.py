#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QDesktopWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.Qt import QButtonGroup
from PyQt5.Qt import QListView
from PyQt5.Qt import QSplashScreen, QDateTime

from GUI.ProprietorWindow.UI import *

class Design_ProprietorWindow(QWidget,Ui_ProprietorWindow):

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def click_receipt(self):
        self.Receipt.setVisible(True)
        self.Receivable.setVisible(False)

    def click_receivable(self):
        self.Receipt.setVisible(False)
        self.Receivable.setVisible(True)

    def combox_changed(self, index):
        self.curFloor.setText(self.comboBox.itemText(index))

        if index==0:
            self.stackedWidgetShop.setCurrentIndex(0)
        elif index==1:
            self.stackedWidgetShop.setCurrentIndex(1)

    def __init__(self, parent=None):
        super(Design_ProprietorWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)


        self.setAttribute(Qt.WA_TranslucentBackground)

        #我的店铺
        self.btnAllShop.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.btnMyShop.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.btnContract.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.btnInf.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.ReceiptCharge.clicked.connect(self.click_receipt)
        self.ReceivableCharge.clicked.connect(self.click_receivable)
        self.btnMenu_Close.clicked.connect(self.close)
        self.Receipt.setVisible(True)
        self.Receivable.setVisible(False)

        #申请进场
        self.comboBox.addItem("1 楼")
        self.comboBox.addItem("2 楼")
        self.comboBox.currentIndexChanged.connect(lambda x: self.combox_changed(x))
        self.combox_changed(0)






if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = Design_ProprietorWindow()

    MainWindow.show()
    MainWindow.move(int((QApplication.desktop().width() - MainWindow.width()) / 2),
                        int((QApplication.desktop().height() - MainWindow.height()) / 2 - 50))
    sys.exit(app.exec_())