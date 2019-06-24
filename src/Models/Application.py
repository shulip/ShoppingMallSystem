#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from Models.DataBase import DatabaseAccessor

class Application(object):
    DB = DatabaseAccessor()
    def __init__(self,ID=None):
        if ID is not None:
            pass
        else:
            pass

    def create_application(self,ID,shopIndex, userName, telenumber, rentTime, rentUsage):
        self.DB.add_new_application_info(ID,shopIndex, userName, telenumber, rentTime, rentUsage)

    def delete_application(self,ID):
        self.DB.delete_application_by_id(ID)