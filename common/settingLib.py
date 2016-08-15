#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by Administrator 
# Time 2016/8/4.
# setting文件专用的函数文件库
# 主要用于储存setting文件中使用的函数

import traceback
import motor.motor_tornado
from pymongo import MongoClient


def get_mongodb_db(flag):
    """
    :param flag: 数据选择 debug=True 测试库， False 线上库
    :return: database 数据库， g_motor_client 基于motor的连接 ，g_py_client 基于 pymongo 的连接
    """
    try:
        if flag:
            # 测试库
            mongodb_path = 'mongodb://112.74.204.250:27017/baseTempletTest?slaveOk=false'
            g_motor_db = motor.motor_tornado.MotorClient(mongodb_path).baseTempletTest
            g_py_db = MongoClient(mongodb_path).baseTempletTest
            return mongodb_path, g_motor_db, g_py_db
        else:
            # 线上库
            mongodb_path = 'mongodb://112.74.204.250:47017/baseTemplet?slaveOk=false'
            g_motor_db = motor.motor_tornado.MotorClient(mongodb_path).baseTemplet
            g_py_db = MongoClient(mongodb_path).baseTemplet
            return mongodb_path, g_motor_db, g_py_db
    except:
        traceback.format_exc()
        return 0
