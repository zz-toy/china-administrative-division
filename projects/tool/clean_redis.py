# -*- coding:utf-8 -*-
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from govstat.settings import REDIS_HOST,REDIS_PORT,REDIS_PARAMS,REDIS_DB,REDIS_PARAMS
import redis

if __name__ == '__main__':
    # redis_connect = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT,
    #                                   password=REDIS_PARAMS.get('password'), db=REDIS_DB)
    #
    # redis_connect.ping()
    # if redis_connect:
    #     if 'province:requests'.encode() in redis_connect.keys():
    #         redis_connect.delete('province:requests')
    #         print("Clean province:requests Success")
    #
    #     if 'province:dupefilter'.encode() in redis_connect.keys():
    #         redis_connect.delete('province:dupefilter')
    #         print("Clean province:dupefilter Success")
    #
    #     if 'province:items'.encode() in redis_connect.keys():
    #         redis_connect.delete('province:items')
    #         print("Clean province:items Success")

    print('Clean Redis Success!')
    pass
