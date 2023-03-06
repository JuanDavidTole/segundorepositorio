class pedido:
    def __init__(self,dusuario, titulomaterial,codigomaterial):
        self.__dusuario=dusuario
        self.titulomaterial=titulomaterial
        self.__codigomaterial=codigomaterial
        self.__fecha_salida=[]
        self.__fecha_entrega=[]
    def getIDusuario(self):
        return self.__dusuario
    def getitulomaterial(self):
        return self.titulomaterial
    def getcodigomaterial(self):
        return self.__codigomaterial

    def agregarfechas(self,fechasali,fechaentreg):
        self.__fecha_salida.append(fechasali)
        self.__fecha_entrega.append(fechaentreg)
        return self.__fecha_salida,self.__fecha_entrega

class lector:
    def __init__(self,nombre,direccion,telefono):
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono
        self.__fecha_inimateria=[]
        self.__fec__salimaterial=[]
    def getnombre(self):    #problema
        return self.__nombre
    def getdireccion(self):
        return self.__direccion
    def gettelefono(self):
        return self.__telefono

    def agregarfechasmate(self,fechasalimate,fechaentregamate):
        self.__fecha_inimateria.append(fechasalimate)
        self.__fec__salimaterial.append(fechaentregamate)
        return self.__fecha_inimateria,self.__fec__salimaterial

class estudiante(lector):
    def __init__(self, nombre, direccion, telefono,codestudiante):
        lector.__init__(self,nombre, direccion, telefono)
        self.__codestudiante=codestudiante
    def getcodestudiante(self):
        return self.__codestudiante


class docente(lector):
    def __init__(self, nombre, direccion, telefono,codedocente):
        lector.__init__(self,nombre, direccion, telefono)
        self.__codedocente=codedocente
    def getcodedocente(self):
        return self.__codedocente

class bibliotecario(pedido):
    def __init__(self,IDusuario, titulomaterial,codigomaterial,ipersonal):
        pedido.__init__(self,IDusuario, titulomaterial, codigomaterial)
        self.__ipersonal=ipersonal
    def idbiliotecario(self):
        return self.__ipersonal


class materiales:
    def __init__(self):
        pass

class libro(materiales):
    def __init__(self,titulibro,tiplibro,autor,editorial):
        materiales.__init__(self)
        self.__titulibro=titulibro
        self.tiplibro=tiplibro
        self.autor=autor
        self.editorial=editorial
    def gettitulo(self):
        return self.__titulibro 
    def gettiplibro(self):
        return self.tiplibro
    def getautor(self):
        return self.autor
    def geteditorial(self):
        return self.editorial
class revista(materiales):
    def __init__(self,titulorevista,tiporevista):
        materiales.__init__(self)
        self.__titulorevista=titulorevista
        self.tiporevista=tiporevista
    def gettitulorevista(self):
        return self.__titulorevista
    def gettiporevista(self):
        return self.tiporevista
        




test=bibliotecario(1234,'pendejo',3138345430,123456)
print(test.getIDusuario())
print(test.getitulomaterial())
print(test.getcodigomaterial())
print(test.idbiliotecario())


