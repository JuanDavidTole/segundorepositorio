def funcion():
    lista1=[]
    for i in my_list:
        if i==lista1:
            print('ya se encuentra en la lista')
            if i not in lista1:
                lista1.append(i)
            print(lista1)
my_list=[1,2,3,4,1,2,3,6,7,8]
funcion()