# -*- coding:utf-8 -*-
from .util import Query, Util


def export_province():
    q = Query()
    provinces = q.fetch_many_province()
    if len(provinces) == 0:
        print('省数据为空')
        return

    data = []  # 通用格式，不带code
    data_with_code = []  # 通用格式，带code
    ui_data = []  # 前端组件格式，不带code
    ui_data_with_code = []  # 前端组件格式，带code
    for item in provinces:
        data_item = {
            'name': item.get('name'),
        }
        data.append(data_item)

        data_item_with_code = {
            'code': item.get('code'),
            'name': item.get('name'),
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
        }
        ui_data_with_code.append(ui_data_item_with_code)

    Util.write_json(data, Util.out_path(), 'province.json')
    Util.write_json(data_with_code, Util.out_path(), 'province-code.json')
    Util.write_csv(data, Util.out_path(), 'province.csv', ['name'])
    Util.write_csv(data_with_code, Util.out_path(), 'province-code.csv', ['code', 'name'])

    Util.write_json(ui_data, Util.out_path(), 'province-ui.json')
    Util.write_json(ui_data_with_code, Util.out_path(), 'province-ui-code.json')

    # export zn
    Util.write_json({
        'errcode': 200,
        'errmsg': '请求成功',
        'data': ui_data
    }, Util.out_path(), 'province-zn.json')
    q.close()


if __name__ == "__main__":
    export_province()
    pass
