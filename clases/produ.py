class producto:
    def __init__(self, nombre, precio):
         self.__nombre=nombre
         self.__precio=precio
         
    def getNombre(self):                                                    
            return self.__nombre  
        
    def getprecio(self):                                                 
            return self.__precio
    def nom(self,nombre):
        self.__nombre=nombre 
    def n(self,precio):
        self.__precio=precio                                                                                                                                     
    def calcular(self):        
       iva=self.__precio*0.19  
       return iva                         
            
    def completo(self):                                                        
        print('nombre',pro.getNombre())                                    
        print('precio',pro.getprecio())
        print('iva',pro.calcular())    
        return " "             
pro=producto('diana',1500)      
print(pro.completo())     
