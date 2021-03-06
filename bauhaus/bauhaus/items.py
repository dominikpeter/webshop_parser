# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BauhausItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    head = scrapy.Field()
    desc = scrapy.Field()
    price = scrapy.Field()
    cat = scrapy.Field()
    url = scrapy.Field()
    details = scrapy.Field()
