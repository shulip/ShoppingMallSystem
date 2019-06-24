#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from Models.DataBase import DatabaseAccessor

class Contract(object):
    DB = DatabaseAccessor()
    def __init__(self,ID=None):
        if ID is not None:
            self.__ID = ID
            self.__contract = self.DB.get_contract_info_by_id(ID)

            self.__information = self.__contract["contractInfo"]
            self.__status = self.__contract["contractStatus"]
            self.__year = self.__contract["contractYear"]

            self.__proprietorSign = self.__contract["proprietorSign"]  # 业主是否签字
            self.__CEOAffirm = self.__contract["CEOAffirm"]  # 总经理是否确认
            self.__CEOSign = self.__contract["CEOSign"]  # 总经理是否签字

            self.__userName = self.__contract["userName"]
            self.__shopIndex = self.__contract["shopIndex"]
            self.__userTelContract = self.__contract["userTelContract"]

        else:
            pass

        # self.__information = ''
        # self.__status = ''
        # self.__year = -1

        # self.__proprietorSign = False  # 业主是否签字
        # self.__CEOAffirm = False  # 总经理是否确认
        # self.__CEOSign = False  # 总经理是否签字

    def add_new_contract_info(self,ID,shopNum,userName,userTelContract,contractInformation,rentTimeManager):
        self.DB.add_new_contract_info(ID,shopNum,userName,userTelContract,contractInformation,rentTimeManager)

    def set_contract_ceoaffirm_by_id(self, user_id, ceoaffirm):

        self.DB.set_contract_ceoaffirm_by_id(user_id, ceoaffirm)

        return None

    def set_contract_ceosign_by_id(self,user_id, ceosign):
        self.DB.set_contract_ceosign_by_id(user_id, ceosign)

        return None

    @property
    def proprietorSign(self):
        return self.__proprietorSign

    @property
    def CEOAffirm(self):
        return self.__CEOAffirm

    @property
    def CEOSign(self):
        return self.__CEOSign
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
        self.__CEOAffirm = 1
        self.DB.set_contract_ceoaffirm_by_id(self.__ID,1)

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
