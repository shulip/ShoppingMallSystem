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
        self.create_application_table()
        self.connect.commit()


    # user table

    def create_user_table(self):
        """
        如果发现数据库中没有用户table，则创建
        :return:
        """
        print("创建用户表")
        self.cursor.execute('CREATE TABLE IF NOT EXISTS '
                       'users(user_id integer, account TEXT,'
                       'password TEXT, user_name TEXT)')

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

    # receivable
    def create_receivable_amount_table(self):
        """
        创建receivableAmountTable
        :return:
        """
        print("创建应收额信息表")
        self.cursor.execute('CREATE TABLE IF NOT EXISTS '
                            'receivableAmounts(PayerId integer, '
                            'electricCharge INTEGER,'
                            ' guaranteeCharge INTEGER, '
                            'propertyFeeCharge INTEGER,'
                            ' waterCharge INTEGER)')

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
        #     user_info["electricCharge"] = receivable_data[0][1]
        #     user_info["guaranteeCharge"] = receivable_data[0][2]
        #     user_info["propertyFeeCharge"] = receivable_data[0][3]
        #     user_info["waterCharge"] = receivable_data[0][4]
        return user_info

    def set_receivable_electriccharge_by_id(self, PayerId, electricCharge):
        self.cursor.execute('UPDATE receivableAmounts SET electricCharge = ? WHERE PayerId = ?',
                            (str(electricCharge), str(PayerId)))
        self.connect.commit()

    def set_receivable_guaranteecharge_by_id(self, PayerId, guaranteeCharge):
        self.cursor.execute('UPDATE receivableAmounts SET guaranteeCharge = ? WHERE PayerId = ?',
                            (str(guaranteeCharge), str(PayerId)))
        self.connect.commit()

    def set_receivable_propertyfee_by_id(self, PayerId, propertyFeeCharge):
        self.cursor.execute('UPDATE receivableAmounts SET propertyFeeCharge = ? WHERE PayerId = ?',
                            (str(propertyFeeCharge), str(PayerId)))
        self.connect.commit()

    def set_receivable_watercharge_by_id(self, PayerId, waterCharge):
        self.cursor.execute('UPDATE receivableAmounts SET waterCharge = ? WHERE PayerId = ?',
                            (str(waterCharge), str(PayerId)))
        self.connect.commit()

    # receipt

    def create_receipt_table(self):
        """
        创建receiptTable
        :return:
        """
        print("创建收据信息表")
        self.cursor.execute('CREATE TABLE IF NOT EXISTS '
                            'receipts(PayerId INTEGER, '
                            'electricCharge INTEGER, '
                            'guaranteeCharge INTEGER, '
                            'propertyFeeCharge INTEGER, '
                            'waterCharge INTEGER)')

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

    def set_receipt_electriccharge_by_id(self, PayerId, electricCharge):
        self.cursor.execute('UPDATE receipts SET electricCharge = ? WHERE PayerId = ?',
                            (str(electricCharge), str(PayerId)))
        self.connect.commit()

    def set_receipt_guaranteecharge_by_id(self, PayerId, guaranteeCharge):
        self.cursor.execute('UPDATE receipts SET guaranteeCharge = ? WHERE PayerId = ?',
                            (str(guaranteeCharge), str(PayerId)))
        self.connect.commit()

    def set_receipt_propertyfee_by_id(self, PayerId, propertyFeeCharge):
        self.cursor.execute('UPDATE receipts SET propertyFeeCharge = ? WHERE PayerId = ?',
                            (str(propertyFeeCharge), str(PayerId)))
        self.connect.commit()

    def set_receipt_watercharge_by_id(self, PayerId, waterCharge):
        self.cursor.execute('UPDATE receipts SET waterCharge = ? WHERE PayerId = ?',
                            (str(waterCharge), str(PayerId)))
        self.connect.commit()

    # applications

    def create_application_table(self):
        print("创建申请信息表")
        self.cursor.execute('CREATE TABLE IF NOT EXISTS '
                            'applications('
                            'userId INTEGER,'
                            'shopIndex INTEGER, '
                            'userName TEXT, '
                            'telenumber TEXT, '
                            'rentTime INTEGER, '
                            'rentUsage TEXT)')

    def add_new_application_info(self, userId, shopIndex, userName, telenumber, rentTime, rentUsage):
        print("添加申请：")
        self.cursor.execute('INSERT INTO applications VALUES (?, ?, ?, ?, ?, ?)',
                            (userId, shopIndex, userName, telenumber, rentTime, rentUsage))
        self.connect.commit()

    def get_all_application_info(self):
        """
        获取所有申请信息
        :return: 一个装者字典的 list ，访问格式   dicName["shopIndex"]
        """
        self.cursor.execute('SELECT * FROM applications ')
        apps = self.cursor.fetchall()
        appInfoList=[]
        for app in apps:
            appInfo={}
            appInfo["ID"]=app[0]
            appInfo["shopIndex"]=app[1]
            appInfo["userName"]=app[2]
            appInfo["telenumber"]=app[3]
            appInfo["rentTime"]=app[4]
            appInfo["rentUsage"]=app[5]
            appInfoList.append(appInfo)

        return appInfoList


    # shop

    def create_shop_table(self):
        """
        创建shopTable
        :return:
        """
        print("创建商铺表")
        self.cursor.execute('CREATE TABLE IF NOT EXISTS '
                            'shops(shopNumber INTEGER, '
                            'ownerId INTEGER)')

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

    # contract

    def create_contract_table(self):
        """
        创建contractInfosTable
        :return:
        """
        print("创建合同信息表")
        self.cursor.execute('CREATE TABLE IF NOT EXISTS '
                            'contractInfos('
                            'relevant_user_id INTEGER,'
                            'information TEXT, '
                            'status TEXT, '
                            '_year TEXT, '
                            'shopIndex INTEGER,'
                            'userName TEXT,'
                            'userTelContract TEXT,'
                            'proprietorSign INTEGER, '
                            'ceoAffirm INTEGER, '
                            'ceoSign INTEGER)')

    def add_new_contract_info(self, user_id, shopIndex, userName, userTelContract, contractInformation,
                              rentTimeManager):

        print("添加合同信息")
        self.cursor.execute('INSERT INTO contractInfos VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                            (user_id, contractInformation, 0, rentTimeManager, shopIndex, userName, userTelContract, 0,
                             0, 0))
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

        user_info["shopIndex"] = contract_data[0][4]
        user_info["userName"] = contract_data[0][5]
        user_info["userTelContract"] = contract_data[0][6]

        user_info["proprietorSign"] = contract_data[0][7]
        user_info["CEOAffirm"] = contract_data[0][8]
        user_info["CEOSign"] = contract_data[0][9]
        return user_info

    # set contract

    def set_contract_ceosign_by_id(self, user_id, ceosign):
        self.cursor.execute('UPDATE contractInfos SET ceoSign = ? WHERE relevant_user_id = ?',
                            (str(ceosign), str(user_id)))
        self.connect.commit()

    def set_contract_ceoaffirm_by_id(self, user_id, ceoaffirm):
        self.cursor.execute('UPDATE contractInfos SET ceoAffirm = ? WHERE relevant_user_id = ?',
                            (str(ceoaffirm), str(user_id)))
        self.connect.commit()

    def set_contract_information_by_id(self, user_id, text):
        self.cursor.execute('UPDATE  contractInfos SET information = ? WHERE relevant_user_id = ? ',
                            (str(text), str(user_id)))
        self.connect.commit()

    def set_contract_status_by_id(self, user_id, status):
        self.cursor.execute('UPDATE contractInfos SET status = ? WHERE relevant_user_id = ?',
                            (str(status), str(user_id)))
        self.connect.commit()

    def set_contract_year_by_id(self, user_id, year):
        self.cursor.execute('UPDATE contractInfos SET _year = ? WHERE relevant_user_id = ?',
                            (str(year), str(user_id)))
        self.connect.commit()

    def set_contract_shopIndex_by_id(self, user_id, shopIndex):
        self.cursor.execute('UPDATE contractInfos SET shopIndex = ? WHERE relevant_user_id = ?',
                            (str(shopIndex), str(user_id)))
        self.connect.commit()

    def set_contract_username_by_id(self, user_id, userName):
        self.cursor.execute('UPDATE contractInfos SET userName = ? WHERE relevant_user_id = ?',
                            (str(userName), str(user_id)))
        self.connect.commit()

    def set_contract_usertelcontract_by_id(self, user_id, userTelContract):
        self.cursor.execute('UPDATE contractInfos SET userTelContract = ? WHERE relevant_user_id = ?',
                            (str(userTelContract), str(user_id)))
        self.connect.commit()

    def set_contract_proprietorsign_by_id(self, user_id, proprietorsign):
        """
        通过id修改合同 proprietroSign
        :param user_id:
        :param proprietorsign: 0 - 不确认，1 - 确认
        :return:
        """
        self.cursor.execute('UPDATE contractInfos SET proprietorSign = ? WHERE relevant_user_id = ?',
                            (str(proprietorsign), str(user_id)))
        self.connect.commit()

    def __del__(self):
        self.cursor.close()
        self.connect.close()


