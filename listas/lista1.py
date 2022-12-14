import random

j=[]
juan=[]
nah=random.randint(10,25)
for i in range (nah):
    j.append(round(random.random()*100))
print("lista",j)
print(j.__len__())
cont=0
ja=0
var=0
var2=0
for i in range (nah):
    cont+=1
    ja+=j[i]
    promedio=ja//cont 
print("la suma de los numeros es",ja)
print("el promedio es",promedio)
for a in j:
    if a < promedio:
        print("el numero es menor al promedio",a)
    if a > promedio:
        print("es mayor al promedio",a)
    else:
        print("el numero es igual al promedio",a)


