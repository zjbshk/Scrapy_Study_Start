# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # ['creater', 'createUserId', 'confirm_price', 'title', 'docId', 'docType', 'docTicket',
    #                    'professionalDoc']
    docId = scrapy.Field()
    title = scrapy.Field()
    docType = scrapy.Field()
    docTicket = scrapy.Field()
    professionalDoc = scrapy.Field()
    creater = scrapy.Field()
    createUserId = scrapy.Field()
    confirm_price = scrapy.Field()
