# -*- coding:utf-8 -*-

from .rule import NAME_KEY, CODE_KEY, LABEL_KEY, VALUE_KEY, CHILDREN_KEY
from .rule import INNER_CITY_CODE_KEY, INNER_CITY_NAME_KEY, INNER_PROVINCE_CODE_KEY, INNER_PROVINCE_NAME_KEY, \
    PROVINCE_NAME_KEY, PROVINCE_CODE_KEY, is_municipality, filter_city


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
        _is_municipality = is_municipality(_province_name)
        tmp_province = {
            INNER_PROVINCE_NAME_KEY: _province_name,
            INNER_PROVINCE_CODE_KEY: _province_code
        }

        tmp_city = {
            INNER_CITY_NAME_KEY: _city_name,
            INNER_CITY_CODE_KEY: _city_code
        }

        _city = filter_city(tmp_province, tmp_city)
        if _city is None or len(_city) == 0:
            print("filter_city 失败")
            continue

        _city_code = _city.get(INNER_CITY_CODE_KEY)

        flatten_item = to_flatten_city_item(_city, tmp_province)
        if not _is_municipality:
            if _province_code not in flatten_dict_data.keys():
                flatten_dict_data[_province_code] = []
            flatten_dict_data[_province_code].append(flatten_item)
        else:
            if _province_code not in flatten_dict_data.keys():
                flatten_dict_data[_province_code] = [flatten_item]

        cascade_item = to_cascade_city_item(_city)
        if len(city_county_mapping) > 0 and _city_code in city_county_mapping.keys():
            cascade_item[CHILDREN_KEY] = city_county_mapping.get(_city_code)

        if len(cascade_item.get(CHILDREN_KEY)) == 0:
            del cascade_item[CHILDREN_KEY]

        if not _is_municipality:
            if _province_code not in cascade_dict_data.keys():
                cascade_dict_data[_province_code] = []
            cascade_dict_data[_province_code].append(cascade_item)
        else:
            if _province_code not in cascade_dict_data.keys():
                cascade_dict_data[_province_code] = [cascade_item]

    return flatten_dict_data, cascade_dict_data
