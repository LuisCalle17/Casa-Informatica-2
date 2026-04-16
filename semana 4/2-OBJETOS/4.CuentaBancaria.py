# Titular, Saldo
# Agregar métodos de mostrar informacion y crear cuenta

class Persona:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def info(self):
        print(f"Hola {self.titular} su saldo actual es {self.saldo}")

persona1 = Persona("Luis Calle", 5000)

persona1.info()



