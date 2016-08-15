#!/usr/bin/env python3
# _*_coding:utf-8_*_
import os

from common.LogManage import get_logger
from common.settingLib import get_mongodb_db

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    cookie_secret="bZJc2sWbQLKVtFhBGFDdGkHn/dsaHsFFa0kRvJ5/xJ89E=",
    login_url="/login",
    xsrf_cookies=True,
    debug=True,

)

# 日志模块
logger = get_logger(
    strFileName="base_templet.log",
    debug=10,
    showStreamLog=True,
    saveLogPath=None
)

# 获取数据库连接
if get_mongodb_db(settings.get("debug", "False")):
    # debug=True 表示使用线上库，Flase表示使用测试库
    database, g_motor_db, g_py_db = get_mongodb_db(settings.get("debug", "False"))
    logger.info("(%s)数据库连接成功" % database)
else:
    logger.info("数据库连接失败")















