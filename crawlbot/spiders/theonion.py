# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from crawlbot.items import CrawlbotItem


class TheonionSpider(CrawlSpider):
    name = 'theonion'
    allowed_domains = ['theonion.com']
    start_urls = ['http://www.theonion.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/article/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = CrawlbotItem()
        
        i['url'] = response.url
        i['title'] = response.xpath('//header[contains(@class, "content-header")]/h1/text()').extract()[0].strip()
        desc = response.xpath('//div[@class="content-text"]//p/text()').extract()
        desc = " ".join(desc)
        i['description'] = desc

        return i
