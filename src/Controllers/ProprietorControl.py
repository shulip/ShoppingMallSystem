#######################################################
# 
# ProprietorControl.py
# Python implementation of the Class ProprietorControl
# Generated by Enterprise Architect
# Created on:      16-5��-2019 12:06:10
# Original author: ����
# 
#######################################################
from Models.Shop import Shop
from Models.Application import Application
from Controllers.User import User
from Controllers.Login import Login

class ProprietorControl(User):

    def __init__(self,ID):
        super().__init__()
        self.__ID = ID
        self.__shop = Shop(ID)
        self.__applicationCon = Application(ID)

    def number(self):
        """
        获取商铺号
        :return: 商铺号
        """
        return self.__shop.number()

    def create_application(self,ID,shopIndex, userName, telenumber, rentTime, rentUsage):
        self.__applicationCon.create_application(ID,shopIndex, userName, telenumber, rentTime, rentUsage)

    def contract_information(self):
        """
        获取合同具体信息
        :return:
        """
        return self.__shop.contract_information()

    def contract_status(self):
        """
        获取合同状态
        :return:
        """
        return self.__shop.contract_status()

    def contract_year(self):
        """
        获取合同年限
        :return:
        """
        return self.__shop.contract_year()

    def contract_CEOAffirm(self):
        return self.__shop.contract_CEOAffirm()

    def contract_CEOSign(self):
        return self.__shop.contract_CEOSign()

    def contract_proprietorSign(self):
        return self.__shop.contract_proprietorSign()

    def receipt_electric(self):
        """
        获取以缴纳电费信息
        :return:
        """
        return self.__shop.receipt_electric()

    def receipt_guarantee(self):
        """
        获取以缴纳保证金信息
        :return:
        """
        return self.__shop.receipt_guarantee()

    def receipt_propertyfee(self):
        """
        获取以缴纳物业费信息
        :return:
        """
        return self.__shop.receipt_propertyfee()

    def receipt_water(self):
        """
        获取以缴纳水费信息
        :return:
        """
        return self.__shop.receipt_water()

    def receivable_electric(self):
        """
        获取以应缴纳电费信息
        :return:
        """
        return self.__shop.receivable_electric()

    def receivable_guarantee(self):
        """
        获取以应缴纳保证金信息
        :return:
        """
        return self.__shop.receivable_guarantee()

    def receivable_propertyfee(self):
        """
        获取以应缴纳物业费信息
        :return:
        """
        return self.__shop.receivable_propertyfee()

    def receivable_water(self):
        """
        获取以应缴纳水费信息
        :return:
        """
        return self.__shop.receivable_water()

    def apply_to_enter(self):
        pass

    def apply_to_sublet(self):
        pass

    def pay(self):
        pass

    def registration(self):
        pass

    def sign_contract(self):
        """
        签字
        :return:None
        """
        #TODO: 更新数据库
        pass

    def view_status(self):

        pass
