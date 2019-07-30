import scrapy
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

class AraniaProductosFybeca(scrapy.Spider):
    name = 'arania_fybeca'

    def start_requests(self):
        urls = generarUrls("", 'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=0&pp=25')

        for url in urls:
            yield scrapy.Request(url=url)
            
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














"""

url = response.xpath('//div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src')
contenedor = response.css('div.product-tile-inner')
titulo = contenedor.css('a.name::text')

def transformar_url_imagen(texto): 
    url = 'https://www.fybeca.com' 
    cadena_a_reemplazar = '../..'   
    print('ASDASDAS') 
    return texto.replace(cadena_a_reemplazar,url)

class ProductoFybeca(scrapy.Item):
    imagen = scrapy.Field(
        input_processor = MapCompose(transformar_url_imagen)
    )
    titulo = scrapy.Field()

from scrapy.loader import ItemLoader
il = ItemLoader(item=ProductoFybecaDos())
il.add_value('imagen',url.extract_first())
il.add_value('titulo', titulo.extract_first())
il.load_item()
"""