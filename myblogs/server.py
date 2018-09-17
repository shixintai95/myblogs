import tornado.ioloop
import tornado.web
import config

from tornado.httpserver import HTTPServer
from application import Application


if __name__ == "__main__":
    app = Application()
    httpServer = HTTPServer(app)
    httpServer.bind(config.options["port"])
    httpServer.start()
    tornado.ioloop.IOLoop.current().start()