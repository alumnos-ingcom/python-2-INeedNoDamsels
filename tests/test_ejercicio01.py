"""
Test correspondientes a 'ejercicio01.py'
"""
################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#!/usr/bin/python
import sys
import pytest

from src.ejercicio01 import paridad

# testing: paridad()
def test_paridad_par_positivo():
    """
    Test que evalúa la paridad de un número entero positivo par.
    """
    numero = 2
    resultado = paridad(numero)
    assert resultado is True, "El resultado no es el esperado."

def test_paridad_impar_positivo():
    """
    Test que evalúa la paridad de un número entero positivo impar.
    """
    numero = 3
    resultado = paridad(numero)
    assert resultado is False, "El resultado no es el esperado."

def test_paridad_cero():
    """
    Test que evalúa la paridad del número cero.
    """
    numero = 0
    resultado = paridad(numero)
    assert resultado is True, "El resultado no es el esperado."
    # ¿Qué? El cero cumple todas las condiciones para ser considerado otro número par más...

def test_paridad_par_negativo():
    """
    Test que evalúa la paridad de un número entero negativo par.
    """
    numero = -2
    resultado = paridad(numero)
    assert resultado is True, "El resultado no es el esperado."

def test_paridad_impar_negativo():
    """
    Test que evalúa la paridad de un número entero negativo impar.
    """
    numero = -3
    resultado = paridad(numero)
    assert resultado is False, "El resultado no es el esperado."

if __name__ == "__main__":
    sys.path.append("src")
    sys.exit(pytest.main())
