class Vehiculo:                                                     # se crea la clase vehiculo
    def __init__(self,tipo):                                        # con el contructor se  se ingresa el parametro  tipo a la clase 
        self.tipo=tipo                                              #se define el atribibuto
    def descripcion(self):                                           # se hace una funcion  descripcion para imprimir el tipo 
        print('Soy generico no tengo descripcion',self.tipo)        # se imprime un texto y se le añade el tipo 
#v=Vehiculo('Cualquier tipo')

    def getTipo(self):                                              # funcion que defiene  getTipo
        return self.tipo                                            # retorna el atributo de tipo
        #return Vehiculo.tipo
    def __str__(self):                                              # define el str 
        return 'Soy objeto de la clase Vehiculo'                    # devuelve el mensaje con ralcion al tipo

class Herramienta:                                                  # se crea una clase herramienta         
    def __init__(self,proposito):                                   # con el constructor se ingresa el parametro proposito el cual pertenece a la clase herramienta 
        self.__proposito=proposito                                  # se define el atribut proposito    
    def getProposito(self):                                          # funcion que define a getProposito    
        return self.__proposito                                     #retorna el contenido del atributo proposito 
    def __str__(self):                                              # se define el str  el cual pertenece a la clase herramienta 
        return 'Soy objeto de la clase Herramienta'                 # imprime el mensaje del  str 
class Terrestre(Vehiculo,Herramienta):                              # se crea una clase terrestre pero trayendo las clases madre vehiculo,herramienta 
    def __init__(self,tipo,proposito):                              # se traen los parametros de las clases madres 
        Herramienta.__init__(self,proposito)                        # llama el constructor de la clase herramienta 
        Vehiculo.__init__(self,tipo)                                # llama el constructor de la clase vehiculo  
    def datos(self):                                                # se crea una funcion terrestre la cual petrenece a la clase terrestre 
        print('Tipo: ',super().getTipo())                           # se imprime un texto tipo y se llama la clase  padre gettipo
        print('Tipo: ',super().getProposito())                      # se imrpime un texto y se llama la clase getPropostito 
    # def __str__(self):
    #     return 'Soy objeto de la clase Terrestre'
               
t=Terrestre("terrestre","carga")                                    # se crea una varibale T para darla informacion a las clases 
t.datos()                                                           # se llama la funcion datos 
print(t.__str__())                                                  # se imrpirme la variable t imprimiendo el primer str que encuentre en las clases
