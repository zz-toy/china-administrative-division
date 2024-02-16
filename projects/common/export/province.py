# -*- coding:utf-8 -*-

from .rule import NAME_KEY, CODE_KEY, LABEL_KEY, VALUE_KEY, CHILDREN_KEY
from .rule import INNER_PROVINCE_CODE_KEY, INNER_PROVINCE_NAME_KEY


def to_flatten_province_item(data: dict) -> dict | None:
    return {
        NAME_KEY: data.get(INNER_PROVINCE_NAME_KEY),
        CODE_KEY: data.get(INNER_PROVINCE_CODE_KEY),
    }


def to_cascade_province_item(data: dict) -> dict | None:
    return {
        LABEL_KEY: data.get(INNER_PROVINCE_NAME_KEY),
        VALUE_KEY: data.get(INNER_PROVINCE_NAME_KEY),
        CODE_KEY: data.get(INNER_PROVINCE_CODE_KEY),
        CHILDREN_KEY: []
    }


def build_province(province_list: list = None, params: tuple = None) -> tuple:
    if province_list is None:
        province_list = []

    if params is None:
        params = ({},)

    province_city_mapping = params[0]

    flatten_data = []
    cascade_data = []
    for item in province_list:
        _province_code = item.get(INNER_PROVINCE_CODE_KEY)
        _province_name = item.get(INNER_PROVINCE_NAME_KEY)
        _province = {
            INNER_PROVINCE_NAME_KEY: _province_name,
            INNER_PROVINCE_CODE_KEY: _province_code,
        }

        flatten_item = to_flatten_province_item(_province)
        flatten_data.append(flatten_item)

        cascade_item = to_cascade_province_item(_province)
        if len(province_city_mapping) > 0 and _province_code in province_city_mapping.keys():
            cascade_item[CHILDREN_KEY] = province_city_mapping.get(_province_code)

        if len(cascade_item.get(CHILDREN_KEY)) == 0:
            del cascade_item[CHILDREN_KEY]
        cascade_data.append(cascade_item)

    return flatten_data, cascade_data
