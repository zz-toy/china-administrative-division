# -*- coding:utf-8 -*-
from .util import Query, Util
from .rule import LABEL_KEY, VALUE_KEY, NAME_KEY, CODE_KEY, PROVINCE_CODE_KEY, CITY_CODE_KEY, filter_county


def export_county():
    q = Query()
    counties = q.fetch_many_county()
    if len(counties) == 0:
        print('区县数据为空')
        return

    provinces = q.fetch_many_province()
    provinces_dict = Util.collection_to_key_dict(provinces)

    cities = q.fetch_many_city()
    cities_dict = Util.collection_to_key_dict(cities)

    data_with_code = []  # 通用格式，带code
    ui_data_with_code = []  # 前端组件格式，带code
    
    for item in counties:
        _province = None
        if len(provinces_dict) > 0 and item.get('province_id') in provinces_dict.keys():
            _province = provinces_dict.get(item.get('province_id'))

        if _province is None:
            print("找不到省信息")
            continue

        _city = None
        if len(cities_dict) > 0 and item.get('city_id') in cities_dict.keys():
            _city = cities_dict.get(item.get('city_id'))

        if _city is None:
            print("找不到城市信息")
            continue

        _county = filter_county(_city, item)
        if _county is None:
            continue

        if len(_county) == 0:
            print("filter_county 失败")
            continue

        data_item_with_code = {
            CODE_KEY: _county.get('code'),
            NAME_KEY: _county.get('name'),
            PROVINCE_CODE_KEY: _province.get('code'),
            CITY_CODE_KEY: _city.get('code'),
        }
        data_with_code.append(data_item_with_code)

        ui_data_item_with_code = {
            LABEL_KEY: _county.get('name'),
            VALUE_KEY: _county.get('name'),
            CODE_KEY: _county.get('code'),
            PROVINCE_CODE_KEY: _province.get('code'),
            CITY_CODE_KEY: _city.get('code'),
        }
        ui_data_with_code.append(ui_data_item_with_code)

    Util.write_json(data_with_code, Util.out_path(), 'county-code.json')
    Util.write_csv(data_with_code, Util.out_path(), 'county-code.csv',
                   [CODE_KEY, NAME_KEY, PROVINCE_CODE_KEY, CITY_CODE_KEY])

    Util.write_json(ui_data_with_code, Util.out_path(), 'county-ui-code.json')
    q.close()


if __name__ == "__main__":
    export_county()
    pass
