"""
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, 
y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), 
donde preferente tendrá el valor True si se trata de un cliente preferente.
 
El programa debe preguntar al usuario por una opción del siguiente menú: 

(1) Añadir cliente, 
(2) Eliminar cliente, 
(3) Mostrar cliente, 
(4) Listar todos los clientes, 
(5) Listar clientes preferentes, 
(6) Terminar.
 
En función de la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
Terminar el programa.

"""

clientes = {}

while True:
    print("""
[1] AÑADIR CLIENTE
[2] ELIMINAR CLIENTE
[3] MOSTRAR CLIENTE  
[4] LISTAR TODOS LOS CLIENTES        
[5] LISTAR CLIENTES PREFERENTES         
[6] SALIR
""")
    
    opcion = input("Elige una opción del menú: ")
    if opcion == "1":
        print("== AÑADIR CLIENTE ==")
        dni = input("Ingrese dni: ")
        nombre = input("Ingrese nombre: ")
        direccion = input("Ingrese dirección: ")
        telefono = input("Ingrese teléfono: ")
        correo = input("Ingrese correo: ")
        preferente = input("Ingrese si es preferente (si/no): ").lower()
        
        cliente= {"nombre":nombre, "direccion":direccion, "telefono":telefono, "correo":correo, "preferente":preferente=="si"}
        clientes[dni] = cliente
     
    elif opcion == "2":
        print("== ELMINAR CLIENTE ==")
        dni = input("Ingrese dni del cliente: ")
        if dni in clientes:
            del clientes[dni]
            print("Cliente eliminado")
        else:
            print(f"Cliente con dni '{dni}' no registrado.")
    
    elif opcion == "3":
        print("== MOSTRAR CLIENTE ==")
        dni = input("Ingrese dni del cliente: ")
        if dni in clientes:
            cliente = clientes[dni]
            print(f"{'NOMBRE':<10}{'DIRECCIÓN':<12}{'TELÉFONO':<10}{'CORREO':<20}{'PREFERENTE':<10}")
            print(f"{cliente['nombre']:<10}{cliente['direccion']:<12}{cliente['telefono']:<10}{cliente['correo']:<20}{cliente['preferente']:<5}")
            # for clave,valor in clientes[dni].items():
            #     print(f"{clave} : {valor}")
        else:
            print(f"Cliente con dni '{dni}' no registrado.")
            
    elif opcion == "4":
        if not clientes:
            print("No hay clientes registrados.")
        else:
            print("== LISTA DE CLIENTES ==")
            print(f"{'DNI':<5}{'NOMBRE':<10}{'DIRECCIÓN':<12}{'TELÉFONO':<10}{'CORREO':<20}{'PREFERENTE':<10}")
            for clave,valor in clientes.items():
                print(f"{clave:<5}{valor['nombre']:<10}{valor['direccion']:<12}{valor['telefono']:<10}{valor['correo']:<20}{valor['preferente']:<10}")
            # for clave,valor in clientes.items():
            #     print(f"{clave} : {valor}")
    elif opcion == "5":
        if not clientes:
            print("No hay clientes registrados.")
        else:
            print("== LISTA DE CLIENTES PREFERENTES ==")
            for clave,valor in clientes.items():
                if valor["preferente"]:
                    print(f"DNI: {clave}  |  Nombre: {valor['nombre']}")
            else:
                print("No hay clientes preferentes registrados.")
    
    elif opcion == "6":
        print("Saliendo del programa: Hasta luego!!")
        break
    else:
        print("Opción inválida, vuelva a ingresar una opción válida.")
    
