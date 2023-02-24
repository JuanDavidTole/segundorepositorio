# ValueError: se produce cuando se llama a una función con un argumento que tiene un valor inapropiado.
#ejercicio adicional 
def ErrordeValor():
    try:
        n=int(input('ingresa tu edad'))
    except ValueError:
        print('No has ingresado un numero, por favor ingrese su edad en numeros')
    else:
        if n>=18:
            print('mayor de edad ')
        elif n<=18:
            print('menor de edad')


ErrordeValor()