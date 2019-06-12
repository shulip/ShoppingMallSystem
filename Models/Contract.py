#!/usr/bin/env python 
# -*- coding:utf-8 -*-

class Contract(object):
    def __init__(self):
        self.__information = ''
        self.__status = ''
        self.__year = -1

        self.__proprietorSign = False  # 业主是否签字
        self.__CEOAffirm = False  # 总经理是否确认
        self.__CEOSign = False  # 总经理是否签字

    @property
    def information(self):
        return self.__information

    @information.setter
    def information(self, _information):
        self.__information = _information

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, _status):
        self.__status = _status

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, _year):
        self.__year = _year

    def affirm(self):
        """
        总经理确认
        :return: None
        """
        self.__CEOAffirm = True

        return None

    def sign(self, status):
        """
        业主或总经理签字
        :return:
        """
        # 业主签字
        if status == 'p':
            self.__proprietorSign = True
        elif status == 'c':
            self.__CEOSign = True

        return None

    @property
    def allInfo(self):
        allInfo = {"information": self.__information,
                   "status": self.__status,
                   "year": self.__year}
        return allInfo

    @allInfo.setter
    def allInfo(self, _allInfo):
        if _allInfo["information"] != '':
            self.information = _allInfo["information"]

        if _allInfo["status"] != '':
            self.status = _allInfo["status"]

        if _allInfo["year"] != '':
            self.year = _allInfo["year"]


if __name__ == '__main__':
    c = Contract()

    c.information = "asas"

    info = {"information": '信息',
            "status": "状态",
            "year": 3}
    c.allInfo = info

    print(c.information)
    print(c.year)
    print(c.status)
