# -*- coding: utf-8 -*-
import scrapy
from github.items import GithubItem

class GithubSpiderSpider(scrapy.Spider):
    name = 'github_spider'
#    allowed_domains = ['github.com']
    @property
    def start_urls(self):
        return ('https://github.com/shiyanlou?tab=repositories&page={}'.format(i) for i in range(1,5))

    def parse(self, response):
        for rep in response.xpath('//li[contains(@class, "public")]'):
            item = GithubItem()
            item['name'] = rep.xpath('.//h3/a/text()').extract_first().strip()
            item['update_time'] = rep.xpath('.//relative-time/@datetime').extract_first()
            rep_url = response.urljoin(rep.xpath('.//h3/a/@href').extract_first())
            request = scrapy.Request(rep_url, callback=self.parse_info)
            request.meta['item'] = item
            yield request

    def parse_info(self, response):
        item = response.meta['item']
        item['commits'] = response.xpath('(//span[@class="num text-emphasized"])[1]/text()').extract_first('0').strip()
        item['branches'] = response.xpath('(//span[@class="num text-emphasized"])[2]/text()').extract_first('0').strip()
        item['releases'] = response.xpath('(//span[@class="num text-emphasized"])[3]/text()').extract_first('0').strip()
        yield item
