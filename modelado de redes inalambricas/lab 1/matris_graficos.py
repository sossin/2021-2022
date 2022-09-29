import matplotlib.pyplot as plt
import numpy as np

inicio = -2
fin = 2
ancho = 0.1
div=np.linspace(inicio,fin, round(1+(fin-inicio)/ancho))
plt.hist(np.random.uniform(-1,1,1000) ,div,color='blue')
plt.show()


