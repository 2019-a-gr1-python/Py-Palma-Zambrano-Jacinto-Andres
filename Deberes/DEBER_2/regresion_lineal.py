import numpy as np
import matplotlib.pyplot as plt
#Se tiene un experimento, que mide la resistividad de un material cuando se somete a
#un voltaje entre 1 y 10 volts y la corriente que lo atraviesa, el experimento arroja los
#resultados que se ven en la figura
x = np.arange(1, 11)
Y = [-7.4, -2.3 , 3 , 7.6 , 12 , 17.9 , 22.5 , 27.6 , 32.1, 37.4]
plt.plot(x, Y, 'ro')
plt.xlabel('Voltaje mV')
plt.ylabel('Corriente uA')
plt.title('Resultados Graficados')
plt.show(block=True)
plt.interactive(False)


#Se quiere conocer relación de la forma y = f(x) = ax + b, si existe y que minimice el
#error de los siguientes datos
A = np.array([[1, 1], [2, 1], [3, 1], [4, 1],
            [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]], np.float64)
Y = np.array([[-7.4], [-2.3], [3], [7.6], [12.0],
              [17.9], [22.5], [27.6], [32.1], [37.4]], np.float64)
# Presentamos el arreglo
print('Estas son las matrices A y Y del sistema ')
print('A = ')
print(A)
print('Y = ')
print(Y)
# Presentamos la transpuesta de la matriz
print('Transpuesta de A')
print(A.T)
S = np.dot(A.T, A)
print('Matriz S')
print(S)
Z = np.dot(A.T, Y)
print('Matriz Z ')
print(Z)
# Escribimos el determinante
print('  Determinante de S != 0 ')
print(np.linalg.det(S))
# Escribimos la matriz Inversa
print(' Matriz Inversa de S ')
print(np.linalg.inv(S))
print(' Valores de a y b que resuelven el sistema ')
X = np.dot(np.linalg.inv(S), Z)
print(X)