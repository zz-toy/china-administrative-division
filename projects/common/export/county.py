# -*- coding:utf-8 -*-

from .rule import NAME_KEY, CODE_KEY, LABEL_KEY, VALUE_KEY, CHILDREN_KEY
from .rule import INNER_COUNTY_CODE_KEY, INNER_COUNTY_NAME_KEY, INNER_PROVINCE_CODE_KEY, INNER_PROVINCE_NAME_KEY, \
    INNER_CITY_NAME_KEY, INNER_CITY_CODE_KEY, is_municipality, PROVINCE_NAME_KEY, PROVINCE_CODE_KEY, \
    CITY_NAME_KEY, CITY_CODE_KEY


def to_flatten_county_item(data: dict, province: dict, city: dict) -> dict | None:
    return {
        NAME_KEY: data.get(INNER_COUNTY_NAME_KEY),
        CODE_KEY: data.get(INNER_COUNTY_CODE_KEY),
        PROVINCE_NAME_KEY: province.get(INNER_PROVINCE_NAME_KEY),
        PROVINCE_CODE_KEY: province.get(INNER_PROVINCE_CODE_KEY),
        CITY_NAME_KEY: city.get(INNER_CITY_NAME_KEY),
        CITY_CODE_KEY: city.get(INNER_CITY_CODE_KEY),
    }


def to_cascade_county_item(data: dict) -> dict | None:
    return {
        LABEL_KEY: data.get(INNER_COUNTY_NAME_KEY),
        VALUE_KEY: data.get(INNER_COUNTY_NAME_KEY),
        CODE_KEY: data.get(INNER_COUNTY_CODE_KEY),
        CHILDREN_KEY: []
    }


def to_county_item(data: dict, append_children: bool = False) -> dict:
    if len(data) == 0:
        return {}
    res = {
        NAME_KEY: data.get(INNER_COUNTY_NAME_KEY)
    }

    if append_children:
        res[CHILDREN_KEY] = []

    return res


def build_county(county_list: list = None, params: tuple = None) -> tuple:
    if county_list is None:
        county_list = []

    if params is None:
        params = ({},)

    county_town_mapping = params[0]

    flatten_dict_data = {}
    cascade_dict_data = {}

    for item in county_list:
        _province_name = item.get(INNER_PROVINCE_NAME_KEY)
        _province_code = item.get(INNER_PROVINCE_CODE_KEY)
        _city_name = item.get(INNER_CITY_NAME_KEY)
        _city_code = item.get(INNER_CITY_CODE_KEY)
        _county_name = item.get(INNER_COUNTY_NAME_KEY)
        _county_code = item.get(INNER_COUNTY_CODE_KEY)
        _is_municipality = is_municipality(_province_name)
        _province = {
            INNER_PROVINCE_NAME_KEY: _province_name,
            INNER_PROVINCE_CODE_KEY: _province_code
        }

        _city = {
            INNER_CITY_NAME_KEY: _city_name,
            INNER_CITY_CODE_KEY: _city_code
        }

        _county = {
            INNER_COUNTY_CODE_KEY: _county_code,
            INNER_COUNTY_NAME_KEY: _county_name
        }

        flatten_item = to_flatten_county_item(_county, _province, _city)
        if _city_code not in flatten_dict_data.keys():
            flatten_dict_data[_city_code] = []
        flatten_dict_data[_city_code].append(flatten_item)

        cascade_item = to_cascade_county_item(_county)
        if len(county_town_mapping) > 0 and _city_code in county_town_mapping.keys():
            cascade_item[CHILDREN_KEY] = county_town_mapping.get(_city_code)

        if len(cascade_item.get(CHILDREN_KEY)) == 0:
            del cascade_item[CHILDREN_KEY]

        if _city_code not in cascade_dict_data.keys():
            cascade_dict_data[_city_code] = []
        cascade_dict_data[_city_code].append(cascade_item)

    return flatten_dict_data, cascade_dict_data
