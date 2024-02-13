import typing
import pymysql
import pymysql.cursors


class DbManager:
    connection = None

    def __init__(self, db_config: dict = None):
        if db_config is None:
            db_config = {}
        self.db_config = db_config
        self._connect()

    def _connect(self):
        if self.connection is None:
            self.connection = pymysql.connect(
                host=self.db_config.get('HOST'),
                port=self.db_config.get('PORT'),
                user=self.db_config.get('USERNAME'),
                password=self.db_config.get('PASSWORD'),
                db=self.db_config.get('DATABASE'),
                charset=self.db_config.get('CHARSET'),
                cursorclass=pymysql.cursors.DictCursor
            )
            self.connection.ping()

    def close(self):
        if self.connection is not None:
            self.connection.close()

    def execute(self, sql) -> bool:
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(sql)
                self.connection.commit()
                return True
            except Exception as e:
                print(e)
                self.connection.rollback()
                return False

    def fetchone(self, table_name: str, columns, where=None, params=None) -> typing.Dict | None:
        if columns and not isinstance(columns, str):
            columns = ', '.join(columns)

        sql = f"SELECT {columns} FROM {table_name}"
        if where:
            sql += f" WHERE {where}"

        with self.connection.cursor() as cursor:
            try:
                cursor.execute(sql, params)
                return cursor.fetchone()
            except Exception as e:
                print(e)
                return None

    def fetchall(self, table_name: str, columns="*", where=None, params=None) -> typing.Tuple | None:
        if columns and not isinstance(columns, str):
            columns = ', '.join(columns)

        sql = f"SELECT {columns} FROM {table_name}"
        if where:
            sql += f" WHERE {where}"

        with self.connection.cursor() as cursor:
            try:
                cursor.execute(sql)
                return cursor.fetchall()
            except Exception as e:
                print(e)
                return None

    def insert(self, table_name: str, data: dict) -> int:
        if not table_name or len(data) == 0:
            return 0

        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = f"INSERT INTO {table_name} ({keys}) VALUES ({values})"
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(sql, tuple(data.values()))
                self.connection.commit()
                return cursor.lastrowid
            except Exception as e:
                print(e)
                self.connection.rollback()
                return 0

    def insert_many(self, table_name: str, column: str, data: list) -> int:
        if not table_name or len(data) == 0 or not column:
            return 0

        column_list = column.split(',')
        values = ', '.join(['%s'] * len(column_list))
        sql = f"INSERT INTO {table_name} ({column}) VALUES ({values})"
        with self.connection.cursor() as cursor:
            try:
                cursor.executemany(sql, data)
                self.connection.commit()
                return self.connection.affected_rows()
            except Exception as e:
                print(e)
                self.connection.rollback()
                return 0

    def update(self, table_name: str, data: dict, where=None, params=None):
        if not where:
            print(ValueError("缺失WHERE条件"))
            return 0

        set_values = ', '.join([f"{k}=%s" for k in data.keys()])
        sql = f"UPDATE {table_name} SET {set_values} WHERE {where}"
        params = tuple(data.values()) + params if params else tuple(data.values())
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(sql, params)
                self.connection.commit()
                return self.connection.affected_rows()
            except Exception as e:
                print(e)
                self.connection.rollback()
                return 0

    def delete(self, table_name: str, where=None, params=None):
        if not where:
            print(ValueError("缺失WHERE条件"))
            return 0

        sql = f"DELETE FROM {table_name} WHERE {where}"
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(sql, params)
                self.connection.commit()
                return self.connection.affected_rows()
            except Exception as e:
                print(e)
                self.connection.rollback()
                return 0


if __name__ == '__main__':
    config = {
        "HOST": "192.168.200.253",
        "PORT": 3400,
        "USERNAME": "root",
        "PASSWORD": "123456",
        "DATABASE": "govstat",
        "CHARSET": "utf8mb4",
    }
    db_manager = DbManager(config)

    # 插入数据
    # insert_sql = "INSERT INTO `province`(`name`,`code`,`url`) values('山西省', '121212', 'http://shanxi.com'),('河北省', '2222', 'http://hebei.com')"
    # res = db_manager.execute(insert_sql)
    # print("res:", res)
    # if res > 0:
    #     print("插入成功")
    # else:
    #     print("插入失败")

    # 插入数据
    # res = db_manager.insert('province', {'name': '陕西省'})
    # print("res:", res)
    # if res > 0:
    #     print("插入成功")
    # else:
    #     print("插入失败")

    # 插入多条数据
    # column = "name,code,url"
    # data = [('山西省', 12, 'xxxx'), ('河北省', 13, 'xxxxx')]
    # res = db_manager.insert_many('province_t', column, data)
    # print('res:', res)

    # 查询单条数据
    # province_record = db_manager.fetchone('province', columns='*', where="name=%s", params=('山西省',))
    # print("province_record:", province_record)

    # 查询多条数据
    # province_records = db_manager.fetchall('province', columns='*')
    # print("province_records:", province_records)
    pass
