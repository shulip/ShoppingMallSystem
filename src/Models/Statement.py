#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from Models.DataBase import DatabaseAccessor

class Statement(object):
    DB = DatabaseAccessor()
    def __init__(self):
        self.__shops = self.DB.get_all_shop_infos()
        print(self.__shops)
        self.__applications = self.DB.get_all_application_info()

    @property
    def applications(self):
        return self.__applications

    @property
    def allInfo(self):
        shopsInfo = []
        for shop in self.__shops:
            shopsInfo.append({"number": shop["number"],
                              "contract": shop["contract"],
                              "receipt": shop["receipt"],
                              "receivable": shop["receivable"]})
        return shopsInfo

    @property
    def contracts(self):
        contractsInfo = []
        for shop in self.__shops:
            contractsInfo.append({
                "ID":shop["id"],
                "number": shop["number"],
                "contractInfo": shop["contractInfo0"],
                "contractStatus":shop["contractStatus0"],
                "contractYear":shop["contractYear0"],
                "contractProprietorSign": shop["contractProprietorSign0"],
                "contractCeoAffirm": shop["contractCeoAffirm0"],
                "contractCeoSign": shop["contractCeoSign0"],

            })
        return contractsInfo

    @property
    def receipts(self):
        receiptsInfo = []
        for shop in self.__shops:
            receiptsInfo.append({
                "ID":shop["id"],
                "number": shop["number"],
                "receiptEleCharge": shop["receiptEleCharge0"],
                "receiptGuarCharge": shop["receiptGuarCharge0"],
                "receiptPropCharge": shop["receiptPropCharge0"],
                "receiptWaterCharge": shop["receiptWaterCharge0"],
            })
        return receiptsInfo

    @property
    def receivable(self):
        receivableInfo = []
        for shop in self.__shops:
            receivableInfo.append({
                "ID": shop["id"],
                "number": shop["number"],
                "receivableEleCharge": shop["receivedEleCharge0"],
                "receivableGuarCharge": shop["receivedGuarCharge0"],
                "receivablePropCharge": shop["receivedPropCharge0"],
                "receivableWaterCharge": shop["receivedWaterCharge0"],
            })
        return receivableInfo

    def print_all(self):
        print("所有信息")

if __name__ == '__main__':
    statement = Statement()
    print("合同信息")
    print(statement.contracts)
    print("收据")
    print(statement.receipts)
    print("应收额")
    print(statement.receivable)