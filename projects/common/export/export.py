# -*- coding:utf-8 -*-
from abc import ABC, abstractmethod
import pandas as pd
from .rule import ALL_CODE_COLUMNS, FILTER_PROVINCES, PROVINCE_COLUMNS, CITY_COLUMNS, COUNTY_COLUMNS, \
    PC_COLUMNS, PCC_COLUMNS, MUNICIPALITIES, SUPPLEMENT_CITY, XIONGAN_COUNTIES, INNER_COUNTY_CHILD_URL
from .rule import INNER_PROVINCE_CODE_KEY, INNER_PROVINCE_NAME_KEY, INNER_CITY_CODE_KEY, \
    INNER_CITY_NAME_KEY, INNER_COUNTY_NAME_KEY, INNER_COUNTY_CODE_KEY, INNER_TOWN_CODE_KEY


class DataSource:
    df = pd.DataFrame()

    def __init__(self, df):
        """code排序"""
        df = df.sort_values(ALL_CODE_COLUMNS)
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
        self.df = df

    def province_df(self):
        """去重"""
        return self.df.loc[:, PROVINCE_COLUMNS].drop_duplicates(subset=[INNER_PROVINCE_NAME_KEY])

    def city_df(self):
        """去重"""
        return self.df.loc[:, CITY_COLUMNS].drop_duplicates(subset=[INNER_CITY_NAME_KEY])

    def county_df(self):
        """去重"""
        return self.df.loc[:, COUNTY_COLUMNS].drop_duplicates()

    def pc_df(self):
        """去重"""
        return self.df.loc[:, PC_COLUMNS].drop_duplicates(subset=[INNER_PROVINCE_NAME_KEY, INNER_CITY_NAME_KEY])

    def pcc_df(self):
        """去重"""
        return self.df.loc[:, PCC_COLUMNS].drop_duplicates(subset=[INNER_PROVINCE_NAME_KEY, INNER_CITY_NAME_KEY,
                                                                   INNER_COUNTY_NAME_KEY])

    def province_list(self) -> list:
        return self.province_df().to_dict(orient='records')

    def pc_list(self):
        """去重"""
        return self.pc_df().to_dict(orient='records')

    def pcc_list(self):
        """去重"""
        return self.pcc_df().to_dict(orient='records')


class BdMapDataSource(DataSource):
    def __init__(self, df):
        super().__init__(df)
        self.set_df()

    def set_df(self):
        """ 过滤台湾，香港，澳门等"""
        df = self.df.copy(deep=False)
        df = df[(~df[INNER_PROVINCE_NAME_KEY].isin(FILTER_PROVINCES))]
        self.df = df


class DBDataSource(DataSource):
    def __init__(self, df):
        super().__init__(df)
        self.set_df()

    def set_df(self):
        # 删除county_child_url 为空的行
        df = self.df.copy(deep=False)
        df = df[~(df[INNER_COUNTY_CHILD_URL] == '')]

        # 直辖市的下级使用直辖市的信息
        cond1 = (df[INNER_PROVINCE_NAME_KEY].isin(MUNICIPALITIES))
        df.loc[cond1, INNER_CITY_NAME_KEY] = df[INNER_PROVINCE_NAME_KEY]
        df.loc[cond1, INNER_CITY_CODE_KEY] = df[INNER_PROVINCE_CODE_KEY]

        # city的下级使用对应county的信息
        cond2 = (df[INNER_CITY_NAME_KEY].isin(SUPPLEMENT_CITY))
        df.loc[cond2, INNER_CITY_NAME_KEY] = df[INNER_COUNTY_NAME_KEY]
        df.loc[cond2, INNER_CITY_CODE_KEY] = df[INNER_COUNTY_CODE_KEY]

        # 雄安新区 下添加对应的县
        cond3 = (df[INNER_COUNTY_NAME_KEY].isin(XIONGAN_COUNTIES))
        df.loc[cond3, INNER_CITY_NAME_KEY] = '雄安新区'
        df.loc[cond3, INNER_CITY_CODE_KEY] = '1331'

        # 处理 市辖区
        cond4 = (self.df[INNER_COUNTY_NAME_KEY] == '市辖区')
        df.loc[cond4, INNER_COUNTY_NAME_KEY] = df[INNER_CITY_NAME_KEY]
        df.loc[cond4, INNER_COUNTY_CODE_KEY] = df[INNER_CITY_CODE_KEY]

        # 广东省中山市（3320）、广东省东莞市（4419）、海南省儋州市（4604）没有县级。
        # for index, row in self.df.iterrows():
        #     print(row)
        #     break
        self.df = df


class ABCExport(ABC):
    def __init__(self, data_source: DataSource, dist_path: str, zn_dist_path: str = ''):
        self.data_source = data_source
        self.dist_path = dist_path
        self.zn_dist_path = zn_dist_path

    @abstractmethod
    def export(self):
        pass
