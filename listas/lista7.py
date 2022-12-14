import random
lista=[]
suma=0
ordenado=[]
cont=0
rango=random.randint(10,25)
for i in range(rango):
    lista.append(round(random.random()*100))
    suma+=lista[i]
    promedio=suma//rango
    
print("promedio",promedio)
print("lista",lista)
print("la suma de los numero es:",suma)
print("cantidad de numero",lista.__len__())