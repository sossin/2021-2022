import numpy as np
import matplotlib.pyplot as plt
import random


def distance( x1,y1,x2,y2):
    return np.sqrt((x2-x1)**2+(y2-y1)**2)
def distance_line(number):
    a=10
    b=30
    distances=[]
    for i in range(number):
        x1=np.random.uniform(0,a)
        y1=np.random.uniform(0,b)

        x2=np.random.uniform(0,a)
        y2=np.random.uniform(0,b)

        distances.append(distance(x1,y1,x2,y2))

    distance.sort()
    return distances

