import scrapy

class IntroSpider(scrapy.Spider):
    name = "introduccion_spider"

    def start_requests(self):
        urls =[
            'http://books.toscrape.com/catalogue/category/books_1/page-1.html'
        ]

        for url in urls:
            yield scrapy.Request(url=url)

    def parse(self,response):
        etiqueta_contenedora = response.xpath("//article[contains(@class,'product_pod')]")
        titulos = etiqueta_contenedora.xpath("//h3/a/@title").extract()
        stocks = etiqueta_contenedora.css('div.product_price > p.instock.availability::text').extract()
        precios = etiqueta_contenedora.css('div.product_price > p.price_color::text').extract()
        print(titulos)
        print(stocks)
        print(precios)