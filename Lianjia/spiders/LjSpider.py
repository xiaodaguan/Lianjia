# coding=utf-8
import scrapy
import json
from Lianjia.items import LianjiaItem


class LJSpider(scrapy.Spider):
    name = "lianjia"
    allow_domains = ["lianjia.com"]
    start_urls = []
    for i in range(200):
        start_urls.append(
            "http://m.api.lianjia.com/house/ershoufang/searchv2?channel=ershoufang_ditie&city_id=110000&limit_count=20&limit_offset=" + str(
                20 * i) + "&min_price=220&max_price=280&orientation=south")

    def parse(self, response):
        root = json.JSONDecoder().decode(response.body)
        if root['data']['return_count'] == 0: return  # 没有内容
        for house in root['data']['list']:
            house_code = house['house_code']
            kv_house_type = house['kv_house_type']
            title = house['title']
            cover_pic = house['cover_pic']
            comm_avg_price = house['comm_avg_price']
            district_id = house['district_id']
            bizcircle_id = house['bizcircle_id']
            bizcircle_name = house['bizcircle_name']
            community_id = house['community_id']
            community_name = house['community_name']
            blueprint_hall_num = house['blueprint_hall_num']
            blueprint_bedroom_num = house['blueprint_bedroom_num']
            area = house['area']
            price = house['price']
            unit_price = house['unit_price']
            sign_price = house['sign_price']
            sign_unit_price = house['sign_unit_price']
            sign_time = house['sign_time']
            sign_source = house['sign_source']
            floor_state = house['floor_state']
            orientation = house['orientation']

            baidu_la = house['baidu_la']
            baidu_lo = house['baidu_lo']
            tags = house['tags']
            school_info = house['school_info']
            subway_info = house['subway_info']

            item = LianjiaItem()
            item['house_code'] = house_code
            item['kv_house_type'] = kv_house_type
            item['title'] = title
            item['cover_pic'] = cover_pic
            item['comm_avg_price'] = comm_avg_price
            item['district_id'] = district_id
            item['bizcircle_id'] = bizcircle_id
            item['bizcircle_name'] = bizcircle_name
            item['community_id'] = community_id
            item['community_name'] = community_name
            item['blueprint_hall_num'] = blueprint_hall_num
            item['blueprint_bedroom_num'] = blueprint_bedroom_num
            item['area'] = area
            item['price'] = price
            item['unit_price'] = unit_price
            item['sign_price'] = sign_price
            item['sign_unit_price'] = sign_unit_price
            item['sign_time'] = sign_time
            item['sign_source'] = sign_source
            item['floor_state'] = floor_state
            item['orientation'] = orientation
            item['baidu_la'] = baidu_la
            item['baidu_lo'] = baidu_lo
            item['tags'] = tags
            item['school_info'] = school_info
            item['subway_info'] = subway_info

            # print(title)
            yield item  # 一定要yield,否则pipeline不会被调用
            # end foreach item
