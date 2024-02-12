import datetime
import json

from govstat.items import ProvinceItem
from govstat.settings import BASE_DIR

from scrapy import signals, Spider, Request
from loguru import logger


class ProvinceSpider(Spider):
    name = "province"
    allowed_domains = ["www.stats.gov.cn"]

    custom_settings = {
        'ITEM_PIPELINES': {
            "govstat.pipelines.ProvincePipeline": 400,
        },
        'LOG_LEVEL': "ERROR",
        'LOG_FILE': 'logs/{}_{}.log'.format(name, datetime.datetime.now().strftime("%Y-%m-%d"))
    }

    crawl_url_count = 0

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

        start_urls = ["https://www.stats.gov.cn/sj/tjbz/tjyqhdmhcxhfdm/2023/index.html"]
        for url in start_urls:
            yield Request(url, callback=self.parse)

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super().from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.custom_spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(spider.custom_response_received, signal=signals.response_received)
        return spider

    def parse(self, response, **kwargs):
        trs = response.xpath('//tr[@class="provincetr"]')
        print("province tr 行数:", len(trs))

        current_url = response.url
        for tr in trs:
            tds = tr.xpath("./td")
            for td in tds:
                text = td.xpath("./a/text()").extract_first()
                href = td.xpath("./a/@href").extract_first()

                item = ProvinceItem()
                item['url'] = current_url
                item['name'] = text
                item['code'] = href.rstrip(".html")
                item['full_code'] = item['code']
                if text in ['北京市', '上海市', '天津市', '重庆市']:
                    item['is_municipality'] = 1
                else:
                    item['is_municipality'] = 0

                if not href:
                    item['child_url'] = ""
                else:
                    item['child_url'] = response.urljoin(href)

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
