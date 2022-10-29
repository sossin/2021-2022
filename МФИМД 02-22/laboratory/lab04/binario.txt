import math

a = int(input("ingrese el primer número:"))
b = int(input("ingrese el segundo número:"))
num1 = a
num2 = b
sh=0
steps=0

if (num1 == 0) or (num2 ==0):
    ans = 0
    #si la respuesta es 0 no necesitamos continuar
else:
    while (num1 % 2 ==0) and (num2 % 2 == 0):
        print("numero a es :", num1)
        print("numero b es :", num2)
        num1 = num1 >> 1
        num2 = num2 >> 1
        sh = sh+1
        steps = steps+1

    while (num1 != num2):
        print("numero a es :",num1)
        print("numero b es :", num2)
        while (num1 & 1 ==0):
            num1 = num1 >> 1
            steps = steps +1
        while (num2 & 1 ==0):
            num2 = num2 >> 1
            steps = steps + 1
        steps = steps + 1
        if num1 < num2:
            num2 = num2 - num1
        if num2 < num1:
            num1 = num1 - num2
        ans = num1 << sh
print("MCD es:" ,ans)
print("mcd real es :", math.gcd(a,b))
print("Pasos :", steps)



















