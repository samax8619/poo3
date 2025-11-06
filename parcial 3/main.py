
from base_datos import BaseDatos

def main():
    base = BaseDatos(10)

    while True:
        print("\n========= SISTEMA DE CONTROL AVÍCOLA =========")
        print("1. Registrar nuevo pollo")
        print("2. Consultar todos los registros")
        print("3. Actualizar información de un pollo")
        print("4. Eliminar registro de un pollo")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            base.crear_animal()
        elif opcion == "2":
            base.leer_animales()
        elif opcion == "3":
            base.actualizar_animal()
        elif opcion == "4":
            base.eliminar_animal()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()
