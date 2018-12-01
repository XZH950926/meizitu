# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#name=name,homes=homes,address=address,price=price,province=meta["province"],city=meta["city"]
class FangItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    homes=scrapy.Field()
    address=scrapy.Field()
    price=scrapy.Field()
    province=scrapy.Field()
    city=scrapy.Field()
class ErShouItem(scrapy.Item):
    name=scrapy.Field()
    homes=scrapy.Field()
    price=scrapy.Field()
    address=scrapy.Field()
    homeuser=scrapy.Field()
    province=scrapy.Field()
    city=scrapy.Field()



