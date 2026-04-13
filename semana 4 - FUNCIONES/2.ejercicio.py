"""
Método con un valor de retorno y parámetros opcionales
Escribe un método que reciba una lista de números, y si no se pasa ninguna lista,
utilice una lista por defecto.

El método debe devolver la suma de los números.

"""

def sumar_lista(lista=None):
    if lista is None:
        lista = [1,2,3,4,5]
    return sum(lista)

# con lista predeterminada
print(f"La suma total de lista predeterminada: {sumar_lista()}")  

# con lista personalizada
print(f"La suma total de lista personalizada: {sumar_lista([1,2,3])}")












