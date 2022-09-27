
print("\033[9;35m"+"Codificacion Rejilla by Elienis")

def grille_encrypt(plaintext: str, grille: List[str]) -> Optional[str]:
    # Hay un trozo de papel de cuadrícula cuadrada con orificios (4*4) en el papel blanco, rejilla: posición del orificio
    # Después de girar la posición del orificio durante una semana, se puede llenar el cuadrado de 4*4. Si no puede, no será válido y volverá directamente a None.
    # Escriba las letras de texto sin formato en los agujeros de izquierda a derecha y de arriba a abajo. Después de girar el papel de orificio 90 grados en el sentido de las agujas del reloj, el orificio se mueve a una posición en blanco y las letras de texto sin formato continúan escribiéndose.
    # Si el mensaje no termina después de girar 3 veces, continúe en la siguiente hoja de papel
    # La letra final se completará, lea el texto cifrado de salida por línea

    # Regrese a la posición cubierta por el orificio después de que la rejilla gire 3 veces
    def check_grille(grille):
        # Ubicación actual del hoyo
        K = [(i, j) for i, l in enumerate(grille) for j, v in enumerate(l) if v == 'X']
        # Convertir lista de rejillas a matriz
        # Rotación de matriz, obtenga la posición del orificio después de cada rotación, y después de 3 rotaciones, obtenga la posición del orificio.
        for i in range(3):
            grille = [[j for j in g ] for g in grille ]
            A = np.mat(grille)  # Lista matriz de par
            B = np.rot90(A,k=-1) # Rotación de la matriz, k es un número positivo en sentido antihorario, k es un número negativo en sentido horario.
            grille = B.tolist() # Matriz para listar
            k = [(i, j) for i, l in enumerate(grille) for j, v in enumerate(l) if v == 'X']
            K.extend(k)
        return K
    K = check_grille(grille) # La posición en la que los orificios se cubren a su vez es también la posición en la que las letras de texto sin formato se rellenan a su vez
 # imprimir('=============================',conjunto (K), len(conjunto (K)))

    if len(set(K)) != 16 or len(K) > 16: # Después de girar 3 veces, el orificio no cubre 4*4=16 cuadrados, o los cuadrados se cubren repetidamente, la rejilla no es válida
        result = None
    else:
        ciphertext = []
        for i in range(0,len(plaintext),16):
            sub_t = plaintext[i:i+16]
            # Narr = np.array([['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]) #创建一个4*4矩阵
            Narr = np.ones((4, 4)).astype(np.str_)  # # Crear una matriz de caracteres de 4*4
            # Complete las letras de texto sin formato en la posición de K a su vez
            for j in range(16):
                x = K[j][0]
                y = K[j][1]
                Narr[x][y] = sub_t[j] if j < len(sub_t) else '' # Evita que la longitud del texto sin formato sea inferior a 16
                # Después de completar, convierta la matriz en una cadena por fila
            sub_c = Narr.tolist()  # Añadir a la lista
            sub_c = ''.join([''.join(i) for i in sub_c])
            ciphertext.append(sub_c)
        result = ''.join(ciphertext)
    # print(result)
    return result


if __name__ == "__main__":
    print("\n")
    numero1 = input("\033[0;51m"+"Por favor ingrese la palabra a encriptar:")
    print("\n")
    print(grille_encrypt(numero1, [".X..", ".X..", "...X", "X..."]))
    print("\n")
    # Estas "afirmaciones" se utilizan para la autocomprobación y no para una prueba automática
    assert (
        grille_encrypt("cardangrilletest", [".X..", ".X..", "...X", "X..."])
        == "actilangeslrdret"
    )
    assert (
        grille_encrypt(
            "quickbrownfoxjumpsoverthelazydog", ["X...", "...X", "..X.", ".X.."]
        )
        == "qxwkbnjufriumcoopyeerldsatoogvhz"
    )
    assert (
        grille_encrypt(
            "quickbrownfoxjumpsoverthelazydog", [".XX.", ".XX.", "..X.", "X..."]
        )
        == None
    )
    assert grille_encrypt("cardangrilletest", ["...X", "....", "....", "...."]) == None


    print("\033[1;33m" + "Codigo encriptado satisfactoriamente \n" + '\033[0;m')
    print("\033[2;35m" + "Ahora largate hijo , que me estorbas")

