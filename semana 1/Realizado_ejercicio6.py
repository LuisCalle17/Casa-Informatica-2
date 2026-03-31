"""
Ejercicio 6: Escribe un programa que solicite al usuario tres números y determine
cuál de ellos es el mayor.

"""
num1 = int(input("Ingrese el primero número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 > num2 and num1 > num3:
    print(f"El número '{num1}' es mayor.")
elif num2 > num1 and num2 > num3:
    print(f"El número '{num2}' es mayor.")
elif num1 == num2 and num1 == num3 and num2 == num3: 
    print("Los numero son iguales")
else:
    print(f"El número '{num3}' es mayor.")

##################################################################
# if max(num1, num2, num3) == num1:
#     print(f"El número '{num1}' es mayor.")
# elif max(num1, num2, num3) == num2:
#     print(f"El número '{num2}' es mayor.")
# else:
#     print(f"El número '{num3}' es mayor.")















