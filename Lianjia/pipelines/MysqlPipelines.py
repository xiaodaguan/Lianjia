# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql

pymysql.install_as_MySQLdb()
import MySQLdb.cursors

from scrapy import log
from scrapy.exceptions import DropItem

from twisted.enterprise import adbapi

import datetime


class MysqlPipeline(object):
    def __init__(self):
        self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        # print(item['title'])
        self.file.write(line)
        return item


class LianjiaMysqlPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool(
            dbapiName='MySQLdb',
            host='guanxiaoda.cn',
            db='housedb',
            user='gxd',
            passwd='s327gxd',
            cursorclass=MySQLdb.cursors.DictCursor,
            charset='utf8',
            use_unicode=False
        )
        self.dbpool.start()

    def process_item(self, item, spider):
        if not item['title']:
            raise DropItem(item)
        else:
            # print(item['title'])
            query = self.dbpool.runInteraction(self._conditional_insert, item)

            ISOFORMAT = '%Y%m%d %H%M%S'

            # sql = "insert into houseinfo(house_code, title) values(%s, %s)"

            return item

    def _conditional_insert(self, tx, item):
        # house_code = house['house_code']
        #      kv_house_type = house['kv_house_type']
        #      title = house['title']
        sql = "insert into houseinfo(house_code, title) values(%s, %s)"
        tx.execute(
            sql,
            (item['house_code'][0], item['title'][0])
        )

        # sql = "insert into houseinfo(\
        #           house_code, " \
        #       "kv_house_type, " \
        #       "title, " \
        #       "cover_pic," \
        #       "comm_avg_price," \
        #       "district_id," \
        #       "bizcircle_id," \
        #       "biz_circle_name," \
        #       "community_id," \
        # "community_name," \
        # "blueprint_hall_num," \
        # "blueprint_bedroom_num," \
        # "area," \
        # "price," \
        # "unit_price," \
        # "sign_price," \
        # "sign_unit_price," \
        # "sign_time," \
        # "sign_source," \
        # "floor_state," \
        # "orientation," \
        # "baidu_la," \
        # "baidu_lo," \
        # "tags," \
        # "school_info," \
        # "subway_info," \
        # "insert_time," \
        # "is_read" \
        # ") values(" \
        # "%s,%s,%s,%s,%s," \
        # "%s,%s,%s,%s,%s," \
        # "%s,%s,%s,%s,%s," \
        # "%s,%s,%s,%s,%s," \
        # "%s,%s,%s,%s,%s," \
        # "%s,%s,%s" \
        #       ")"
        # tx.execute(sql, (
        #
        #     item['house_code'],
        #     item['kv_house_typ'],
        #     item['title'],
        #     item['cover_pic'],
        #     item['comm_avg_pric'],
        #     item['district_id'],
        #     item['bizcircle_id'],
        #     item['bizcircle_name'],
        #     item['community_id'],
        #     item['community_name'],
        #     item['blueprint_hall_num'],
        #     item['blueprint_bedroom_num'],
        #     item['are'],
        #     item['price'],
        #     item['unit_price'],
        #     item['sign_price'],
        #     item['sign_unit_pric'],
        #     item['sign_time'],
        #     item['sign_source'],
        #     item['floor_state'],
        #     item['orientatio'],
        #     item['baidu_la'],
        #     item['baidu_lo'],
        #     item['tags'],
        #     item['school_info'],
        #     item['subway_info']
        #
        # ))
