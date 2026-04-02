"""
2. Sumar todos los elementos de un array
Crea un programa que tome una lista de números y calcule la suma de todos sus elementos.

"""

numeros = [1, 2, 3, 4, 5, 6]
# usando la funcion max()
print(f"La suma total de los numeros es: {sum(numeros)}")

#==========================================================================
# usando bucle for
numeros = [1, 2, 3, 4, 5, 6]
suma = 0
for i in numeros:
    suma += i

print(f"La suma total de los numeros es: {suma}")

#==========================================================================
# usando bucle while
numeros = [1, 2, 3, 4, 5, 6]
suma = 0
i = 0
while i < len(numeros):
    suma += numeros[i]
    i += 1
print(f"La suma total de los numeros es: {suma}")







