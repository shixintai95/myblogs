import os

BASE_PATH = os.path.dirname(__file__)

options = {
    "port": 8000
}

mysql = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "sxt123123",
    "dbName": "blog",
}


settings = {
    "static_path": os.path.join(BASE_PATH, "static"),
    "template_path": os.path.join(BASE_PATH, "templates"),
    # 设置安全cookie需要添加的配置,base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
    "cookie_secret": "NwbmfWPOQiGduwgftJRme98bbzWPREStp5WR5cm3hoI=",
    "debug": True,
    "login_url": "/login",
    "xsrf_cookies": True,
}