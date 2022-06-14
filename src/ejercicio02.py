################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Estadísticas
"""
def max_y_min(secuencia):
    """
    Función que determina los valores máximos, minimos y el promedio de una secuencia de números.
    """
    i = total = 0
    primera_vez = True

    while i != len(secuencia):
        total += secuencia[i]

        if primera_vez is True:
            minimo = maximo = secuencia[i]
            primera_vez = False
        if secuencia[i] > maximo:
            maximo = secuencia[i]
        elif secuencia[i] < minimo:
            minimo = secuencia[i]

        i += 1

    promedio = total / len(secuencia)

    return (maximo, minimo, promedio)

def principal():
    """
    Función que solicita el ingreso de una secuencia de números hasta el ingreso de 0 (cero).
    """
    numero, secuencia = 1, []

    print("Ingrese una secuencia de números (<0> para salir): ")
    while numero != 0:
        numero = float(input(" >> "))
        if numero != 0:
            secuencia.append(numero)

    assert len(secuencia) > 0, "¡No se ha ingresado ningun número!"

    maximo, minimo, promedio = max_y_min(secuencia)
    print(f"Máximo: {maximo}, mínimo: {minimo}\nPromedio: {promedio}")

if __name__ == "__main__":
    principal()
