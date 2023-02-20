#Detetrminar que tipo de palabra es: aguda, grave, esdrujula sobre esdrujula

def muci():
  texto=input('Escriba su palabra o frase: ').lower()
  codigo=['m','u','r','c','i','e','l','a','g','o'] #es una lista
  print("murcielago")
  print("0123456789")
  salida=''
  for i in range(len(texto)):
    if texto[i] in codigo:
      salida+=str(codigo.index(texto[i]))
    else:
      salida+=texto[i]
  print(salida)
muci()