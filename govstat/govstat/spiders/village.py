import datetime
import json

from govstat.items import VillageItem
from govstat.database import DbManager
from govstat.settings import BASE_DIR

from scrapy import signals, Spider, Request
from loguru import logger


class VillageSpider(Spider):
    name = "village"
    allowed_domains = ["www.stats.gov.cn"]
    custom_settings = {
        'ITEM_PIPELINES': {
            "govstat.pipelines.VillagePipeline": 400,
        },
        'LOG_LEVEL': "ERROR",
        'LOG_FILE': 'logs/{}_{}.log'.format(name, datetime.datetime.now().strftime("%Y-%m-%d"))
    }

    crawl_url_count = 0
    db_manager = None

    def start_requests(self):
        log_filename = "{}/logs/{}_cache_{}.log".format(BASE_DIR, self.name,
                                                        datetime.datetime.now().strftime("%Y-%m-%d"))

        logger.configure(handlers=[
            {
                "sink": log_filename,
                "format": "{time:%Y-%m-%d %H:%M:%S} | {level} | {message}",
                "colorize": False,
                "serialize": True,
                "encoding": 'utf8',
                "rotation": "2048 MB",
                "enqueue": True
            }
        ])

        towns = self.db_manager.fetchall('town', 'id')
        print('towns:', towns)
        if towns is None:
            towns = ()

        for town in towns:
            _town = self.db_manager.fetchone('town', '*', 'id=%s', params=(town.get('id'),))
            if _town is None:
                print('{} is not exists'.format(town))
                continue
            if _town.get('child_url'):
                yield Request(_town.get('child_url'), callback=self.parse, meta={'town': _town})

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super().from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.custom_spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(spider.custom_response_received, signal=signals.response_received)
        spider.db_manager = DbManager(spider.settings.get('DB'))
        return spider

    def parse(self, response, **kwargs):
        town = response.meta['town']

        trs = response.xpath('//tr[@class="villagetr"]')
        print("village tr 行数:", len(trs))

        current_url = response.url
        for tr in trs:
            code_td = tr.xpath("./td[1]")
            classify_code_td = tr.xpath("./td[2]")
            text_td = tr.xpath("./td[3]")

            item = VillageItem()
            item['name'] = text_td.xpath("text()").extract_first()
            code = code_td.xpath("text()").extract_first()
            item['code'] = code
            item['full_code'] = code
            item['classify_code'] = classify_code_td.xpath("text()").extract_first()
            item['url'] = current_url
            item['province_id'] = town.get('province_id')
            item['city_id'] = town.get('city_id')
            item['county_id'] = town.get('county_id')
            item['town_id'] = town.get('id')

            logger.info(item)
            yield item
        pass

    def custom_response_received(self, response):
        self.crawl_url_count += 1
        print(json.dumps({'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                          'url': response.url, 'crawl_url_count': self.crawl_url_count}, ensure_ascii=False))

    def custom_spider_closed(self):
        print(json.dumps({'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                          'text': f"{self.__class__.__name__} 已退出"}, ensure_ascii=False))
