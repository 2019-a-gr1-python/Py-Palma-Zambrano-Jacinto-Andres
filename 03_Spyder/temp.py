# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

print("Hola")

nombre = "Jacinto"
edad = 25

print(nombre)

import numpy as np
import pandas as pd 

lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numeros = np.array((1,2,3,4))
numeros_serie_a = pd.Series(lista_numeros)
numeros_serie_b = pd.Series(tupla_numeros)
numeros_serie_c = pd.Series(np_numeros)
numeros_serie_d = pd.Series([
        True,
        False,
        12,
        12.21,
        "ASDF",
        None,
        (),
        [],
        {'nombre':"Jacinto"}])

numeros_serie_a[0]

lista_ciudades = ["Ambato","Cuenca","Loja","Quito"]
serie_ciudades = pd.Series(lista_ciudades, 
                           index = ["A","C","L","Q"])
serie_ciudades["Q"]
serie_ciudades[0]
serie_ciudades[1]
serie_ciudades[2]
serie_ciudades[3]
serie_ciudades["L"]

print(type(serie_ciudades))

valores_ciudad = {
        "Ibarra":9500,
        "Guayaquil":10000,
        "Cuenca":7000,
        "Quito":8000,
        "Loja":3000
        }
serie_valor_ciudad = pd.Series(valores_ciudad)
ciudades_menores_5000 = serie_valor_ciudad < 5000

serie_menor_5000 = serie_valor_ciudad[ciudades_menores_5000]


serie_valor_ciudad = serie_valor_ciudad *1.1
serie_valor_ciudad["Quito"] = 8750

print("Lima" in serie_valor_ciudad) #False
print("Loja" in serie_valor_ciudad) #True

ciudades_menores_5000 = serie_valor_ciudad == 3000
print(serie_valor_ciudad)

np.square(serie_valor_ciudad)
np.sin(serie_valor_ciudad)

ciudades_uno = pd.Series({
        "Quito":1500,
        "Loha":4000
        })

ciudades_dos = pd.Series({
        "Montañita":300,
        "Guayaquil":10000,
        "Quito":2000
        })
print(ciudades_uno * ciudades_dos)

randomico = np.random.rand(3)
serie_tres_rand = pd.Series(randomico)

ciudades_uno.index

#Concatenar Series
pd.concat([ciudades_uno,ciudades_dos])

#Concatenar series sin que se repitan valores
pd.concat([ciudades_uno,ciudades_dos], verify_integrity=True)



