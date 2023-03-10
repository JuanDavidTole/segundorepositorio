# iniciamos  con la identiicacion de las rutas 'absolutas' y las 'relativas' la cuales  se diferncian  es que la abosuta es cuando incia desde desde el disco duro y la relativa cuando inia desde la carpeta 
# se puedne usar estas rutas para entrar a otro documento y poder leerlo y modificalrlo
flujo=open('archivos/inicio.txt','a') # se crea una variable 'flujo' que es igual a open que tiene como parametro la ruta en donde esta el archivo 
#datos=flujo.read()                     # se instacia una variable 'datos' que es igual a la variable flujo se le aregra el .read para que lea  los datos que se encuntran la carpeta archivos 
#print(datos)                           # se imprime la varibale datos con la informacion de la variable flujos 
flujo.write('\nCuando estudian con juicio') #  se agrega flujo.write para agregarle una escritura en la carpeta  a la cual estamos llamando por medio de la ruta 
datos=flujo.read()                          # datos igual a fujo.read  para que nos muestre la nueva informacion que se escribio en la carpeta inicio
print(datos)                            # se imprime la variable datos 
