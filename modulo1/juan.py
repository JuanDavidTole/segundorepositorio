def insertar(lista):
    n=int(input('ingrese notas de los estudiantes'))
    if n in lista:
        print('ya se encuentra en la lista')
    else:
        lista.append(n)

    print('estas son las notas ingresadas',lista)

def borrar (lista):
    n=input('cuantas notas desea borrar  de la lista ')
    for i in (n):
        valorb=int(input('ingrese la nota que desea borrar'))
        if i not in lista:
            lista.remove(valorb)
    print(lista)
    print('nota eliminada/n')
def suma(lista):
    suma=0
    for x in lista:
        suma=suma+x
        print('la suma de las notas  es:', suma)

