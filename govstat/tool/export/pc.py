# -*- coding:utf-8 -*-

from .util import Query, Util
from .rule import LABEL_KEY, VALUE_KEY, NAME_KEY, CODE_KEY, CHILDREN_KEY, is_municipality, filter_city


def export_pc():
    q = Query()
    provinces = q.fetch_many_province()
    if len(provinces) == 0:
        print('省数据为空')
        return

    provinces_dict = Util.collection_to_key_dict(provinces)

    cities = q.fetch_many_city()
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
            }

            # 特殊处理直辖市
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
            }
            if not _is_municipality:
                if item.get('province_id') not in cities_province_id_dict_with_code.keys():
                    cities_province_id_dict_with_code[item.get('province_id')] = []
                cities_province_id_dict_with_code[item.get('province_id')].append(data_item_with_code)
            else:
                if item.get('province_id') not in cities_province_id_dict_with_code.keys():
                    cities_province_id_dict_with_code[item.get('province_id')] = [data_item]

            # ui_data
            ui_data_item = {
                LABEL_KEY: _city.get('name'),
                VALUE_KEY: _city.get('name'),
            }
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
            }
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

    Util.write_json(data, Util.out_path(), 'pc.json')
    Util.write_json(data_with_code, Util.out_path(), 'pc-code.json')

    Util.write_json(ui_data, Util.out_path(), 'pc-ui.json')
    Util.write_json(ui_data_with_code, Util.out_path(), 'pc-ui-code.json')

    # export zn
    Util.write_json({
        'errcode': 200,
        'errmsg': '请求成功',
        'data': ui_data
    }, Util.out_path(), 'pc-zn.json')
    q.close()


if __name__ == "__main__":
    export_pc()
    pass
