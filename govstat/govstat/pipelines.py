# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from govstat.database import DbManager
from govstat.items import ProvinceItem, CityItem, CountyItem, TownItem, VillageItem


class GovstatPipeline:
    def process_item(self, item, spider):
        print("govstat item:", item)
        return item


class ProvincePipeline:
    def __init__(self, crawler):
        self.crawler = crawler
        self.db = DbManager(crawler.settings.get("DB"))
        self.item_list = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler=crawler)

    def open_spider(self, spider):
        self.item_list.clear()

    def close_spider(self, spider):
        self.batch_insert(self.item_list)
        self.db.close()

    def batch_insert(self, data) -> bool:
        affected_rows = self.db.insert_many('province', 'name,code,full_code,url,child_url,'
                                                        'is_municipality,creator,updater', data)
        if affected_rows <= 0:
            print("province 保存失败")
            return False

        self.item_list.clear()
        return True

    def process_item(self, item, spider):
        if not isinstance(item, ProvinceItem):
            return

        province = self.db.fetchone('province', columns='*', where='name=%s', params=(item.get('name'),))
        if province is not None:
            return item

        self.item_list.append((item.get('name'), item.get('code'), item.get('full_code'), item.get('url'),
                               item.get('child_url'), item.get('is_municipality'), 'province_spider',
                               'province_spider'))

        if len(self.item_list) >= self.crawler.settings.get("BATCH_INSERT_SIZE"):
            self.batch_insert(self.item_list)

        return item


class CityPipeline:
    def __init__(self, crawler):
        self.crawler = crawler
        self.db = DbManager(crawler.settings.get("DB"))
        self.item_list = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler=crawler)

    def open_spider(self, spider):
        self.item_list.clear()

    def close_spider(self, spider):
        self.batch_insert(self.item_list)
        self.db.close()

    def batch_insert(self, data) -> bool:
        affected_rows = self.db.insert_many('city', 'name,code,full_code,url,child_url,province_id,'
                                                    'creator,updater', self.item_list)
        if affected_rows <= 0:
            print("city 保存失败")
            return False

        self.item_list.clear()
        return True

    def process_item(self, item, spider):
        if not isinstance(item, CityItem):
            return item

        city = self.db.fetchone('city', columns='*', where='name=%s AND province_id=%s',
                                params=(item.get('name'), item.get('province_id')))
        if city is not None:
            return item

        self.item_list.append((item.get('name'), item.get('code'), item.get('full_code'), item.get('url'),
                               item.get('child_url'), item.get('province_id'), 'city_spider',
                               'city_spider'))

        if len(self.item_list) >= self.crawler.settings.get("BATCH_INSERT_SIZE"):
            self.batch_insert(self.item_list)

        return item


class CountyPipeline:
    def __init__(self, crawler):
        self.crawler = crawler
        self.db = DbManager(crawler.settings.get("DB"))
        self.item_list = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler=crawler)

    def open_spider(self, spider):
        self.item_list.clear()

    def close_spider(self, spider):
        self.batch_insert(self.item_list)
        self.db.close()

    def batch_insert(self, data) -> bool:
        affected_rows = self.db.insert_many('county',
                                            'name,code,full_code,url,child_url,province_id,city_id,'
                                            'creator,updater', self.item_list)
        if affected_rows <= 0:
            print("county 保存失败")
            return False

        self.item_list.clear()
        return True

    def process_item(self, item, spider):
        if not isinstance(item, CountyItem):
            return item

        county = self.db.fetchone('county', columns='*', where='name=%s AND city_id=%s',
                                  params=(item.get('name'), item.get('city_id')))
        if county is not None:
            return item

        self.item_list.append((item.get('name'), item.get('code'), item.get('full_code'), item.get('url'),
                               item.get('child_url'), item.get('province_id'), item.get('city_id'),
                               'county_spider',
                               'county_spider'))

        if len(self.item_list) < self.crawler.settings.get("BATCH_INSERT_SIZE"):
            self.batch_insert(self.item_list)

        return item


class TownPipeline:
    def __init__(self, crawler):
        self.crawler = crawler
        self.db = DbManager(crawler.settings.get("DB"))
        self.item_list = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler=crawler)

    def open_spider(self, spider):
        self.item_list.clear()

    def close_spider(self, spider):
        self.batch_insert(self.item_list)
        self.db.close()

    def batch_insert(self, data) -> bool:
        affected_rows = self.db.insert_many('town',
                                            'name,code,full_code,url,child_url,province_id,city_id,'
                                            'county_id,creator,updater', self.item_list)
        if affected_rows <= 0:
            print("town 保存失败")
            return False

        self.item_list.clear()
        return True

    def process_item(self, item, spider):
        if not isinstance(item, TownItem):
            return item

        town = self.db.fetchone('town', columns='*', where='name=%s AND county_id=%s',
                                params=(item.get('name'), item.get('county_id')))
        if town is not None:
            return item

        self.item_list.append((item.get('name'), item.get('code'), item.get('full_code'), item.get('url'),
                               item.get('child_url'), item.get('province_id'), item.get('city_id'),
                               item.get('county_id'), 'town_spider', 'town_spider'))

        if len(self.item_list) < self.crawler.settings.get("BATCH_INSERT_SIZE"):
            self.batch_insert(self.item_list)

        return item


class VillagePipeline:
    def __init__(self, crawler):
        self.crawler = crawler
        self.db = DbManager(crawler.settings.get("DB"))
        self.item_list = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler=crawler)

    def open_spider(self, spider):
        self.item_list.clear()

    def close_spider(self, spider):
        self.batch_insert(self.item_list)
        self.db.close()

    def batch_insert(self, data) -> bool:
        affected_rows = self.db.insert_many('village',
                                            'name,code,full_code,classify_code,url,'
                                            'province_id,city_id,'
                                            'town_id,county_id,creator,updater', self.item_list)
        if affected_rows <= 0:
            print("village 保存失败")
            return False

        self.item_list.clear()
        return True

    def process_item(self, item, spider):
        if not isinstance(item, VillageItem):
            return item

        village = self.db.fetchone('village', columns='*', where='name=%s AND town_id=%s',
                                   params=(item.get('name'), item.get('town_id')))
        if village is not None:
            return item

        self.item_list.append((item.get('name'), item.get('code'), item.get('full_code'),
                               item.get('classify_code'), item.get('url'), item.get('province_id'),
                               item.get('city_id'), item.get('town_id'), item.get('county_id'),
                               'village_spider', 'village_spider'))

        if len(self.item_list) >= 200:
            self.batch_insert(self.item_list)

        return item
