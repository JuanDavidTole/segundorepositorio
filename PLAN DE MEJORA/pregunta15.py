def funcion(numero1,numero2):
    for i in range(1,numero2):
        if(i%numero1==0):
            print(i,'es multiplo de',numero2)
        else:
            print(i,'no es multiplo de',numero2)
funcion(100,10)

#NUMEROS PRIMOS 
def funcion(num1,num2):
    for i in range(-1,num2):
        if(i%num1==1):
            print(i,'es primo de',num2)
        else:
            print(i,' no es primo de',num2)
funcion(2,3) 

#NUMEROS mayor  
def funcion(num1, num2):
    for i in range(num2):
        if(i>=num1):
            print(i,'es mayor que ',num1)
            print(i,'es igual que',num1)
        else:
            print(i,'es menor que ',num1)
funcion(10,15)