
class Animal:
    def __init__(self, codigo, raza, edad, huevos_semanales):
        self.codigo = codigo
        self.raza = raza
        self.edad = edad
        self.huevos_semanales = huevos_semanales

    def mostrar_info(self):
        print("-----------------------------------------")
        print(f"Código del Animal: {self.codigo}")
        print(f"Raza: {self.raza}")
        print(f"Edad (meses): {self.edad}")
        print(f"Producción semanal: {self.huevos_semanales} huevos")
