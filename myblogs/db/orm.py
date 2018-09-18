from db.mysql_db import MysqlDB


class ORM:

    def save(self):
        # 开始拼接
        table_name = self.__class__.__name__.lower()
        fields_str = values_str = "("
        for key, value in self.__dict__.items():
            fields_str += (key + ",")
            if isinstance(value, str):
                values_str += ("'" + value + "',")
            else:
                values_str += (str(value) + ",")
        fields_str = fields_str[:len(fields_str)-1] + ")"
        values_str = values_str[:len(values_str)-1] + ")"

        sql = "insert into " + table_name + fields_str + " values" + values_str
        print("orm save():", sql)
        db = MysqlDB()
        return db.insert(sql)

    def select_one(self, *args, **kwargs):
        """
        查询一条记录，可以传入多个参数
        :param args: 传入需要查询的字段名
        :param kwargs: where语句后跟的字段名和条件
        :return:
        """
        table_name = self.__class__.__name__.lower()
        field_str = values_str = ""
        for field in args:
            field_str += (field + ",")
        # 拼接字段名
        field_str = field_str[:len(field_str)-1]
        for key, value in kwargs.items():
            if isinstance(value, str):
                values_str += (key + "='" + value + "' and ")
            else:
                values_str += (key + "=" + value + " and ")
        # 拼接查询条件
        values_str = values_str[:len(values_str)-4]
        print("orm select_one() columns:", field_str)
        print("orm select_one() values:", values_str)
        sql = "select " + field_str + " from " + table_name + " where " + values_str
        print("orm select_one() sql:", sql)
        db = MysqlDB()
        return db.get_one(sql)

    def select_all(self, *args, **kwargs):
        """
        查询多条记录，可以传入多个参数
        :param args: 传入需要查询的字段名
        :param kwargs: where语句后跟的字段名和条件
        :return:
        """
        table_name = self.__class__.__name__.lower()
        field_str = values_str = ""
        if len(args) == 0:
            field_str = "*"
        else:
            for field in args:
                field_str += (field + ",")
            field_str = field_str[:len(field_str)-1]
        if len(kwargs) == 0:
            values_str = "1"
        else:
            for key, value in kwargs.items():
                if isinstance(value, str):
                    values_str += (key + "='" + value + "' and ")
                else:
                    values_str += (key + "=" + value + " and ")
            values_str = values_str[:len(values_str)-4]
        print("orm select_all() columns:", field_str)
        print("orm select_all() values:", values_str)
        sql = "select " + field_str + " from " + table_name + " where " + values_str + " order by create_time desc"
        print("orm select_all() sql:", sql)
        db = MysqlDB()
        return db.get_all_list(sql, table_name)

    def update(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """
        table_name = self.__class__.__name__.lower()
        field_str = values_str = ""
        # 拼接设置值
        num = 0
        for field in args:
            if num % 2 == 0:
                field_str += (field + "=")
            else:
                if isinstance(field, str):
                    field_str += ("'" + field + "',")
                else:
                    field_str += (str(field) + ",")
            num += 1
        field_str = field_str[:len(field_str) - 1]
        print("orm update() columns:", field_str)
        # 拼接条件
        for key, value in kwargs.items():
            if isinstance(value, str):
                values_str += (key + "='" + value + "' and ")
            else:
                values_str += (key + "=" + value + " and ")
        values_str = values_str[:len(values_str)-4]
        print("orm update() values:", values_str)
        sql = "update " + table_name + " set " + field_str + " where " + values_str
        print("orm update() sql:", sql)
        db = MysqlDB()
        return db.update(sql)
