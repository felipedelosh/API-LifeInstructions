import random

class RandomPersonGenerator:
    def __init__(self):
        self.first_name = self.generar_nombre()
        self.middle_name = self.generar_nombre()
        self.last_name = self.generar_apellido()
        self.second_last_name = self.generar_apellido()
        self.age = self.generar_edad()
        self.gender = self.generar_genero()

    def generar_nombre(self):
        nombres = ["Felipe", "Juan", "Carlos", "Andrés", "David", "Jorge", "Ricardo", "Mateo", "Santiago", "Alejandro"]
        return random.choice(nombres)

    def generar_apellido(self):
        apellidos = ["Rodríguez", "Gómez", "López", "González", "García", "Martínez", "Ramírez", "Sánchez", "Hernández", "Díaz"]
        return random.choice(apellidos)

    def generar_edad(self):
        return random.randint(0, 100)

    def generar_genero(self):
        return random.choice(['Masculino', 'Femenino'])

    def __repr__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name} {self.second_last_name}, Edad: {self.age}, Género: {self.gender}"
