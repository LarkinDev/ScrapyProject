from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import CloseSpider, DropItem
from .model import ScrapyData, db_connect, create_table
from itemadapter import ItemAdapter


class ScrapyPipeline:

    def __init__(self):
        # engine = db_connect()
        # create_table(engine)
        self.file = open('items.txt', 'a+')
        # self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        self.file.write(item["title"]+"\n")
        # session = self.Session()
        # data = ScrapyData(title=item['title'], url=item['url'])
        # try:
        #     session.add(data)
        #     session.commit()
        # except:
        #     session.rollback()
        #     raise
        # finally:
        #     session.close()
        return item

    # raise DropItem()
