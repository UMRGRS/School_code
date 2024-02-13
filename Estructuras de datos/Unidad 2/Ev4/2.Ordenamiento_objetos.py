import random

class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __repr__(self):
        return (f'Edad: {self.edad}')
    
nombres = [
    "J.K. Rowling",
    "George Orwell",
    "Jane Austen",
    "Stephen King",
    "Gabriel García Márquez",
    "Haruki Murakami",
    "Agatha Christie",
    "Ernest Hemingway",
    "Tolkien",
    "Leo Tolstoy"
]

personas = []

for i in range(10):
    personas.append(Persona(nombres[i], random.randrange(30,100)))

def ReverseBubble(lista):
    for x in range(len(lista)-1,0,-1):
        for i in range(x):
            if lista[i].edad<lista[i+1].edad:
                lista[i], lista[i+1] = lista[i+1],lista[i]

ReverseBubble(personas)

print(personas)

