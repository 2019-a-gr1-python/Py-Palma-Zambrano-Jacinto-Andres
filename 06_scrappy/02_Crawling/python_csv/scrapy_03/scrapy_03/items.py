# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst

def transformar_url_imagen(texto): 

    url = 'https://www.fybeca.com' 
    cadena_a_reemplazar = '../..'
    return texto.replace(cadena_a_reemplazar,url)
   
def obtener_precio(precio):

    if(len(precio)==43):
        return float(precio[12:17])
    else:
        return float(precio[12:16])

class ProductoFybeca(scrapy.Item):
    imagen = scrapy.Field(
        input_processor = MapCompose(
            transformar_url_imagen
            ),
        output_processor = TakeFirst()
    )
    titulo = scrapy.Field()
    precio = scrapy.Field(
        input_processor = MapCompose(
            obtener_precio
            ),
        output_processor = TakeFirst()
    )