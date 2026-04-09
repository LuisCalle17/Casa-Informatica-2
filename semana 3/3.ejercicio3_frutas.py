'''
Escribir un programa que guarde en un diccionario los precios 
de las frutas de la tabla, pregunte al usuario por una fruta,
un número de kilos y muestre por pantalla el precio de ese número 
de kilos de fruta. Si la fruta no está en el diccionario debe mostrar
un mensaje informando de ello.

Fruta	Precio
Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70
'''
frutas = {
    "Platano":  1.35,
    "Manzana":  0.80,
    "Pera"   :  0.85,
    "Naranja":  0.70
}

compras = []

while True:
    print("""
Platano:  1.35
Manzana:  0.80
Pera   :  0.85
Naranja:  0.70\n""")
    
    fruta = input("Que fruta desea comprar?: ").title()
    if fruta in frutas:
        cantidad = int(input("Ingrese cuantos kilos desea: "))
        precio = f"{fruta:<10} -   Precio: {frutas[fruta] * cantidad:.2f}"
        compras.append(precio)
    else:
        print("Fruta no disponible.")
    
    continuar = input("Desea seguir comprando? (s/n): ").lower()
    if continuar == "n":
        break

if len(compras) > 0:
    for i in compras:
        print(i)
else:
    print("Lista de compras vacía.")
    




