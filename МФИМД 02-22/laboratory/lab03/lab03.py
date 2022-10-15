from pyfiglet import figlet_format

#importamos la funcion para colocar letras en la portada
#импортируем функцию размещения букв на обложке

print(figlet_format( "Cifrado de gama by Elienis", font = "cybermedium"))

#crearemos un archivo que se llama Source.txt y comenzaremos a escrivir en el
#мы создадим файл Source.txt и начнем в него писать

archivo = open('Sourse.txt','w')
n= 0
while n < 1:
    texto=input('ingresa la frase a encriptar' )
    # вводим в файл фразу для шифрования
    #introducimos en el archivo la frase a encriptar
    archivo.write(texto+'\n')
    n=n+1

archivo.close()
#cerramos el archivo
# закрыть файл

# cadena aleatoria de bits como clave y la combina con el texto sin formato
# случайная строка битов в качестве ключа и комбинирует ее с обычным текстом
A = 15
B = 17
M = 4096
Y0 = 4003

#definimos gamma y denotamos las variables aleatorias
#определить гамму и обозначить случайные величины
def Gamma(y):
    gamma_list = []
    for _ in range(8):
        y = (A * y + B) % M
        gamma_list.append(y)
    return gamma_list

#definimos la funcion encriptar, abrimos el txt de entrada Source y escribimos en Result
#определить функцию шифрования, открыть исходный входной txt и записать в результат
def Crypt():
    gamma = Gamma(Y0)
    res = open("Result.txt", "w", encoding="utf-8")
    with open('Sourse.txt', 'r', encoding="utf-8") as f:
        r_int = ""
        r = ""
        while True:
            temp = f.read(8)
            if temp:
                for i, item in enumerate(temp):
                    r_int = r_int + " " + str(ord(item) ^ gamma[i])
                    # объединить гамма-переменную с введенным текстом
                    #combinamos la variable gama con el texto intriducido
                    r = r + " " + chr(ord(item) ^ gamma[i])
                    res.write(chr(ord(item) ^ gamma[i]))

            else:
                break
    print(r_int)
    res.close()
#guardamos en resultado en el archivo Result.txt
# сохранить результат в файле Result.txt
Crypt()

# definimos la funcion para desencriptar y generar un archivo llamado NewResult
# определить функцию для расшифровки и создания файла с именем NewResult
def DeCrypt():
    gamma = Gamma(Y0)
    #crearemos un nuevo archivo que contendra la frase decifrada
    # создаст новый файл, который будет содержать расшифрованную фразу
    res = open("NewResult.txt", "w", encoding="utf-8")

    # abrimos el archivo con la frase cifrada
    with open('Result.txt', 'r', encoding="utf-8") as f:
        r_int = ""
        r = ""
        while True:
            temp = f.read(8)
            if temp:
                for i, item in enumerate(temp):

                    # realizamos el decifrado de gamma
                    # выполнить гамма-расшифровку

                    r_int = r_int + " " + str(ord(item) ^ gamma[i])
                    r = r + chr(ord(item) ^ gamma[i])
                    res.write(chr(ord(item) ^ gamma[i]))
            else:
                break
    print(r_int)
    #imprimimos el resultado y lo grabamos
    # распечатываем результат и сохраняем
    res.close()


DeCrypt()

print("a continuacion se mostrara el texto cifrado\n") # распечатать результаты шифрования
with open("C:/Users/kami/Documents/matematica/lab03/Result.txt","r") as archivo:
    for linea in archivo:
        print(linea)

print("a continuacion se mostrara el texto decifrado\n") # вывести расшифрованные результаты
with open("C:/Users/kami/Documents/matematica/lab03/NewResult.txt","r") as archivo:
    for linea in archivo:
        print(linea)