"""
4.  Contar números pares e impares en un array
Haz un programa que cuente cuántos números pares e impares hay en una lista.

"""
# Utilizando for
numeros = [1, 2, 3, 4, 5, 6, 8, 10]

pares = 0
impares = 0

for i in numeros:
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Hay {pares} números pares.")
print(f"Hay {impares} números impares.")

#==========================================================================
# Utilizando while
numeros = [1, 2, 3, 4, 5, 6, 8, 10, 7, 11, 20]

pares = 0
impares = 0
i = 0

while i < len(numeros):
    if numeros[i] % 2 == 0:
        pares += 1
    else:
        impares += 1
    i += 1

print(f"Hay {pares} números pares.")
print(f"Hay {impares} números impares.")



