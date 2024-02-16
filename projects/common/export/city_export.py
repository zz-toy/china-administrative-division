# -*- coding:utf-8 -*-

from common.helper import Helper
from .export import ABCExport
from .city import build_city
from .rule import CITY_FLATTEN_JSON_FILENAME, \
    CITY_FLATTEN_CSV_FILENAME, \
    CITY_CASCADE_JSON_FILENAME, \
    NAME_KEY, CODE_KEY, PROVINCE_NAME_KEY, PROVINCE_CODE_KEY


class CityExport(ABCExport):
    def export(self):
        res = build_city(city_list=self.data_source.pc_list())
        Helper.write_json(Helper.flatten_dict_values(res[0]), self.dist_path, CITY_FLATTEN_JSON_FILENAME)
        Helper.write_csv(Helper.flatten_dict_values(res[0]), self.dist_path, CITY_FLATTEN_CSV_FILENAME,
                         [NAME_KEY, CODE_KEY, PROVINCE_NAME_KEY, PROVINCE_CODE_KEY])
        Helper.write_json(Helper.flatten_dict_values(res[1]), self.dist_path, CITY_CASCADE_JSON_FILENAME)
        print('=======================')
