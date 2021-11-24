from scrapy import item
from scrapy import linkextractors
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule, Spider
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class PianosItem(Item):
    marca = Field()
    modelo = Field()
    precio = Field()

class MercuryCrawler(CrawlSpider):
    name = 'AudiomusicaCrawler'
    start_urls = ['https://www.mercurymusic.cl/pianos-y-teclados']
    allowed_domains = ['https://www.mercurymusic.cl']

    rules = (
        Rule(LinkExtractor(allow=r'p=')),
        Rule(LinkExtractor(allow=r'-'), callback= 'parse_items'),
    )

    def parse_items(self, response):
        item = ItemLoader(PianosItem(), response)
        item.add_xpath('marca', '//*[@id="amasty-shopby-product-list"]/div[3]/ol/li[1]/div/div[2]/span/text()')
        item.add_xpath('modelo', '//*[@id="amasty-shopby-product-list"]/div[3]/ol/li[1]/div/div[2]/strong/a/text()')
        item.add_xpath('precio', '//*[@id="product-price-1838"]/span/text()')
        yield item.load_item()

