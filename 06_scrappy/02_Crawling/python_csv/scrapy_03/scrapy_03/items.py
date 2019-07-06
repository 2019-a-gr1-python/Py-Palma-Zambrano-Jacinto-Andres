# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose

class Scrapy03Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def transformar_url_imagen(texto):
    url = 'https://www.fybeca.com'
    cadena_a_reemplazar = '../..'
    return texto.replace(cadena_a_reemplazar,url)

class ProductoFybeca(scrapy.Item):
    imagen = scrapy.Field(
        input_processor = MapCompose(transformar_url_imagen)
    )
    titulo = scrapy.Field()
