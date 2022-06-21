"""
Test correspondientes a 'ejercicio06.py'
"""
################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#!/usr/bin/python
import sys
import pytest

from src.ejercicio06 import codificar, decodificar

# testing: codificar()
def test_codificar():
    """
    Test que evalúa la correcta codificación de un texto, rotándolo 13 posiciones.
    """
    texto = "09azAZ"
    posiciones = 13
    resultado = codificar(texto, posiciones)
    assert resultado == "09nmNM", "El resultado no es el esperado."

def test_decodificar():
    """
    Test que evalúa la correcta decodificación de un texto, rotándolo 13 posiciones.
    """
    texto = "09nmNM"
    posiciones = 13
    resultado = decodificar(texto, posiciones)
    assert resultado == "09azAZ", "El resultado no es el esperado."

if __name__ == "__main__":
    sys.path.append("src")
    sys.exit(pytest.main())
