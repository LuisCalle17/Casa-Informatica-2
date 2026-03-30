"""
Ejercico 5: Escribe un programa que tome una calificación numérica de un
estudiante (entre 0 y 100) y le asigne una letra según la siguiente tabla:

- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- Menos de 60: F

"""

calificacion = int(input("Ingrese calificación entre 0 - 100: "))

if calificacion <= 100 and calificacion >= 90:
    print("Calificación: A")
elif calificacion <=89 and calificacion >= 80:
    print("Calificación: B")
elif calificacion <= 79 and calificacion >= 70:
    print("Calificación: C")
elif calificacion <= 69 and calificacion >= 60:
    print("Calificación: C")
elif calificacion < 60:
    print("Calificación: C")
else:
    print("Solo se permite clasificaciones de 0 a 100")

























