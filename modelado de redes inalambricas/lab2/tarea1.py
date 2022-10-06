import numpy as np
import matplotlib.pyplot as plt
import random

exp_100 = np.random.exponential(1, size=100)
exp_1000 =np.random.exponential(1, size=1000)
norm_100 =np.random.normal(0, 1, size=100)
norm_1000 =np.random.normal(0, 1, size=1000)

print("Distribucion exp tamaño 100:", np.mean(exp_100))
print("Distribucion exp tamaño 1000:", np.var(exp_100))

histo = random.randint(100, 1000)
plt.hist(histo, 2)
plt.grid()
plt.show()

# Graficando histograma
mu, sigma = 0, 0.2 # media y desvio estandar
datos = np.random.normal(mu, sigma, 1000) #creando muestra de datos

# histograma de distribución normal.
cuenta, cajas, ignorar = plt.hist(datos, 100)
plt.ylabel('frequencia')
plt.xlabel('valores')
plt.title('Histograma')
plt.show()