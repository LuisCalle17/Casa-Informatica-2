"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
Física, Química, Historia y Lengua) en una lista.
Pregunte al usuario la nota que ha sacado en cada asignatura, y después 
las muestre por pantalla con el mensaje
En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas
de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

"""

cursos = ["Matematica", "Fisica", "Quimica", "Historia", "Lengua"]

notas = []

for i in cursos:
    nota = int(input(f"Ingrese la nota que saco en el curso de '{i}': "))
    notas.append(nota)
    
for i in range(len(cursos)):
    print(f"En {cursos[i]} has sacado {notas[i]}")


