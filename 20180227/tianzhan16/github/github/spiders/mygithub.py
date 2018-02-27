# -*- coding: utf-8 -*-
import scrapy
from github.items import GithubItem

class MygithubSpider(scrapy.Spider):
    name = 'mygithub'
    allowed_domains = ['github.com']
    @property
    def start_urls(slef):
        return ('https://github.com/shiyanlou?tab=repositories&page={}'.format(i) for i in range(1,5))

    def parse(self, response):
        for rep in response.xpath('//li[contains(@class, "public")]'):
            item = GithubItem()
            item['name'] = rep.xpath('.//a/text()').extract_first().strip()
            item['update_time'] = rep.xpath('.//relative-time/@datetime').extract_first().strip()
            yield item
