# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CvmarketPipeline(object):
    def process_item(self, item, spider):
        # try:
        #     item['main'] = [x.strip() for x in item['main'] if x.strip()]
        # except:
        #     pass
        
        # try:
        #     item['job-details'] = [x.strip() for x in item['job-details'] if x.strip()]
        # except:
        #     pass
        return item
