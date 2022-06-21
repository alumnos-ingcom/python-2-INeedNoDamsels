"""
Test correspondientes a 'ejercicio04.py'
"""
################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#!/usr/bin/python
import sys
import pytest

from src.ejercicio04 import fibonacci

# testing: fibonacci()
def test_fibonacci():
    """
    Test que evalúa el valor del n-ésimo termino de la sucesión infinita de Fibonacci.
    """
    termino = 15
    resultado = fibonacci(termino)
    assert resultado == 610, "El resultado no es el esperado."

if __name__ == "__main__":
    sys.path.append("src")
    sys.exit(pytest.main())
