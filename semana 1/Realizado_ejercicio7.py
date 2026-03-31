"""
Ejercico 7: Escribe un programa que solicite al usuario un número entero y
determine si es par o impar.

"""   

numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
    
    