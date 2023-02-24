values = (1, 0) # en esta parte se le dan unos valores a la tupla 
#x,y=10,12
#print(divmod(10,3))
try: # esto es exsencial para que se ejecute la exepcion 
    q, r = divmod(*values) # en esta parte se le asignan valores a 'q,r'  los valores que se le asignan son  los de values 
    #print('valor de q=',q)
    print(f'q={q}') # la 'f' se utiliza para que se pueda unir la escritura con los valores que obtienen 'q,r'
    print(f'r={r}')
except (ZeroDivisionError, TypeError) as e: # en esta parte se ejecuta la expecion de  ZeroDivisionError si estan haciendo una division en cero, el   TypeError esta indicando la clase de error que se genero 
    print(type(e), e) # en esta parte se imprime el  ZeroDivisionError y por que el error 