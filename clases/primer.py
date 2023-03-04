class persona:                                                              # se crea la clase persona  
    def __init__(self,nombre,documento):                                    # se crea una funcion con el contructor y sus parametros ('metodo'self,nombre,documento
        self.__nombre=nombre                                                # se define el atributo  nombre  relacionado con el parametro de la funcion
        self.__documento=documento                                          # se define el atributo documento relacionado con el parametro de la funcion
        #print('Constructor Activado')

    def getNombre(self):                                                    #se define el metodo getNombre
        return self.__nombre                                                #retorna el metodo nombre 

    def setNombre(self,nombre):                                             # se fija el nombre con setNombre
        self.__nombre=nombre                                                # en esta parte se guarda y se define el nombre relacionado con el parametro nombre 
    def getdocumento(self):                                                 # se define el metodo  getdocumento
        return self.__documento                                             # returna el docuemnto 
    def setdocumento(self,documento):                                       # en esta parte se fija el documento 
        self.__documento=documento                                          # en esta parte se guarda y se define el documento relacionado con el parametro documento  


class Aprendiz(persona):                                                    # se crea la clase aprendiz llamando a la clase madre (persona)
    def __init__(self,nombre,documento,ficha):                              #se crea una funcion con el constructor llamando los parametros de la clase madre (self,nombre,documento)
        persona.__init__(self,nombre,documento)                             # se relacionan los parametros o metodos con el contructor con la clase madre 
        self.__ficha=ficha                                                    #se relaciona el atributo con el parametro ficha 
    def getFicha(self):                                                     # se realiza una funcion definiendo getFicha
        return self.__ficha                                                 # devuelve el atributo ficha y lo imprime incluso si se ecnutra privado 
    def completo(self):                                                       # se crea una funcion para imprimir  la informacion de la clase madre y la clase aprendiz   
        print('nombre',apre.getNombre())                                    # se imprime el nombre llamando a apre.getNombre lo cual el puso aprendiz para que la informacion agregada entre donde corresponde 
        print('documento',apre.getdocumento())                              # se imprime el documento apre.getdocumento() lo cual apre es donde se definio y se le agrego el docuemento 
        print('ficha',apre.getFicha())                                      # se imprime el numero de ficha  apre.getFicha lo cual apre se definio y se le agrego el numero de ficha   
        return " "


apre=Aprendiz('juancho',1023366557,2560664)                                  #el obejto apre lo cual se le da igual a aprendiz, para que la informacion que le doy se guarde en nombre,docuemnto y ficha 
print(apre.completo())                                                      # se imprime la funcion completo en donde esta toda la informacion agregada anterior mente 

print(apre.completo())
