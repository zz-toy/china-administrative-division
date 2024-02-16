# -*- coding:utf-8 -*-

MUNICIPALITIES = ['北京市', '天津市', '上海市', '重庆市']
XIONGAN_COUNTIES = ['雄县', '安新县', '容城县']
FILTER_PROVINCES = ['苏鲁交界', '香港', '澳门', '台湾省']

"""内部代码使用，不会变"""
INNER_PROVINCE_NAME_KEY = 'province_name'
INNER_PROVINCE_CODE_KEY = 'province_code'
INNER_CITY_NAME_KEY = 'city_name'
INNER_CITY_CODE_KEY = 'city_code'
INNER_COUNTY_NAME_KEY = 'county_name'
INNER_COUNTY_CODE_KEY = 'county_code'
INNER_TOWN_NAME_KEY = 'town_name'
INNER_TOWN_CODE_KEY = 'town_code'

"""导出文件使用，可变"""
LABEL_KEY = 'label'
VALUE_KEY = 'value'
NAME_KEY = 'name'
CODE_KEY = 'code'
PROVINCE_NAME_KEY = 'province_name'
PROVINCE_CODE_KEY = 'province_code'
CITY_NAME_KEY = 'city_name'
CITY_CODE_KEY = 'city_code'
COUNTY_NAME_KEY = 'county_name'
COUNTY_CODE_KEY = 'county_code'
TOWN_NAME_KEY = 'town_name'
TOWN_CODE_KEY = 'town_code'
CHILDREN_KEY = 'children'
LEVEL_KEY = 'level'

PROVINCE_COLUMNS = [INNER_PROVINCE_NAME_KEY, INNER_PROVINCE_CODE_KEY]
CITY_COLUMNS = [INNER_CITY_NAME_KEY, INNER_CITY_CODE_KEY]
COUNTY_COLUMNS = [INNER_COUNTY_NAME_KEY, INNER_COUNTY_CODE_KEY]
TOWN_COLUMNS = [INNER_TOWN_NAME_KEY, INNER_TOWN_CODE_KEY]
PC_COLUMNS = [x for ll in [PROVINCE_COLUMNS, CITY_COLUMNS] for x in ll]
PCC_COLUMNS = [x for ll in [PROVINCE_COLUMNS, CITY_COLUMNS, COUNTY_COLUMNS] for x in ll]
PCCT_COLUMNS = [x for ll in [PROVINCE_COLUMNS, CITY_COLUMNS, COUNTY_COLUMNS, TOWN_COLUMNS] for x in ll]
ALL_COLUMNS = [x for ll in [PROVINCE_COLUMNS, CITY_COLUMNS, COUNTY_COLUMNS, TOWN_COLUMNS] for x in ll]
ALL_CODE_COLUMNS = ALL_COLUMNS[1::2]

# province 导出文件配置
PROVINCE_FLATTEN_JSON_FILENAME = 'province-flatten.json'
PROVINCE_FLATTEN_CSV_FILENAME = 'province-flatten.csv'
PROVINCE_CASCADE_JSON_FILENAME = 'province-cascade.json'

# city 导出文件配置
CITY_FLATTEN_JSON_FILENAME = 'city-flatten.json'
CITY_FLATTEN_CSV_FILENAME = 'city-flatten.csv'
CITY_CASCADE_JSON_FILENAME = 'city-cascade.json'

# county 导出文件配置
COUNTY_FLATTEN_JSON_FILENAME = 'county-flatten.json'
COUNTY_FLATTEN_CSV_FILENAME = 'county-flatten.csv'
COUNTY_CASCADE_JSON_FILENAME = 'county-cascade.json'

# province_city 导出文件配置
PC_JSON_FILENAME = 'pc.json'

# province_city_county 导出文件配置
PCC_JSON_FILENAME = 'pcc.json'


# province_city_county_town 导出文件配置
PCCT_JSON_FILENAME = 'pcct.json'


def is_municipality(province_name: str) -> bool:
    return province_name in MUNICIPALITIES


def if_filter_province(name: str) -> bool:
    return name in ['苏鲁交界', '香港', '澳门', '台湾省']


def filter_city(province: dict, city: dict) -> dict | None:
    """直辖市city处理"""
    if province is None or city is None:
        return city

    if province.get(INNER_PROVINCE_NAME_KEY) in MUNICIPALITIES:
        return {
            INNER_CITY_CODE_KEY: province.get(INNER_PROVINCE_CODE_KEY),
            INNER_CITY_NAME_KEY: province.get(INNER_PROVINCE_NAME_KEY),
        }
    return city


def filter_county(city: dict, county: dict) -> dict | None:
    """county 市辖区 处理"""
    if city is None or county is None:
        return county

    if not county.get('child_url'):
        return None
    elif county.get('name') == '市辖区':
        return {
            INNER_COUNTY_CODE_KEY: city.get(INNER_PROVINCE_CODE_KEY),
            INNER_COUNTY_NAME_KEY: city.get(INNER_PROVINCE_NAME_KEY),
        }
    return county


def province_code(field) -> str:
    return str(field)[:2]


def city_code(field) -> str:
    return str(field)[:4]


def county_code(field) -> str:
    return str(field)[:6]


def town_code(field) -> str:
    return str(field)[:9]


def is_belong_to_xiongan(county: dict) -> bool:
    """county属不属于雄安新区"""
    if county is None:
        return False
    if len(county) == 0:
        return False

    return county.get('name') in XIONGAN_COUNTIES


def is_xiongan_city(city: dict) -> bool:
    """是不是雄安新区"""
    if city is None:
        return False
    if len(city) == 0:
        return False

    return city.get('name') == "雄安新区"


def if_city_supplement(city: dict):
    """city下级是否补进，一般对应county为地级市"""
    if city is None:
        return False
    if len(city) == 0:
        return False

    return city.get('name') in ['省直辖县级行政区划', '自治区直辖县级行政区划']
