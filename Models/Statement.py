#!/usr/bin/env python 
# -*- coding:utf-8 -*-

class Statement(object):
    def __init__(self):
        self.__shops = []

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
            contractsInfo.append({"number": shop.number,
                                  "contract": shop.contract})
        return contractsInfo

    @property
    def receipts(self):
        receiptsInfo = []
        for shop in self.__shops:
            receiptsInfo.append({"number": shop.number,
                                 "receipt": shop.receipt})
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
