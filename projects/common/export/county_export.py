# -*- coding:utf-8 -*-

from .export import ABCExport
from common.helper import Helper
from .county import build_county
from .rule import COUNTY_FLATTEN_JSON_FILENAME, \
    COUNTY_FLATTEN_CSV_FILENAME, \
    COUNTY_CASCADE_JSON_FILENAME, \
    NAME_KEY, CODE_KEY, PROVINCE_NAME_KEY, PROVINCE_CODE_KEY, \
    CITY_NAME_KEY, CITY_CODE_KEY


class CountyExport(ABCExport):
    def export(self):
        res = build_county(county_list=self.data_source.pcc_list())
        Helper.write_json(Helper.flatten_dict_values(res[0]), self.dist_path, COUNTY_FLATTEN_JSON_FILENAME)
        Helper.write_csv(Helper.flatten_dict_values(res[0]), self.dist_path, COUNTY_FLATTEN_CSV_FILENAME,
                         [NAME_KEY, CODE_KEY, CITY_NAME_KEY, CITY_CODE_KEY, PROVINCE_NAME_KEY, PROVINCE_CODE_KEY])
        Helper.write_json(Helper.flatten_dict_values(res[1]), self.dist_path, COUNTY_CASCADE_JSON_FILENAME)
        print('=======================')
