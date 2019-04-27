# -*- coding: utf-8 -*-
import scrapy, re
from scrapy_project.items import ScrapyProjectItem


class BdwkSeleniumSpider(scrapy.Spider):
    name = 'bdwk_selenium'
    allowed_domains = ['wenku.baidu.com']
    base_url = "https://wenku.baidu.com"
    start_urls = [base_url + '/view/a2eaa1273069a45177232f60ddccda38376be193.html']

    def parse(self, response):
        try:
            html = response.body.decode()
        except:
            return

        start_str = "WkInfo.DocInfo = {"
        end_str = "};"
        start = html.find(start_str) + len(start_str)
        end = html.find(end_str, start) - len(end_str)
        key_value_str = html[start:end]
        key_values = re.sub(r"['+\s]", "", re.sub(r"//\s.+?\n", "", key_value_str)).split(",")

        item = ScrapyProjectItem()
        arr_key = ['creater', 'createUserId', 'confirm_price', 'title', 'docId', 'docType', 'docTicket',
                   'professionalDoc']
        for key in arr_key:
            for key_value in key_values:
                start = key_value.find(key + ":")
                if start != -1:
                    start = start + len(key) + 1
                    value = key_value[start:]
                    item[key] = value
        yield item

        href_list = response.xpath("//div[@class='item']//a/@href")
        for href in href_list:
            yield scrapy.Request(self.base_url + href.extract(), callback=self.parse)
