import random

# p is the number to check, a is the base, d is odd, r is the power
def Check_If_Composite (p, a, d, r) :

    # If the below is true, then the number is likely to be prime.
    # Condition 1: If ( a ^ d ) = 1 ( mod p ) i.e find out if ( a ^ d ) % p = 1
    # Condition 2: If ( a ^ ( ( 2 ^ 0 ) . d ) = - 1 ( mod p )
    # i.e find out if ( a ^ d ) = -1 (mod p) which is same as finding out if ( a ^ d ) % p = p - 1
    remainder = pow (a, d, p)

    if (remainder == 1 or remainder == p - 1) :
        return False

    # Note : Remainder is already calulated above. It is (a ^ d) % p.
    # Below loop would calulate if (a ^ (( 2 ^ t ).d)) == -1 (mod p) for some 1 <= t <= r-1
    # And ( a ^ d ) = -1 (mod p) is same as ( a ^ d )  % p = p - 1
    # Example ( a ^ d . a ^ d) % p = (a ^ 2.d) mod p
    for t in range (1, r) :
        if ((remainder * remainder) % p == p - 1) :
            return False
    return True

def Check_If_Prime (p, iterations) :

     if (p == 2 or p == 3) :
         return True

     # p is even
     if (p % 2 == 0) :
         return False

     # p - 1 has to be even as p is odd
     d = p - 1
     r = 0
     while ((d % 2) == 0) :
         d = int ( d / 2 )
         r += 1

     for i in range ( iterations + 1 ) :
         # Choose a random a ∈ { 1, 2, . . . , p − 1 }.
         a = random.randrange ( 2, p )
         # If it is definitely composite, then it is not prime.
         if ( Check_If_Composite(p, a, d, r) == True ) :
             return False
     return True

def main():

    tests = int(input("Cuantos numeros quieres chequear : "))

    for i in range(tests):
       p = int(input("Verificando si es primo : "))
       if (Check_If_Prime(p, 5) == True):
            print("Si")
       else:
            print("No")

if __name__ == "__main__" :
    main()