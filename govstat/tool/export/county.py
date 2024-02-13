# -*- coding:utf-8 -*-
from .util import Query,Util


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

    data = []  # 通用格式，不带code
    data_with_code = []  # 通用格式，带code
    ui_data = []  # 前端组件格式，不带code
    ui_data_with_code = []  # 前端组件格式，带code
    
    for item in counties:
        province_code = ''
        city_code = ''
        if len(provinces_dict) > 0 and item.get('province_id') in provinces_dict.keys():
            province_code = provinces_dict.get(item.get('province_id')).get('code')

        if len(cities_dict) > 0 and item.get('city_id') in cities_dict.keys():
            city_code = cities_dict.get(item.get('city_id')).get('code')

        data_item = {
            'name': item.get('name'),
        }
        data.append(data_item)

        data_item_with_code = {
            'code': item.get('code'),
            'name': item.get('name'),
            'province_code': province_code,
            'city_code': city_code,
        }
        data_with_code.append(data_item_with_code)

        ui_data_item = {
            'label': item.get('name'),
            'value': item.get('name'),
        }
        ui_data.append(ui_data_item)

        ui_data_item_with_code = {
            'label': item.get('name'),
            'value': item.get('name'),
            'code': item.get('code'),
            'province_code': province_code,
            'city_code': city_code,
        }
        ui_data_with_code.append(ui_data_item_with_code)

    Util.write_json(data, Util.out_path(), 'county.json')
    Util.write_json(data_with_code, Util.out_path(), 'county-code.json')
    Util.write_csv(data, Util.out_path(), 'county.csv', ['name'])
    Util.write_csv(data_with_code, Util.out_path(), 'county-code.csv', ['code', 'name', 'province_code', 'city_code'])

    Util.write_json(ui_data, Util.out_path(), 'county-ui.json')
    Util.write_json(ui_data_with_code, Util.out_path(), 'county-ui-code.json')
    q.close()


if __name__ == "__main__":
    export_county()
    pass
