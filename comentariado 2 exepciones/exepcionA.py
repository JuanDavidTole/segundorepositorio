try: # el try sirve para que se ejecute la exepcion 
    #print(1/1))  # en el  momento en el que ponga el parentecis de mas  phyton directamente le aviasara con  lo que tiene mal, sin haber ejecutado el codigo 
    raise SyntaxError   #  en esta parte el raise esta haciedo  que se  imprima directamente el error   
except SyntaxError as e:  #  aqui se  asigana una variable 'e' al SyntaxError llegado el caso en  que el error este muy extendido 
    print(e) # en esta parte se imprime el  la variable  de la expecion 
    print('Cierra el parentesis')  # es esta arte se imrpime el  mensjae de la la exepcion  o el erro
    
try:# el try sirve para que se ejecute la exepcion 
    #raise ZeroDivisionError # en esta parte raise esta generando el error de  ZeroDivisionError
    print(1/0)  #aqui se realiza  la diviison  1/0
#except (ZeroDivisionError) as e: 
except ZeroDivisionError as zde: # esta parte se le da  el nombre de una variable al  ZeroDivisionError
    print(zde) # en esta parte se imprime la viarbel del ZeroDivisionError
    #print('prueba error')