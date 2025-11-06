from base_datos import BaseDatos

class Interfaz:
    def __init__(self):
        self.bd = BaseDatos()

    def menu(self):
        while True:
            print("\n--- Menú de la Granja Avícola ---")
            print("1. Agregar animal")
            print("2. Leer registros")
            print("3. Actualizar animal")
            print("4. Eliminar animal")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                codigo = input("Código del animal: ")
                raza = input("Raza: ")
                edad = int(input("Edad: "))
                huevos = int(input("Huevos producidos esta semana: "))
                self.bd.agregar(codigo, raza, edad, huevos)

            elif opcion == "2":
                self.bd.leer()

            elif opcion == "3":
                codigo = input("Código del animal a actualizar: ")
                raza = input("Nueva raza (o Enter para no cambiar): ") or None
                edad = input("Nueva edad (o Enter para no cambiar): ")
                edad = int(edad) if edad else None
                huevos = input("Nueva cantidad de huevos (o Enter para no cambiar): ")
                huevos = int(huevos) if huevos else None
                self.bd.actualizar(codigo, raza, edad, huevos)

            elif opcion == "4":
                codigo = input("Código del animal a eliminar: ")
                self.bd.eliminar(codigo)

            elif opcion == "5":
                print("Saliendo del sistema.")
                break

            else:
                print("Opción inválida, intente nuevamente.")