"""
Test correspondientes a 'ejercicio02.py'
"""
################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#!/usr/bin/python
import sys
import pytest

from src.ejercicio02 import max_y_min

# testing: max_y_min()
def test_max_y_min_positivos():
    """
     Test que evalúa una secuencia de números positivos
    y determina su máximo, mínimo y promedio de valores.
    """
    secuencia = [1, 5, 2, 4, 3]
    resultado = max_y_min(secuencia)
    assert resultado == (5, 1, 3), "El resultado no es el esperado."

def test_max_y_min_negativos():
    """
     Test que evalúa una secuencia de números negativos
    y determina su máximo, mínimo y promedio de valores.
    """
    secuencia = [-1, -3, -5, -2, -4]
    resultado = max_y_min(secuencia)
    assert resultado == (-1, -5, -3), "El resultado no es el esperado."

def test_max_y_min_ambos():
    """
     Test que evalúa una secuencia de números
    y determina su máximo, mínimo y promedio de valores.
    """
    secuencia = [-2, -1, 0, 1, 2]
    resultado = max_y_min(secuencia)
    assert resultado == (2, -2, 0), "El resultado no es el esperado."

if __name__ == "__main__":
    sys.path.append("src")
    sys.exit(pytest.main())
