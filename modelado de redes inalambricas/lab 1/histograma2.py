import numpy as np
import matplotlib.pyplot as plt

# Parameters
n = 1 # number of points
a = 5 # upper bound
b = -5 # lower bound

# Random coordinates [b,a) uniform distributed
coordy = (b - a) *  np.random.random_sample((n,)) + a # generar aleatorio y
coordx = (b - a) *  np.random.random_sample((n,)) + a # generate aleatorio x

# Create limits (x,y)=((-5,5),(-5,5))
plt.xlim((b,a))
plt.ylim((b,a))

# Plot points
for i in range(n):
    plt.plot(coordx[i],coordy[i],'ro')

plt.show()