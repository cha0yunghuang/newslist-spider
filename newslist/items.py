# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewslistItem(scrapy.Item):
    post_title = scrapy.Field()
    post_date = scrapy.Field()
    pass
