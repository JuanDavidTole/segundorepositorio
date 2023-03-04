class Aprendiz:                                             # se crea la clase aprendiz 
    def __init__(self,nombre):                              # se crea el constructor cons sus parametros 
        self.__nombre=nombre                                # se define nombre 
        self.__cursos=[]                                    # se define la lista crusos 
    def agregarCurso(self,nombreCurso):                     # se crea una funcion de agregarCursos con el parametro nombreCurso 
        self.__cursos.append(nombreCurso)                   # los nombres de los crusos que se escriban se agregaran a la lsita cursos
    def verCursos(self):                                    # se crea una funcion para ver el contendio de crusos 
        return self.__cursos                                # retorna el contenido de cursos 

class Curso:                                                # se crea la clase cursos 
    def __init__(self,nombreCurso):                         # se crea el constructor llamando el parametro nombreCruso 
        self.__nombreCurso=nombreCurso                      # define nombreCruso 

    def getNombreCurso(self):                               # se crea un metodo de agregacion a los cursos 
        return self.__nombreCurso                           # lo cual ingresara directamente los cursos a la  lista curos 
    
ob=Aprendiz('Miguel')                                       # se crea la variable ob que es igual a la clase aprendiz y se le agrega el nombre de miguel 
c1=Curso('Python Basico')                                   # se crea la variable c1 lo cual es para asigna  el nombre de los curos en este caso grega Python Basico'
c2=Curso('Python Intermedio')                               # se crea la variable c2 lo cual es para asigna  el nombre de los curos en este caso grega 'Python Intermedio
c3=Curso('Java Basico')                                     #se crea la variable c2 lo cual se le asigna  el nombre de los curos en este caso grega 'Python Intermedio

ob.agregarCurso(c1)                                         # el objeto 'ob' se utiliza  para agregar los objetos a la lista cursos con el metodo agregarCurso(c1)
ob.agregarCurso(c2)                                         # el objeto 'ob' se utiliza  para agregar los objetos a la lista cursos con el metodo agregarCurso(c1)    
ob.agregarCurso(c3)                                         # el objeto 'ob' se utiliza  para agregar los objetos a la lista cursos con el metodo agregarCurso(c1)

for curso in ob.verCursos():                                # se utiliza un for para recorrer la lista cursos  e imprimir el metodo verCursos 
    print(curso.getNombreCurso())                           #  se utiliza un print en el cual llamamos la lista de curos e imprimimos el nombre de los cursos agregados 

del ob                                                      # se elimina el objeto ob=aprendiz 
#print(ob)                                                   # se imrpime el obejto ob
print('.....',c1.getNombreCurso())                          # se imprime la variable c1 con el nombre del curso que contiene 

