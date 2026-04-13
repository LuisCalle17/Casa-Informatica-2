
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def mostrar_info(self):
        print(f"Titulo: {self.titulo} y el autor es: {self.autor}")

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
        

libro1.mostrar_info()

