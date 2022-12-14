
#exepciones con  while 
def divisores():
    while True:
        try:
            num=int(input('ingrese numero'))
            for i in range (num+1):
                if num%i==0:
                    print(i,'divisor')
            break
        except ZeroDivisionError:
            print('indeterminado')
        except TypeError:
            print(type(num),'dato no soportado')
        except ValueError:
            print('dato erroneo')

divisores()

print('el programa sigue en linea')


#exepciones

def divisores(num):
    try:
        for i in range (num+1):
            if num%i==0:
                print(i,'divisor')
    except ZeroDivisionError:
            print('indeterminado')
    except TypeError:
            print(type(num),'dato no soportado')
    except ValueError:
            print('dato erroneo')
var=int(input('ingresar numero'))
divisores(var)
print('el programa sigue en linea')




