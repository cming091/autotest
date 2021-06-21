# coding=utf-8
from utils import cfg
import logging
import pymysql


class Mysql:
    def __init__(self, db_name, host_type='wes'):
        try:
            if host_type == 'wes':
                host = cfg.G_CONFIG_DICT['mysql.host']
                user = cfg.G_CONFIG_DICT['mysql.username']
                password = cfg.G_CONFIG_DICT['mysql.password']
            elif host_type == 'tes':
                host = cfg.G_CONFIG_DICT['tes_mysql.host']
                user = cfg.G_CONFIG_DICT['tes_mysql.username']
                password = cfg.G_CONFIG_DICT['tes_mysql.password']
            # logging.debug(f"mysql connect, host={cfg.G_CONFIG_DICT['mysql.host']}, db={db_name}")
            self.__conn = pymysql.connect(host=host,
                                          user=user,
                                          password=password,
                                          db=db_name,
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor
                                          )
        except pymysql.err.OperationalError as e:
            self.__conn = None
            logging.error(f"connect to mysql error, {e}")
            exit(1)

    def query(self, sql):
        # logging.debug(f"mysql query, sql: {sql}")
        result = None
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
                self.__conn.commit()
        except pymysql.err.OperationalError as e:
            logging.error(f"mysql query error, unable to fetch data, {e}")
        except pymysql.err.Error as e:
            logging.error(f"mysql query error, {e}")

        return result

    def delete(self, sql):
        number = None
        # logging.debug(f"mysql delete, sql: {sql}")
        try:
            with self.__conn.cursor() as cursor:
                number = cursor.execute(sql)
                self.__conn.commit()
        except pymysql.err.Error as e:
            logging.error(f"delete error, {e}")
            self.__conn.rollback()
        return number

    def insert(self, sql):
        number = None
        # logging.debug(f"mysql insert, sql: {sql}")
        try:
            with self.__conn.cursor() as cursor:
                number = cursor.execute(sql)
                self.__conn.commit()
        except pymysql.err.Error as e:
            logging.error(f"insert error, {e}")
            self.__conn.rollback()
        return number

    def update(self, sql):
        number = None
        # logging.debug(f"mysql upate, sql: {sql}")
        try:
            with self.__conn.cursor() as cursor:
                number = cursor.execute(sql)
                self.__conn.commit()
        except pymysql.err.Error as e:
            logging.error(f"insert error, {e}")
            self.__conn.rollback()
        return number

    def close(self):
        self.__conn.close()
