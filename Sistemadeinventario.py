import datetime

class EquipoDeportivo:
    def __init__(self, nombre, precio_costo, precio_venta, cantidad_stock):
        self.nombre = nombre
        self.precio_costo = precio_costo
        self.precio_venta = precio_venta
        self.cantidad_stock = cantidad_stock
        self.fecha_creacion = datetime.date.today()

    def vender(self, cantidad_vendida):
        if cantidad_vendida <= self.cantidad_stock:
            self.cantidad_stock -= cantidad_vendida
            print(f"Se vendieron {cantidad_vendida} unidades de {self.nombre}.")
            print(f"Cantidad original: {self.cantidad_stock + cantidad_vendida}")
            print(f"Cantidad actual: {self.cantidad_stock}")
        else:
            print(f"No hay suficiente stock para vender {cantidad_vendida} unidades de {self.nombre}.")

    def __str__(self):
        return f"Nombre: {self.nombre}\nPrecio de costo: ${self.precio_costo}\nPrecio de venta: ${self.precio_venta}\nCantidad en stock: {self.cantidad_stock}\nFecha de creación: {self.fecha_creacion}"

# Ejemplo de uso
balón_futbol = EquipoDeportivo("Balón de Fútbol", 10, 15, 50)
raqueta_tenis = EquipoDeportivo("Raqueta de Tenis", 30, 50, 20)

print(balón_futbol)

balón_futbol.vender(10)

print(raqueta_tenis)