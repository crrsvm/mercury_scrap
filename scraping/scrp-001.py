from scrapy import item
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Hotel(Item):
    nombre = Field()
    precio = Field()
    descripcion = Field()
    amenities = Field()

class TripAdvisor(CrawlSpider):
    name = 'Hoteles'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    star_urls = ['https://www.tripadvisor.cl/Tourism-g294305-Santiago_Santiago_Metropolitan_Region-Vacations.html']

    download_delay = 2

    rules = (
        Rule(
            LinkExtractor(
                allow=r'piano-digital-'
            ), follow=True, callback="parse_piano"
        )

    )

    def parse_piano(self, response):
        sel = Selector(response)
        item = ItemLoader(Hotel(), sel)

        item.add_xpath('nombre', '//h1[@id="HEADING"]/text()')
        item.add_xpath('precio', '')
        item.add_xpath('descripcion', '')
        item.add_xpath('amenities', '')

        yield item.load_item()