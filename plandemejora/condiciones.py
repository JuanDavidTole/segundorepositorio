#para designar un resultado falso y True para designar un resultado correcto. He aquí un ejemplo de la sintaxis:



"""if  edad >= 18: 
     print("mayor de edad") 
else: 
     print("menor de edad")"""""
     
     
print('cuantos años tienes')
edad=input()
edad=int(edad)

if edad<=17:
    print('eres menor de edad')
    
if edad>=18:
    print('eres mayor de edad')
    
    
    



#•	1 La reducción se aplica si el niño es menor o si la persona tiene 60 .


print('cuantos años tienes')
edad=input()
edad=int(edad)

if edad>=1:
    print('aplica reduccion')
    
if edad<=60:
    print('aplica reduccion')

if edad>61:
    print('no aplica reduccion')
    
    
#•3	Si no apruebas el bachillerato...

print('ingrese su nota')

nota=input
nota=int(nota)

if nota>=5:
    print('paso muy bien')
if nota>4:
    print('ha pasado')
if nota>=3:
    print('paso raspando')
if nota<3:
    print('perdio')

#encuentre en el mismo nivel de indentación que la instrucción for. El programa sigue su curso, el bucle ha terminado. Apliquemos nuestros conocimientos en el ejemplo siguiente:

print("Antes de la instrucción For") 
for i in range(3):                       # Creación del bucle 
  print("  Inicio del cuerpo del bucle") # || Cuerpo 
  print("  i =",i)                       # || 
  print("  Final del cuerpo del bucle")  # \/ 
print("Después de la instrucción For ")

#Intente adivinar la salida que producirá en pantalla este código. No hay ninguna trampa, el índice de bucle i va a empezar a 0 y el último valor que tomará será 2. He aquí el resultado obtenido:

for i in range(3): 
   print(i) 
   if i == 1: 
    print("i vale 1") 
    print("----")

