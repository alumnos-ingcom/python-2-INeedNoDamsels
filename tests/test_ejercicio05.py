"""
Test correspondientes a 'ejercicio05.py'
"""
################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#!/usr/bin/python
import sys
import pytest

from src.ejercicio05 import balanceados

# testing: balanceados()

abiertos  = ["[", "{", "(", "<"]
cerrados  = ["]", "}", ")", ">"]

def test_balanceados_correcto():
    """
    Test que evalúa el balanceo de una cadena cerrada.
    """
    cadena    = "[]{}()<>"
    resultado = balanceados(cadena, abiertos, cerrados)
    assert resultado is True, "El resultado no es el esperado."

def test_balanceados_correcto_complejo():
    """
    Test que evalúa el balanceo de una cadena cerrada más compleja.
    """
    cadena    = "[{<(]>})"
    resultado = balanceados(cadena, abiertos, cerrados)
    assert resultado is True, "El resultado no es el esperado."

def test_balanceados_incorrecto():
    """
    Test que evalúa el balanceo de una cadena abierta o mal cerrada.
    """
    cadena    = "[]}{()<>"
    resultado = balanceados(cadena, abiertos, cerrados)
    assert resultado is False, "El resultado no es el esperado."

if __name__ == "__main__":
    sys.path.append("src")
    sys.exit(pytest.main())
