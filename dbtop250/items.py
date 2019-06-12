# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Dbtop250Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #电影名
    title = scrapy.Field()
    #导演
    director = scrapy.Field()
    #电影简介
    content = scrapy.Field()
    #时长
    time = scrapy.Field()
    #电影封页
    image = scrapy.Field()
    #链接
    url = scrapy.Field()
