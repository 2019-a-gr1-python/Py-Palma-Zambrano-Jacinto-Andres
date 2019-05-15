from skimage import data
import matplotlib.pyplot as plt
import numpy as np

camara = data.camera()
print(f'Tipo {type(camara)}')
print(f'Shape {camara.shape}')
print(f'Tamaño {camara.size}')
print(f'Valor mínimo {camara.min()} Valor máximo {camara.max()}')
print(f'Valor medio {camara.mean()}')
plt.imshow(camara)
plt.show(block=True)
plt.interactive(False)

num_filas, num_columnas = camara.shape
fila, columna = np.ogrid[:num_filas, :num_columnas]
cont_filas, cont_columnas = num_filas / 2, num_columnas / 2
mask_disco = ((fila - cont_filas) ** 2 + (columna - cont_columnas) ** 2 >
              (num_filas / 2) ** 2)
camara[mask_disco] = 0
plt.imshow(camara)
plt.show(block=True)
plt.interactive(False)

mitad_inferior = fila > cont_filas
mitad_disco_inferior = np.logical_and(mitad_inferior, mask_disco)
camara2 = data.camera()
camara2[mitad_disco_inferior] = 0
plt.imshow(camara2)
plt.show(block=True)
plt.interactive(False)