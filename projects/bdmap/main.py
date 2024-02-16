# -*- coding:utf-8 -*-
import sys
import os

import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.export.rule import ALL_COLUMNS
from common.export.province_export import ProvinceExport
from common.export.city_export import CityExport
from common.export.county_export import CountyExport
from common.export.pc_export import PcExport
from common.export.pcc_export import PccExport
from common.export.export import BdMapDataSource
from common.helper import Helper


if __name__ == '__main__':
    dist_path = f"{Helper.dist_path()}/bdmap"
    zn_dist_path = f"{Helper.dist_path()}/zn"
    df = pd.read_excel(f"{Helper.dist_path()}/bdmap/Township_Area_A_20230913.xlsx", sheet_name='Sheet1', header=None,
                       names=ALL_COLUMNS)

    data_source = BdMapDataSource(df)

    province_export = ProvinceExport(data_source, dist_path, zn_dist_path)
    province_export.export()

    city_export = CityExport(data_source, dist_path)
    city_export.export()

    county_export = CountyExport(data_source, dist_path)
    county_export.export()

    pc_export = PcExport(data_source, dist_path, zn_dist_path)
    pc_export.export()

    pcc_export = PccExport(data_source, dist_path, zn_dist_path)
    pcc_export.export()

    print("从百度地图数据导出success")
