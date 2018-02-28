# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from github.models import Repository, engine

class GithubPipeline(object):
    def process_item(self, item, spider):
        if len(item['commits'].split(',')) == 1:
            item['commits'] = int(item['commits'])
        else:
            a,b = item['commits'].split(',')
            item['commits'] = int(a+b)
        item['branches'] = int(item['branches'])
        item['releases'] = int(item['releases'])
        self.session.add(Repository(**item))
        return item

    def open_spider(self, spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()
