# -*- coding:utf-8 -*-
import csv
import json
import os.path
import itertools
from common.settings import BASE_DIR


class Helper:
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
    def dist_path():
        return f'{BASE_DIR}/../dist'
