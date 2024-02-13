# -*- coding:utf-8 -*-
import csv
import json

from govstat.settings import DB, BASE_DIR
from govstat.database import DbManager


class Query:
    db = None

    def __init__(self):
        self.db = DbManager(DB)

    def close(self):
        if self.db is not None:
            self.db.close()

    def fetch_many_province(self, columns="*", where=None, params=None) -> tuple:
        rows = self.db.fetchall("province", columns="*", where=None, params=None)
        if rows is None:
            return ()
        return rows

    def fetch_many_city(self, columns="*", where=None, params=None) -> tuple:
        rows = self.db.fetchall("city", columns="*", where=None, params=None)
        if rows is None:
            return ()
        return rows

    def fetch_many_county(self, columns="*", where=None, params=None) -> tuple:
        rows = self.db.fetchall("county", columns="*", where=None, params=None)
        if rows is None:
            return ()
        return rows

    def fetch_many_town(self, columns="*", where=None, params=None) -> tuple:
        rows = self.db.fetchall("town", columns="*", where=None, params=None)
        if rows is None:
            return ()
        return rows

    def fetch_many_village(self, columns="*", where=None, params=None) -> tuple:
        rows = self.db.fetchall("village", columns="*", where=None, params=None)
        if rows is None:
            return ()
        return rows


class Util:
    @staticmethod
    def collection_to_key_dict(collection: tuple | list, key: str = 'id') -> dict:
        if collection is None:
            return {}
        if not key:
            return {}

        res = {}
        for item in collection:
            if item.get(key) in res.keys():
                continue
            res[item.get(key)] = item

        return res

    @staticmethod
    def out_path() -> str:
        return BASE_DIR + '/../dist'

    @staticmethod
    def write_json(data, out_path: str, filename: str):
        if data is None:
            print('写入数据不能为空')
            return

        if not out_path or not filename:
            print('路径或文件名不能为空')
            return

        with open(f"{out_path}/{filename}", "w", encoding="utf8") as file:
            json.dump(data, file, ensure_ascii=False, separators=(',', ':'))

        print(f"create {filename} success")

    @staticmethod
    def write_csv(data: list, out_path: str, filename: str, header=None):
        if data is None or len(data) == 0:
            print('写入数据不能为空')
            return

        if not out_path or not filename:
            print('路径或文件名不能为空')
            return

        if header is None:
            header = []

        with open(f"{out_path}/{filename}", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=header, quoting=csv.QUOTE_NONNUMERIC)
            writer.writeheader()
            writer.writerows(data)

        print(f"create {filename} success")