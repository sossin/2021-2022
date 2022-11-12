filas = 2
columnas = 2
matriz = []
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        valor =float(input("Fila {}, colnmna{}:".format(i+1,j+1)))
        matriz[i].append(valor)

print()
for fila in matriz:
    print("[", end="")
    for elemento in fila:
        print("{:8.2}".format(elemento), end="")
    print()
print()