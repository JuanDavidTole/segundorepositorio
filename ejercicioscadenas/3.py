#Cual es el valor numerico de acuerdo a los códigos del alfabeto


def  numerico():
    numeros={}
    cod='asljdblaskjbfkjsbaf'
    for i in cod :
        val=ord(i)
        numeros[i]=val
    print(numeros)
numerico()