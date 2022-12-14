import random

lista=[]
ordenado=[]
cont=0
rango=random.randint(10,25)
for i in range(rango):
    lista.append(round(random.random()*100))
    cont=0
    for j in lista:
        if lista[i]==j:
            cont+=1
    if cont!=0:
        ordenado.append(cont)
    else:
        ordenado.append(0)

mayor=0
pos=0
for i in range(lista.__len__()):
    if mayor<ordenado[i]:
       mayor=ordenado[i]
print('El mayor es ',mayor)
for j in range(len(ordenado)):
    if mayor==ordenado[j]:
        print('la moda es ',lista[j])

print(lista)
print("cantidad de numeros",lista.__len__())