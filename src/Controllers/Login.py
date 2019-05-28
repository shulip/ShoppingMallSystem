
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

    def run(self,name,password,identity):
        self.__putin(name,password,identity)
        self.__judge()
        if self.__identity == 'p':  # 业主
            pass
        elif self.__identity == 'ceo':     # CEO
            pass
        elif self.__identity == 'cfo':     # CFO
            pass
        elif self.__identity == 'm':       # 市场管理员
            pass

if __name__ == '__main__':
    login = Login()
    login.run("as","sa")