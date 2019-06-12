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

    def __init__(self):
        # self.connect = sqlite3.connect('shoppingMall.db')
        self.connect = sqlite3.connect(os.getcwd() + "//shoppingMall.db")
        self.cursor = self.connect.cursor()
        self.name = "DatabaseAccessor"
        self.create_user_table()
        self.create_revenue_table()
        print("初始化类!")

    def test(self):
        print("我的成员变量为：" + self.name)

    #   如果发现数据库中没有用户table，则创建
    def create_user_table(self):
        print("创建用户表")
        self.cursor.execute('CREATE TABLE IF NOT EXISTS '
                       'users(user_id integer, account TEXT,'
                       'password TEXT, user_name TEXT)')

    #   如果发现数据库中没有资金信息table，则创建
    def create_revenue_table(self):
        print("创建资金信息表")
        self.cursor.execute('CREATE TABLE IF NOT EXISTS '
                       'revenueInfos(revenue_info_id integer, revenue_info TEXT,'
                       'relevant_user_id integer)')

    #   添加用户，分别对应id account password userName
    #   注意，添加操作无法撤回，小心调用这个函数
    def add_new_user(self, user_id, account, password, username):
        print("添加用户：")
        self.cursor.execute('INSERT INTO users VALUES (?, ?, ?, ?)',
                  (user_id, account, password, username))
        self.connect.commit()

    #   添加资金信息，现在有资金信息id，相关信息和有关user的id三个数据
    def add_new_revenue_info(self, revenue_id, revenue_info, relevant_user_id):
        print("添加资金信息：")
        self.cursor.execute('INSERT INTO revenueInfos VALUES (?, ?, ?)',
                  (revenue_id, revenue_info, relevant_user_id))
        self.connect.commit()

    #   根据id获取用户所有信息
    def get_user_info_by_id(self, user_id):
        print("获取对应id的用户信息")
        self.cursor.execute('SELECT * FROM users WHERE user_id= ?',
                            user_id)
        data = self.cursor.fetchall()
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