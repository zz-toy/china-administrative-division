# -*- coding:utf-8 -*-

from .rule import NAME_KEY, CODE_KEY, LABEL_KEY, VALUE_KEY, CHILDREN_KEY
from .rule import INNER_CITY_CODE_KEY, INNER_CITY_NAME_KEY, INNER_PROVINCE_CODE_KEY, INNER_PROVINCE_NAME_KEY, \
    PROVINCE_NAME_KEY, PROVINCE_CODE_KEY, is_municipality


def to_flatten_city_item(data: dict, province: dict) -> dict | None:
    return {
        NAME_KEY: data.get(INNER_CITY_NAME_KEY),
        CODE_KEY: data.get(INNER_CITY_CODE_KEY),
        PROVINCE_NAME_KEY: province.get(INNER_PROVINCE_NAME_KEY),
        PROVINCE_CODE_KEY: province.get(INNER_PROVINCE_CODE_KEY),
    }


def to_cascade_city_item(data: dict) -> dict | None:
    return {
        LABEL_KEY: data.get(INNER_CITY_NAME_KEY),
        VALUE_KEY: data.get(INNER_CITY_NAME_KEY),
        CODE_KEY: data.get(INNER_CITY_CODE_KEY),
        CHILDREN_KEY: []
    }


def build_city(city_list: list = None, params: tuple = None) -> tuple:
    if city_list is None:
        city_list = []

    if params is None:
        params = ({},)

    city_county_mapping = params[0]

    flatten_dict_data = {}
    cascade_dict_data = {}

    for item in city_list:
        _province_name = item.get(INNER_PROVINCE_NAME_KEY)
        _province_code = item.get(INNER_PROVINCE_CODE_KEY)
        _city_name = item.get(INNER_CITY_NAME_KEY)
        _city_code = item.get(INNER_CITY_CODE_KEY)
        _province = {
            INNER_PROVINCE_NAME_KEY: _province_name,
            INNER_PROVINCE_CODE_KEY: _province_code
        }

        _city = {
            INNER_CITY_NAME_KEY: _city_name,
            INNER_CITY_CODE_KEY: _city_code
        }

        flatten_item = to_flatten_city_item(_city, _province)
        if _province_code not in flatten_dict_data.keys():
            flatten_dict_data[_province_code] = []
        flatten_dict_data[_province_code].append(flatten_item)

        cascade_item = to_cascade_city_item(_city)
        if len(city_county_mapping) > 0 and _city_code in city_county_mapping.keys():
            cascade_item[CHILDREN_KEY] = city_county_mapping.get(_city_code)

        if len(cascade_item.get(CHILDREN_KEY)) == 0:
            del cascade_item[CHILDREN_KEY]

        if _province_code not in cascade_dict_data.keys():
            cascade_dict_data[_province_code] = []
        cascade_dict_data[_province_code].append(cascade_item)

    return flatten_dict_data, cascade_dict_data
