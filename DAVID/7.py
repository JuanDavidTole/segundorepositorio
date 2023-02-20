def tiempopa():
    presente=['ra','re','ras','ran','reis','remos']
    while True:
        print('La primera palabra que ingrese es para saber si se encuentra en futuro')

        ingrese=input('ingrese el verbo')
        
        for ingrese in presente:
            if ingrese.endwith(presente):
                print('es una palabra en futuro')
            else:
                print('la palabra no esta en futuro')

tiempopa()
