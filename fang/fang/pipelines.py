# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json
Basedir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class FangPipeline(object):
    def process_item(self, item, spider):
        province=item["province"]
        city = item["city"]
        province_path=os.path.join(Basedir,province)
        if not os.path.exists(province):
            os.mkdir(province_path)
        city_path=os.path.join(province_path,city)
        if not os.path.exists(city_path):
            os.mkdir(city_path)
        newHomePath=os.path.join(city_path,"sf.json")
        if not os.path.exists(newHomePath):
            with open(newHomePath,"a+") as f:
                f.write(json.dumps(dict(item),ensure_ascii=False))
        return item
