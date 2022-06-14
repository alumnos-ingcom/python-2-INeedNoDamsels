################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
6. El cifrado de Cesar
"""
def codificar(texto, posiciones):
    """
    Función que codifica el texto recibido.
    """
    texto_codificado = ""
    for i in texto:
        valor = ord(i) + posiciones
        if valor > 90:
            valor -= 26

        texto_codificado += chr(valor)

    return texto_codificado

def decodificar(texto, posiciones):
    """
    Función que decodifica el texto recibido.
    """
    texto_decodificado = ""
    for j in texto:
        valor = ord(j) - posiciones
        if valor < 65:
            valor += 26

        texto_decodificado += chr(valor)

    return texto_decodificado

def principal():
    """
     Función que solicita el ingreso de un texto
    y lo codifica o decodifica rotando cada caracter una cantidad de posiciones ajustable.
    """
    print("<1> Codificar <2> Decodificar")
    opcion = int(input(" >> Ingrese operación: "))
    assert 0 < opcion < 3, "Opción ingresada fuera de rango."

    texto_original = input(" >> Ingrese el texto: ")
    posiciones = int(input(" >> Ingrese el número de rotaciones: "))
    if opcion == 1:
        texto_final = codificar(texto_original, posiciones)
    else:
        texto_final = decodificar(texto_original, posiciones)

    print(f"\n'{texto_original}' -> '{texto_final}'")

if __name__ == "__main__":
    principal()
