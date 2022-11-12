import random
import time


#El siguiente Algoritmo de Strassen es sacado de
#https://github.com/stanislavkozlovski/Algorithms/blob/master/Coursera/algorithms_stanford/Strassen%20Matrix%20Multiplication/python/strassen.py

def default_matrix_multiplication(a, b):
    """
    Only for 2x2 matrices
    """
    if len(a) != 2 or len(a[0]) != 2 or len(b) != 2 or len(b[0]) != 2:
        raise Exception('Matrices should be 2x2!')
    #print(a[0][0] * b[0][1] + a[0][1] * b[1][1])
    new_matrix = [[a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
                  [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]

    return new_matrix


def matrix_addition(matrix_a, matrix_b):
    # print(matrix_a)
    return [[matrix_a[row][col] + matrix_b[row][col]
             for col in range(len(matrix_a[row]))] for row in range(len(matrix_a))]


def matrix_subtraction(matrix_a, matrix_b):
    return [[matrix_a[row][col] - matrix_b[row][col]
             for col in range(len(matrix_a[row]))] for row in range(len(matrix_a))]


def split_matrix(a):
    """
    Given a matrix, return the TOP_LEFT, TOP_RIGHT, BOT_LEFT and BOT_RIGHT quadrant
    """
    if len(a) % 2 != 0 or len(a[0]) % 2 != 0:
        raise Exception('Odd matrices are not supported!')

    matrix_length = len(a)
    mid = matrix_length // 2
    top_left = [[a[i][j] for j in range(mid)] for i in range(mid)]
    bot_left = [[a[i][j] for j in range(mid)] for i in range(mid, matrix_length)]

    top_right = [[a[i][j] for j in range(mid, matrix_length)] for i in range(mid)]
    bot_right = [[a[i][j] for j in range(mid, matrix_length)] for i in range(mid, matrix_length)]

    return top_left, top_right, bot_left, bot_right


def get_matrix_dimensions(matrix):
    return len(matrix), len(matrix[0])


def strassen(matrix_a, matrix_b):
    """
    Recursive function to calculate the product of two matrices, using the Strassen Algorithm.
    Currently only works for matrices of even length (2x2, 4x4, 6x6...etc)
    """
    if get_matrix_dimensions(matrix_a) != get_matrix_dimensions(matrix_b):
        raise Exception(f'Both matrices are not the same dimension! \nMatrix A:{matrix_a} \nMatrix B:{matrix_b}')
    if get_matrix_dimensions(matrix_a) == (2, 2):
        return default_matrix_multiplication(matrix_a, matrix_b)

    A, B, C, D = split_matrix(matrix_a)
    E, F, G, H = split_matrix(matrix_b)

    p1 = strassen(A, matrix_subtraction(F, H))
    p2 = strassen(matrix_addition(A, B), H)
    p3 = strassen(matrix_addition(C, D), E)
    p4 = strassen(D, matrix_subtraction(G, E))
    p5 = strassen(matrix_addition(A, D), matrix_addition(E, H))
    p6 = strassen(matrix_subtraction(B, D), matrix_addition(G, H))
    p7 = strassen(matrix_subtraction(A, C), matrix_addition(E, F))

    top_left = matrix_addition(matrix_subtraction(matrix_addition(p5, p4), p2), p6)
    top_right = matrix_addition(p1, p2)
    bot_left = matrix_addition(p3, p4)
    bot_right = matrix_subtraction(matrix_subtraction(matrix_addition(p1, p5), p3), p7)

    # construct the new matrix from our 4 quadrants
    new_matrix = []
    for i in range(len(top_right)):
        new_matrix.append(top_left[i] + top_right[i])
    for i in range(len(bot_right)):
        new_matrix.append(bot_left[i] + bot_right[i])
    return new_matrix

#Fin de algoritmo de Strassen



#Funciones adicionales para generar matriz aleatoria
def generateMat(f, c):
    M = []
    for i in range(f):
        M.append([])
        for j in range(c):
            M[i].append(random.randint(0,10))
    return M

#Funcion adicional para mostrar la matriz
def mostrarMat(M):
    print("\n")
    for fila in M:
        print(fila)
    print("\n")

# Algoritmo de multiplicacion de matrices de forma iterativa
#https://gist.github.com/parzibyte/bb96d0c5089858b3de2110ec208f55a5#file-producto-py

def producto_matrices(a, b):
    filas_a = len(a)
    filas_b = len(b)
    columnas_a = len(a[0])
    columnas_b = len(b[0])
    if columnas_a != filas_b:
        return None
    # Asignar espacio al producto. Es decir, rellenar con "espacios vacíos"
    producto = []
    for i in range(filas_b):
        producto.append([])
        for j in range(columnas_b):
            producto[i].append(None)
    # Rellenar el producto
    for c in range(columnas_b):
        for i in range(filas_a):
            suma = 0
            for j in range(columnas_a):
                suma += a[i][j]*b[j][c]
            producto[i][c] = suma
    return producto

#Fin de algoritmo de producto de 2 matrices

#_________________________________________________________________________
print("    Programa que multiplica 2 matrices    ")
orden = int(input("Generar orden: "))

A = generateMat(orden,orden)
B = generateMat(orden,orden)

mostrarMat(A)
mostrarMat(B)

print("Strassen")
inicio = time.time()
C = strassen(A,B)
fin = time.time()
mostrarMat(C)
tStrassen = fin -inicio

print("Tradicional")
inicio = time.time()
D= producto_matrices(A,B)
fin = time.time()
mostrarMat(D)
tTradicional = fin -inicio
print("Tiempo de strassen: " , tStrassen)
print("Tiempo de normal: " , tTradicional)