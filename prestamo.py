class Prestamo:
    def __init__(self, libro, socio, fecha):
        self.libro = libro
        self.socio = socio
        self.fecha = fecha

    def registrar_prestamo(self):
        print(f"Préstamo registrado: Libro {self.libro.titulo}, por el socio {self.socio.nombre}")
        self.libro.prestar()
