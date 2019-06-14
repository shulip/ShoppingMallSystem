from Controllers.Login import Login

class User(object):
    m_Login= Login()

    def __init__(self):
        pass

    def login(self,name,password,identity):
        self.m_Login.run(name,password,identity)
        print(identity)

    def registration(self):
        pass


if __name__ == '__main__':
    user = User()
    user.login('12',12)