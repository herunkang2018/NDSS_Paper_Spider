# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NdssSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    paper = scrapy.Field()
    pdf = scrapy.Field()
    slide = scrapy.Field()
    video = scrapy.Field()
    pass