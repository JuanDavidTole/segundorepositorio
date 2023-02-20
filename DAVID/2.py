# Pida una cadena por teclado y diga cual es su valor al sumar sus codigos
def cod():
    numeros=[]
    sum=0
    cod=input('digite las letras a sumar ')
    for i in cod:
        val= ord(i)
        numeros.append(val)
    for x in numeros:
        sum+= x

    print(numeros)
    print(sum)

cod()