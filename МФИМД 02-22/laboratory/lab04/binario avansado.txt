def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

a = int(input("ingrese el primer número:"))
b = int(input("ingrese el segundo número:"))
x = a
y = b
if __name__ == '__main__':
    gcd, x, y = extended_gcd(x, y)
    print('el maximo comun divisor es', gcd)

    print("los coeficientes de la identidad de Bézout son")
    print(f'x = {x}, y = {y}')
