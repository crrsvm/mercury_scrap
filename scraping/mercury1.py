from scrapy import item
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Piano(Item):
    marca = Field()
    nombre = Field()
    precio = Field()
    descripcion = Field()

class Mercury(CrawlSpider):
    name = 'Pianos'
    # custom_settings = {
    #     'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    # }
    star_urls = ['https://www.mercurymusic.cl/pianos-y-teclados']

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
        item = ItemLoader(Piano(), sel)

        item.add_xpath('marca', '//div[@class="brand-name attribute"]/text()')
        item.add_xpath('nombre', '//span[@class="base"]/text()')
        item.add_xpath('precio', '//span[@class="price"]/text()')
        item.add_xpath('descripcion', '//div[@class="value"]/text()')

        yield item.load_item()
