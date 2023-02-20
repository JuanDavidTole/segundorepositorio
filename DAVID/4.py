#cuantas veces se repite un caracter dado

def funcion( ):
    cod=input('ingrese algunos valores')
    letras=[]
    contador=0
    tamano=(len(cod))

    for i in cod:
        if i not in letras:
            letras.append(i)
        elif i in letras:
            contador=contador +1
    tamano2=len(letras)
    print(letras)
    print("el abecedario tiene",tamano,"letras")
    print(" el abecedario sin repetir tiene",tamano2,"letras")
    print('se repiten',contador,'veces ')
    
funcion()