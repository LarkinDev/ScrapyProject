import json
import scrapy
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from ..items import SrealityItem
from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import CloseSpider, DropItem
from ..model import ScrapyData, db_connect, create_table


class SrealitySpider(scrapy.Spider):
    name = "sreality"

    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-crash-reporter")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-in-process-stack-traces")
        chrome_options.add_argument("--disable-logging")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument("--output=/dev/null")

        chrome_prefs = {}
        chrome_options.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def start_requests(self):
        for i in range(1, 11):
            url = "https://www.sreality.cz/hledani/prodej/byty?strana="+str(i)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #filename = "test.csv"
        self.driver.implicitly_wait(10)
        self.driver.get(response.url)
        item = SrealityItem()
        names = self.driver.find_elements(By.CSS_SELECTOR, "span.name.ng-binding")
        urls = []
        for i in range(1, 21):
            xpath = "/html/body/div[2]/div[1]/div[2]/div[3]/div[3]/div/div/div/div/div[3]/div/div[" + str(i) + "]/preact/div/div/a[1]/img"
            link = self.driver.find_element(By.XPATH, xpath)
            urls.append(link)

        for name, url in zip(names, urls):
            title = name.text
            link = url.get_attribute("src")
            item['title'] = title
            item['url'] = link
            self.add_to_db(item)

    def add_to_db(self, item):
        session = self.Session()
        data = ScrapyData(title=item['title'], url=item['url'])
        try:
            session.add(data)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

