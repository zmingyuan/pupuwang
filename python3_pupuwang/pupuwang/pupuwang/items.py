# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PupuwangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class PupuwangItem(scrapy.Item):
    # 求租标题
    title = scrapy.Field()
    # 求租链接
    url = scrapy.Field()
    # 求租行业
    industry = scrapy.Field()
    # 发布时间
    pubtime = scrapy.Field()
    # 面积大小
    size = scrapy.Field()
    # 期望租金
    rent = scrapy.Field()
    # 详情描述
    describe = scrapy.Field()