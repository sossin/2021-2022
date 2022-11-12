import numpy as np
"definimos la funcion de jacobi" \
"a = la matriz que representa el sistema de ecuaciones" \
"b= vector de valores independiente" \
"x0= vector de variables" \
"tol=tolerancia" \
"n= numero de pasos "
def jacobi (A,b,x0,tol,n):
    "matriz diagonal de la matriz"
    D=np.diag(np.diag(A))
    "L MATRIZ triangular inferior de A"
    "U MATRIZ triangular superior de A"
    LU=A-D
    x=x0
    for i in range(n):
        "D es la inversa de la matriz D"
        D_inv=np.linalg.inv(D)
        xtemp = x
        "X Es el producto entre matrices "
        x=np.dot(D_inv,np.dot(-LU,x))+np.dot(D_inv,b)
        print("Iteracion",i,":x =",x)
        "en caso que el valor del vector" \
        "sea menor que la tolerancia, retorno a x"
        if np.linalg.norm(x-xtemp)<tol:
            return x
    return x
"matriz que representa el sistema de ecuaciones a solucionar "
A= np.array([
    [10,-1,2,0],
    [-1,11,-1,3],
    [2,-1,10,.1],
    [0,3,-1,8]
])

import numpy as np
"b =vector de valores independientes"
b=([6,25,-11,15])
x0=np.zeros(4)
tol=1e-3
n= 500
x = jacobi(A,b,x0,tol,n)