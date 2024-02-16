# -*- coding:utf-8 -*-

import sys
import os

import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.export.province_export import ProvinceExport
from common.export.city_export import CityExport
from common.export.county_export import CountyExport
from common.export.pc_export import PcExport
from common.export.pcc_export import PccExport
from common.export.export import DataSource
from common.helper import Helper
from common.db.query import Query
from govstat.govstat.settings import DB


if __name__ == '__main__':
    out_path = f"{Helper.dist_path()}/govstat"

    q = Query(DB)
    df = pd.DataFrame(q.fetch_many_town_join())

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

    print("从数据库导出success")
