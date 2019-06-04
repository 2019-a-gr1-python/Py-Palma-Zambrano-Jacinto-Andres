import pandas as pd
import pandas_datareader.data as wb
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

data = pd.read_csv('accidents_2017.csv')
path_guardado = 'accident_2017.pickle'
data.to_pickle(path_guardado)
df_pickle_guardado = pd.read_pickle(path_guardado)

columnas_usar = ['Id','District Name','Neighborhood Name','Street','Weekday','Month','Day','Hour','Part of the day','Mild injuries','Serious injuries','Victims','Vehicles involved','Longitude','Latitude']
lista = pd.read_csv('accidents_2017.csv', usecols=columnas_usar)

hora_dia = lista['Part of the day'].unique()
cantidadxpartedia = np.zeros(hora_dia.size)

for idNacionalidad, pais in enumerate(hora_dia):
    cantidadxpartedia[idNacionalidad] = lista[lista['Part of the day'] == pais].Street.count()

plt.figure(1)
plt.title('Cantidad de Accidentes por Parte del Día')
plt.xlabel('Parte del Dia')
plt.ylabel('Cantidad Accidentes')
plt.xticks(rotation=90)
plt.bar(hora_dia, cantidadxpartedia)
plt.show()
plt.show(block=True)
plt.interactive(False)


fig = plt.figure(figsize=(8,18))
data.Month[data.Weekday=='Friday'].value_counts().plot(kind='barh',alpha=1)
plt.title('Cantidad de Accidentes por Mes que suceden en Viernes')
plt.show()
plt.show(block=True)
plt.interactive(False)


inmigrantes = np.unique(df_pickle_guardado['Neighborhood Name'].get_values(), return_counts = True)
cantidad=inmigrantes[0][np.where(inmigrantes[1] >= 300)]
cantidad_incidencia = inmigrantes[1][np.where(inmigrantes[1] >= 300)]

impr2 = cantidad
vol = cantidad_incidencia
plt.figure(figsize=(8,8))
plt.pie(vol, labels=impr2, autopct='%1.2f%%', textprops={'fontsize': 14})
plt.title("Barrios con Incidencias de 300 o mas accidentes", fontsize=20)
plt.show()


def arreglo_ocurrencia_horas(df, tipo_tiempo):
    horas_como_entero = df[tipo_tiempo].get_values().astype(int)
    ocurrencias_media_noche = len(df[tipo_tiempo].get_values()[np.where(horas_como_entero < 0)])

    ocurrencias_pasada_media_noche = df[tipo_tiempo].get_values()[np.where(horas_como_entero > 0)]
    antes_de_10_AM = ocurrencias_pasada_media_noche[np.where(ocurrencias_pasada_media_noche < 0)]
    ocurrencias_antes_de_10_AM = np.unique(antes_de_10_AM.astype("<U1"), return_counts=True)[1]

    pasadas_10_AM = df[tipo_tiempo].get_values()[np.where(horas_como_entero > 0)]
    ocurrecias_pasadas_10_AM = np.unique(pasadas_10_AM.astype("<U2"), return_counts=True)[1]

    cantidad_crimenes_por_hora = [ocurrencias_media_noche]
    cantidad_crimenes_por_hora.extend(ocurrencias_antes_de_10_AM)
    cantidad_crimenes_por_hora.extend(ocurrecias_pasadas_10_AM)

    return cantidad_crimenes_por_hora

horas = ("0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23")
plt.figure(figsize=(10,6))
plt.title("Accidentes vs Horas", fontsize=20)
plt.xlabel("Horas", fontsize=15)
plt.ylabel("Accidentes", fontsize=15)
indice = np.arange(len(arreglo_ocurrencia_horas(df_pickle_guardado,'Hour')))
plt.xticks(indice, horas)
plt.yticks(np.arange(0,np.max(arreglo_ocurrencia_horas(df_pickle_guardado,'Hour')),100))
plt.plot(arreglo_ocurrencia_horas(df_pickle_guardado,'Hour'))
for x,y in zip(indice,arreglo_ocurrencia_horas(df_pickle_guardado,'Hour')):
    plt.text(x,y,y,fontsize='medium')
plt.show()
plt.show(block=True)
plt.interactive(False)

arreglo_distrito = np.unique(df_pickle_guardado['District Name'].get_values(), return_counts = True)
serie_distrito = pd.Series(arreglo_distrito[1],
                           index=arreglo_distrito[0]
                           )
accidentes_new = serie_distrito.sort_values(ascending=False).index.values.tolist()
ocurrencia_accidentes = serie_distrito.sort_values(ascending=False)
posicion_y = np.arange(len(accidentes_new))
plt.figure(figsize=(15,25))
plt.barh(posicion_y, ocurrencia_accidentes, align ="center")
plt.yticks(posicion_y, accidentes_new)
plt.xlabel('Incidencia', fontsize=15)
plt.title("Cantidad de Accidentes por Distrito", fontsize=20)
for i, v in enumerate(ocurrencia_accidentes):
    plt.text(v + 3, i, str(v),fontsize='x-large')
plt.show()
plt.show(block=True)
plt.interactive(False)

accidentes_calle = np.unique(df_pickle_guardado['Street'].get_values(), return_counts = True)
cantidad=accidentes_calle[0][np.where(accidentes_calle[1] >= 80)]
cantidad_incidencia = accidentes_calle[1][np.where(accidentes_calle[1] >= 80)]

impr2 = cantidad
vol = cantidad_incidencia
plt.figure(figsize=(10,10))
plt.pie(vol, labels=impr2, autopct='%1.1f%%', shadow=True, textprops={'fontsize': 14})
plt.title("Calles con mayor cantidad de accidentes (80 o más)", fontsize=20)
plt.show()
plt.show(block=True)
plt.interactive(False)

data2 = pd.read_csv('immigrants_by_nationality.csv')
path_guardado2 = 'immigrants_by_nationality.pickle'
data2.to_pickle(path_guardado2)
df_pickle_guardado2 = pd.read_pickle(path_guardado2)

columnas_usar2 = ['Year','District Code','District Name','Neighborhood Code','Neighborhood Name','Nationality','Number']
lista = pd.read_csv('immigrants_by_nationality.csv', usecols=columnas_usar2)


anio = lista['Year'].unique()
cantidadxanio = np.zeros(anio.size)

for idNacionalidad2, pais2 in enumerate(anio):
    cantidadxanio[idNacionalidad2] = lista[lista['Year'] == pais2].Nationality.count()

plt.figure(1)
plt.title('Cantidad Inmigrantes en Barcelona por Año')
plt.xlabel('Año')
plt.ylabel('Cantidad Inmigrantes')
plt.xticks(rotation=90)
plt.bar(anio, cantidadxanio)
plt.show()
plt.show(block=True)
plt.interactive(False)
