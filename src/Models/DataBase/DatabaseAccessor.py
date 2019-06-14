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
        self.connect = sqlite3.connect(os.getcwd() + "//shoppingMall.db")
        self.cursor = self.connect.cursor()
        self.name = "DatabaseAccessor"
        self.create_user_table()
        self.create_contract_table()
        self.create_receipt_table()
        self.create_receivable_amount_table()
        self.create_shop_table()

    def create_user_table(self):
        """
        如果发现数据库中没有用户table，则创建
        :return:
        """
        print("创建用户表")
        self.cursor.execute('CREATE TABLE IF NOT EXISTS '
                       'users(user_id integer, account TEXT,'
                       'password TEXT, user_name TEXT)')

    def create_contract_table(self):
        """
        创建contractInfosTable
        :return:
        """
        print("创建合同信息表")
        self.cursor.execute('CREATE TABLE IF NOT EXISTS '
                            'contractInfos(relevant_user_id INTEGER,information TEXT, status TEXT, _year TEXT, '
                            'proprietorSign INTEGER, ceoAffirm INTEGER, ceoSign INTEGER)')

    def create_receivable_amount_table(self):
        """
        创建receivableAmountTable
        :return:
        """
        print("创建应收额信息表")
        self.cursor.execute('CREATE TABLE IF NOT EXISTS '
                            'receivableAmounts(PayerId integer, electricCharge INTEGER,'
                            ' guaranteeCharge INTEGER, propertyFeeCharge INTEGER, waterCharge INTEGER)')

    def create_receipt_table(self):
        """
        创建receiptTable
        :return:
        """
        print("创建收据信息表")
        self.cursor.execute('CREATE TABLE IF NOT EXISTS '
                            'receipts(PayerId INTEGER, electricCharge INTEGER, '
                            'guaranteeCharge INTEGER, propertyFeeCharge INTEGER, waterCharge INTEGER)')

    def create_shop_table(self):
        """
        创建shopTable
        :return:
        """
        print("创建商铺表")
        self.cursor.execute('CREATE TABLE IF NOT EXISTS '
                            'shops(shopNumber INTEGER, ownerId INTEGER)')

    def add_new_user(self, user_id, account, password, username):
        """
        添加用户，添加操作无法撤回，小心调用这个函数
        :param user_id:
        :param account:
        :param password:
        :param username:
        :return:
        """
        print("添加用户：")
        self.cursor.execute('INSERT INTO users VALUES (?, ?, ?, ?)',
                  (user_id, account, password, username))
        self.connect.commit()

    def add_new_receipt_info(self, payer_id, electric_charge,
                             guarantee_charge, property_fee_charge, water_charge):
        """
        添加收据信息
        :param payer_id:
        :param electric_charge:
        :param guarantee_charge:
        :param property_fee_charge:
        :param water_charge:
        :return:
        """
        print("添加资金信息：")
        self.cursor.execute('INSERT INTO receipts VALUES (?, ?, ?, ?, ?)',
                  (payer_id, electric_charge, guarantee_charge, property_fee_charge, water_charge))
        self.connect.commit()

    def add_new_receivable_amount_info(self, payer_id, electric_charge,
                             guarantee_charge, property_fee_charge, water_charge):
        """
        添加应收额信息
        :param payer_id:
        :param electric_charge:
        :param guarantee_charge:
        :param property_fee_charge:
        :param water_charge:
        :return:
        """
        print("添加应收额信息")
        self.cursor.execute('INSERT INTO receivableAmounts VALUES (?, ?, ?, ?, ?)',
                  (payer_id, electric_charge, guarantee_charge, property_fee_charge, water_charge))
        self.connect.commit()
        #   字典的列表
        #   list_.append({})

    def add_new_contract_info(self, info, status, year):
        """
        添加合同信息，默认三个bool值皆为false
        :param info:
        :param status:
        :param year:
        :return:
        """
        print("添加合同信息")
        self.cursor.execute('INSERT INTO contractInfos VALUES (?, ?, ?, ?, ?, ?)',
                            (info, status, year, 0, 0, 0))
        self.connect.commit()

    def add_new_shop_info(self, shop_number, owner_id):
        """
        添加商铺信息
        :param shop_number:
        :param owner_id:
        :return:
        """
        print("添加商铺信息")
        self.cursor.execute('INSERT INTO shops VALUES (?, ?)',
                            (shop_number, owner_id))
        self.connect.commit()

    def get_contract_info_by_id(self, user_id):
        """
        根据id获取合同信息
        :param user_id:
        :return:
        """
        self.cursor.execute('SELECT * FROM contractInfos WHERE relevant_user_id = ?',
                            str(user_id))
        contract_data = self.cursor.fetchall()
        user_info = {}
        user_info["contractInfo"] = contract_data[0][1]
        user_info["contractStatus"] = contract_data[0][2]
        user_info["contractYear"] = contract_data[0][3]
        user_info["proprietorSign"] = contract_data[0][4]
        user_info["CEOAffirm"] = contract_data[0][5]
        user_info["CEOSign"] = contract_data[0][6]
        return user_info

    def get_receipt_info_by_id(self, user_id):
        """
        根据id获取账单信息
        :param user_id:
        :return:
        """
        self.cursor.execute('SELECT * FROM receipts WHERE PayerId = ?',
                            str(user_id))
        receipt_data = self.cursor.fetchall()
        user_info = {}
        user_info["electricCharge"] = receipt_data[0][1]
        user_info["guaranteeCharge"] = receipt_data[0][2]
        user_info["propertyFeeCharge"] = receipt_data[0][3]
        user_info["waterCharge"] = receipt_data[0][4]
        return user_info

    def get_receivable_info_by_id(self, user_id):
        """
        根据id获取应收额信息
        :param user_id:
        :return:
        """
        self.cursor.execute('SELECT * FROM receivableAmounts WHERE PayerId= ?',
                            str(user_id))
        receivable_data = self.cursor.fetchall()
        user_info = {}
        user_info["electricCharge"] = receivable_data[0][1]
        user_info["guaranteeCharge"] = receivable_data[0][2]
        user_info["propertyFeeCharge"] = receivable_data[0][3]
        user_info["waterCharge"] = receivable_data[0][4]
        return user_info

    def get_user_info_by_id(self, user_id):
        """
        根据id获取用户所有信息（合同、已收额、应收额）
        :param user_id: id
        :return:返回与用户id相关的合同、已收额、应收额信息
        """
        print("获取对应id的合同、已收额、应收额")
        self.cursor.execute('SELECT * FROM receivableAmounts WHERE PayerId= ?',
                            str(user_id))
        receivable_data = self.cursor.fetchall()
        self.cursor.execute('SELECT * FROM receipts WHERE PayerId= ?',
                            str(user_id))
        receipt_data = self.cursor.fetchall()
        self.cursor.execute('SELECT * FROM contractInfos WHERE relevant_user_id = ?',
                            str(user_id))
        contract_data = self.cursor.fetchall()
        user_info = {}
        #   contract
        for user, i in zip(contract_data, range(len(contract_data))):
            user_info["contractInfo{}".format(i)] = user[1]
            user_info["contractStatus{}".format(i)] = user[2]
            user_info["contractYear{}".format(i)] = user[3]

        #   receivable
        for user, i in zip(receivable_data, range(len(receivable_data))):
            user_info["receivedEleCharge{}".format(i)] = user[1]
            user_info["receivedGuarCharge{}".format(i)] = user[2]
            user_info["receivedPropCharge{}".format(i)] = user[3]
            user_info["receivedWaterCharge{}".format(i)] = user[4]
        #   receipt
        for user, i in zip(receipt_data, range(len(receipt_data))):
            user_info["receiptEleCharge{}".format(i)] = user[1]
            user_info["receiptGuarCharge{}".format(i)] = user[2]
            user_info["receiptPropCharge{}".format(i)] = user[3]
            user_info["receiptWaterCharge{}".format(i)] = user[4]
        return user_info

    def get_shop_number_by_user_id(self, user_id):
        """
        根据用户id获取他拥有的商店number的字典，用dict["number%d"]来获取
        :param user_id:
        :return:用户id对应的商店number的字典，用dict["number%d"]来获取
        """
        print("获得对应用户id的商铺number")
        self.cursor.execute('SELECT shopNumber FROM shops WHERE ownerId = ?', str(user_id))
        shop_numbers = self.cursor.fetchall()
        numbers_dict = {}
        for shopNum, i in zip(shop_numbers, range(len(shop_numbers))):
            numbers_dict["number{}".format(i)] = shopNum[0]
        return numbers_dict

    def get_user_id_by_shop_number(self, shopNumber):
        """
        根据用户id获取他拥有的商店number的字典，用dict["number%d"]来获取
        :param user_id:
        :return:用户id对应的商店number的字典，用dict["number%d"]来获取
        """
        print("获得店铺对应的id")
        self.cursor.execute('SELECT ownerId FROM shops WHERE shopNumber = ?', str(shopNumber))
        user = self.cursor.fetchall()

        assert len(user) <= 1

        return user[0]


    def get_all_shop_infos(self):
        """
        获取所有商店的相关信息，number id 合同 应收额 已收额
        :return:一个装有一系列字典的链表，每一个字典中包含 number id 合同 应收额 已收额
        """
        #   number id 各种
        print("获得所有商铺的相关信息")
        #   获取所有商铺的number 与 id shop_infos[0][0] shop_infos[0][1]
        self.cursor.execute('SELECT * FROM shops')
        shop_infos = self.cursor.fetchall()
        #   根据用户id获取所有与id有关的合同 应收额 已收额
        shop_info_list = []
        for number_id in shop_infos:
            temp_user_info = {}
            temp_user_info["number"] = number_id[0]
            temp_user_info["id"] = number_id[1]
            #   将填入number 和 id 的字典装入链表中
            shop_info_list.append(temp_user_info)
        for number_id in shop_info_list:
            this_id = number_id["id"]
            print("获取对应id的合同、已收额、应收额")
            self.cursor.execute('SELECT * FROM receivableAmounts WHERE PayerId= ?',
                                str(this_id))
            receivable_data = self.cursor.fetchall()
            self.cursor.execute('SELECT * FROM receipts WHERE PayerId= ?',
                                str(this_id))
            receipt_data = self.cursor.fetchall()
            self.cursor.execute('SELECT * FROM contractInfos WHERE relevant_user_id = ?',
                                str(this_id))
            contract_data = self.cursor.fetchall()
            #   contract
            for user, i in zip(contract_data, range(len(contract_data))):
                number_id["contractInfo{}".format(i)] = user[1]
                number_id["contractStatus{}".format(i)] = user[2]
                number_id["contractYear{}".format(i)] = user[3]
                number_id["contractProprietorSign{}".format(i)] = user[4]
                number_id["contractCeoAffirm{}".format(i)] = user[5]
                number_id["contractCeoSign{}".format(i)] = user[6]
            #   receivable
            for user, i in zip(receivable_data, range(len(receivable_data))):
                number_id["receivedEleCharge{}".format(i)] = user[1]
                number_id["receivedGuarCharge{}".format(i)] = user[2]
                number_id["receivedPropCharge{}".format(i)] = user[3]
                number_id["receivedWaterCharge{}".format(i)] = user[4]
            #   receipt
            for user, i in zip(receipt_data, range(len(receipt_data))):
                number_id["receiptEleCharge{}".format(i)] = user[1]
                number_id["receiptGuarCharge{}".format(i)] = user[2]
                number_id["receiptPropCharge{}".format(i)] = user[3]
                number_id["receiptWaterCharge{}".format(i)] = user[4]
        return shop_info_list

    def __del__(self):
        self.cursor.close()
        self.connect.close()


"""TEST

"""
testAccessor = DatabaseAccessor()
shopNumbers = testAccessor.get_shop_number_by_user_id(1)
user_info = testAccessor.get_user_info_by_id(1)
all_shop_info = testAccessor.get_all_shop_infos()
test = testAccessor.get_receivable_info_by_id(1)
print(test)





