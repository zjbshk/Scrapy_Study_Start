# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

import re


class BdwkSpider(CrawlSpider):
    name = 'bdwk'
    # allowed_domains = ['wenku.baidu.com']
    start_urls = ['https://wenku.baidu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/view/\w{10,}\.html.*'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'/browse/widget/viewrecom\?pagelets\[\].*'),follow=True),
    )

    def parse_item(self, response):
        try:
            html = response.body.decode("gb2312")
        except:
            return

        start_str = "WkInfo.DocInfo = {"
        end_str = "};"
        start = html.find(start_str) + len(start_str)
        end = html.find(end_str, start) - len(end_str)
        key_value_str = html[start:end]
        key_values = re.sub(r"['+\s]", "", re.sub(r"//\s.+?\n", "", key_value_str)).split(",")

        item = {}
        arr_key = ['creater', 'createUserId', 'confirm_price', 'title', 'docId', 'docType', 'docTicket',
                   'professionalDoc']
        for key in arr_key:
            for key_value in key_values:
                start = key_value.find(key + ":")
                if start != -1:
                    start = start + len(key) + 1
                    value = key_value[start:]
                    item[key] = value
        if item.get("docId") and item.get("title"):
            yield item
            yield scrapy.Request(
                "https://wenku.baidu.com/browse/widget/viewrecom?pagelets[]=view-like-recom&doc_id=" + item["docId"],
                callback=self.parse_item)
