#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by Administrator 
# Time 2016/8/15.


from admin.controller.baseController import BaseController


class IndexController(BaseController):
    def get(self):
        self.render("admin/index.html")



