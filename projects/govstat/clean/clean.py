# -*- coding:utf-8 -*-

import pandas as pd
from common.export.clean import ABCClean
from common.helper import Helper
from common.db.query import Query
from ..govstat.settings import DB


class GovStatClean(ABCClean):
    def __init__(self):
        self._q = Query(DB)
        self._dist_path = f"{Helper.dist_path()}/govstat"
        self.set_df(self.read_db_to_df())
        print(self._df)

    def generate(self):
        print("GovStatClean generate")
        pass

    def read_db_to_df(self):
        town_join_list = self._q.fetch_many_town_join()
        df = None
        if town_join_list is None or len(town_join_list) == 0:
            df = pd.DataFrame()
        else:
            df = pd.DataFrame(town_join_list)
        return df
