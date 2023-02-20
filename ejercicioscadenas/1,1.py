#- Cuantas letras del abecedario estan en la cadena, si estan repetidas cuentela solo una vez
def funcion( ):
    abecedario="sjkfdbsdkjbfiqnkjvnca"
    letras=[]
    tamano=(len(abecedario))

    for i in abecedario:
        if i not in letras:
            letras.append(i)
    tamano2=len(letras)
    print("abecedario")
    print(letras)
    print("el abecedario tiene",tamano,"letras")
    print(" el abecedario sin repetir tiene",tamano2,"letras")
    
    
funcion()