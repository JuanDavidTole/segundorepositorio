#IndexError: se produce cuando se intenta acceder a un índice que está fuera del rango de una lista, tupla o matriz.
# ejercicio adicional 
def ErrordeIndice():
    lista = [1, 2, 3]
    try:
        print(lista[4])
    except IndexError:
        print("IndexError: Índice fuera de rango")
    else:
        print(' fue el indice encontrado  en la lista',lista)

ErrordeIndice()