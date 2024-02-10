# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import typing

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from govstat.database import DbManager
from govstat.items import ProvinceItem, CityItem, CountyItem, TownItem, VillageItem


class GovstatPipeline:
    def process_item(self, item, spider):
        print("govstat item:", item)
        return item


class ProvincePipeline:
    def __init__(self, crawler, db_settings):
        self.crawler = crawler
        self._db_manager = DbManager(db_settings)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            crawler=crawler,
            db_settings=crawler.settings.get("DB"),
        )

    def process_item(self, item, spider):
        if not isinstance(item, ProvinceItem):
            return item

        province = self._db_manager.fetchone('province', columns='*', where='name=%s', params=(item.get('name'),))
        if province is not None:
            return item

        item['id'] = self._db_manager.insert('province', {
            'name': item.get('name'),
            'code': item.get('code'),
            'url': item.get('url'),
            'child_url': item.get('child_url'),
            'is_municipality': item.get('is_municipality'),
            'creator': 'province_spider',
            'updater': 'province_spider',
        })

        if item.get('id') <= 0:
            print("province 保存失败:", item)
            return None

        return item


class CityPipeline:
    def __init__(self, crawler, db_settings):
        self.crawler = crawler
        self._db_manager = DbManager(db_settings)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            crawler=crawler,
            db_settings=crawler.settings.get("DB"),
        )

    def process_item(self, item, spider):
        if not isinstance(item, CityItem):
            return item

        city = self._db_manager.fetchone('city', columns='*', where='name=%s AND province_id=%s',
                                         params=(item.get('name'), item.get('province_id')))
        if city is not None:
            return item

        item['id'] = self._db_manager.insert('city', {
            'name': item.get('name'),
            'code': item.get('code'),
            'url': item.get('url'),
            'child_url': item.get('child_url'),
            'province_id': item.get('province_id'),
            'creator': 'city_spider',
            'updater': 'city_spider',
        })

        if item.get('id') <= 0:
            print("city 保存失败:", item)
            return None

        return item


class CountyPipeline:
    def __init__(self, crawler, db_settings):
        self.crawler = crawler
        self._db_manager = DbManager(db_settings)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            crawler=crawler,
            db_settings=crawler.settings.get("DB"),
        )

    def process_item(self, item, spider):
        if not isinstance(item, CountyItem):
            return item

        county = self._db_manager.fetchone('county', columns='*', where='name=%s AND city_id=%s',
                                           params=(item.get('name'), item.get('city_id')))
        if county is not None:
            return item

        item['id'] = self._db_manager.insert('county', {
            'name': item.get('name'),
            'code': item.get('code'),
            'url': item.get('url'),
            'child_url': item.get('child_url'),
            'province_id': item.get('province_id'),
            'city_id': item.get('city_id'),
            'creator': 'county_spider',
            'updater': 'county_spider',
        })

        if item.get('id') <= 0:
            print("county 保存失败:", item)
            return None

        return item


class TownPipeline:
    def __init__(self, crawler, db_settings):
        self.crawler = crawler
        self._db_manager = DbManager(db_settings)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            crawler=crawler,
            db_settings=crawler.settings.get("DB"),
        )

    def process_item(self, item, spider):
        if not isinstance(item, TownItem):
            return item

        town = self._db_manager.fetchone('town', columns='*', where='name=%s AND county_id=%s',
                                         params=(item.get('name'), item.get('county_id')))
        if town is not None:
            return item

        item['id'] = self._db_manager.insert('town', {
            'name': item.get('name'),
            'code': item.get('code'),
            'url': item.get('url'),
            'child_url': item.get('child_url'),
            'province_id': item.get('province_id'),
            'city_id': item.get('city_id'),
            'county_id': item.get('county_id'),
            'creator': 'town_spider',
            'updater': 'town_spider',
        })

        if item.get('id') <= 0:
            print("town 保存失败:", item)
            return None

        return item


class VillagePipeline:
    def __init__(self, crawler, db_settings):
        self.crawler = crawler
        self._db_manager = DbManager(db_settings)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            crawler=crawler,
            db_settings=crawler.settings.get("DB"),
        )

    def process_item(self, item, spider):
        if not isinstance(item, VillageItem):
            return item

        village = self._db_manager.fetchone('village', columns='*', where='name=%s AND town_id=%s',
                                            params=(item.get('name'), item.get('town_id')))
        if village is not None:
            return item

        item['id'] = self._db_manager.insert('village', {
            'name': item.get('name'),
            'code': item.get('code'),
            'classify_code': item.get('classify_code'),
            'url': item.get('url'),
            'province_id': item.get('province_id'),
            'city_id': item.get('city_id'),
            'county_id': item.get('county_id'),
            'town_id': item.get('town_id'),
            'creator': 'village_spider',
            'updater': 'village_spider',
        })

        if item.get('id') <= 0:
            print("village 保存失败:", item)
            return None

        return item
