# -*- coding:utf-8 -*-
"""
此文件定义了数据导出对应的清洗规则
"""

"""
定义key名称，可全局替换
"""
LABEL_KEY = 'label'
VALUE_KEY = 'value'
NAME_KEY = 'name'
CODE_KEY = 'code'
PROVINCE_NAME_KEY = 'province_name'
PROVINCE_CODE_KEY = 'province_code'
CITY_NAME_KEY = 'city_name'
CITY_CODE_KEY = 'city_code'
COUNTY_NAME_KEY = 'county_name'
COUNTY_CODE_KEY = 'county_code'
TOWN_NAME_KEY = 'town_name'
TOWN_CODE_KEY = 'town_code'
CHILDREN_KEY = 'children'
LEVEL_KEY = 'level'

municipalities = ['北京市', '天津市', '上海市', '重庆市']

xiongan_counties = ['雄县', '安新县', '容城县']


def is_municipality(province_name: str) -> bool:
    return province_name in municipalities


def filter_county(city: dict, county: dict) -> dict | None:
    """county 市辖区 处理"""
    if city is None or county is None:
        return county

    if not county.get('child_url'):
        return None
    elif county.get('name') == '市辖区':
        return city
    return county


def filter_city(province: dict, city: dict) -> dict | None:
    """直辖市city处理"""
    if province is None or city is None:
        return city

    if province.get('name') in municipalities:
        return province
    return city


def is_belong_to_xiongan(county: dict) -> bool:
    """county属不属于雄安新区"""
    if county is None:
        return False
    if len(county) == 0:
        return False

    return county.get('name') in xiongan_counties


def is_xiongan_city(city: dict) -> bool:
    """是不是雄安新区"""
    if city is None:
        return False
    if len(city) == 0:
        return False

    return city.get('name') == "雄安新区"


def if_city_supplement(city: dict):
    """city下级是否补进，一般对应county为地级市"""
    if city is None:
        return False
    if len(city) == 0:
        return False

    return city.get('name') in ['省直辖县级行政区划', '自治区直辖县级行政区划']
