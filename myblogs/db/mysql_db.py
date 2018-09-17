import pymysql
import config


class MysqlDB:
    instance = None
    host = config.mysql["host"]
    user = config.mysql["user"]
    password = config.mysql["password"]
    dbName = config.mysql["dbName"]

    # 设置单例模式
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


    # 连接数据库
    def connect(self):
        self.db = pymysql.connect(self.host, self.user, self.password, self.dbName)
        self.cursor = self.db.cursor()

    # 关闭数据库
    def close(self):
        self.cursor.close()
        self.db.close()

    # 查询一条数据
    def get_one(self, sql):
        res = None
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            self.close()
        except:
            print("查询失败")
        return res

    # 获取所有
    # 结果集返回的是tuple类型
    def get_all_tuple(self, sql):
        res = None
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.close()
        except:
            print("查询失败")
        return res

    def get_all_list(self, sql, table_name, *args):
        result_list = []
        field_list = []
        if len(args) > 0:
            for item in args:
                field_list.append(item)
        else:
            # 查询表头字段
            field_sql = "select column_name from information_schema.columns " \
                        "where table_name='%s' and table_schema='%s'" % (self.dbName, table_name)
            field = self.get_all_tuple(field_sql)
            for item in field:
                field_list.append(item[0])
        # ((1, 'zhangsan', 23), (2, 'wanghu', 43))
        result_tuple = self.get_all_tuple(sql)
        for values in result_tuple:
            obj = {}
            count = 0
            for value in values:
                obj[field_list[count]] = value
                count += 1
            result_list.append(obj)
        return result_list

    # 修改
    def update(self, sql):
        return self._common(sql)

    # 删除
    def delete(self, sql):
        return self._common(sql)

    # 插入
    def insert(self, sql):
        return self._common(sql)

    def _common(self, sql):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.close()
        except:
            print("执行失败")
            self.db.rollback()
        return count

