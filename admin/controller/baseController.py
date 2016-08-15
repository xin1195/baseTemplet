#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by Administrator 
# Time 2016/8/15.

import tornado.web

from setting import g_motor_db


class BaseController(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseController, self).__init__(application, request, **kwargs)
        self.db = g_motor_db

    def data_received(self, chunk):
        pass

    def get_current_user(self):
        return self.get_secure_cookie("user")

    def on_finish(self):
        pass
