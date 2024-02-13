# -*- coding:utf-8 -*-

from tool.export.util import Query,Util


def export_pc():
    q = Query()
    provinces = q.fetch_many_province()
    if len(provinces) == 0:
        print('省数据为空')
        return

    cities = q.fetch_many_city()

    cities_province_id_dict = {}
    cities_province_id_dict_with_code = {}
    cities_province_id_dict_ui = {}
    cities_province_id_dict_ui_with_code = {}

    if len(cities) > 0:
        for item in cities:
            if item.get('province_id') in cities_province_id_dict.keys():
                continue

            data_item = {
                'name': item.get('name'),
            }
            cities_province_id_dict[item.get('province_id')] = data_item

            data_item_with_code = {
                'name': item.get('name'),
                'code': item.get('code'),
            }
            cities_province_id_dict_with_code[item.get('province_id')] = data_item_with_code

            ui_data_item = {
                'label': item.get('name'),
                'value': item.get('name'),
            }
            cities_province_id_dict_ui[item.get('province_id')] = ui_data_item

            ui_data_item_with_code = {
                'label': item.get('name'),
                'value': item.get('name'),
                'code': item.get('code'),
            }
            cities_province_id_dict_ui_with_code[item.get('province_id')] = ui_data_item_with_code

    data = []  # 通用格式，不带code
    data_with_code = []  # 通用格式，带code
    ui_data = []  # 前端组件格式，不带code
    ui_data_with_code = []  # 前端组件格式，带code
    for item in provinces:
        # data
        data_item = {
             'name': item.get('name'),
             'children': []
        }

        if item.get('id') in cities_province_id_dict.keys():
            data_item['children'].append(cities_province_id_dict.get(item.get('id')))

        if len(data_item.get('children')) == 0:
            del data_item['children']

        data.append(data_item)

        # data_with_code
        data_item_with_code = {
            'name': item.get('name'),
            'code': item.get('code'),
            'children': []
        }

        if item.get('id') in cities_province_id_dict_with_code.keys():
            data_item_with_code['children'].append(cities_province_id_dict_with_code.get(item.get('id')))

        if len(data_item_with_code.get('children')) == 0:
            del data_item_with_code['children']

        data_with_code.append(data_item_with_code)

        # ui_data
        ui_data_item = {
            'label': item.get('name'),
            'value': item.get('name'),
            'children': []
        }

        if item.get('id') in cities_province_id_dict_ui.keys():
            ui_data_item['children'].append(cities_province_id_dict_ui.get(item.get('id')))

        if len(ui_data_item.get('children')) == 0:
            del ui_data_item['children']

        ui_data.append(ui_data_item)

        # ui_data_item_with_code
        ui_data_item_with_code = {
            'label': item.get('name'),
            'value': item.get('name'),
            'code': item.get('code'),
            'children': []
        }

        if item.get('id') in cities_province_id_dict_ui_with_code.keys():
            ui_data_item_with_code['children'].append(cities_province_id_dict_ui_with_code.get(item.get('id')))

        if len(ui_data_item_with_code.get('children')) == 0:
            del ui_data_item_with_code['children']

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
