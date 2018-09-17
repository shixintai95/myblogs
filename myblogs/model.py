from db.orm import ORM
from datetime import datetime


class User(ORM):

    def __init__(self, username=None, password=None, count=None):
        self.username = username
        self.password = password
        self.create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.count = count

# u = User("sxt", "pwej")
# print(u.__dict__)

# CREATE TABLE `user` (
#   `id` int NOT NULL auto_increment,
#   `username` varchar(20) NOT NULL,
#   `password` varchar(20) NOT NULL,
#   `create_time` timestamp NOT NULL ,
#   PRIMARY KEY  (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

# fields_str = "(username,password,create_time,"
# fields_str = fields_str[:len(fields_str)-1] + ")"
# print(fields_str)

# t = ["name", "pass"]
# print(tuple(t))

# s = "abc" + 1
# print(s)


class Blog(ORM):
    def __init__(self, blog_title=None, blog_type=None, blog_content=None, uname=None):
        self.blog_title = blog_title
        self.blog_type = blog_type
        self.blog_content = blog_content
        self.uname = uname

# v = b'admin'
# m = str(v)
# print(m)
# m = m[2:-1]
# print(m)

# m = "(name,age,sex)"
# print(tuple(m))
# t = {}
# print(len(tuple(t)))


# CREATE TABLE `blog` (
#   `bid` int NOT NULL auto_increment,
#   `blog_title` varchar(50) NOT NULL,
#   `blog_type` varchar(20) NOT NULL,
#   `blog_content` text,
#   `uname` varchar(20) NOT NULL,
#   primary key  (`bid`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
