from Aprendiz import *                                                                  # se importa la clase aprendiz 
from Curso import *                                                                     # se importa la calse curos 

with open('herencia/aprendices.txt','r') as flujo:                                       # se abre  el archivo herencia en la capeta aprendices  que esta en extto y se crea  la variable flujo para que se puedan pasar los datos 
    datos=flujo.read()                                                                    # se isntacia la variable datos que es igual a flujo.read que nos ayudara a traer lo que se encuentra en la carpeta aprendices 
    print(datos)                                                                        # se imprime lo que se encuentra en la carpeta aprendices 
    #flujo.write('2560664,maria,123')
aprendices=[]                                                                             # se intancia una lista aprendices 
with open('herencia/aprendices.txt','r') as flujo:                                        #se abre nuevamente el archivo herencia en la caperta aprendices se vuelve a instanciar la variable flujos 
    for linea in flujo:                                                                 # se utizala el for para que recorra las lineas  y el flujo es para que las lleve a la carpeta aprendices 
        #print(linea)
        aprendices.append(linea.rsplit())                                               # en esta liena se utiliza el rsplit para que el resultado que nos dio el for lienas  las divida en una lista llena de listas

datosxlinea=[]                                                                            # se instacia una lista datosxliena 
for aprendiz in aprendices:                                                             # se utiliza el for para que aprendiz recorra la lista aprendices 
    datosxlinea.append(aprendiz[0].split(','))                                          # en esta linea se llama  a la lista anteriomente creada   aprendiz la recorre en la posicion  cero  y punto split  separa  esa lista  en comas 

#print(ob.getNombre())

print(datosxlinea)                                                                      # se imprime la lista datosxliena  ya separadas las listas detros de las listas 

listaDeObjetos=[]                                                                       #se  instacia una lista vacia  llamda listaDeObjetos 
for apr in datosxlinea:                                                                 # se utiliza el for para que apr recorra datosxlinea que fue la anerior lista ya separa por comas 
     f=apr[0]                                                                           #se instacnia f en la posicion cero para que nos traiga el  numero  de la ficha que se encuentra   en aprendices.txt
     n=apr[1]                                                                           # se instancia n en la posicion 1 para que traiga el nombre que se encuentra en  aprendices 
     d=apr[2]                                                                           # se  instacia d en la posicion 2 para que nos traiga el docuemnto que se encuentra en aprendices 
     ob=Aprendiz(f,n,d)                                                                 # se instancia el ob en la calse aprendiz  llamando las anteriores variables 
     print(ob)                                                                            # se imprime el ob
     listaDeObjetos.append(ob)                                                            # se agrega el objeto en la lista nombrada lsitaDeObjetos 

for xx in listaDeObjetos:                                                               # se utiliza para que for para que xx recorra la anterior lista 
    print(xx.getNombre())                                                               # con lo que recorrio  xx se imprime el metodo getnombre 
    print(xx.getDocumento())                                                            # con lo que recorrio  xx se imprime el metodo getdocumento
    print(xx.getFicha())                                                                # con lo que recorrio  xx se imprime el metodo getficha 