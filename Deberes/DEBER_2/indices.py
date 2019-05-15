import numpy as np
arreglo_frutas = np.array([
    ['Piña','Manzana','Pera','Melon'],
    ['Pera','Uva','Naranja','Papaya'],
    ['Frutilla','Platano','Granadilla','Sandia']
])

arreglo_frutas3d = np.array([
    [['Piña', 'Manzana'],
     ['Pera', 'Melon'],
     ['Uvilla', 'Durazno']],

    [['Pera', 'Uva'],
     ['Naranja', 'Papaya'],
     ['Coco', 'Cereza']],

    [['Frutilla', 'Platano'],
     ['Granadilla', 'Sandia'],
     ['Tamarindo', 'Toronja']]
])

print(arreglo_frutas3d)
arreglox = np.array([
    [0, 0, 2]

])
arregloy = np.array([
    [0, 0, 1]
])
arregloz = np.array([
    [0, 0, 1]
])
print('Seleccion dentro de las dimensiones', arreglo_frutas3d[arreglox,arregloy,arregloz])

frutas1d = arreglo_frutas.flatten()
print(frutas1d)
print(np.where(arreglo_frutas3d.astype('<U1') == 'P'))
print(frutas1d[np.where(frutas1d.astype('<U1') == 'P')])
print(arreglo_frutas3d[np.where(arreglo_frutas3d.astype('<U1') == 'P')])