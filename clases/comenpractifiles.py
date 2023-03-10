from Aprendiz import *                                                                    # se improta la clase aprendiz 
from Curso import *                                                                        # se importa la clase curso

nombre=input('ingrese nombre del aprendiz')                                          # se instancia  una variable para que se pueda ingresar el nombre de aprendiz 
documento=int(input('ingrese documento del aprendiz'))                               # se instancia uuna variable para que se pueda ingresar docuemnto del aprendiz 
ficha=input('ingrese ficha del aprendiz')                                            # se instancia una variabe para que se pueda ingresar el numero de la ficha 

ap=Aprendiz(ficha,nombre,documento)                                                  # se  instacia un objeto el cual esta asiganado ala clase aprendiz con los parametros ficha, nombre, documento 

nombreCurso=input('ingrese nombre del curso')                                        # se instania la variable nombrecuros para que se pueda ingresar el nombre del curos 
horas=int(input('ingrese intensidad horaria del curso'))                             # se instancia una variable para que se pueda ingresar las  horas del curos 
c1=Curso(nombreCurso,horas)                                                          # se intancia un objeto el cual tiene asignado la clase curos y dos parametros de  nombre curso y horas 
ap.agregarCurso(c1)                                                                  #se utliza el objeto ob  llamando agregarcursos  y se agrega en curosos  

with open('herencia/aprendices.txt','a') as flujo:                                   #  el with boloque el codigo que abre el domcumento peroa demas se le agrega 'as flujo'
     flujo.write(ap.getFicha()+','+ap.getNombre()+','+str(ap.getDocumento())+'\n')       # se utiliza el flujo para que el write escriba en el documento aprendices  los metodos de la clase aprendiz  