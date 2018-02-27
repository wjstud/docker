# -*- coding: utf-8 -*-
import scrapy
from github.items import GithubItem

class GthbSpider(scrapy.Spider):
    name = 'gthb'
    allowed_domains = ['github.com']

    def start_requests(self):
        url_tmpl = 'https://github.com/shiyanlou?tab=repositories&page={}'
        urls = (url_tmpl.format(i) for i in range(1,4))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for rep in response.xpath('//li[@class="col-12 d-block width-full py-4 border-bottom public source"]'):
            item = GithubItem()
            item['name'] = rep.xpath('.//a/text()').extract_first().strip()
            item['update_time'] = rep.xpath('.//relative-time/@datetime').extract_first().strip()
            yield item
