num = int(input(" ingrese un numero"))

if num  >=0 and num <=9:
    print(" el numero contiene una cifra")

if num  >=10 and num  <=99:
    print(" el numero contiene dos cifras")
if num >=100 and num <=999: 
        print(" el numero contien tres cifras")
if num >=1000 and  num <=9999:
            print("el numero contiene cuatro cifras")
else:
    print("el numero es invalido")