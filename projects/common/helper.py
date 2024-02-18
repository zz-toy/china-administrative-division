# -*- coding:utf-8 -*-
import csv
import json
import os.path
import itertools

from common.export.rule import CODE_KEY, CHILDREN_KEY, LABEL_KEY, LEVEL_TOP, VALUE_KEY, LEVEL_SECOND
from common.settings import BASE_DIR


class Helper:
    @staticmethod
    def dist_path():
        return f'{BASE_DIR}/../dist'

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
    def write_json(data, out_path: str, filename: str):
        if data is None:
            print('写入数据不能为空')
            return

        if not out_path or not filename:
            print('路径或文件名不能为空')
            return

        with open(os.path.join(out_path, filename), "w", encoding="utf8") as file:
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

        with open(os.path.join(out_path, filename), "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=header, quoting=csv.QUOTE_NONNUMERIC)
            writer.writeheader()
            writer.writerows(data)

        print(f"create {filename} success")

    @staticmethod
    def flatten_dict_values(data: dict):
        if data is None:
            return []
        return list(itertools.chain.from_iterable(list(data.values())))

    @staticmethod
    def filter_province(data: str) -> str:
        if data[-1] == "省":
            return data.rstrip("省")
        if data[-1] == "市":
            return data.rstrip("市")

        return data

    @staticmethod
    def filter_city(data: str) -> str:
        if data[-1] == "市":
            return data.rstrip("市")

        return data

    @staticmethod
    def to_zn_data(data: list = None, level: int = LEVEL_TOP):
        if data is None:
            data = []

        for item in data:
            if isinstance(item, dict):
                if level == LEVEL_TOP:
                    item[LABEL_KEY] = Helper.filter_province(item[LABEL_KEY])
                    item[VALUE_KEY] = Helper.filter_province(item[VALUE_KEY])
                elif level == LEVEL_SECOND:
                    item[LABEL_KEY] = Helper.filter_city(item[LABEL_KEY])
                    item[VALUE_KEY] = Helper.filter_city(item[VALUE_KEY])

                if CODE_KEY in item.keys():
                    del item[CODE_KEY]

                if CHILDREN_KEY in item.keys() and isinstance(item.get(CHILDREN_KEY), list):
                    Helper.to_zn_data(data=item.get(CHILDREN_KEY), level=level+1)

    @staticmethod
    def zn_json_data(data: list = None) -> dict:
        Helper.to_zn_data(data)
        return {
            "errcode": 200,
            "errmsg": "success",
            "data": data
        }
