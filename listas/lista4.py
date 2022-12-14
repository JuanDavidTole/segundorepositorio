import random
lista=[]
nah=random.randint(10,25)
for i in range (nah):
    lista.append(round(random.random()*100))
print("desorden",lista)
print("canidad de numeros",lista.__len__())

ba=False
ha=False
while ba==False:
    ba=True
    for i in range (len(lista)-1):
        if lista[i]>lista[i+1]:
            h=lista[i]
            lista[i]=lista[i+1]
            lista[i+1]=h
            ba=False

print("orde menor a mayor",lista)

while ha==False:
    ha=True
    for a in range(len(lista)-1):
        if lista[a]<lista[a+1]:
            ju=lista[a]
            lista[a]=lista[a+1]
            lista[a+1]=ju
            ha=False

print("de mayor a menor",lista)
