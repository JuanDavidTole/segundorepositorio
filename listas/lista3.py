import random
j=[]
suma=0
sumpar=0
par=0
imparsuma=0
impar=0
nah=random.randint(10,25)
for i in range (nah):
    j.append(round(random.random()*100))
    if j[i]%2==0:
        print("es par",j[i])
        sumpar+=j[i]
        par+=1
        promepar=sumpar//nah
    else: 
        print(j[i], "es impar")
        imparsuma+=j[i]
        impar+=1 
        imparprome=imparsuma//nah
print("cuantos numeros hay",j.__len__())
print("la suma de par es",sumpar)
print("la suma de impares es",imparsuma,"y el promedio es",imparprome)