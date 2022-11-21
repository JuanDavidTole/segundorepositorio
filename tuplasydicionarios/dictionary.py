dict= {'gato':'chat', 'perro':'chien', 'caballo':'cheval'}
#metodo  get
print(dict.get('gato'))
print(dict['perro'])

#eliminar
del dict ['perro']
print(dict)

#agregar nueva clave de valor
dict.update({'pollo': 'chiken'})
dict['pato']='duck'
print(dict)


#eliminar el utlimo del diccionario
dict.popitem()
print(dict)

#devolver tupla por cada valor
for esp, fr in dict.items():
    print(esp,  '->',fr)

#metodo values
for x in dict.values:
    print(x)


anidado={
    'documento':123,
    'nombre':{
        'nombre': 'pablo',
        'apellido':'gomez'

    }
}


