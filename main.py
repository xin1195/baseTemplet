#!/usr/bin/env python3
# _*_coding:utf-8_*_


import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

from setting import settings
from urls import urls

define("port", default=8000, help="run on the given port", type=int)

application = tornado.web.Application(
    handlers=urls,
    **settings
)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application, xheaders=True)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
