#!/usr/bin/env python3
# _*_coding:utf-8_*_
from tornado import web

from admin.controller.indexController import IndexController
from admin.controller.loginController import LoginController

admin_urls = [
    # 首页 登录 登出
    web.URLSpec(r"/", IndexController, name="index"),
    web.URLSpec(r"/admin", IndexController, name="admin"),
    web.URLSpec(r"/login", LoginController, name="login"),
    # web.URLSpec(r"/logout", AdminLogoutHandler, name="logout"),
    # # 用户管理
    # web.URLSpec(r"/admin/user", AdminUserHandler, name="admin_user"),
    # web.URLSpec(r"/admin/user/add", AdminUserAddHandler, name="admin_user_add"),
    # web.URLSpec(r"/admin/user/update", AdminUserUpdateHandler, name="admin_user_update"),
    # web.URLSpec(r"/admin/user/delete", AdminUserDeleteHandler, name="admin_user_delete"),
    # # 角色管理
    # web.URLSpec(r"/admin/role", AdminRoleHandler, name="admin_role"),
    # web.URLSpec(r"/admin/role/add", AdminRoleAddHandler, name="admin_role_add"),
    # web.URLSpec(r"/admin/role/update", AdminRoleUpdateHandler, name="admin_role_update"),
    # web.URLSpec(r"/admin/role/delete", AdminRoleDeleteHandler, name="admin_role_delete"),
    # # 权限节点管理
    # web.URLSpec(r"/admin/node", AdminNodeHandler, name="admin_node"),
    # web.URLSpec(r"/admin/node/add", AdminNodeAddHandler, name="admin_node_add"),
    # web.URLSpec(r"/admin/node/update", AdminNodeUpdateHandler, name="admin_node_update"),
    # web.URLSpec(r"/admin/node/delete", AdminNodeDeleteHandler, name="admin_node_delete"),
    # # 用户角色管理
    # web.URLSpec(r"/admin/user_role", AdminUserRoleHandler, name="admin_user_role"),
    # web.URLSpec(r"/admin/user_role/add", AdminUserRoleAddHandler, name="admin_user_role_add"),
    # web.URLSpec(r"/admin/user_role/update", AdminUserRoleUpdateHandler, name="admin_user_role_update"),
    # web.URLSpec(r"/admin/user_role/delete", AdminUserRoleDeleteHandler, name="admin_user_role_delete"),
    # # 角色节点管理
    # web.URLSpec(r"/admin/role_node", AdminRoleNodeHandler, name="admin_role_node"),
    # web.URLSpec(r"/admin/role_node/add", AdminRoleNodeAddHandler, name="admin_role_node_add"),
    # web.URLSpec(r"/admin/role_node/update", AdminRoleNodeUpdateHandler, name="admin_role_node_update"),
    # web.URLSpec(r"/admin/role_node/delete", AdminRoleNodeDeleteHandler, name="admin_role_node_delete"),

]
