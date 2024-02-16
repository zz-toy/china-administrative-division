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
from common.export.export import DataSource
from common.helper import Helper


if __name__ == '__main__':
    out_path = f"{Helper.dist_path()}/bdmap"
    df = pd.read_excel(f"{Helper.dist_path()}/bdmap/Township_Area_A_20230913.xlsx", sheet_name='Sheet1', header=None, names=ALL_COLUMNS)

    data_source = DataSource(df)

    province_export_export = ProvinceExport(data_source, out_path)
    province_export_export.export()

    city_export = CityExport(data_source, out_path)
    city_export.export()

    county_export = CountyExport(data_source, out_path)
    county_export.export()

    pc_export = PcExport(data_source, out_path)
    pc_export.export()

    pcc_export = PccExport(data_source, out_path)
    pcc_export.export()

    print("从百度地图数据导出success")
