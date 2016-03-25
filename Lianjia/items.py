# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    house_code = scrapy.Field()
    kv_house_type = scrapy.Field()
    title = scrapy.Field()
    cover_pic = scrapy.Field()
    comm_avg_price = scrapy.Field()
    district_id = scrapy.Field()
    bizcircle_id = scrapy.Field()
    bizcircle_name = scrapy.Field()
    community_id = scrapy.Field()
    community_name = scrapy.Field()
    blueprint_hall_num = scrapy.Field()
    blueprint_bedroom_num = scrapy.Field()
    area = scrapy.Field()
    price = scrapy.Field()
    unit_price = scrapy.Field()
    sign_price = scrapy.Field()
    sign_unit_price = scrapy.Field()
    sign_time = scrapy.Field()
    sign_source = scrapy.Field()
    floor_state = scrapy.Field()
    orientation = scrapy.Field()
    baidu_la = scrapy.Field()
    baidu_lo = scrapy.Field()
    tags = scrapy.Field()
    school_info = scrapy.Field()
    subway_info = scrapy.Field()

    pass
