#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from .Contract import Contract
from .Receipt import *
from .Receivable import *

class Shop(object):
    DB = DatabaseAccessor()
    def __init__(self,ID):
        self.__ID = ID
        self.__contract = Contract(ID)
        self.__receipt = Receipt(ID)
        self.__receivable = Receivable(ID)
        self.__number = self.DB.get_shop_number_by_user_id(ID)

    @property
    def number(self):
        return self.__number

    def contract_information(self):
        return self.__contract.information

    def contract_status(self):
        return self.__contract.status

    def contract_year(self):
        return self.__contract.year

    def contract_proprietorSign(self):
        return self.__contract.proprietorSign

    def contract_CEOAffirm(self):
        return self.__contract.CEOAffirm

    def contract_CEOSign(self):
        return self.__contract.CEOSign

    def receipt_electric(self):
        return self.__receipt.electric

    def receipt_guarantee(self):
        return self.__receipt.guarantee

    def receipt_propertyfee(self):
        return self.__receipt.propertyfee

    def receipt_water(self):
        return self.__receipt.water

    def receivable_electric(self):
        return self.__receivable.electric

    def receivable_guarantee(self):
        return self.__receivable.guarantee

    def receivable_propertyfee(self):
        return self.__receivable.propertyfee

    def receivable_water(self):
        return self.__receivable.water

    @property
    def contract(self):
        return self.__contract.allInfo

    @property
    def receipt(self):
        return self.__receipt.allInfo

    @property
    def receivable(self):
        return self.__receivable.allInfo

    def print_all(self):

        print("全部信息")