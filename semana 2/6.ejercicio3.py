"""
3.  Encontrar el número más grande en un array
Escribe un programa que determine el mayor número en una lista.

"""
## Utilizando la funcion max()
numeros = [5, 10, 6, 1, 8]
print(f"El mayor numero es: {max(numeros)}")

#==========================================================================
## Utilizando bucle for
numeros = [5, 10, 6, 1, 8]
mayor = 0

for i in numeros:
    if mayor < i:
        mayor = i

print(f"El número mayor es: {mayor}")

#==========================================================================
## Utilizando bucle while
numeros = [10, 8, 20, 87, 5]
mayor = numeros[0]
i = 0

while i < len(numeros):
    if numeros[i] > mayor:
        mayor = numeros[i]    
    i += 1
        
print(f"El número mayor es: {mayor}")
