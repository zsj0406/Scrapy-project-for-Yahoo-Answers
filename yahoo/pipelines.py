# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
import json
import codecs


class YahooPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonWritePipeline(object):
	def __init__(self):
		self.file = open('yahoo_pain.json','wb')

	def process_item(self,item,spider):
		line = json.dumps(dict(item))+"\n"
		self.file.write(line)
		return item

	def spider_closed(self,spider):
		self.file.close()
