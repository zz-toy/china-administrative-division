# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class GovstatItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ProvinceItem(Item):
    id = Field()
    name = Field()
    code = Field()
    full_code = Field()
    url = Field()
    is_municipality = Field()
    child_url = Field()


class CityItem(Item):
    id = Field()
    name = Field()
    code = Field()
    full_code = Field()
    url = Field()
    province_id = Field()
    child_url = Field()


class CountyItem(Item):
    id = Field()
    name = Field()
    code = Field()
    full_code = Field()
    url = Field()
    province_id = Field()
    city_id = Field()
    child_url = Field()


class TownItem(Item):
    id = Field()
    name = Field()
    code = Field()
    full_code = Field()
    url = Field()
    province_id = Field()
    city_id = Field()
    county_id = Field()
    child_url = Field()


class VillageItem(Item):
    id = Field()
    name = Field()
    code = Field()
    full_code = Field()
    classify_code = Field()
    url = Field()
    province_id = Field()
    city_id = Field()
    county_id = Field()
    town_id = Field()
