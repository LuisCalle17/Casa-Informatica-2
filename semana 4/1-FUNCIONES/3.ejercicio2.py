"""
Método que modifica una lista.
Escribe un método que reciba una lista y le agregue un nuevo elemento.

"""
# def agregar_elemento(lista, elemento):
#    lista.append(elemento)
#    return lista

# mi_lista = [1,2,3]
# print(agregar_elemento(mi_lista,200))


    
###########################################################

def agregar_elemento():
   lista = []
   
   while True:
      try:
         numero = int(input("Ingrese número para agregar a la lista: "))
         lista.append(numero)
      except ValueError:
         print("Error: Por favor, ingrese un número válido.")

      continuar = input("Desea seguir agregando números? (S/N): ").lower()
      if continuar == "n":
         break
   
   return lista

lista = agregar_elemento()
print(f"Números de la lista: {lista}")
      
      
   






