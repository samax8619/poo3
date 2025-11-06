# clases.py

# Clase base tipo interfaz (sin ABC)
class InterfazCRUD:
    def crear_animal(self, animal):
        pass

    def leer_animales(self):
        pass

    def actualizar_animal(self, codigo, nueva_raza, nueva_edad):
        pass

    def eliminar_animal(self, codigo):
        pass


# Clase Animal
class Animal:
    def __init__(self, codigo, raza, edad):
        self.__codigo = codigo
        self.__raza = raza
        self.__edad = edad

    # Getters
    def get_codigo(self):
        return self.__codigo

    def get_raza(self):
        return self.__raza

    def get_edad(self):
        return self.__edad

    # Setters
    def set_raza(self, raza):
        self.__raza = raza

    def set_edad(self, edad):
        self.__edad = edad


# Clase BaseDatos que hereda de InterfazCRUD
class BaseDatos(InterfazCRUD):
    def __init__(self):
        self.__animales = []               # Lista de objetos Animal
        self.__produccion = {}             # Diccionario {codigo: [cantidades]}

    # Implementación de los métodos CRUD
    def crear_animal(self, animal):
        self.__animales.append(animal)
        self.__produccion[animal.get_codigo()] = []

    def leer_animales(self):
        return self.__animales

    def actualizar_animal(self, codigo, nueva_raza, nueva_edad):
        for animal in self.__animales:
            if animal.get_codigo() == codigo:
                animal.set_raza(nueva_raza)
                animal.set_edad(nueva_edad)
                return True
        return False

    def eliminar_animal(self, codigo):
        for animal in self.__animales:
            if animal.get_codigo() == codigo:
                self.__animales.remove(animal)
                del self.__produccion[codigo]
                return True
        return False

    # Métodos extra de producción semanal
    def registrar_produccion(self, codigo, cantidad):
        if codigo in self.__produccion:
            self.__produccion[codigo].append(cantidad)
        else:
            print("El animal no existe en la base de datos.")

    def consultar_produccion(self, codigo):
        if codigo in self.__produccion:
            return self.__produccion[codigo]
        else:
            return []

    def produccion_total(self, codigo):
        if codigo in self.__produccion:
            return sum(self.__produccion[codigo])
        else:
            return 0
