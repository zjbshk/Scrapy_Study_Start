# -*- coding: utf-8 -*-
import scrapy
from scrapy_project.items import ScrapyProjectItem


class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['wz.sun0769.com']

    baseUrl = "http://wz.sun0769.com/index.php/question/reply?page="
    offset = 0
    start_urls = [baseUrl + str(offset)]

    def parse(self, response):
        td_list = response.xpath("//table[2]//tr/td[3]/a[@title]")
        for td in td_list:
            item = ScrapyProjectItem()
            title = td.xpath("./@title").extract()[0]
            href = td.xpath("./@href").extract()[0]
            item["title"] = title
            item["href"] = href
            yield item

        if self.offset < 145930:
            self.offset += 30
            yield scrapy.Request(self.baseUrl + str(self.offset), callback=self.parse)
