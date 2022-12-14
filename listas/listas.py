import random

tam=int(input(" cuantos numeros"))
vector=[]

for i in range(tam):
    vector.append(round(random.random()*100))

print(vector)
print(vector.__len__())
par=0
impar=0
sumpar=0
sumaimpa=0
propar=0
proimpa=0
for i in range(tam):
    #print("posicion" ,i, "elemento",vector[i])
    if vector[i]%2==0:
        print(vector[i], "es par")
        sumpar+=vector[i]
        par+=1
        propar=sumpar//tam
    else:
        print(vector[i], "es impar")
        sumaimpa+=vector[i]
        impar+=1
        proimpa=sumaimpa//tam
print("pares"  ,par,  "impares" ,impar)
print("la suma de los pares es",sumpar, "la suma de los impares es", sumaimpa)
print(" el promedio de los pares es", propar, "el promedio de los impares es", proimpa)

