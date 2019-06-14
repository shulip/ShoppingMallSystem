#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from Models.DataBase import DatabaseAccessor

class Receivable(object):
    DB = DatabaseAccessor()
    def __init__(self, ID):
        self.__ID = ID
        self.__receivable = self.DB.get_receivable_info_by_id(self.__ID)

        self.__electricCharge = self.__receivable["electricCharge"]
        self.__guaranteeCharge = self.__receivable["guaranteeCharge"]
        self.__propertyFeeCharge = self.__receivable["propertyFeeCharge"]
        self.__waterCharge = self.__receivable["waterCharge"]

        # self.__electricCharge = 0.0
        # self.__guaranteeCharge = 0.0
        # self.__propertyFeeCharge = 0.0
        # self.__waterCharge = 0.0

    @property
    def electric(self):
        return self.__electricCharge

    @electric.setter
    def electric(self, _electric):
        self.__electricCharge = _electric

    @property
    def guarantee(self):
        return self.__guaranteeCharge

    @guarantee.setter
    def guarantee(self, _guarantee):
        self.__guaranteeCharge = _guarantee

    @property
    def propertyfee(self):
        return self.__propertyFeeCharge

    @propertyfee.setter
    def propertyfee(self, _propertyfee):
        self.__propertyFeeCharge = _propertyfee

    @property
    def water(self):
        return self.__waterCharge

    @water.setter
    def water(self, _water):
        self.__waterCharge = _water

    @property
    def allInfo(self):
        allInfo = {"electric": self.__electricCharge,
                   "guarantee": self.__guaranteeCharge,
                   "propertyFee": self.__propertyFeeCharge,
                   "water":self.__waterCharge}
        return allInfo

