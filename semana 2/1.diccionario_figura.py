"""
EJERCICIOS DE FIGURAS GEOMÉTRICAS

"""
figuras = {
    3: "Triángulo",
    4: "Cuadrado o Rectángulo",
    5: "Pentágono",
    6: "Hexágono",
    7: "Héptagono",
    8: "Octágono"
}
lados = int(input("Introduce los lados de la figura: "))

figura = figuras.get(lados, "Figura no reconocida")
print(f"La figura con {lados} lados es: {figura}")






