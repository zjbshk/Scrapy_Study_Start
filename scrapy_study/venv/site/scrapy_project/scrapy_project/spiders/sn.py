# -*- coding: utf-8 -*-
import scrapy
from scrapy_project.items import ScrapyProjectItem


class SnSpider(scrapy.Spider):
    name = 'sn'
    allowed_domains = ['suning.com']
    baseUrl = 'https://book.suning.com'
    listUrl = 'https://list.suning.com'
    start_urls = [baseUrl]
    flag = "//h3/a"

    def parse(self, response):
        a_list = response.xpath(self.flag)
        self.flag = "//dd/a"
        for a in a_list:
            hrefs = a.xpath("./@href").extract()
            if len(hrefs) == 0:
                continue
            href = hrefs[0]
            if href.find("list") == -1:
                continue
            if not href.startswith("https:"):
                href = "https:" + href
            yield scrapy.Request(href, callback=self.parse)

        img_list = response.xpath("//div[@class='img-block']//img")
        for img in img_list:
            item = ScrapyProjectItem()
            item["title"] = img.xpath("./@alt").extract()[0]
            hrefs = img.xpath("./@src").extract()
            if len(hrefs) > 0:
                item["href"] = hrefs[0]
            else:
                item["href"] = "no link"
            yield item

        nextPageHrefs = response.xpath("//a[@pagenum]/@href")
        for nextPage in nextPageHrefs:
            href = self.listUrl + nextPage.extract()
            yield scrapy.Request(href, callback=self.parse)
