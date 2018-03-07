# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from flask_doc.items import PageItem

class FlaskSpider(scrapy.spiders.CrawlSpider):
    name = 'flask'
    allowed_domains = ['flask.pocoo.org']
    start_urls = ['http://flask.pocoo.org/docs/0.12/']
    rules = (
            Rule(LinkExtractor(allow=('docs/0.12/')),
                callback='parse_page',
                follow = True
                ),
            )

    def parse_page(self, response):
        item = PageItem()
        url = str(response.url)
        text = response.xpath('//div[@class="body"]').extract_first()
        item['url'] = url
        item['text'] = text
        yield item

#        yield {
#               'url': str(response.url),
#               'text': response.xpath('//div[@class="body"]').extract()
#                }
