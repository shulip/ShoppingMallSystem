#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from .Contract import Contract
from .Receipt import *
from .Receivable import *

class Shop(object):
    def __init__(self,number,):
        self.__number = number
        self.__contract = Contract()
        self.__receipt = Receipt()
        self.__receivable = Receivable()

    @property
    def number(self):
        return self.__number

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