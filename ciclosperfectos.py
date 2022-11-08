numero=int(input("ingrese numero"))
i=1
total=0
while(i<numero):
    if numero%i==0:
        total=total+i
    i=i+1


if total==numero:
    print("el numero es perfecto:", numero)
else:
    print("no es perfecto", numero)

     




    