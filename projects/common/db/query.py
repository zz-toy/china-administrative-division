# -*- coding:utf-8 -*-

from .database import DbManager


class Query:
    db = None

    def __init__(self, db_config: dict = None):
        self.db = DbManager(db_config)

    def close(self):
        if self.db is not None:
            self.db.close()

    def fetch_many_province(self, columns="*", where=None, params=None) -> tuple:
        rows = self.db.fetchall("province", columns, where, params)
        if rows is None:
            return ()
        return rows

    def fetch_many_city(self, columns="*", where=None, params=None) -> tuple:
        rows = self.db.fetchall("city", columns, where, params)
        if rows is None:
            return ()
        return rows

    def fetch_many_county(self, columns="*", where=None, params=None) -> tuple:
        rows = self.db.fetchall("county", columns, where, params)
        if rows is None:
            return ()
        return rows

    def fetch_many_town(self, columns="*", where=None, params=None) -> tuple:
        rows = self.db.fetchall("town", columns, where, params)
        if rows is None:
            return ()
        return rows

    def fetch_many_village(self, columns="*", where=None, params=None) -> tuple:
        rows = self.db.fetchall("village", columns, where, params)
        if rows is None:
            return ()
        return rows

    def fetch_xiongan_city(self, columns="*") -> dict:
        record = self.db.fetchone("city", columns, where="name=%s", params=("雄安新区",))
        if record is None:
            return {}
        return record

    def fetch_baoding_city(self, columns="*") -> dict:
        record = self.db.fetchone("city", columns, where="name=%s", params=("保定市",))
        if record is None:
            return {}
        return record

    def fetch_many_town_join(self) -> tuple | None:
        """字段顺序不能乱"""
        sql = """
            SELECT
        	b.NAME AS province_name,
        	b.full_code AS province_code,
        	c.NAME AS city_name,
        	c.full_code AS city_code,
        	d.NAME AS county_name,
        	d.full_code AS county_code,
        	a.NAME AS town_name,
        	a.full_code AS town_code 
        FROM
        	town AS a
        	LEFT JOIN province AS b ON a.province_id = b.id
        	LEFT JOIN city AS c ON a.city_id = c.id
        	LEFT JOIN county AS d ON a.county_id = d.id"""
        with self.db.connection.cursor() as cursor:
            try:
                cursor.execute(sql)
                return cursor.fetchall()
            except Exception as e:
                print(e)
                return None
