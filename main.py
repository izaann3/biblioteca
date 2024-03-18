#este archivo tiene que estar fuera del directorio pq sera el que llamara a todo
from biblioteca import Libro, Socio, Prestamo

if __name__ == "__main__":
    libro1 = Libro("LOTR", "J. R. R. Tolkien", 2)
    libro2 = Libro("1984", "George Orwell", 20)

    socio1 = Socio("Izan", "Lozano", 101)
    socio2 = Socio("Carlos", "Bonilla", 202)

    libro1.informacion()
    socio1.informacion()
    socio1.solicitar_prestamo(libro1, "2024-03-15")
    libro1.informacion()
    socio1.devolver_prestamo(libro1)
    libro1.informacion()
