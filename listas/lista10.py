import random
from cmath import sqrt
j=[]
suma=0
nah=random.randint(10,25)
for i in range (nah):
    j.append(round(random.random()*100))
    

franco = suma / len(j)
pinocho = sum((a-franco)**2 
for a in j) / len(j)
desviacion =sqrt(pinocho)
print(j)
print("cantidad de numeros es",j.__len__())
print("desviacion estandar ",desviacion)
