# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re


class Ku588Spider(CrawlSpider):
    name = 'ku588'
    allowed_domains = ['588ku.com']
    start_urls = ['http://588ku.com/']

    rules = (
        Rule(LinkExtractor(allow=r'http://588ku\.com/\w+/\d+\.html'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'http://588ku\.com/\[a-z\-_]+/\d+\.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        div_list = response.xpath("//div[@class='imgText-info'][1]/div")
        if len(div_list) > 0:
            item = {}
            item["url"] = response.url
            title = response.css("span.title-name a::text").extract_first()
            item["title"] = title
            for div in div_list:
                label = div.xpath("./span[1]/text()").extract()[0]
                values = div.xpath("./span[2]/text()").extract()
                if len(values) > 0:
                    value = values[0]
                    item[label] = re.sub(r"\s+", "", value)
                    yield item
