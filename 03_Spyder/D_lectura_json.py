# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 10:14:02 2019

@author: dr
"""

import json
import pandas as pd
import os

path = "C:\\Users\\Dario\\Documents\\Python-R\\Py-Palma-Zambrano-Jacinto-Andres\\03_Spyder\\artwork"

archivo = '\\a\\000\\a00001-1035.json'

path_archivo = path + archivo

llaves = ['id','all_artists',
          'title','medium',
          'dateText','acquisitionYear',
          'height','width','units']


def leer_json(path_archivo,llaves):
    with open(path_archivo) as texto_json:
        contenido_json = json.load(texto_json)
    registro_df_lista = []
    for llave in llaves:
        valor = contenido_json[llave]
        registro_df_lista.append(valor)
    return registro_df_lista

leer_json(path_archivo, llaves)

def leer_json_en_carpetas(directorio,llaves):
    trabajos_arte = []
    print(type(os.walk(directorio)))
    for path_raiz, lista_directorios,archivos in os.walk(directorio):
        print(path_raiz)
        print(type(path_raiz))
        print(lista_directorios)
        print(type(lista_directorios))
        print(archivos)
        print(type(archivos))
        
        for nombre_archivo in archivos: 
            if nombre_archivo.endswith('json'):
                directorio_archivo = os.path.join(path_raiz,nombre_archivo)
                pieza_arte = leer_json(directorio_archivo,llaves)
                trabajos_arte.append(pieza_arte)
    
    df = pd.DataFrame.from_records(
            trabajos_arte,
            columns = llaves,
            index = 'id')       
    return df
        
leer_json_en_carpetas(path,llaves)



