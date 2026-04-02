"""
5. Crear una lista con los cuadrados de los números del 1 al 10
Usa un bucle para crear una lista que contenga los cuadrados de los números del 1 al 10.

"""
## Utilizando for
cuadrados = []

for i in range(1, 11):
    cuadrado = i ** 2
    cuadrados.append(cuadrado)

print(f"Lista de cuadrados de 1 al 10: {cuadrados}")

#==========================================================================
## Utilizando while

cuadrados = []
i = 1

while i < 11:
    cuadrado = i ** 2
    cuadrados.append(cuadrado)
    i += 1

print(f"Lista de cuadrados de 1 al 10: {cuadrados}")

