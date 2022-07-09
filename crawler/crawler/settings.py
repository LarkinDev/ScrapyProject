BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'

ROBOTSTXT_OBEY = False

COOKIES_ENABLED = True
COOKIES_DEBUG = True

#LOG_LEVEL = 'INFO'

# ITEM_PIPELINES = {
#     'crawler.pipelines.ScrapyPipeline': 300,
# }

DATABASE = {
    'drivername': 'postgresql',
    'host': 'db',
    'port': '5432',
    'username': 'docker',
    'password': 'docker',
    'database': 'scrapyDB'
}