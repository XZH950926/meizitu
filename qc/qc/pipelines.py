# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .bloomfilterOnRedis import BloomFilter
from scrapy.exceptions import IgnoreRequest
class QcPipeline(object):
    def process_item(self, item, spider):
        return item

# class myFiterPipeline(object):
#     def __init__(self):
#         self.s=set()
#     def process_item(self,item,spider):
#         print(self.s)
#         if item["name"] in self.s:
#             raise IgnoreRequest("用户重复")
#         else:
#             self.s.add(item["name"])
#             return item

class myFiterPipeline(object):
    def __init__(self):
        self.bf=BloomFilter(host="39.105.54.29")
    def process_item(self,item,spider):
        mu=item["myuuid"]
        mu=mu.encode("utf-8")
        if self.bf.isContains(mu):  # 判断字符串是否存在
            print('exists!')
        else:
            print('not exists!')
            self.bf.insert(mu)
        return item




