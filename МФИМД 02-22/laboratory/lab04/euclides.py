from pyfiglet import figlet_format
print(figlet_format( "MCD by Elienis", font = "cybermedium"))
import math

comprobar = True

while comprobar:
    #introducimos las variables en numeros enteros
    a = int(input("ingrese el primer número:"))
    b = int(input("ingrese el segundo número:"))

    MCD = False
    # si a y b es mayor que 0 y que a y b sean diferentes
    if a  > 0 and b  > 0 and a != b:

        comprobar = False
        #creo variable auxiliar en caso de que b sea menor que a
        if b < a:
            aux = a
            a=b
            b= aux

        i=a
        #creamos ciclo mientras mcd sea falso y i sea mayor o igual a 1
        while not MCD and i >= 1:
            #si a es igual a 0 e i , imprimimos esa variable
            if a % i == 0 and b % i== 0 :
                print(" el MCD es ",i)
                MCD =True

                #decrementamos 1 en el bucle hasta que i sea una division exacta
            else:
                i-= 1

    # si el usuario no coloco los numeros correctos , manda a pedir los numeros
    else:
        if a == b:
            print("Los numeros son iguales, intentelo de nuevo ")
        else:
            print("Los numeros no son correctos, intentelo neuvamente")