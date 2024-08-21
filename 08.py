#crear una clase fábrica que tenga los atributos llantas, color y precio; luego crear dos clases
#más que hereden de fábrica para autos y moto,crear objetos para clases
#que muestren la cantidad de llantas color y precio de los vehículos en pantalla.
#Agregar una funcion que determine un descuento del 10% en el precio de llanta mayor a 100.000 pesos

class Fabrica:
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

    def mostrar_info(self):
        print(f"Llantas: {self.llantas}")
        print(f"Color: {self.color}")
        print(f"Precio: {self.precio:.2f}")

    def aplicar_descuento(self):
        if self.precio > 100000:
            self.precio *= 0.9
            print("Se aplicó un descuento del 10%")
        else:
            print("No se aplicó descuento")


class Moto(Fabrica):
    def __init__(self, color, precio):
        super().__init__(2, color, precio)


class Carro(Fabrica):
    def __init__(self, color, precio):
        super().__init__(4, color, precio)


# Crear objetos
moto = Moto("Rojo", 80000)
carro = Carro("Azul", 150000)

# Mostrar información y aplicar descuento
print("Moto:")
moto.mostrar_info()
moto.aplicar_descuento()
moto.mostrar_info()

print("\nCarro:")
carro.mostrar_info()
carro.aplicar_descuento()
carro.mostrar_info()