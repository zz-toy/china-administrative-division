import datetime
import json
from common.db.database import DbManager
from ..items import CityItem
from ..settings import BASE_DIR
from scrapy import signals, Spider, Request
from loguru import logger


class CitySpider(Spider):
    name = "city"
    allowed_domains = ["www.stats.gov.cn"]
    custom_settings = {
        'ITEM_PIPELINES': {
            "govstat.pipelines.CityPipeline": 400,
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
                "rotation": "200 MB",
                "enqueue": True
            }
        ])

        provinces = self.db_manager.fetchall('province', 'id')
        if provinces is None:
            provinces = ()

        for province in provinces:
            _province = self.db_manager.fetchone('province', '*', 'id=%s', params=(province.get('id'),))
            if _province is None:
                print('{} is not exists'.format(province))
                continue
            if _province.get('child_url'):
                yield Request(_province.get('child_url'), callback=self.parse, meta={'province': _province})

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super().from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.custom_spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(spider.custom_response_received, signal=signals.response_received)
        spider.db_manager = DbManager(spider.settings.get('DB'))
        return spider

    def parse(self, response, **kwargs):
        province = response.meta['province']

        trs = response.xpath('//tr[@class="citytr"]')
        print("city tr 行数:", len(trs))

        current_url = response.url
        for tr in trs:
            code_td = tr.xpath("./td[1]")
            text_td = tr.xpath("./td[2]")

            item = CityItem()
            item['url'] = current_url

            if len(code_td.xpath("./a")) == 0 or len(code_td.xpath("./a")) == 0:
                code = code_td.xpath("text()").extract_first()
                text = text_td.xpath("text()").extract_first()
                item['child_url'] = ""
            else:
                href = code_td.xpath("./a/@href").extract_first()
                code = code_td.xpath("./a/text()").extract_first()
                text = text_td.xpath("./a/text()").extract_first()
                if not href:
                    item['child_url'] = ''
                else:
                    item['child_url'] = response.urljoin(href)

            item['name'] = text
            item['code'] = code[:4]
            item['full_code'] = code
            item['province_id'] = province.get('id')

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
