from .prestamo import Prestamo

class Socio:
    def __init__(self, nombre, apellido, identificador):
        self.nombre = nombre
        self.apellido = apellido
        self.identificador = identificador

    def informacion(self):
        print(f"nombre: {self.nombre}, apellido: {self.apellido}, identificador: {self.identificador}")

    def solicitar_prestamo(self, libro, fecha):
        print(f"Préstamo solicitado por {self.nombre} {self.apellido}, con el número de socio {self.identificador} en el día de préstamo {fecha}")
        prestamo = Prestamo(libro, self, fecha)
        prestamo.registrar_prestamo()

    def devolver_prestamo(self, libro):
        libro.ejemplares += 1
        print(f"Libro devuelto: {libro.titulo}, autor: {libro.autor}")
