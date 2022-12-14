import random
juan=random.randint(10,25)
cont=0
a=2
v=[]
for i in range (juan):
    v.append(round(random.random()*100))
print(v)
print("Cantidad de numeros",len(v))
for i in range(juan):
    for i in range(juan):
        if v[i]%a!=0:
            a=a+1
        elif v[i]==a:
            print(v[i],"es primo")
        else:
            print(v[i],"no es primo")
