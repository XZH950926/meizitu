# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy_redis.spiders import RedisSpider
from fang.items import FangItem,ErShouItem
class SfSpider(scrapy.Spider):
    name = 'sf'
    allowed_domains = ['fang.com']
    # start_urls = ['http://www1.fang.com/SoufunFamily.htm']
    # redis_key = 'fang'
    def parse(self, response):
        trs=response.xpath("//div[@id='c02']/table[@class='table01']//tr")
        province=None
        for tr in trs:
            first_td = tr.xpath("./td[2]//text()").get()
            if first_td:
                province=first_td
            citys_herf=tr.xpath("./td[3]/a/@href").getall()
            citys=tr.xpath("./td[3]/a/text()").getall()
            ershou_url=None
            new_house_url=None
            for index,city in enumerate(citys):
                if city=='北京':
                    ershou_url='http://esf.fang.com/'
                    new_house_url='http://newhouse.fang.com/house/s/'
                else:
                    lst=citys_herf[index].split("fang")
                    new_house_url='newhouse.fang'.join(lst)
                    ershou_url='ers.fang'.join(lst)
                yield scrapy.Request(new_house_url,callback=self.newHouseParse,meta={"province":province,"city":city})
                yield scrapy.Request(ershou_url,callback=self.erShouParse,meta={"province":province,"city":city})

    def newHouseParse(self,response):
        meta = dict(response.meta)
        lis = response.xpath("//div[@id='newhouse_loupai_list']/ul/li[not(@class)]")
        for li in lis:
            name = li.xpath(".//div[@class='nlcd_name']/a/text()").get()
            if not name:
                continue  # 继续下次循环
            name = re.sub("\s", "", name, 0).strip()
            homesLst = li.xpath(".//div[@class='house_type clearfix']//text()").getall()
            homesLsts = ",".join(homesLst)
            homes = re.sub("\s", '', homesLsts, 0).strip()  # 正则(几居室和房子的面积)
            address = li.xpath(".//div[@class='nlc_details']/div[@class='relative_message clearfix']/div[@class='address']/a/text()").get().strip()
            address = re.sub("\t", '', address, 0).strip()
            price = li.xpath(".//div[@class='nhouse_price']/span/text()").get()
            yield FangItem(name=name,homes=homes,address=address,price=price,province=meta["province"],city=meta["city"])
        nextUrl = response.xpath("//div[@class='page']/ul/li/a[@class='next']/@href").get()
        if nextUrl:
            nextUrl = response.url+nextUrl  # 进行下一页的拼接
            yield scrapy.Request(nextUrl, callback=self.newHouseParse, meta=meta)

    def erShouParse(self,response):
        meta=dict(response.meta)
        dls=response.xpath("//div[@class='shop_list shop_list_4']/dl")
        for dl in dls:
            name=dl.xpath(".//dd[1]/h4/a/text()").get()
            homes=dl.xpath(".//dd[1]/p[1]/text()").get()
            homeuser = dl.xpath(".//dd[1]/p[1]/span[@class='people_name']/text()").get()
            address=dl.xpath(".//dd[1]/p[2]/a/span/text()").get()
            price=dl.xpath(".//dd[@class='price_right']/span/b/text()").get()
            yield ErShouItem(name=name,homes=homes,homeuser=homeuser,address=address,price=price,province=meta["province"],city=meta["city"])
        nextUrl=response.xpath("//div[@id='list_D10_15']/p[1]/a/@href").get()
        if nextUrl:
            nextUrl=response.url+nextUrl
            yield scrapy.Request(nextUrl,callback=self.erShouParse,meta=meta)
