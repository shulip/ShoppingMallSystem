import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from GUI.LoginWindow import Design_LoginWindow
from GUI import ProprietorWindow,CEOWindow,ManagerWindow
class Login(object):
    def __init__(self):
        self.__identity = ""
        self.__ID = ""
        self.__password = ""

    def __judge(self):
        pass

    def __putin(self,ID,password,identity):
        self.__ID = ID
        self.__password = password
        self.__identity = identity
        print("name:%s\npassword:%s\nidentity:%s\n"%(self.__ID,self.__password,self.__identity))

    def run(self,name,password,identity):

        self.__putin(name,password,identity)
        self.__judge()
        print(1)
        # app = QtWidgets.QApplication(sys.argv)
        print(2)
        if self.__identity == "业主":  # 业主
            print(3)
            from GUI import ProprietorWindow
            self.Window = ProprietorWindow(self.__ID)
            print(4)
        elif self.__identity == 'ceo':     # CEO
            from GUI import CEOWindow
            self.Window = CEOWindow(self.__ID)
        else:       # 市场管理员
            from GUI import ManagerWindow
            self.Window = ManagerWindow(self.__ID)
        self.Window.show()
        # self.Window.move(int((QApplication.desktop().width() - Window.width()) / 2),
        #             int((QApplication.desktop().height() - Window.height()) / 2 - 50))
        # sys.exit(app.exec_())

if __name__ == '__main__':
    login = Login()
    login.run("as","as","as")