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
    start_urls = ['https://www.audiomusica.com/pianos-y-teclados.html']
    allowed_domains = ['https://www.audiomusica.com']

    rules = (
        Rule(LinkExtractor(allow=r'p=')),
        Rule(LinkExtractor(allow=r'piano-digital-'), callback= 'parse_items'),
    )

    def parse_items(self, response):
        item = ItemLoader(PianosItem(), response)
        item.add_xpath('marca', '//*[@id="maincontent"]/div[2]/div/div[1]/div[1]/div/span/img/text()')
        item.add_xpath('modelo', '//*[@id="maincontent"]/div[2]/div/div[1]/div[2]/h1/span/text()')
        item.add_xpath('precio', '//*[@id="product-price-1832"]/span/text()')
        yield item.load_item()