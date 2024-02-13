# -*- coding:utf-8 -*-

from .util import Query, Util
from .rule import LABEL_KEY, VALUE_KEY, NAME_KEY, CODE_KEY, CHILDREN_KEY, is_municipality, filter_city, filter_county, is_belong_to_xiongan, is_xiongan_city


def export_pcc():
    q = Query()
    provinces = q.fetch_many_province()
    if len(provinces) == 0:
        print('省数据为空')
        return

    provinces_dict = Util.collection_to_key_dict(provinces)

    cities = q.fetch_many_city()
    cities_dict = Util.collection_to_key_dict(cities)

    counties = q.fetch_many_county()
    counties_city_id_dict = {}
    counties_city_id_dict_with_code = {}
    counties_city_id_dict_ui = {}
    counties_city_id_dict_ui_with_code = {}

    xiongan_county_list = []
    xiongan_county_list_with_code = []
    xiongan_county_list_ui = []
    xiongan_county_list_ui_with_code = []

    if len(counties) > 0:
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

            # data
            data_item = {
                NAME_KEY: _county.get('name'),
            }
            if _city.get('id') not in counties_city_id_dict.keys():
                counties_city_id_dict[_city.get('id')] = []
            if is_belong_to_xiongan(_county):
                xiongan_county_list.append(data_item)
            else:
                counties_city_id_dict[_city.get('id')].append(data_item)

            # data_with_code
            data_item_with_code = {
                NAME_KEY: _county.get('name'),
                CODE_KEY: _county.get('code'),
            }
            if _city.get('id') not in counties_city_id_dict_with_code.keys():
                counties_city_id_dict_with_code[_city.get('id')] = []
            if is_belong_to_xiongan(_county):
                xiongan_county_list_with_code.append(data_item_with_code)
            else:
                counties_city_id_dict_with_code[_city.get('id')].append(data_item_with_code)

            # ui_data
            ui_data_item = {
                LABEL_KEY: _county.get('name'),
                VALUE_KEY: _county.get('name'),
            }
            if _city.get('id') not in counties_city_id_dict_ui.keys():
                counties_city_id_dict_ui[_city.get('id')] = []
            if is_belong_to_xiongan(_county):
                xiongan_county_list_ui.append(ui_data_item)
            else:
                counties_city_id_dict_ui[_city.get('id')].append(ui_data_item)

            # ui_data_with_code
            ui_data_item_with_code = {
                LABEL_KEY: _county.get('name'),
                VALUE_KEY: _county.get('name'),
                CODE_KEY: _county.get('code'),
            }
            if _city.get('id') not in counties_city_id_dict_ui_with_code.keys():
                counties_city_id_dict_ui_with_code[_city.get('id')] = []
            if is_belong_to_xiongan(_county):
                xiongan_county_list_ui_with_code.append(ui_data_item_with_code)
            else:
                counties_city_id_dict_ui_with_code[_city.get('id')].append(ui_data_item_with_code)


    # 加入到雄安新区, 而不是保定
    xiongan_city = q.fetch_xiongan_city()
    if len(xiongan_city) == 0:
        print("未查询到雄安新区")
        return

    cities_province_id_dict = {}
    cities_province_id_dict_with_code = {}
    cities_province_id_dict_ui = {}
    cities_province_id_dict_ui_with_code = {}

    if len(cities) > 0:
        for item in cities:
            _province = None
            if len(provinces_dict) > 0 and item.get('province_id') in provinces_dict.keys():
                _province = provinces_dict.get(item.get('province_id'))
            if _province is None:
                print("找不到省信息")
                continue

            _city = filter_city(_province, item)
            if _city is None or len(_city) == 0:
                print("filter_city 失败")
                continue

            _is_municipality = is_municipality(_province.get('name'))

            # data
            data_item = {
                NAME_KEY: _city.get('name'),
                CHILDREN_KEY: []
            }

            if item.get('id') in counties_city_id_dict.keys():
                data_item[CHILDREN_KEY] = counties_city_id_dict.get(item.get('id'))
            elif is_xiongan_city(_city):
                data_item[CHILDREN_KEY] = xiongan_county_list

            if len(data_item.get(CHILDREN_KEY)) == 0:
                del data_item[CHILDREN_KEY]

            if not _is_municipality:
                if item.get('province_id') not in cities_province_id_dict.keys():
                    cities_province_id_dict[item.get('province_id')] = []
                cities_province_id_dict[item.get('province_id')].append(data_item)
            else:
                if item.get('province_id') not in cities_province_id_dict.keys():
                    cities_province_id_dict[item.get('province_id')] = [data_item]

            # data_with_code
            data_item_with_code = {
                NAME_KEY: _city.get('name'),
                CODE_KEY: _city.get('code'),
                CHILDREN_KEY: []
            }
            if item.get('id') in counties_city_id_dict_with_code.keys():
                data_item_with_code[CHILDREN_KEY] = counties_city_id_dict_with_code.get(item.get('id'))
            elif is_xiongan_city(_city):
                data_item_with_code[CHILDREN_KEY] = xiongan_county_list_with_code

            if len(data_item_with_code.get(CHILDREN_KEY)) == 0:
                del data_item_with_code[CHILDREN_KEY]

            if not _is_municipality:
                if item.get('province_id') not in cities_province_id_dict_with_code.keys():
                    cities_province_id_dict_with_code[item.get('province_id')] = []
                cities_province_id_dict_with_code[item.get('province_id')].append(data_item_with_code)
            else:
                if item.get('province_id') not in cities_province_id_dict_with_code.keys():
                    cities_province_id_dict_with_code[item.get('province_id')] = [data_item_with_code]

            # ui_data
            ui_data_item = {
                LABEL_KEY: _city.get('name'),
                VALUE_KEY: _city.get('name'),
                CHILDREN_KEY: []
            }
            if item.get('id') in counties_city_id_dict_ui.keys():
                ui_data_item[CHILDREN_KEY] = counties_city_id_dict_ui.get(item.get('id'))
            elif is_xiongan_city(_city):
                ui_data_item[CHILDREN_KEY] = xiongan_county_list_ui

            if len(ui_data_item.get(CHILDREN_KEY)) == 0:
                del ui_data_item[CHILDREN_KEY]

            if not _is_municipality:
                if item.get('province_id') not in cities_province_id_dict_ui.keys():
                    cities_province_id_dict_ui[item.get('province_id')] = []
                cities_province_id_dict_ui[item.get('province_id')].append(ui_data_item)
            else:
                if item.get('province_id') not in cities_province_id_dict_ui.keys():
                    cities_province_id_dict_ui[item.get('province_id')] = [ui_data_item]

            # ui_data_with_code
            ui_data_item_with_code = {
                LABEL_KEY: _city.get('name'),
                VALUE_KEY: _city.get('name'),
                CODE_KEY: _city.get('code'),
                CHILDREN_KEY: []
            }

            if item.get('id') in counties_city_id_dict_ui_with_code.keys():
                ui_data_item_with_code[CHILDREN_KEY] = counties_city_id_dict_ui_with_code.get(item.get('id'))
            elif is_xiongan_city(_city):
                ui_data_item_with_code[CHILDREN_KEY] = xiongan_county_list_ui_with_code

            if len(ui_data_item_with_code.get(CHILDREN_KEY)) == 0:
                del ui_data_item_with_code[CHILDREN_KEY]

            if not _is_municipality:
                if item.get('province_id') not in cities_province_id_dict_ui_with_code.keys():
                    cities_province_id_dict_ui_with_code[item.get('province_id')] = []
                cities_province_id_dict_ui_with_code[item.get('province_id')].append(ui_data_item_with_code)
            else:
                if item.get('province_id') not in cities_province_id_dict_ui_with_code.keys():
                    cities_province_id_dict_ui_with_code[item.get('province_id')] = [ui_data_item_with_code]

    data = []  # 通用格式，不带code
    data_with_code = []  # 通用格式，带code
    ui_data = []  # 前端组件格式，不带code
    ui_data_with_code = []  # 前端组件格式，带code

    for item in provinces:
        # data
        data_item = {
            NAME_KEY: item.get('name'),
            CHILDREN_KEY: []
        }

        if item.get('id') in cities_province_id_dict.keys():
            data_item[CHILDREN_KEY] = cities_province_id_dict.get(item.get('id'))

        if len(data_item.get(CHILDREN_KEY)) == 0:
            del data_item[CHILDREN_KEY]

        data.append(data_item)

        # data_with_code
        data_item_with_code = {
            NAME_KEY: item.get('name'),
            CODE_KEY: item.get('code'),
            CHILDREN_KEY: []
        }

        if item.get('id') in cities_province_id_dict_with_code.keys():
            data_item_with_code[CHILDREN_KEY] = cities_province_id_dict_with_code.get(item.get('id'))

        if len(data_item_with_code.get(CHILDREN_KEY)) == 0:
            del data_item_with_code[CHILDREN_KEY]

        data_with_code.append(data_item_with_code)

        # ui_data
        ui_data_item = {
            LABEL_KEY: item.get('name'),
            VALUE_KEY: item.get('name'),
            CHILDREN_KEY: []
        }

        if item.get('id') in cities_province_id_dict_ui.keys():
            ui_data_item[CHILDREN_KEY] = cities_province_id_dict_ui.get(item.get('id'))

        if len(ui_data_item.get(CHILDREN_KEY)) == 0:
            del ui_data_item[CHILDREN_KEY]

        ui_data.append(ui_data_item)

        # ui_data_item_with_code
        ui_data_item_with_code = {
            LABEL_KEY: item.get('name'),
            VALUE_KEY: item.get('name'),
            CODE_KEY: item.get('code'),
            CHILDREN_KEY: []
        }

        if item.get('id') in cities_province_id_dict_ui_with_code.keys():
            ui_data_item_with_code[CHILDREN_KEY] = cities_province_id_dict_ui_with_code.get(item.get('id'))

        if len(ui_data_item_with_code.get(CHILDREN_KEY)) == 0:
            del ui_data_item_with_code[CHILDREN_KEY]

        ui_data_with_code.append(ui_data_item_with_code)

    Util.write_json(data, Util.out_path(), 'pcc.json')
    Util.write_json(data_with_code, Util.out_path(), 'pcc-code.json')

    Util.write_json(ui_data, Util.out_path(), 'pcc-ui.json')
    Util.write_json(ui_data_with_code, Util.out_path(), 'pcc-ui-code.json')

    Util.write_json({
        'errcode': 200,
        'errmsg': '请求成功',
        'data': ui_data
    }, Util.out_path(), 'pcc-zn.json')
    q.close()


if __name__ == "__main__":
    export_pcc()
    pass
