# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class DaguerrePostItem(Item):
    post_id = Field()
    post_title = Field()
    post_url = Field()
    post_image_list = Field()