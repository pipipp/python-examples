# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ExampleItem(scrapy.Item):
    """
    定义数据结构
    """
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
