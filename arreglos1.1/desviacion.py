import random
from cmath import sqrt



x=[]
sum=0
nah=random.randint(10,25)
for i in range (nah):
    x.append(round(random.random()*100))
    

franco = sum/ len(x)
pinocho = sum((a-franco)**2 
for a in x) / len(x)
desviacion =sqrt(pinocho)
print(x)
print("cantidad de numeros es",x.__len__())
print("desviacion estandar ",desviacion)