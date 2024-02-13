# -*- coding:utf-8 -*-

from .util import Query, Util
from .rule import LABEL_KEY, VALUE_KEY, NAME_KEY, CODE_KEY, PROVINCE_CODE_KEY


def export_city():
    q = Query()
    cities = q.fetch_many_city()
    if len(cities) == 0:
        print('城市数据为空')
        return

    provinces = q.fetch_many_province()
    provinces_dict = Util.collection_to_key_dict(provinces)

    data_with_code = []  # 通用格式，带code
    ui_data_with_code = []  # 前端组件格式，带code

    for item in cities:
        _province = None
        if len(provinces_dict) > 0 and item.get('province_id') in provinces_dict.keys():
            _province = provinces_dict.get(item.get('province_id'))
        if _province is None:
            print("找不到省信息")
            continue

        _city = item
        data_item_with_code = {
            CODE_KEY: _city.get('code'),
            NAME_KEY: _city.get('name'),
            PROVINCE_CODE_KEY: _province.get('code')
        }
        data_with_code.append(data_item_with_code)

        ui_data_item_with_code = {
            LABEL_KEY: _city.get('name'),
            VALUE_KEY: _city.get('name'),
            CODE_KEY: _city.get('code'),
            PROVINCE_CODE_KEY: _province.get('code')
        }
        ui_data_with_code.append(ui_data_item_with_code)

    Util.write_json(data_with_code, Util.out_path(), 'city-code.json')
    Util.write_csv(data_with_code, Util.out_path(), 'city-code.csv', [CODE_KEY, NAME_KEY, PROVINCE_CODE_KEY])

    Util.write_json(ui_data_with_code, Util.out_path(), 'city-ui-code.json')
    q.close()


if __name__ == "__main__":
    export_city()
    pass
