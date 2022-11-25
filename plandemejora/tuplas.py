#El lenguaje Python facilita el retorno de múltiples elementos de una función. Veamos un ejemplo:

def Medio(PuntoA,PuntoB) : 
        xA,yA = PuntoA 
        xB,yB = PuntoB 
        xM = (xA+xB) / 2 
        yM = (yA+yB) / 2 
        return xM,yM 
P1 = (1,1) 
P2 =  3,5 
M = Medio(P1,P2) 
print(M) 

#Las tuplas se declaran simplemente separando con comas los elementos que las componen defina la salida como por ejemplo:

tupla = "primero", "segundo", "tercero", "cuarto", "quinto", "sexto"
print(tupla)

#para agregar un elemento a una tupla deberías  hacerlo como en este ejemplo:

tupla = "primero", "segundo", "tercero", "cuarto", "quinto", "sexto"
tupla.insert('octavo')
print(tupla)

#Para acceder a los elementos de una tupla se hace exactamente igual que con las	 listas	

tupla=("primero", 2, True, "Otro") 
print (tupla[2]) # Mostrará "True" 
print (tupla[1:3]) # Mostrará "(2, True)"

