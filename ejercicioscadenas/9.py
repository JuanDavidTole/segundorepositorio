 #Invente un cifrado de texto tipo murcielago o César. Puede utilizar alguna formula matemática para este fin.

def muci():
  texto=input('Escriba su palabra o frase: ').lower()
  codigo=['c','o','n','f','i','g','u','r','a'] #es una lista
  print("configura")
  print("012345678")
  salida=''
  for i in range(len(texto)):
    if texto[i] in codigo:
      salida+=str(codigo.index(texto[i]))
    else:
      salida+=texto[i]
  print(salida)
muci()