#He aquí hay un ejercicio de entrenamiento, intente encontrar los resultados:

L = [4,15,7] 
print(L) 
print(L[2]) 
L[0] += 1 
print(L) 
L[2] += 9 
print(L) 
L.clear() 
print(L)

#Se pueden fusionar los elementos de dos listas para formar una nueva lista

L = [4,15,7] 
M = [1,2] 
R = L + M 
print(L) 
print(M) 
print(R)

#Puede añadir un elemento al final de la lista utilizando la sintaxis: 
#.Del mismo modo, puede eliminar el elemento al final de la lista 
#utilizando el comando L.pop() y eliminar un elemento en una posición determinada usando: L.pop(posicion). He aquí un ejemplo:

L = [4,15,7] 
L.append(8) 
print(L) 
L.insert(1,5) 
print(L) 
L.pop(2) 
print(L) 
L.pop() 
print(L)

#remover un elemento de la lista 
listaA=[1,2,3,4,5 ]
listaA.remove(2)
print(listaA)

#He aquí algunos ejemplos:
L = [ 0, 10, 20, 30, 40, 50, 60, 70, 80 ] 
print(L[0:2]) 
print(L[2:-2]) 
print(L[3:]) 
print(L[:3])
