diccio={'badbuny':{
    'genero':'trap',
    'aguacero':' duracion 3:30 ',
    'no soy celoso':' duracion 2:15',},

    'los cangris':{
        'genero':'regueton',
        'yo no soy tu marido':'duracion 2:00',
        'donde estan las gatas':'duracion 3:00',},

        'la etnia':{
            'genero': 'rap',
            'nocturno':'duracion 4:13',
            'mi religion':'duracion 3:51',},
            'nueva lista':{}
}


#buscar artista

def buscandoartista(diccio):
    buscandoartista=input('que artista buscas: ')
    for i in diccio.keys():
        if buscandoartista==i:
            print('esta en la lista',buscandoartista)
            return None
    print('El artista no esta')

print(buscandoartista(diccio))

#buscar cancion
def nombre():
    for i in diccio:
        a1=input('busque el artista')
        if a1 in diccio[i]:
            print('esta en la lista', diccio[i])
        else:
            print('dato no registrdo')
print(a1)
"""def busca_cancion(diccio):
    busca_cancion=input('Que cancion buscas')
    for i in diccio.keys():
        artista=diccio[i]
        for a in artista.values():
            if busca_cancion==a:
                print('La cancion se encuentra en la lista :',busca_cancion)
                return None
    print('La cancion no se encuentra en la lista')
print(busca_cancion(diccio))"""

#agregar cancion
def cancion(diccio):
    cancion=input('ingrese una cancion')
    diccio.update({cancion:{'nuevalista'}})
    return diccio
print(cancion(diccio))






#agregar info de cancion

def agregar_info_cancion(diccio):
    cancion=input('ingresar nueva cancion')
    if cancion not in diccio:
        print('cancion no esta en lista')
        return diccio
    genero=input('ingresar genero')
    artista=input('ingresar nombre del artista')
    duracion=input('ingresar duracion de la cancion')
    if cancion in diccio:
        diccio.update({cancion:{'genero':genero,'artista':artista,'duracion':duracion}})
        return diccio
print(cancion(diccio))


#eliminar cancion

def eliminar_cancion(diccio):
    busqueda=input('cancion que deseas eliminar')
    for i in sorted(diccio.keys()):
        if busqueda==i:
            del diccio [i]
            print('la cancion', busqueda,'se a eliminado')
            return None
    print('la cancion no se ha encontrado')

print(eliminar_cancion(diccio))


while True:
    print('1-buscar cancion')
    print('2-ingresar artista')
    print('3-ingresar cancion')
    print('4-lista')
    print('5-buscar cantante')
    print('6-salir')
    print("7-eliminar")
    print("8-mas corta")

    ctrl=int(input('Ingrese la opcion'))
    match ctrl:
        case 1:
            nombre(diccio)
        case 2:
            cantante(diccio)
        case 3:
            cancion(diccio)
        case 4:
            imprimir()
        case 5:
            buscar(diccio)
        case 6:
            break
        case 7:
            eliminarartista(diccio)
