
from abc import ABC, abstractmethod

class InterfazCRUD(ABC):
    @abstractmethod
    def crear_animal(self):
        pass

    @abstractmethod
    def leer_animales(self):
        pass

    @abstractmethod
    def actualizar_animal(self):
        pass

    @abstractmethod
    def eliminar_animal(self):
        pass
