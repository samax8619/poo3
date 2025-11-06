# interfaz.py
from clases import Animal, BaseDatos

class Interfaz:
    def __init__(self):
        self.bd = BaseDatos()

    def menu(self):
        while True:
            print("\n--- SISTEMA DE CONTROL DE GRANJA AVÍCOLA ---")
            print("1. Registrar nuevo animal")
            print("2. Ver todos los animales")
            print("3. Actualizar datos de un animal")
            print("4. Eliminar un animal")
            print("5. Registrar producción semanal")
            print("6. Consultar producción de un animal")
            print("7. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                codigo = input("Código del animal: ")
                raza = input("Raza: ")
                edad = int(input("Edad: "))
                nuevo = Animal(codigo, raza, edad)
                self.bd.crear_animal(nuevo)
                print("Animal registrado con éxito.")

            elif opcion == "2":
                print("\nLista de animales:")
                for a in self.bd.leer_animales():
                    print(f"Código: {a.get_codigo()} - Raza: {a.get_raza()} - Edad: {a.get_edad()} años")

            elif opcion == "3":
                codigo = input("Código del animal a actualizar: ")
                raza = input("Nueva raza: ")
                edad = int(input("Nueva edad: "))
                if self.bd.actualizar_animal(codigo, raza, edad):
                    print("Animal actualizado correctamente.")
                else:
                    print("No se encontró el animal.")

            elif opcion == "4":
                codigo = input("Código del animal a eliminar: ")
                if self.bd.eliminar_animal(codigo):
                    print("Animal eliminado.")
                else:
                    print("No se encontró el animal.")

            elif opcion == "5":
                codigo = input("Código del animal: ")
                cantidad = int(input("Cantidad de huevos producidos esta semana: "))
                self.bd.registrar_produccion(codigo, cantidad)
                print("Producción registrada correctamente.")

            elif opcion == "6":
                codigo = input("Código del animal: ")
                produccion = self.bd.consultar_produccion(codigo)
                total = self.bd.produccion_total(codigo)
                print(f"Producción semanal: {produccion}")
                print(f"Producción total acumulada: {total} huevos.")

            elif opcion == "7":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida.")
