"""def funcion(h,j):
    if (len(h)== len(j)):
        return 'son iguales'
    elif (len(h)>= len(j)):
        return 'h es mayor '
    else:
        'son diferentes '
h=(3,2,4)
j=(20000,1)
print(funcion(h,j))"""

def funcion():
    n=int(input('ingrese un numero '))
    for i in range(n):
        if i>=7:
           print  ('pasa el rango')
        else:
             print('no pasa el rango')
funcion()

