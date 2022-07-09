from scrapy.crawler import CrawlerProcess
from crawler.spiders.sreality_spider import SrealitySpider
from scrapy import signals
from scrapy.utils.project import get_project_settings
import os
import time


process = CrawlerProcess(get_project_settings())
process.crawl(SrealitySpider)

def spider_ended(spider, reason):
    print('Spider ended:', spider.name, reason)

for crawler in process.crawlers:
    crawler.signals.connect(spider_ended, signal=signals.spider_closed)

process.start()