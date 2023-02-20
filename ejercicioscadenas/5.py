# Solicite cadena e imprimala en todas las formas posibles en cuanto a mayusculas y minusculas

def inter():
    n=input('ingrese una cadena ')

    print('todas las letras en mayusculas:',n.swapcase())
    print('la primera letra en mayuscula:', n.title())
    print(' reemplaza todas las letras minúsculas con sus equivalentes en mayúsculas:',n.upper())
    print('todas las letras en minusculas:',n.lower())

inter()