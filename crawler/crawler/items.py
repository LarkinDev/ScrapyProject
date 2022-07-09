from scrapy import Item, Field


class SrealityItem(Item):
    title = Field()
    url = Field()
