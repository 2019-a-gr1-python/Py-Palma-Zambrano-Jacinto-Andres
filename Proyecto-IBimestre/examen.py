import pandas as pd
import pandas_datareader.data as wb
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

data = pd.read_csv('accidents_2017.csv')

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




