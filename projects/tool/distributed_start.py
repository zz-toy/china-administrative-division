#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
import redis
from govstat import settings

if __name__ == '__main__':
    # 将start_url 存储到redis中的redis_key中，启动爬虫
    REDIS_KEY = "province:start_urls"
    START_URL = json.dumps({"url": "https://www.stats.gov.cn/sj/tjbz/tjyqhdmhcxhfdm/2023/index.html"})
    START_URL1 = json.dumps({"url": "https://www.stats.gov.cn/sj/tjbz/tjyqhdmhcxhfdm/2023/11.html"})

    redis_connect = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT,
                                      password=settings.REDIS_PARAMS.get('password'), db=settings.REDIS_DB)
    redis_connect.lpush(REDIS_KEY, START_URL)
    redis_connect.lpush(REDIS_KEY, START_URL1)
