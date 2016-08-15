#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by Administrator 
# Time 2016/7/27.

from tornado import gen
from setting import logger, g_py_db
import traceback


@gen.coroutine
def check_auth_sync(self):
    try:
        node_id = self.request.uri.split("?")[0]
        # 查询用户属于哪些角色
        role_ids = []
        query = {"username": self.get_secure_cookie("user").decode('utf-8')}
        show = {"_id": 0}
        user_role_dict = yield self.db.sys_user_role.find_one(query, show)
        for role_id, role_name in user_role_dict.get("role", {}).items():
            role_ids.append(role_id)
        # 查询这些角色有哪些权限
        node_ids = set()
        query = {"role_id": {"$in": role_ids}}
        cursor = self.db.sys_role_node.find(query, show)
        while (yield cursor.fetch_next):
            sys_role_node = cursor.next_object()
            for node_id, node_name in sys_role_node.get("node", {}).items():
                node_ids.add(node_id)
        if node_id in node_ids:
            return 1
        else:
            return 0
    except:
        logger.error(traceback.format_exc())
        return 0


def check_auth(self):
    try:
        url_node_id = self.request.uri.split("?")[0]
        # 查询用户属于哪些角色
        role_ids = []
        query = {"username": self.get_secure_cookie("user").decode('utf-8')}
        show = {"_id": 0}
        user_role_dict = g_py_db.sys_user_role.find_one(query, show)
        for role_id, role_name in user_role_dict.get("role", {}).items():
            role_ids.append(role_id)
        # 查询这些角色有哪些权限
        node_ids = set()
        query = {"role_id": {"$in": role_ids}}
        sys_role_nodes = g_py_db.sys_role_node.find(query, show)
        for sys_role_node in sys_role_nodes:
            for node_id, node_name in sys_role_node.get("node", {}).items():
                node_ids.add(node_id)
        if url_node_id in node_ids:
            return 1
        else:
            return 0
    except:
        logger.error(traceback.format_exc())
        return 0


# 权限装饰器
def auth_permissions(func):
    def inner(self, *args, **kwargs):
        ret = check_auth(self)
        if ret:
            return func(self, *args, **kwargs)
        else:
            self.render("admin/403.html")

    return inner