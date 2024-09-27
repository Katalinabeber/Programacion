class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_datos(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)

    def mostrar_resultado(self):
        if self.nota >= 6:
            print(f"{self.nombre} ha aprobado con una nota de {self.nota}.")
        else:
            print(f"{self.nombre} no ha aprobado con una nota de {self.nota}.")

# Crear un objeto de la clase Alumno
alumno1 = Alumno("Juan Pérez", 7.5)

# Imprimir los datos del alumno
alumno1.imprimir_datos()

# Mostrar el resultado de la nota
alumno1.mostrar_resultado()   
