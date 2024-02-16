# -*- coding:utf-8 -*-

from common.helper import Helper
from .export import ABCExport
from .province import build_province
from .rule import PROVINCE_FLATTEN_JSON_FILENAME, \
    PROVINCE_FLATTEN_CSV_FILENAME, \
    PROVINCE_CASCADE_JSON_FILENAME, \
    NAME_KEY, CODE_KEY


class ProvinceExport(ABCExport):
    def export(self):
        res = build_province(province_list=self.data_source.province_list())
        Helper.write_json(res[0], self.dist_path, PROVINCE_FLATTEN_JSON_FILENAME)
        Helper.write_csv(res[0], self.dist_path, PROVINCE_FLATTEN_CSV_FILENAME, [NAME_KEY, CODE_KEY])
        Helper.write_json(res[1], self.dist_path, PROVINCE_CASCADE_JSON_FILENAME)
        print('=======================')
