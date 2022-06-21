################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
3. Súper-puestos
"""
def superposicion(lista_a, lista_b):
    """
    Función que determina el grado de superposición además del inicio de la misma.
    """
    grado, inicio, primera_vez = 0, 0, True

    if len(lista_a) == len(lista_b) or len(lista_a) < len(lista_b):
        repeticiones = len(lista_a)
    else:
        repeticiones = len(lista_b)

    for i in range(repeticiones):
        if (lista_a[i] != "") and (lista_a[i] != " "):
            if (lista_b[i] != "") and (lista_b[i] != " "):
                grado += 1

                if primera_vez is True: # si es la 1era vez que se superponen, guarda la posición.
                    inicio, primera_vez = i + 1, False

    return (grado, inicio)

def principal():
    """
    Función que solicita el ingreso de dos listas y devuelve su grado de superposición.
    """
    lista_a = input(" >> Ingrese algo: ")
    lista_b = input(" >> ... algo más: ")

    grado, inicio = superposicion(lista_a, lista_b)
    print(f"\nSuperposición de grado {grado}.", end = "")

    if grado != 0:
        print(f" Iniciada en la posición {inicio}\n\
 (o para los programadores, en la {inicio - 1}).")

if __name__ == "__main__":
    principal()
