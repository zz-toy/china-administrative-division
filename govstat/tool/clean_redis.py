# -*- coding:utf-8 -*-


from govstat import settings
import redis

if __name__ == '__main__':
    redis_connect = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT,
                                      password=settings.REDIS_PARAMS.get('password'), db=settings.REDIS_DB)
    redis_connect.ping()
    if redis_connect:
        if 'province:requests'.encode() in redis_connect.keys():
            redis_connect.delete('province:requests')
            print("Clean province:requests Success")

        if 'province:dupefilter'.encode() in redis_connect.keys():
            redis_connect.delete('province:dupefilter')
            print("Clean province:dupefilter Success")

        if 'province:items'.encode() in redis_connect.keys():
            redis_connect.delete('province:items')
            print("Clean province:items Success")

    print('Clean Redis Success!')
