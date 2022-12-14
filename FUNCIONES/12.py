def numeros(x,y,z):
    if x==y==z:
        return 'todos los numero son iguales'

    elif x==y:
        return 'primer y segundo digito se parecen'

    elif y==z:
        return 'segundo y tercer digito se parecen'

    elif x==z:
        return 'primero y tercer digito son iguales'

    else:
        return 'todos son diferentes'

print(numeros(1,20,20))