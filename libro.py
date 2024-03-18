class Libro:
    def __init__(self, titulo, autor, ejemplares):
        self.titulo = titulo
        self.autor = autor
        self.ejemplares = ejemplares

    def informacion(self):
        print(f"Título: {self.titulo}, autor: {self.autor}, ejemplares disponibles: {self.ejemplares}")

    def prestar(self):
        if self.ejemplares > 0:
            self.ejemplares -= 1
            print(f"Libro prestado: {self.titulo}, autor: {self.autor}")
        else:
            print(f"No tenemos ejemplares de {self.titulo}")
