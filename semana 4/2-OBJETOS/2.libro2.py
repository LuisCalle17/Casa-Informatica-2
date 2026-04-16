
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def actualizar_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo
        print(f"El nuevo titulo es: {nuevo_titulo}")

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
        
libro1.actualizar_titulo("Tierra de hombres")










