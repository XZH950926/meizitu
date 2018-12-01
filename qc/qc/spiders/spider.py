# -*- coding: utf-8 -*-
import scrapy
from scrapy.dupefilter import BaseDupeFilter
from ..items import QcItem
class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['baidu.com']
    start_urls = ["http://baidu.com/?date=2018"]
    custom_settings={
        "DUPEFILTER_CLASS":"qc.filter.myDupeFilter"
    }
    def parse(self, response):
        print("------")
        lst1=QcItem(myuuid="1",name="zhangsan",age=14)
        lst2=QcItem(myuuid="2",name="lisi",age=8)
        lst3=QcItem(myuuid="3",name="zhangsan",age=14)
        yield lst1
        yield lst2
        yield lst3
        yield scrapy.Request("http://baidu.com/?date=2017",callback=self.parse)
        yield scrapy.Request("http://baidu.com/?date=2016",callback=self.parse)