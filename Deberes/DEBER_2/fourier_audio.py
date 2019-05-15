import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from IPython.display import Audio
from skimage import util

#Importar el archivo de audio
Audio('Dark-mysterious-theme.wav')
#Obtener los valores de muestra, que son 2 por ser sonido en estéreo
velocidad, audio = wavfile.read('Dark-mysterious-theme.wav')
#Se convierte a un solo canal (mono) mediante la media de los valores de izquierda y derecha
audio = np.mean(audio, axis=1)

#Se calcula la longitud del audio
N = audio.shape[0]
L = N / velocidad

print(f'Longitud del audio : {L:.2f} segundos')

f, ax = plt.subplots()
ax.plot(np.arange(N) / velocidad, audio)
ax.set_xlabel('Tiempo[s]')
ax.set_ylabel('Amplitud [desconocida]')
plt.show(block=True)
plt.interactive(False)

#Dividir la señal en segmentos de 1024 muestras,
#  cada segmento se superpone al anterior en 100 muestras.
M = 1024

segmentos = util.view_as_windows(audio, window_shape=(M,), step=100)
print(f'Forma del audio: {audio.shape}, Forma del audio por partes: {segmentos.shape}')
ventana = np.hanning(M + 1)[:-1]
segmentos = segmentos * ventana
segmentos = segmentos.T
print('Forma de los `segmentos`:', segmentos.shape)

espectro = np.fft.fft(segmentos, axis=0)[:M // 2 + 1:-1]
espectro = np.abs(espectro)

f, ax = plt.subplots(figsize=(4.8, 2.4))

#gráfico de registro de la relación de la señal dividida por la señal máxima
#La unidad específica utilizada para la relación es el decibelio, 20log10 (relación de amplitud).
S = np.abs(espectro)
S = 20 * np.log10(S / np.max(S))

ax.imshow(S, origin='lower', cmap='viridis',
          extent=(0, L, 0, velocidad / 2 / 1000))
ax.axis('tight')
ax.set_ylabel('Frecuencia [kHz]')
ax.set_xlabel('Tiempo [s]')
plt.show(block=True)
plt.interactive(False)