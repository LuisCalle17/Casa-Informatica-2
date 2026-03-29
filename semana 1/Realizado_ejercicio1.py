"""
Ejercicio 1: Escribe un programa que solicite al usuario dos números y muestre su
suma, resta, multiplicación, división, división entera y residuo (módulo).

"""
# Solicita números
num1 = float(input("Ingrese el primero número: "))
num2 = float(input("Ingrese el segundo número: "))

# Se realiza las operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 if num2 != 0 else "No se puede dividir entre 0"
div_entera = num1 // num2 if num2 != 0 else "No se puede dividir entre 0"
modulo = num1 % num2 if num2 != 0 else "No se puede dividir entre 0"

print("=== CALCULADORA ===")
print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multiplicación: {num1} x {num2} = {multiplicacion}")
print(f"División: {num1} / {num2} = {division}")
print(f"División entera: {num1} // {num2} = {div_entera}")
print(f"Residuo: {num1} % {num2} = {modulo}")













