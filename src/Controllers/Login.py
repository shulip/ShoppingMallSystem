import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from GUI.LoginWindow import Design_LoginWindow
from GUI import *
class Login(object):
    def __init__(self):
        self.__identity = ""
        self.__name = ""
        self.__password = ""

    def __judge(self):
        pass

    def __putin(self,name,password,identity):
        self.__name = name
        self.__password = password
        self.__identity = identity
        print("name:%s\npassword:%s\nidentity:%s\n"%(self.__name,self.__password,self.__identity))

    def run(self,name,password,identity):

        self.__putin(name,password,identity)
        self.__judge()
        app = QtWidgets.QApplication(sys.argv)


        if self.__identity == 'p':  # 业主
            Window = ProprietorWindow()
        elif self.__identity == 'ceo':     # CEO
            Window = CEOWindow()
        elif self.__identity == 'cfo':     # CFO
            Window = CEOWindow()
        else:       # 市场管理员
            Window = ManagerWindow()
        Window.show()
        Window.move(int((QApplication.desktop().width() - Window.width()) / 2),
                    int((QApplication.desktop().height() - Window.height()) / 2 - 50))
        sys.exit(app.exec_())

if __name__ == '__main__':
    login = Login()
    login.run("as","as","as")