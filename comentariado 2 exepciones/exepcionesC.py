def try_syntax(numerator, denominator): # en la funcion se dan dos varibales las cuales son 'numerator, denominator'
    try: # es esencial para que se ejecuten las exepciones 
        print(f'In the try block: {numerator}/{denominator}')  # en esta parte se imprime el los valores que se les dio al numerador y al denominador 
        #quiero ver el resultado de la operacion en el print # para ver el resultado en print se haria de la siguiente manera 
        #print('valores ingresados',numerator,denominator) #la manera
        result = numerator / denominator # en esta parte muestra el resultado de la division  de los valores asignados a  numerador y al denominador utilizando las variables 
    except ZeroDivisionError as zde: # llegado el caso en que la division sea entre cero en esta parte generara esta expecion  ZeroDivisionError ademas de que la exepcion toma el nombre de zde 
        print(zde)  # en esta parte se imprime la variable de  ZeroDivisionError
    else: # si lo ingresado en el programa es valido entrara en el else de lo contario en la exepcion ZeroDivisionError
        print('The result is:', result) # en esta parte se imrpime el resultado de la operacion 
        return result # en esta parte retorna el  resultado 
    finally: # esta parte es para que finalize el programa 
        print('Exiting') # en esta parte sale del progrma 
        #return "Fallo por zero"
#print(try_syntax(12, 4))
print(try_syntax(11, 8)) # en esta parte  se le dan los valores a  numerador y al denominador 