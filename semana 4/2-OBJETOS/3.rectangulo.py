
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        area = (self.base * self.altura)
        return area

area1 = Rectangulo(6,10)
print(f"El área del rectángulo es: {area1.area()}")












