#crear una clase fábrica que tenga los atributos llantas, color y precio; luego crear dos clases
#más que hereden de fábrica para autos y moto,crear objetos para clases
#que muestren la cantidad de llantas color y precio de los vehículos en pantalla.

class Fabrica:
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

    def mostrar_info(self):
        print(f"Llantas: {self.llantas}")
        print(f"Color: {self.color}")
        print(f"Precio: {self.precio}")


class Auto(Fabrica):
    def __init__(self, color, precio):
        super().__init__(4, color, precio)


class Moto(Fabrica):
    def __init__(self, color, precio):
        super().__init__(2, color, precio)


# Crear objetos
auto = Auto("Rojo", 20000)
moto = Moto("Azul", 5000)

# Mostrar información
print("Auto:")
auto.mostrar_info()

print("\nMoto:")
moto.mostrar_info()