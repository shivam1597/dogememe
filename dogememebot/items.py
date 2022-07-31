# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DogememebotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    time_posted = scrapy.Field() 
    image_url = scrapy.Field()
    shortcode = scrapy.Field()
    hashtags = scrapy.Field()
    username = scrapy.Field()
    id = scrapy.Field()
