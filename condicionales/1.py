Du = input("Ingrese costo de los minutos")
a = float(Du)
b = (a*50)+200
if a <= 3:
    print("costo de llamada: 200")
elif a > 4:
    print(" costo llamada:",b)