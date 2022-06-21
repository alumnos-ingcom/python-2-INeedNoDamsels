################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
5. Corchetes balanceados
"""
def balanceados(cadena, abiertos, cerrados):
    """
    Función que determina el estado de la cadena recibida.
    """
    cantidad_abiertos = cantidad_cerrados = 0

    for i in cadena:
        if i in abiertos:
            cantidad_abiertos += 1
        elif i in cerrados:
            cantidad_cerrados += 1

    if cantidad_abiertos == cantidad_cerrados:
        reemplazo = cadena.replace("[]", "").replace("()", "").replace("{}", "").replace("<>", "")
        if len(reemplazo) != 0:
            for _ in range(len(reemplazo)):
                if (reemplazo[0] in abiertos) and (reemplazo[-1] in cerrados): # todo bien hasta que el usuario introduce algo como "[}{]" :(
                    valor_verdad = True
                else:
                    valor_verdad = False
        else:
            valor_verdad = True
    else:
        valor_verdad = False

    return valor_verdad

def principal():
    """
     Función que solicita el ingreso de una cadena de corchetes (o llaves, paréntesis, etc)
    y retorna un valor de verdad indicando su estado.
    """
    abiertos = ["[", "{", "(", "<"]
    cerrados = ["]", "}", ")", ">"]
    todo_ok  = True
    cadena   = input(" >> Ingrese una cadena de corchetes: ")
    while todo_ok is True:
        for i in cadena:
            if (not i in abiertos) and (not i in cerrados):
                print("No era tan complicado...\n")
                todo_ok = False

        if todo_ok is True:
            valor_verdad = balanceados(cadena, abiertos, cerrados)
            print(f"¿La cadena está balanceada...? ¡{valor_verdad}!")
            break
        else:
            principal()

if __name__ == "__main__":
    principal()
