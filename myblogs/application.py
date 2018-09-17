from tornado import web
from tornado.web import Application

from view import index
import config
import os


class Application(Application):

    def __init__(self):
        handler = [
            # (r"/", index.IndexHandler),
            (r"/login", index.LoginHandler),
            (r"/register", index.RegisterHandler),
            (r"/logout", index.LogoutHandler),
            (r"/home", index.HomeHandler),
            (r"/release", index.ReleaseHandler),
            (r"/showblogs", index.ShowBlogsHandler),
            (r"/(.*)$", index.StaticFileHandler,
             {"path": os.path.join(config.BASE_PATH, "static/html"),
              "default_filename": "index.html"})
        ]
        super().__init__(handler, **config.settings)
