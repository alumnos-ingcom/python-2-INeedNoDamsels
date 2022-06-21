################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
1. Pares e impares
"""

def paridad(numero):
    """
    Función que determina la paridad de un número entero.
    """
    numero = abs(numero)
    repeticiones = int(numero / 2)

    for _ in range(repeticiones):
        numero -= 2

    return bool(numero == 0)

def principal():
    """
    Función que solicita el ingreso de un número entero y determina su paridad.
    """
    numero = int(input(" >> Ingrese un número entero: "))
    valor_verdad = paridad(numero)

    print(f"¿{numero} es par...? ¡{valor_verdad}!")

if __name__ == "__main__":
    principal()
