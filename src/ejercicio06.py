################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
6. El cifrado de Cesar
"""
import sys

class Error(Exception):
    """ Clase base para excepciones. """

class CaracterDeTipoIncorrecto(Error):
    """ Salta cuando se ingresa un caracter que no sea de tipo a-z, A-Z o 0-9 """

class ValorFueraDeRango(Error):
    """ Salta cuando se ingresa un valor fuera del rango permitido. """

def codificar(texto, posiciones):
    """ Función que codifica el texto recibido. """
    texto_codificado = ""

    for i in texto:
        valor = ord(i) + posiciones

        try:
            if 48 <= ord(i) <= 57:    # 0-9
                if valor > 57:
                    valor -= posiciones
            elif 65 <= ord(i) <= 90:  # A-B
                if valor > 90:
                    valor -= 26
            elif 97 <= ord(i) <= 122: # a-b
                if valor > 122:
                    valor -= 26
            else:
                raise CaracterDeTipoIncorrecto
        except CaracterDeTipoIncorrecto:
            sys.exit()

        texto_codificado += chr(valor)

    return texto_codificado

def decodificar(texto, posiciones):
    """ Función que decodifica el texto recibido. """
    texto_decodificado = ""

    for j in texto:
        valor = ord(j) - posiciones
        try:
            if 48 <= ord(j) <= 57:    # 0-9
                if valor < 48:
                    valor += posiciones
            elif 65 <= ord(j) <= 90:  # A-B
                if valor < 65:
                    valor += 26
            elif 97 <= ord(j) <= 122: # a-b
                if valor < 97:
                    valor += 26
            else:
                raise CaracterDeTipoIncorrecto
        except CaracterDeTipoIncorrecto:
            sys.exit()

        texto_decodificado += chr(valor)

    return texto_decodificado

def principal():
    """
     Función que solicita el ingreso de un texto
    y lo codifica o decodifica rotando cada caracter una cantidad de posiciones ajustable.
    """
    print("     El cifrado de César\n<1> Codificar <2> Decodificar")
    try:
        opcion = int(input(" >> "))
        if not 0 < opcion < 3:
            raise ValorFueraDeRango
    except ValorFueraDeRango:
        print("    ^ Error: opción inválida.")
        sys.exit()

    texto_original = input(" >> Ingrese el texto: ")
    posiciones = int(input(" >> Ingrese el número de rotaciones: "))
    if opcion == 1:
        texto_final = codificar(texto_original, posiciones)
    else:
        texto_final = decodificar(texto_original, posiciones)

    print(f"\n'{texto_original}' -> '{texto_final}'")

if __name__ == "__main__":
    principal()
