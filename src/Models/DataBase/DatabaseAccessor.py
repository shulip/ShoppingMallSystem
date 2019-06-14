#!/usr/bin/env python 
# -*- coding:utf-8 -*-

"""
已收额：Receivable
    包含 electricCharge
         guaranteeCharge
         propertyFeeCharge
         waterCharge
应收额：
    包含 electricCharge
         guaranteeCharge
         propertyFeeCharge
         waterCharge
合同：Contract
    包含 information
         status
         year
         
获取用户信息获取以上全部
"""
import sqlite3
import os


class DatabaseAccessor(object):

    electricCharge = "ElectricCharge"
    guaranteeCharge = "GuaranteeCharge"
    propertyFeeCharge = "PropertyFeeCharge"
    waterCharge = "WaterCharge"

    def __init__(self):
        # self.connect = sqlite3.connect('shoppingMall.db')
        self.connect = sqlite3.connect(os.getcwd() + "//shoppingMall.db")
        self.cursor = self.connect.cursor()
        self.name = "DatabaseAccessor"
        self.create_user_table()
        self.create_revenue_table()

    #   如果发现数据库中没有用户table，则创建
    def create_user_table(self):
        print("创建用户表")
        self.cursor.execute('CREATE TABLE IF NOT EXISTS '
                       'users(user_id integer, account TEXT,'
                       'password TEXT, user_name TEXT)')

    #   创建contractInfosTable
    def create_contract_table(self):
        print("创建合同信息表")
        self.cursor.execute('CREATE TABLE IF NOT EXISTS '
                            'contractInfos(relevant_user_id INTEGER,information TEXT, status TEXT, _year TEXT, '
                            'proprietorSign INTEGER, ceoAffirm INTEGER, ceoSign INTEGER)')

    #   创建receivableAmountTable
    def create_receivable_amount_table(self):
        print("创建应收额信息表")
        self.cursor.execute('CREATE TABLE IF NOT EXISTS '
                            'receivableAmounts(PayerId integer, electricCharge INTEGER,'
                            ' guaranteeCharge INTEGER, propertyFeeCharge INTEGER, waterCharge INTEGER)')

    #   创建receiptTable
    def create_receipt_table(self):
        print("创建收据信息表")
        self.cursor.execute('CREATE TABLE IF NOT EXISTS '
                            'receipts(PayerId INTEGER, electricCharge INTEGER, '
                            'guaranteeCharge INTEGER, propertyFeeCharge INTEGER, waterCharge INTEGER)')

    #   创建shopTable
    def create_shop_table(self):
        print("创建商铺表")
        self.cursor.execute('CREATE TABLE IF NOT EXISTS '
                            'shops(shopNumber INTEGER, ownerId INTEGER)')

    #   添加用户，添加操作无法撤回，小心调用这个函数
    def add_new_user(self, user_id, account, password, username):
        print("添加用户：")
        self.cursor.execute('INSERT INTO users VALUES (?, ?, ?, ?)',
                  (user_id, account, password, username))
        self.connect.commit()

    #   添加收据信息，分别对应
    def add_new_receipt_info(self, payer_id, electric_charge,
                             guarantee_charge, property_fee_charge, water_charge):
        print("添加资金信息：")
        self.cursor.execute('INSERT INTO receipts VALUES (?, ?, ?, ?, ?)',
                  (payer_id, electric_charge, guarantee_charge, property_fee_charge, water_charge))
        self.connect.commit()

    #   添加应收额信息
    def add_new_receivable_amount_info(self, payer_id, electric_charge,
                             guarantee_charge, property_fee_charge, water_charge):
        print("添加应收额信息")
        self.cursor.execute('INSERT INTO receivableAmounts VALUES (?, ?, ?, ?, ?)',
                  (payer_id, electric_charge, guarantee_charge, property_fee_charge, water_charge))
        self.connect.commit()
        #   字典的列表
        #   list_.append({})

    #   添加合同信息，默认三个bool值皆为false
    def add_new_contract_info(self, info, status, year):
        print("添加合同信息")
        self.cursor.execute('INSERT INTO contractInfos VALUES (?, ?, ?, ?, ?, ?)',
                            (info, status, year, 0, 0, 0))

    #   添加商铺信息
    def add_new_shop_info(self, shop_number, owner_id):
        print("添加商铺信息")
        self.cursor.execute('INSERT INTO shops VALUES (?, ?)',
                            (shop_number, owner_id))

    #   根据id获取用户所有信息（合同、已收额、应收额）
    def get_user_info_by_id(self, user_id):
        print("获取对应id的合同、已收额、应收额")
        self.cursor.execute('SELECT * FROM receivableAmounts WHERE PayerId= ?',
                            user_id)
        receivable_data = self.cursor.fetchall()
        self.cursor.execute('SELECT * FROM receipts WHERE PayerId= ?',
                            user_id)
        receipt_data = self.cursor.fetchall()
        self.cursor.execute('SELECT * FROM contractInfos WHERE relevant_user_id = ?',
                            user_id)
        contract_data = self.cursor.fetchall()


        #由于我们默认一个id对应一个用户，所以取回的数据只有一行
        searchedUser = {
            "id": data[0][0],
            "account": data[0][1],
            "password": data[0][2],
            "name": data[0][3]
        }
        #data[row]代表第几个取回的数据组
        #data[row][column]代表这个数据组的第几个数据
        print(data[0][0])
        #for row in data:
               #print(row)
        return searchedUser

    def get_shop_number_by_user_id(self, user_id):
        pass

    #   根据资金信息id获取用户所有信息
    def get_revenue_info_by_id(self, revenue_id):
        print("获取对应id的资金信息：")
        self.cursor.execute('SELECT * FROM revenueInfos WHERE user_id= ?',
                            revenue_id)
        data = self.cursor.fetchall()
        searchedRevenue_info = {
            "id": data[0][0],
            "info": data[0][1],
            "relevantUserId": data[0][2]
        }
        return searchedRevenue_info

    #
    def get_all_shop_infos(self):
        print("获得所有商铺的相关信息")

    #   删除对应id的用户
    def delete_user_info_by_id(self, user_id):
        print("删除对应id的用户")
        self.cursor.execute('DELETE FROM users WHERE user_id = ?',
                            user_id)
        self.connect.commit()

    #   删除对应id的资金信息
    def delete_revenue_info_by_id(self, revenue_id):
        print("删除对应id的资金信息")
        self.cursor.execute('DELETE FROM revenueInfos WHERE user_id = ?',
                            revenue_id)
        self.connect.commit()

    def __del__(self):
        self.cursor.close()
        self.connect.close()
        print("我被销毁了QWQ")