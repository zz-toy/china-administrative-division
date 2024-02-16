# -*- coding:utf-8 -*-

from common.helper import Helper
from .export import ABCExport
from .province import build_province
from .city import build_city
from .rule import PC_JSON_FILENAME


class PcExport(ABCExport):
    def export(self):
        build_city_res = build_city(self.data_source.pc_list())
        res = build_province(province_list=self.data_source.province_list(), params=(build_city_res[1],))
        Helper.write_json(res[1], self.dist_path, PC_JSON_FILENAME)
        print('=======================')
