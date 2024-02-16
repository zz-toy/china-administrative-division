# -*- coding:utf-8 -*-
from abc import ABC, abstractmethod


# -*- coding:utf-8 -*-
import pandas as pd
from .rule import (INNER_PROVINCE_CODE_KEY, INNER_PROVINCE_NAME_KEY, INNER_CITY_CODE_KEY,
                   INNER_TOWN_CODE_KEY, ALL_CODE_COLUMNS, INNER_COUNTY_CODE_KEY,
                   FILTER_PROVINCES, PROVINCE_COLUMNS, CITY_COLUMNS, TOWN_COLUMNS, COUNTY_COLUMNS, PC_COLUMNS,
                   PCC_COLUMNS, PCCT_COLUMNS)


class DataSource:
    df = pd.DataFrame()

    def __init__(self, df):
        self.set_df(df)

    def set_df(self, df):
        """code列统一转成字符串"""
        df[INNER_PROVINCE_CODE_KEY] = df[INNER_PROVINCE_CODE_KEY].astype(str)
        df[INNER_CITY_CODE_KEY] = df[INNER_CITY_CODE_KEY].astype(str)
        df[INNER_COUNTY_CODE_KEY] = df[INNER_COUNTY_CODE_KEY].astype(str)
        df[INNER_TOWN_CODE_KEY] = df[INNER_TOWN_CODE_KEY].astype(str)
        """获取真实的code"""
        df[INNER_PROVINCE_CODE_KEY] = df[INNER_PROVINCE_CODE_KEY].str[:2]
        df[INNER_CITY_CODE_KEY] = df[INNER_CITY_CODE_KEY].str[:4]
        df[INNER_COUNTY_CODE_KEY] = df[INNER_COUNTY_CODE_KEY].str[:6]
        df[INNER_TOWN_CODE_KEY] = df[INNER_TOWN_CODE_KEY].str[:9]
        """ 过滤台湾，香港，澳门等"""
        condition = (~df[INNER_PROVINCE_NAME_KEY].isin(FILTER_PROVINCES))
        df = df[condition]
        """code排序"""
        df = df.sort_values(ALL_CODE_COLUMNS)
        self.df = df

    def province_df(self):
        """去重"""
        return self.df.loc[:, PROVINCE_COLUMNS].drop_duplicates()

    def city_df(self):
        """去重"""
        return self.df.loc[:, CITY_COLUMNS].drop_duplicates()

    def county_df(self):
        """去重"""
        return self.df.loc[:, COUNTY_COLUMNS].drop_duplicates()

    def town_df(self):
        """去重"""
        return self.df.loc[:, TOWN_COLUMNS].drop_duplicates()

    def pc_df(self):
        """去重"""
        return self.df.loc[:, PC_COLUMNS].drop_duplicates()

    def pcc_df(self):
        """去重"""
        return self.df.loc[:, PCC_COLUMNS].drop_duplicates()

    def pcct_df(self):
        """去重"""
        return self.df.loc[:, PCCT_COLUMNS].drop_duplicates()

    def province_list(self) -> list:
        return self.province_df().to_dict(orient='records')

    def pc_list(self):
        """去重"""
        return self.pc_df().to_dict(orient='records')

    def pcc_list(self):
        """去重"""
        return self.pcc_df().to_dict(orient='records')

    def pcct_list(self):
        """去重"""
        return self.pcct_df().to_dict(orient='records')


class ABCExport(ABC):
    def __init__(self, data_source: DataSource, dist_path: str):
        self.data_source = data_source
        self.dist_path = dist_path

    @abstractmethod
    def export(self):
        pass