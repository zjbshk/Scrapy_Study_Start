# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JwggSpider(CrawlSpider):
    name = 'jwgg'
    allowed_domains = ['jwc.jxnu.edu.cn']
    start_urls = ['http://jwc.jxnu.edu.cn/Portal/ArticlesList.aspx?type=Jwgg']
    index = 1

    rules = (
        Rule(LinkExtractor(allow=r'ArticlesView.aspx\?id=\d+'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'ArticlesList.aspx\?type=jwgg&page=\d+'),  follow=True),
    )

    def parse_item(self, response):
        # titles = response.xpath("//div[@class='main-content']/div/text()")
        print(self.index, response.url)
        self.index += 1
        item = {}
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        return item
