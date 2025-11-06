class BaseDatos:
    def __init__(self):
        self.datos = {}

    def agregar(self, codigo, raza, edad, huevos):
        if codigo in self.datos:
            print("El código ya existe en la base de datos.")
        else:
            self.datos[codigo] = {
                "raza": raza,
                "edad": edad,
                "huevos": huevos
            }
            print("Animal agregado correctamente.")

    def leer(self):
        if not self.datos:
            print("No hay registros.")
        else:
            for codigo, info in self.datos.items():
                print(f"Código: {codigo}, Raza: {info['raza']}, Edad: {info['edad']}, Huevos: {info['huevos']}")

    def actualizar(self, codigo, raza=None, edad=None, huevos=None):
        if codigo in self.datos:
            if raza:
                self.datos[codigo]['raza'] = raza
            if edad:
                self.datos[codigo]['edad'] = edad
            if huevos:
                self.datos[codigo]['huevos'] = huevos
            print("Registro actualizado.")
        else:
            print("El código no existe.")

    def eliminar(self, codigo):
        if codigo in self.datos:
            del self.datos[codigo]
            print("Registro eliminado.")
        else:
            print("El código no existe.")