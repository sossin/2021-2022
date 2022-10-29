from pyfiglet import figlet_format
print(figlet_format( "MCD Euclides by Elienis", font = "cybermedium"))
import math

def euclides(num1, num2, iteracciones=1):
    # Si el num1 es inferior al num2, los invertimos
    if num1 < num2:
        num1, num2 = num2, num1

    # obtenemos el resto de la division
    resto = num1 % num2

    if resto == 0:
        return (num2, iteracciones)

    # llamamos nuevamente a la función pasando como primer parametro el
    # segundo numero y el resto de la division
    return euclides(num2, resto, iteracciones + 1)

a = int(input("ingrese el primer número:"))
b = int(input("ingrese el segundo número:"))
num1 = a
num2 = b

comunDivisor, iteracciones = euclides(num1, num2)

print("El comun divisor de {} y {} es {}".format(num1, num2, comunDivisor))
print("Se ha encontrado en {} iteracciones".format(iteracciones))