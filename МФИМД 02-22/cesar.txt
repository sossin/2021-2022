from __future__ import print_function
from pyfiglet import figlet_format


print( figlet_format("Cesar by Elienis", font = "cybermedium" ) )


def main():
    message = input("Introducir Mensaje: ")
    key = int(input("Elige una Clave [1-26]: "))
    mode = input("quieres Cifrar o Descifrar [c/d]: ")

    if mode.lower().startswith('c'):
        mode = "cifrar"
    elif mode.lower().startswith('d'):
        mode = "descifrar"

    translated = encdec(message, key, mode)
    if mode == "cifrar":
        print(("Tu Mensaje Cifrado es:", translated))
    elif mode == "descifrar":
        print(("Tu Mensaje Descifrado es:", translated))


def encdec(message, key, mode):
    message = message.upper()
    translated = ""
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode == "cifrar":
                num = num + key
            elif mode == "descifrar":
                num = num - key

            if num >= len(LETTERS):
                num -= len(LETTERS)
            elif num < 0:
                num += len(LETTERS)

            translated += LETTERS[num]
        else:
            translated += symbol
    return translated


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
    input()

    print(figlet_format("gracias por usar", font="cybermedium"))