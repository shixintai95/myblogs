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
                values_str += (value + ",")
        fields_str = fields_str[:len(fields_str)-1] + ")"
        values_str = values_str[:len(values_str)-1] + ")"

        sql = "insert into " + table_name + fields_str + " values" + values_str
        print(sql)
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
        print(field_str)
        print(values_str)
        sql = "select " + field_str + " from " + table_name + " where " + values_str
        print(sql)
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
            values_str = 1
        else:
            for key, value in kwargs.items():
                if isinstance(value, str):
                    values_str += (key + "='" + value + "' and ")
                else:
                    values_str += (key + "=" + value + " and ")
            values_str = values_str[:len(values_str)-4]
        print(field_str)
        print(values_str)
        sql = "select " + field_str + " from " + table_name + " where " + values_str
        print(sql)
        db = MysqlDB()
        return db.get_all_list(sql, table_name)
