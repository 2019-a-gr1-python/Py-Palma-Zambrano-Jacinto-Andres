# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 11:08:48 2019

@author: dr
"""

import pandas as pd
import numpy as np
import os
import sqlite3

path_guardado = 'C:\\Users\\Dario\\Documents\\Python-R\\Py-Palma-Zambrano-Jacinto-Andres\\03_Spyder\\data\\artwork_data.pickle'

df_completo_pickel = pd.read_pickle(path_guardado)

df = df_completo_pickel.iloc[49980:50019,:].copy()

#   Tipos de archivos
#   £
#   - JSON
#   - SQL
#   - EXCEL

##################################EXCEL#######################################

df.to_excel('ejemplo_basico.xlsx')

df.to_excel('ejemplo_basico_sin_indices.xlsx', index=False)

columnas = ['artist','title','year']

df.to_excel('columnas.xlsx', columns = columnas)

# Múltiples hojas de trabajo (worksheet)

writer = pd.ExcelWriter('multiples_worksheet.xlsx',
                        engine = 'xlsxwriter')

df.to_excel(writer, sheet_name = 'Preview')

df.to_excel(writer, sheet_name = 'Preview Dos', index = False)

df.to_excel(writer, sheet_name = 'Preview', columns = columnas)

writer.save()

artistas_contados = df_completo_pickel['artist'].value_counts()

writer = pd.ExcelWriter('colores.xlsx', engine = 'xlsxwriter')

artistas_contados.to_excel(writer, sheet_name = 'Artistas contados')

hoja_artistas = writer.sheets['Artistas contados']

rango_celdas = 'B2:B{}'.format(len(artistas_contados.index)+1)

formato = {
        'type':'2_color_scale',
        'min_value':'10',
        'min_type':'percentile',
        'max_value':'99',
        'max_type':'percentile'       
        }
hoja_artistas.conditional_format(rango_celdas, formato)

writer.save()


#################################### SQL ####################################

with sqlite3.connect('bdd_python.db') as conexion:
    df.to_sql('Alguien', conexion)

###with sqlite3.connect('mysql))') as conexion:
###    ds.to_sql('Alguien', conexion)

################################# JSON #######################################
    
df.to_json('artistas.json')
#######


############################### Aplicar los demás formatos ##################

artistas_contados = df_completo_pickel['artist'].value_counts()

writer = pd.ExcelWriter('formato1.xlsx', engine = 'xlsxwriter')

artistas_contados.to_excel(writer, sheet_name = '3_color_scale')
artistas_contados.to_excel(writer, sheet_name = 'data_bar')

hoja_artistas_3_color_state = writer.sheets['3_color_scale']
hoja_artistas2_data_bar = writer.sheets['data_bar']

rango_celdas = 'B2:B{}'.format(len(artistas_contados.index)+1)

formato_3_color_state = {
        'type':'3_color_scale',
        'min_value':'5',
        'min_type':'percent',
        'max_value':'300',
        'max_type':'percent' 
        }

hoja_artistas.conditional_format(rango_celdas, formato)

writer.save()