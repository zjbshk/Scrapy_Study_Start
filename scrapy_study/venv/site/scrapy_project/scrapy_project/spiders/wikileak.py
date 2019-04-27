# -*- coding: utf-8 -*-
import scrapy


class WikileakSpider(scrapy.Spider):
    name = 'wikileak'
    # allowed_domains = ['wikileaks.org']
    baseUrl = "https://file.wikileaks.org/file/"
    start_urls = [baseUrl]

    def parse(self, response):
        a_list = response.xpath("//pre/a")
        for a in a_list:
            print(a.extract())

