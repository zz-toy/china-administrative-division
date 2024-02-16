# -*- coding:utf-8 -*-

from .clean import GovStatClean
from common.helper import Helper
from common.export.city import build_city
from common.export.rule import EXPORT_CITY_CODE_JSON_FILENAME, \
    EXPORT_CITY_CODE_CSV_FILENAME, \
    EXPORT_CITY_UI_CODE_JSON_FILENAME, \
    NAME_KEY, CODE_KEY


class CityClean(GovStatClean):
    def generate(self):
        res = build_city(city_list=self.pc_list(), append_children=False)
        Helper.write_json(Helper.flatten_dict_values(res[1]), self._dist_path, EXPORT_CITY_CODE_JSON_FILENAME)
        Helper.write_csv(Helper.flatten_dict_values(res[1]), self._dist_path, EXPORT_CITY_CODE_CSV_FILENAME,
                         [CODE_KEY, NAME_KEY])
        Helper.write_json(Helper.flatten_dict_values(res[3]), self._dist_path, EXPORT_CITY_UI_CODE_JSON_FILENAME)
        print('=======================')


if __name__ == "__main__":
    city_clean = CityClean('../../../dist/bdmap/Township_Area_A_20230913.xlsx')
    city_clean.generate()
