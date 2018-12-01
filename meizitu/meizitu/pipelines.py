# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from scrapy.pipelines.images import ImagesPipeline
class MeizituPipeline(object):
#     def open_spider(self,spider):
#         basedir=os.path.dirname(os.path.dirname(__file__))
#         self.path=os.path.join(basedir,"images")
#         if not os.path.exists(self.path):
#             os.mkdir(self.path)

    def process_item(self, item, spider):
         return item


import scrapy
class myImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)
