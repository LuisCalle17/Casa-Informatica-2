# nombre y salario (horas y pago/hora)
# calcular salario

class Salario:
    def __init__(self, nombre, pago_horas, horas):
        self.nombre = nombre
        self.pago_horas = pago_horas
        self.horas = horas
    
    def calcular_salario(self):
        salario = self.pago_horas * self.horas
        return salario
    
    def obtener_horas(self):
        return self.horas


nombre = input("Ingrese su nombre: ")
pago_horas = float(input("Ingrese su pago por horas: "))
horas = int(input("Ingrese horas trabajadas: "))

#Trabajador1
trabajador1 = Salario(nombre, pago_horas, horas)
salario1 = trabajador1.calcular_salario()
print(f"El salario de {trabajador1.nombre} es de S/{salario1:.2f}")
horas1 = trabajador1.obtener_horas()
print(f"Cantidad de horas trabajadas de {trabajador1.nombre} son: {horas1}")


#########################################################################################

class Salario:
    def __init__(self, nombre, pago_horas, horas):
        self.nombre = nombre
        self.pago_horas = pago_horas
        self.horas = horas
    
    def solicitar_datos(self):
        nombre = input("Ingrese su nombre: ")
        pago_horas = float(input("Ingrese su pago por horas: "))
        horas = int(input("Ingrese horas trabajadas: "))
        return nombre, pago_horas, horas
    
    def calcular_salario(self):
        salario = self.pago_horas * self.horas
        return salario
    
    def obtener_horas(self):
        return self.horas

print("TRABAJADOR 1")
trabajador1 = Salario("", 0, 0) #como corrigo este error, no me deja crear el objeto sin pasarle los parametros 
datos1 = trabajador1.solicitar_datos()
trabajador1.nombre, trabajador1.pago_horas, trabajador1.horas = datos1
salario1 = trabajador1.calcular_salario()
print(f"El salario de {trabajador1.nombre} es de S/{salario1:.2f}")
horas1 = trabajador1.obtener_horas()
print(f"Cantidad de horas trabajadas de {trabajador1.nombre} es: {horas1}")

print("\nTRABAJADOR 2")
trabajador2 = Salario("",0 ,0)
datos2 = trabajador2.solicitar_datos()
trabajador2.nombre, trabajador2.pago_horas, trabajador2.horas = datos2
salario2 = trabajador2.calcular_salario()
print(f"El salario de {trabajador2.nombre} es de S/{salario2:.2f}")
horas2 = trabajador2.obtener_horas()
print(f"Cantidad de horas trabajadas de {trabajador2.nombre} es: {horas2}")




























# 1:17
