################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
4. Fibonacci
"""
def fibonacci(termino):
    """
    Función que determina el valor del n-esimo término en la sucesión de fibonacci.
    """
    primero = segundo = 1

    for _ in range(termino - 2):
        numero = primero + segundo
        primero, segundo = segundo, numero

    return numero

def principal():
    """
     Función que solicita el ingreso del n-esimo termino de la sucesión de fibonacci
    y retorna el número correspondiente.
    """
    termino = int(input("Sucesión de fibonacci\n >> Ingrese un n-esimo termino: "))
    assert termino > 2, "El término debe ser positivo y mayor que dos (2)."

    numero = fibonacci(termino)
    print(f"\nEl termino {termino} corresponde al número {numero}")

if __name__ == "__main__":
    principal()
