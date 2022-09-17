
from pyfiglet import figlet_format


print( figlet_format("Atbash by Elienis", font = "cybermedium" ) )



def atbash(message):
    ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ZYX = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
    result = ''

    for letter in message:
        result += ZYX[ABC.index(letter)]

    return result

if __name__ == "__main__":
    message = input('Escribe un mensaje y presione enter: ')
    print(f'Resultado cifrado: { atbash(message.upper()) }')
    print(figlet_format("gracias por usar ", font="cybermedium"))
