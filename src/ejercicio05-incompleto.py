################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
5. Corchetes balanceados
"""
def balanceados(cadena):
    """
    """
    valor_verdad = False

    while
    for j in range(len(cadena)):
        if (cadena[j] == "[") and (cadena[j - 1] == "]"):

    return valor_verdad

def principal():
    """
    """
    todo_ok = True
    cadena = input(" >> Ingrese una cadena de corchetes: ")
    while todo_ok is True:
        for i in cadena:
            if (i != "[") and (i != "]"):
                print("No era tan complicado...\n")
                todo_ok = False

        if todo_ok is True:
            valor_verdad = balanceados(cadena)
            print(f"¿La cadena está balanceada...? ¡{valor_verdad}!")
            break
        else:
            principal()

if __name__ == "__main__":
    principal()
