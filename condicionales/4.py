from statistics import median_low


num1 = int(input(" ingrese primer numero:"))
num2 = int(input(" ingrese segundo numero:"))
num3 = int (input(" ingrese tercer numero:"))

mayor = max(num1, num2, num3)
medio = (num1, num2, num3) 
menor = min(num1, num2, num3)

print ("el numero es ") 
print (mayor, medio, menor)