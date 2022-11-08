numero=int(input("ingrese su numero:"))
if numero > 1:
    cont=0
    for i in range (2,numero):
        resto=numero%i
        if resto==0:
            cont=+1
    if cont==0:
        print("el numero es primo:", numero)
    else:
        print("no es un numero primo:", numero)
else:
    print("no es un numero primo:", numero)