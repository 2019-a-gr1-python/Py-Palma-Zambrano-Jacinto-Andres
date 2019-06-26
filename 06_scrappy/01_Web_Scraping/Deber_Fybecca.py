import numpy as np
import pandas as pd
import re
from scrapy.utils import response



# fetch('https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=567&q=&s=0&pp=25&ds=n')
#Obtener los nombres de los productos
productos = response.xpath('/html/body/div/div/div/div/div/ul/li/@data-name').extract()
productos
#Obtener los precios sin descuento - sin formato
precios_descuento = response.xpath('//div[contains(@class,"price-member")]/div[@data-bind]').extract()
precios_descuento
#obtener los precios con descuento - sin formato
precios2 =response.xpath('/html/body/div/div/div/div/div/ul/li/div/div/div/div[@class="price"]').extract()

#Formateo de los precios
for i in range(len(precios2)):
    precios2[i] = re.findall(r"\d\d.\d.|\d.\d.", precios2[i])

for i in range(len(precios_descuento)):
    precios_descuento[i] = re.findall(r"\d\d.\d.|\d.\d.", precios_descuento[i])

#Creación de el DataFrame
df_precios = pd.DataFrame(precios2,columns=['Precio Total'],index=productos)
df_precios

df_descuentos = pd.DataFrame(precios_descuento,columns=['Precio Descuento'],index=productos)
df_descuentos

#Transforamción del valor de string a float
df_precios['Precio Total'] = df_precios['Precio Total'].astype('float64')

df_descuentos['Precio Descuento'] = df_descuentos['Precio Descuento'].astype('float64')

#Descuento entre los valores
descuento_total = (df_precios['Precio Total'].max()) -(df_descuentos['Precio Descuento'].max())
print("{0:.2f}".format(descuento_total))