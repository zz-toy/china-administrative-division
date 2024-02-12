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
        self._db_manager = DbManager(crawler.settings.get("DB"))
        self._item_list = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler=crawler)

    def process_item(self, item, spider):
        if not isinstance(item, ProvinceItem):
            return item

        province = self._db_manager.fetchone('province', columns='*', where='name=%s', params=(item.get('name'),))
        if province is not None:
            return item

        if len(self._item_list) < self.crawler.settings.get("BATCH_INSERT_SIZE"):
            # self._item_list.append({
            #     'name': item.get('name'),
            #     'code': item.get('code'),
            #     'full_code': item.get('full_code'),
            #     'url': item.get('url'),
            #     'child_url': item.get('child_url'),
            #     'is_municipality': item.get('is_municipality'),
            #     'creator': 'province_spider',
            #     'updater': 'province_spider',
            # })

            self._item_list.append((item.get('name'), item.get('code'), item.get('full_code'), item.get('url'),
                                    item.get('child_url'), item.get('is_municipality'), 'province_spider',
                                    'province_spider'))
        else:
            affected_rows = self._db_manager.insert_many('province', 'name,code,full_code,url,child_url,'
                                                                     'is_municipality,'
                                                                     'creator,updater', self._item_list)
            self._item_list.clear()

            if affected_rows <= 0:
                print("province 保存失败")
                return None
        return item


class CityPipeline:
    def __init__(self, crawler):
        self.crawler = crawler
        self._db_manager = DbManager(crawler.settings.get("DB"))
        self._item_list = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler=crawler)

    def process_item(self, item, spider):
        if not isinstance(item, CityItem):
            return item

        city = self._db_manager.fetchone('city', columns='*', where='name=%s AND province_id=%s',
                                         params=(item.get('name'), item.get('province_id')))
        if city is not None:
            return item

        if len(self._item_list) < self.crawler.settings.get("BATCH_INSERT_SIZE"):
            # item['id'] = self._db_manager.insert('city', {
            #     'name': item.get('name'),
            #     'code': item.get('code'),
            #     'full_code': item.get('full_code'),
            #     'url': item.get('url'),
            #     'child_url': item.get('child_url'),
            #     'province_id': item.get('province_id'),
            #     'creator': 'city_spider',
            #     'updater': 'city_spider',
            # })
            self._item_list.append((item.get('name'), item.get('code'), item.get('full_code'), item.get('url'),
                                    item.get('child_url'), item.get('province_id'), 'city_spider',
                                    'city_spider'))
        else:
            affected_rows = self._db_manager.insert_many('city',
                                                         'name,code,full_code,url,child_url,province_id,'
                                                         'creator,updater', self._item_list)
            self._item_list.clear()

            if affected_rows <= 0:
                print("city 保存失败")
                return None

        return item


class CountyPipeline:
    def __init__(self, crawler):
        self.crawler = crawler
        self._db_manager = DbManager(crawler.settings.get("DB"))
        self._item_list = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler=crawler)

    def process_item(self, item, spider):
        if not isinstance(item, CountyItem):
            return item

        county = self._db_manager.fetchone('county', columns='*', where='name=%s AND city_id=%s',
                                           params=(item.get('name'), item.get('city_id')))
        if county is not None:
            return item

        if len(self._item_list) < self.crawler.settings.get("BATCH_INSERT_SIZE"):
            # item['id'] = self._db_manager.insert('county', {
            #     'name': item.get('name'),
            #     'code': item.get('code'),
            #     'full_code': item.get('full_code'),
            #     'url': item.get('url'),
            #     'child_url': item.get('child_url'),
            #     'province_id': item.get('province_id'),
            #     'city_id': item.get('city_id'),
            #     'creator': 'county_spider',
            #     'updater': 'county_spider',
            # })
            self._item_list.append((item.get('name'), item.get('code'), item.get('full_code'), item.get('url'),
                                    item.get('child_url'), item.get('province_id'), item.get('city_id'),
                                    'county_spider',
                                    'county_spider'))
        else:
            affected_rows = self._db_manager.insert_many('county',
                                                         'name,code,full_code,url,child_url,province_id,city_id,'
                                                         'creator,updater', self._item_list)
            self._item_list.clear()

            if affected_rows <= 0:
                print("county 保存失败")
                return None

        return item


class TownPipeline:
    def __init__(self, crawler):
        self.crawler = crawler
        self._db_manager = DbManager(crawler.settings.get("DB"))
        self._item_list = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler=crawler)

    def process_item(self, item, spider):
        if not isinstance(item, TownItem):
            return item

        town = self._db_manager.fetchone('town', columns='*', where='name=%s AND county_id=%s',
                                         params=(item.get('name'), item.get('county_id')))
        if town is not None:
            return item

        if len(self._item_list) < self.crawler.settings.get("BATCH_INSERT_SIZE"):
            # item['id'] = self._db_manager.insert('town', {
            #     'name': item.get('name'),
            #     'code': item.get('code'),
            #     'full_code': item.get('full_code'),
            #     'url': item.get('url'),
            #     'child_url': item.get('child_url'),
            #     'province_id': item.get('province_id'),
            #     'city_id': item.get('city_id'),
            #     'county_id': item.get('county_id'),
            #     'creator': 'town_spider',
            #     'updater': 'town_spider',
            # })

            self._item_list.append((item.get('name'), item.get('code'), item.get('full_code'), item.get('url'),
                                    item.get('child_url'), item.get('province_id'), item.get('city_id'),
                                    item.get('county_id'), 'town_spider', 'town_spider'))
        else:
            affected_rows = self._db_manager.insert_many('town',
                                                         'name,code,full_code,url,child_url,province_id,city_id,'
                                                         'county_id,creator,updater', self._item_list)
            self._item_list.clear()

            if affected_rows <= 0:
                print("town 保存失败")
                return None

        return item


class VillagePipeline:
    def __init__(self, crawler):
        self.crawler = crawler
        self._db_manager = DbManager(crawler.settings.get("DB"))
        self._item_list = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler=crawler)

    def process_item(self, item, spider):
        if not isinstance(item, VillageItem):
            return item

        village = self._db_manager.fetchone('village', columns='*', where='name=%s AND town_id=%s',
                                            params=(item.get('name'), item.get('town_id')))
        if village is not None:
            return item

        if len(self._item_list) < 200:
            # item['id'] = self._db_manager.insert('village', {
            #     'name': item.get('name'),
            #     'code': item.get('code'),
            #     'full_code': item.get('full_code'),
            #     'classify_code': item.get('classify_code'),
            #     'url': item.get('url'),
            #     'province_id': item.get('province_id'),
            #     'city_id': item.get('city_id'),
            #     'county_id': item.get('county_id'),
            #     'town_id': item.get('town_id'),
            #     'creator': 'village_spider',
            #     'updater': 'village_spider',
            # })

            self._item_list.append((item.get('name'), item.get('code'), item.get('full_code'),
                                    item.get('classify_code'), item.get('url'), item.get('province_id'),
                                    item.get('city_id'), item.get('town_id'), item.get('county_id'),
                                    'village_spider', 'village_spider'))
        else:
            affected_rows = self._db_manager.insert_many('village',
                                                         'name,code,full_code,classify_code,url,'
                                                         'province_id,city_id,'
                                                         'town_id,county_id,creator,updater', self._item_list)
            self._item_list.clear()

            if affected_rows <= 0:
                print("village 保存失败")
                return None

        return item
