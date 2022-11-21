diccio={'bad buny':{
    'genero':'trap',
    'cancion':'aguacero',
    'duracion':'3:30',
    'cancion2':'no soy celoso',
    'duracion2':'2:15'},

    'los cangris':{
        'genero':'regueton',
        'canci':'yo no soy tu marido',
        'duracion':'2:00',
        'cancio':'donde estan las gatas',
        'duracion':'3:00'},

        'la etnia':{
            'genero': 'rap',
            'cancion':'nocturno',
            'duracion':'4:13',
            'cancion':'mi religion',
            'duracion':'3:51'}
}

print(diccio['bad buny']['cancion'])
print(diccio['bad buny']['duracion'])

#agregar cancion
def cancion(diccio):
    cancion=input('ingrese una cancion')
    diccio.update({cancion:{}})
    return diccio

#agregar info de cancion

def agregar_info_cancion(diccio):
    nuevacancion=input('ingresar nueva cancion')
    if cancion not in diccio:
            print('cancion no esta en lista')
    return diccio
genero=input('ingresar genero')
artista=input('ingresar nombre del artista')
duracion=input('ingresar duracion de la cancion')


print(diccio)

#eliminar cancion

def eliminar_cancion(diccio):
    busqueda=input('cancion que deseas eliminar')
    for i in sorted(diccio.keys()):
        if busqueda==i:
            del diccio [i]
            print('la cancion', busqueda,'se a eliminado')
            return None
    print('la cancion no se ha encontrado')

#buscar artista

def buscando_artista(diccio):
    buscando=input('que artista buscas')
    for e in (diccio.values()):
        if buscando==e['artista']:
            print('el artista',buscando,'se encuentra en la lista ')
            return None
    print('El artista no se encuentra en la lista')

#buscar cacnion
def busca_cancion(diccio):
    busca=input('Que cancion bsucas')
    for i in sorted(diccio.keys()):
        if busca==i:
            print('La cancion',busca,'se encuentra en la lista su duracion es:',diccio[i]['duracion'])
            return None
        print('La cancion no se encuentra en la lista')








