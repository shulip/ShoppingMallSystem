#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from Models.DataBase import DatabaseAccessor

class Statement(object):
    DB = DatabaseAccessor()
    def __init__(self):
        self.__shops = self.DB.get_all_shop_infos()

    @property
    def allInfo(self):
        shopsInfo = []
        for shop in self.__shops:
            shopsInfo.append({"number": shop.number,
                              "contract": shop.contract,
                              "receipt": shop.receipt,
                              "receivable": shop.receivable})
        return shopsInfo

    @property
    def contracts(self):
        contractsInfo = []
        for shop in self.__shops:
            contractsInfo.append({
                "ID":shop.id,
                "number": shop.number,
                "contractInfo": shop.contractInfo,
                "contractStatus":shop.contractStatus,
                "contractYear":shop.contractYear,
            })
        return contractsInfo

    @property
    def receipts(self):
        receiptsInfo = []
        for shop in self.__shops:
            receiptsInfo.append({
                "ID":shop.id,
                "number": shop.number,
                "receiptEleCharge": shop.receiptEleCharge,
                "receiptGuarCharge": shop.receiptGuarCharge,
                "receiptPropCharge": shop.receiptPropCharge,
                "receiptWaterCharge": shop.receiptWaterCharge,
            })
        return receiptsInfo

    @property
    def receivable(self):
        receivableInfo = []
        for shop in self.__shops:
            receivableInfo.append({"number": shop.number,
                                   "receivable": shop.receivable})
        return receivableInfo

    def print_all(self):
        print("所有信息")
