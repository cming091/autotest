# coding=utf-8
import redis
from utils import cfg


class Redis:
    def __init__(self):
        self.__redis_obj = redis.StrictRedis(cfg.G_CONFIG_DICT['redis.host'], cfg.G_CONFIG_DICT['redis.port'])

    def get_redis(self):
        return self.__redis_obj
