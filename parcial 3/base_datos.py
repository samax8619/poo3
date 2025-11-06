
from interfaz_crud import InterfazCRUD
from animal import Animal

class BaseDatos(InterfazCRUD):
    def __init__(self, tamano):
        self.animales = []
        self.tamano = tamano

    def crear_animal(self):
        if len(self.animales) >= self.tamano:
            print("La base de datos está llena, no se pueden agregar más animales.")
            return

        codigo = input("Ingrese el código único del pollo: ")
        raza = input("Ingrese la raza: ")
        edad = int(input("Ingrese la edad (en meses): "))
        huevos = int(input("Ingrese la cantidad de huevos producidos esta semana: "))

        self.animales.append(Animal(codigo, raza, edad, huevos))
        print("Animal agregado correctamente.")

    def leer_animales(self):
        if not self.animales:
            print("No hay registros en la base de datos.")
            return

        print("\n=== LISTADO DE ANIMALES ===")
        for animal in self.animales:
            animal.mostrar_info()

    def actualizar_animal(self):
        codigo = input("Ingrese el código del animal a actualizar: ")
        encontrado = False

        for animal in self.animales:
            if animal.codigo == codigo:
                encontrado = True
                print("Animal encontrado. Actualice los datos:")

                animal.raza = input("Nueva raza: ")
                animal.edad = int(input("Nueva edad (meses): "))
                animal.huevos_semanales = int(input("Nueva producción semanal de huevos: "))

                print("Datos actualizados correctamente.")
                break

        if not encontrado:
            print("No se encontró un animal con ese código.")

    def eliminar_animal(self):
        codigo = input("Ingrese el código del animal a eliminar: ")
        for i, animal in enumerate(self.animales):
            if animal.codigo == codigo:
                del self.animales[i]
                print("Animal eliminado correctamente.")
                return
        print("No se encontró un animal con ese código.")
