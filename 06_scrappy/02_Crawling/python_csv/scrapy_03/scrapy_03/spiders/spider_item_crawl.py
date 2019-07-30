import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_03.items import ProductoFybeca
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

def generarUrls(self, url_inicial):

        grupo_urls = []
        n=0
        final_de_url = url_inicial[69:]

        for url in range(7):
            url_inicial = url_inicial[0:68]+str(n)+final_de_url
            grupo_urls.append(url_inicial)
            n=n+25
       
        return grupo_urls

class AraniaProductosFybeca(CrawlSpider):
    name = 'arania_crawl_fybeca'

    allowed_domains = [
        'fybeca.com'
    ]
    
    start_urls = generarUrls("", 'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=0&pp=25')

    #start_urls = [ "https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=50&pp=25" ]

    url_segmento_permitido = (
        'FybecaWeb/pages/search-results.jsf?s={0-150}&pp=25&cat=238&b=-1&ot=0',
    )

    regla = ( 
        Rule(LinkExtractor(
            allow_domains=allowed_domains,
            allow=url_segmento_permitido,
        ), callback='parse')
        ,
    )

    rules = regla

    def parse(self, response):

        productos = response.css('div.product-tile-inner')
        for producto in productos:
            existe_producto = len( producto.css('div.detail'))
            if(existe_producto > 0):
                #titulo = producto.css('a.name::text')
                #url = producto.xpath('//div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src')
                producto_loader = ItemLoader(
                    item = ProductoFybeca(),
                    selector = producto
                )
                producto_loader.default_output_processor = TakeFirst()

                producto_loader.add_css(
                    'titulo',
                    'a.name::text'
                    )
                producto_loader.add_xpath(
                    'imagen',
                    'div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src'
                    )

                producto_loader.add_css(
                    'precio',
                    '.price::attr(data-bind)'
                    )

                yield producto_loader.load_item()

                #print(titulo.extract_first())
                #print(url.extract_first())     