"""TEST

"""
testAccessor = DatabaseAccessor()
#shopNumbers = testAccessor.get_shop_number_by_user_id(1)
#user_info = testAccessor.get_user_info_by_id(1)
#all_shop_info = testAccessor.get_all_shop_infos()
#test = testAccessor.get_receivable_info_by_id(1)

#testAccessor.add_new_contract_info(100, "没事", "jb状态", 2019)
#testAccessor.add_new_receipt_info(100,111,222,333,444)
#testAccessor.add_new_receivable_amount_info(100,11,22,33,44)

testAccessor.add_new_application_info(12,100,"name1","186",100,"没用")
testAccessor.add_new_application_info(13,101,"name2","187",100,"没用")
testAccessor.add_new_application_info(14,102,"name3","188",100,"没用")

print("改之前：")
test=testAccessor.get_all_application_info()
for info in test:
    print(info["ID"])

#testAccessor.set_receipt_electriccharge_by_id(100,123)
#testAccessor.set_receipt_guaranteecharge_by_id(100,123)
#testAccessor.set_receipt_propertyfee_by_id(100,123)
#testAccessor.set_receipt_watercharge_by_id(100,123)

#testAccessor.set_receivable_electriccharge_by_id(100,1203)
#testAccessor.set_receivable_guaranteecharge_by_id(100,1203)
#testAccessor.set_receivable_propertyfee_by_id(100,1203)
#testAccessor.set_receivable_watercharge_by_id(100,1203)



#testAccessor.set_contract_ceoaffirm_by_id(100, 1)
#testAccessor.set_contract_information_by_id(100, "好事！")
#testAccessor.set_contract_status_by_id(100, "可以")
#testAccessor.set_contract_ceosign_by_id(100, 1)
#testAccessor.set_contract_year_by_id(100, 2077)
#testAccessor.set_contract_proprietorsign_by_id(100, 1)



print("改之后")
testAccessor.cursor.execute('SELECT * FROM applications')
test = testAccessor.cursor.fetchall()
for info in test:
    print(info)

testAccessor.cursor.execute('DELETE FROM contractInfos WHERE relevant_user_id = 100')
testAccessor.connect.commit()
testAccessor.cursor.execute('DELETE FROM receivableAmounts WHERE PayerId = 100')
testAccessor.connect.commit()
testAccessor.cursor.execute('DELETE FROM receipts WHERE PayerId = 100')
testAccessor.connect.commit()
testAccessor.cursor.execute('DELETE FROM applications WHERE shopIndex >= 100')
testAccessor.connect.commit()






