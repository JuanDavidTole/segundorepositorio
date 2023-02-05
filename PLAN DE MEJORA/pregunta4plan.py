#Realice una funcion en la cual se añada valores a un diccionario sí no se encuentra en el mismo
def funcion(diccionario,key,value):
    if key not in diccionario.keys():
        diccionario[key] = value
        print(diccionario)
    else:
        print('Ya se encuentra en el diccionario')

dic={'Arsenal':'Ødegaard','Manchester United':'Rashford','Barcelona': 'Dempelé'}
funcion(dic,'Napoli','Kvaratskhelia')


"""
#relacion de los valores 

def funcion (diccionary):
    for i in diccionary.values():
        print(i)
diccionary={'shakira':'waka waka','pique':'casio','clara':'mente'}
funcion(diccionary)


#el resultado seran las llaves 

def funcion (di):
    for i in di.items():
        print (i)
di={'carro':'mercedez','moto':'mt09','avion':'f22'}

funcion(di)
"""