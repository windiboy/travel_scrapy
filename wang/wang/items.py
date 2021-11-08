# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WangItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    url = scrapy.Field()
