#Paso 1
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_atributos(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
#Paso 2
class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, puertas, transmision):
        super().__init__(marca, modelo, año)
        self.puertas = puertas
        self.transmision = transmision

    def mostrar_atributos_auto(self):
        self.mostrar_atributos()
        print(f"Puertas: {self.puertas}")
        print(f"Transmisión: {self.transmision}")


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada, tipo_motor):
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada
        self.tipo_motor = tipo_motor

    def mostrar_atributos_motocicleta(self):
        self.mostrar_atributos()
        print(f"Cilindrada: {self.cilindrada}cc")
        print(f"Tipo de motor: {self.tipo_motor}")
#Paso 3
auto = Auto("Toyota", "Corolla", 2015, 4, "Automática")
auto.mostrar_atributos_auto()

motocicleta = Motocicleta("Honda", "CBR500R", 2020, 500, "4T")
motocicleta.mostrar_atributos_motocicleta()