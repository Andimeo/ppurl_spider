# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PpurlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    format = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    publish_date = scrapy.Field()
    ISBN = scrapy.Field()
    size = scrapy.Field()
    link = scrapy.Field()
    pages = scrapy.Field()
