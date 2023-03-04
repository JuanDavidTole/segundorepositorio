class Curso:                                            # se crea la clase curso 
    def __init__(self,titulo):                          # se crea el contructor con el parametro titulo
        self.__titulo=titulo                            # se define el titulo 

    def getTitulo(self):                               # se crea un metodo llamadol getTitulo
        return self.__titulo                            # retorna el titulo  del curos 

class Aprendiz:                                         # se crea la clase aprendiz 
    def __init__(self,nombre):                          # se crea el contructor con el parametro nombre 
        self.__nombre=nombre                            # se define el nombre
        self.__cursos=[]                                # se defie una lista llamda curos 

    def agregarCurso(self,nombreCursito):               # se crea un metodo llamado agregarCrusos con el parametro nombreCrusito 
        cursito=Curso(nombreCursito)                    #  se define nombreCrusito 
        self.__cursos.append(cursito)                   # crusito se agrega a la lista cursos

    def getCursos(self):                                # se crea un metodo getCrusos   
        return self.__cursos                            # retorna los cursos que se encuentran en la lista 
    
ap=Aprendiz('Sofia')                                     # se crea una variable ap=Aprendiz lo cual se le asigna un nombre 
ap.agregarCurso('Python Basico')                         # se utliza la variabale para aregegar 'ap' y se le agrega a nombre curos 'Phyton Basico'
ap.agregarCurso('Python Intermedio')                      # se utliza la variabale para aregegar 'ap' y se le agrega a nombre curos 'Phyton Intermedio'  

for c in ap.getCursos():                                # se implementa un for  para qur recorra  el metodo ap.getCuros 
    print(c.getTitulo())                                # e imprima el titulo de los cursos que se encuentran en la lista crusos 

del ap                                                  # re borra la variable ap osea el aprendiz 