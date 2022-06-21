"""
Test correspondientes a 'ejercicio03.py'
"""
################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#!/usr/bin/python
import sys
import pytest

from src.ejercicio03 import superposicion

# testing: superposicion()
def test_superposicion_nula():
    """
     Test que evalúa el grado de superposición entre dos cadenas de caracteres vacías
    e indica el inicio de la misma.
    """
    lista_a = ""
    lista_b = ""
    resultado = superposicion(lista_a, lista_b)
    assert resultado == (0, 0), "El resultado no es el esperado."

def test_superposicion_parcial():
    """
     Test que evalúa el grado de superposición entre dos cadenas de caracteres
    de distintos tamaños e indica el inicio de la misma.
    """
    lista_a = "uno, dos, tres"
    lista_b = "   probando..."
    resultado = superposicion(lista_a, lista_b)
    assert resultado == (9, 4), "El resultado no es el esperado."

def test_superposicion_total():
    """
     Test que evalúa el grado de superposición entre dos cadenas de caracteres
    de igual tamaño e indica el inicio de la misma.
    """
    lista_a = "hola"
    lista_b = "chau"
    resultado = superposicion(lista_a, lista_b)
    assert resultado == (4, 1), "El resultado no es el esperado."

if __name__ == "__main__":
    sys.path.append("src")
    sys.exit(pytest.main())
