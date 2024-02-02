import random

class Estudiante():
    def __init__(self, nombre):
        self.nombre = nombre
        self.edad = random.randrange(1,20)
        self.grade = random.randrange(1,10)
    
    def __str__(self):
        return (f'Nombre: {self.nombre}, Edad: {self.edad}, Calificación: {self.grade}')

nombres = ["Juan", "María", "Carlos", "Laura", "Pedro", "Ana", "Luis", "Carmen", "Miguel", "Isabel"]
estudiantes = []

for nombre in nombres:
    estudiantes.append(Estudiante(nombre))

mayor = None
for estudiante in estudiantes:
    if(mayor == None):
        mayor=estudiante
    elif(estudiante.grade > mayor.grade):
        mayor = estudiante

print(mayor)