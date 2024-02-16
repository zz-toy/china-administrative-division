# -*- coding:utf-8 -*-

from common.helper import Helper
from .export import ABCExport
from .province import build_province
from .city import build_city
from .county import build_county
from .rule import PCC_JSON_FILENAME


class PccExport(ABCExport):
    def export(self):
        build_county_res = build_county(self.data_source.pcc_list())
        build_city_res = build_city(self.data_source.pc_list(), params=(build_county_res[1],))
        res = build_province(province_list=self.data_source.province_list(), params=(build_city_res[1],))

        Helper.write_json(res[1], self.dist_path, PCC_JSON_FILENAME)
