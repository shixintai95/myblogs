from tornado import web
from tornado.web import RequestHandler

import model


# 登录
class LoginHandler(RequestHandler):

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)

    def get(self, *args, **kwargs):
        # 正常登陆情况下，进入home的url
        next = self.get_query_argument("next", "home")
        if next == "/release" or next == "/showblogs":
            flag = "nologin"
        else:
            flag = ""
        url = "login?next=%s" % next
        self.render("login/login.html", flag=flag, url=url)

    def post(self, *args, **kwargs):
        username = self.get_body_argument("username")
        password = self.get_body_argument("password")
        user = model.User()
        db_password = user.select_one("password", "count", username=username)

        url = "login?next="
        if db_password is not None:
            if password == db_password[0]:
                self.set_secure_cookie("username", username, expires_days=None)
                # 设置登录次数
                user.update("count", db_password[1] + 1, username=username)
                self.redirect(self.get_query_argument("next", "home"))
            else:
                self.render("login/login.html", flag="error", url=url)
        else:
            self.render("login/login.html", flag=None, url=url)


# 注册
class RegisterHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("login/register.html")

    def post(self, *args, **kwargs):
        username = self.get_body_argument("username")
        password = self.get_body_argument("password")
        user = model.User(username, password, 1)
        result = user.save()
        if result == 1:
            self.write("注册成功")
            self.redirect("/login")
        else:
            self.write("注册失败,请重新注册")
            self.redirect("/register")


# 注销
class LogoutHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.clear_cookie("username")
        self.redirect("/login")


# 主页
class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("login/home.html", username=self.get_secure_cookie("username"))


# 发布博客
class ReleaseHandler(RequestHandler):

    # 设置用户验证：
    # 1.首先给要验证的请求加上装饰器，
    # 2.然后在全局配置中配置"login_url"请求不通过后，所要跳转的地址
    # 3.执行方法get_current_user(),若返回true，则进入请求; 否则进入全局配置的地址
    @web.authenticated
    def get(self, *args, **kwargs):
        self.render("release/release.html")

    def post(self, *args, **kwargs):
        blog_title = self.get_argument("blog_title")
        blog_type = self.get_argument("blog_type")
        blog_content = self.get_argument("blog_content")
        username = self.get_secure_cookie("username")
        blog = model.Blog(blog_title, blog_type, blog_content, str(username)[2:-1])
        result = blog.save()
        if result == 1:
            self.redirect("/showblogs")
        else:
            self.write("发布失败")

    def get_current_user(self):
        cookie = self.get_secure_cookie("username")
        return cookie


# 查看博客
class ShowBlogsHandler(RequestHandler):
    @web.authenticated
    def get(self, *args, **kwargs):
        username = self.get_secure_cookie("username")
        blog = model.Blog()
        blog_list = blog.select_all(uname=str(username)[2:-1])
        print(blog_list)
        self.render("release/show.html", blog_list=blog_list)

    def get_current_user(self):
        cookie = self.get_secure_cookie("username")
        return cookie

