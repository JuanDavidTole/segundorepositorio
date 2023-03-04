class product:
    def __init__(self,nombre,precio):
        self.__nombre=nombre
        self.__precio=precio
    def getnom(self):
        return self.__nombre
    def getpre(self):
        return self.__precio
    def nom(self,nombre):
        self.__nombre=nombre
    def pre(self,precio):
        self.__precio=precio
class presupuesto(product):
    def __init__(self, nombre, precio, iv,cont):
        self.__iv=iv
        product.__init__(self,nombre,precio,cont)
    def getiv(self):
        return self.__iv
    def iva(self):
        print("Precio con IVA:",ob.getpre()*ob.getiv())
        return ""
    def tod(self):
            print("Nombre del producto:",ob.getnom())
            print("Precio del producto:",ob.getpre())
            print("Iva convertido en decimal:",ob.getiv())
            print(ob.iva())
            print(ob.tot())
            return ""
ob=presupuesto('andres',1500,0.19)
print(ob.tod())