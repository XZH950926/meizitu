# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import MeizituItem
class SpiderSpider(CrawlSpider):
    name = 'spider'
    allowed_domains = ['meizitu.com']
    start_urls = ['http://www.meizitu.com/a/more_1.html']

    rules = (
        Rule(LinkExtractor(allow=r'.*more_\d+.html'), follow=True),
        Rule(LinkExtractor(allow=r'.*\d{4}.html'),callback='parse_item',follow=False)
    )

    def parse_item(self, response):
        # i = {}
        # #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # #i['name'] = response.xpath('//div[@id="name"]').extract()
        # #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        image_urls=response.xpath("//*[@id='picture']/p/img/@src").getall()
        item=MeizituItem(image_urls=image_urls)
        yield item
