# -*- coding:utf-8 -*-
'''
Created on 2014-9-4

@author: yuzhongfu
'''

import os
import sys
import logging.handlers

"""各种日志级别对应的值
CRITICAL = 50
ERROR = 40
WARNING = 30
INFO = 20
DEBUG = 10
NOTSET = 0
"""
_logger_level = 30
_dictLogger = {}
_default_log_name = "common_api.log"
__doc__ = """"""


class LogManage:
    def __init__(self, strFileName=_default_log_name, debug=_logger_level, bShowStreamLog=False, strSaveLogPath=None):

        self.__strShowStreamLog = True
        self.__logger = None
        # 保存日志的文件名
        self.__strFileName = strFileName
        # 保存日志的文件路径
        self.__strSaveLogPath = strSaveLogPath
        # 单个文件大小设置为20M
        self.__nLogFileSize = 20 * 1024 * 1024
        # 最多保存10个文件
        self.__nLogFileNum = 10
        # 日志级别
        self.__nLogLevel = debug
        # 是否显示流日志
        self.__bShowStreamLog = bShowStreamLog
        # 日志格式
        self.__objLogFormat = "[%(asctime)s][%(filename)s][%(lineno)s][thread:%"
        self.__objLogFormat += "(thread)s][process:%(process)s][%(levelname)s] %(message)s"

        self.__initLogger()

    def __initLogger(self):
        # 同一个logger只允许初始化一次
        global _dictLogger
        logger = _dictLogger.get(self.__strFileName, None)
        if logger is not None:
            self.__logger = logger
            return

        # 保存的文件夹不存在，则创建
        dirFileName = os.path.dirname(self.__strFileName)
        strFileName = os.path.basename(self.__strFileName)

        if dirFileName == "" or dirFileName == ".":
            dirFileName = sys.path[0]
            dirFileName = os.path.join(dirFileName, "logs")

        if self.__strSaveLogPath:
            dirFileName = os.path.join(self.__strSaveLogPath, "logs")

        dirFileName = os.path.realpath(dirFileName)

        if not os.path.exists(dirFileName):
            os.makedirs(dirFileName)

        self.__strFileName = os.path.join(dirFileName, strFileName)

        # 文件handler
        fileHandler = logging.handlers.RotatingFileHandler(self.__strFileName,
                                                           maxBytes=self.__nLogFileSize,
                                                           backupCount=self.__nLogFileNum)
        # 实例化formatter
        formatter = logging.Formatter(self.__objLogFormat)
        fileHandler.setFormatter(formatter)

        self.__logger = logging.getLogger(self.__strFileName)
        # 为logger添加handler
        self.__logger.addHandler(fileHandler)
        _dictLogger[self.__strFileName] = self.__logger
        # 增加一个流handler
        steamHandler = logging.StreamHandler()
        steamHandler.setFormatter(formatter)
        self.steamHandler = steamHandler
        if self.__bShowStreamLog:
            self.__logger.addHandler(steamHandler)

        # 设置日志级别
        self.__logger.setLevel(self.__nLogLevel)

    def addStreamHandler(self):
        # 增加一个流handler
        try:
            # 如果已经增加直接返回
            if self.__strShowStreamLog:
                return
            self.__logger.addHandler(self.steamHandler)
        except:
            pass

    def setLogLevel(self, logLevel):
        # 重新设置日志级别
        self.__logger.setLevel(self.__nLogLevel)

    def getLogger(self):
        return self.__logger


def get_logger(strFileName=_default_log_name,
               debug=_logger_level,
               showStreamLog=False,
               saveLogPath=None):
    global _dictLogger
    logger = _dictLogger.get(strFileName, None)
    if logger is not None:
        return logger

    objLogger = LogManage(strFileName, debug, showStreamLog, saveLogPath)
    logger = objLogger.getLogger()

    return logger


def _testLog():
    logger = get_logger(strFileName="log_api.log",
                        debug=30,
                        showStreamLog=True,
                        saveLogPath=None)
    # logger.error("ERROR-ERROE-" * 5)
    # logger.debug("DEBUG-DEBUG-" * 5)
    #
    # objLogger = LogManage("nameas.log")
    # logger = objLogger.getLogger()
    # for item in xrange(1):
    #     logger.error("%5d" % item * 50)


if __name__ == "__main__":
    _testLog()
