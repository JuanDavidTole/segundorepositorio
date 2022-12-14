canciones={}
def nombre(canciones):
    for i in (canciones.values()):
        a1=input("busque la cancion")
        if a1 == i:
            print("la cancion ya existe verifique en la opcion 4 :)")
        else:
            print("dato no registrado")
        """for x in canciones.values():
            return x"""

def imprimir():
    print(canciones)


def cantante(canciones):
    artista=input("ingrese el artista: ")
    canciones.update({artista:{}}) 
    return canciones


def cancion(canciones):
    artista1=input("ingrese el artista: ")
    if artista1 not in canciones:
        print('El artista no se encuentra, agreguelo primero')
        return canciones
    cancion=input("Ingrese el nombre del cancion: ")
    genero=input("genero: ")
    duracion=input("cuant dura la cancion: ")
    if artista1 in canciones:
        canciones.update({artista1:{"cancion":cancion,"genero":genero,"duracion":duracion}})

def buscar(canciones):
    buscar=input("que artista desea buscar: ")
    for i in (canciones.keys()):
        if buscar==i:
            print("el artista",buscar,"ya esta en la lista y su genero es",canciones[i]["genero"])
            return None
    print("no existe :)")








while True:
    print('1-buscar cancion')
    print('2-ingresar artista')
    print('3-ingresar cancion')
    print('4-lista')
    print('5-buscar cantante')
    print('6-salir')
    print("7-mas larga")
    print("8-mas corta")
    ctrl=int(input('Ingrese la opcion'))
    match ctrl:
        case 1:
            nombre(canciones)
        case 2:
            cantante(canciones)
        case 3:
            cancion(canciones)
        case 4:
            imprimir()
        case 5:
            buscar(canciones)
        case 6:
            break