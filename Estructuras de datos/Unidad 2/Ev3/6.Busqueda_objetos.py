class Libro():
    def __init__(self, autor, titulo):
        self.titulo = titulo
        self.autor = autor
        
    def __repr__(self):
        return (f'Titulo: {self.titulo}, Autor: {self.autor}')

def Find_book(arr, autor):
    for libro in arr:
        if libro.autor == autor:
            return libro

libros_inv = []
autores = [
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
libros = [
    "Harry Potter y la piedra filosofal",
    "1984 - George Orwell",
    "Orgullo y prejuicio",
    "El resplandor",
    "Cien años de soledad",
    "Tokio Blues - Haruki Murakami",
    "Asesinato en el Orient Express",
    "Adiós a las armas",
    "El señor de los anillos",
    "Guerra y paz"
]

for x, aut in enumerate(autores):
    libros_inv.append(Libro(aut, libros[x]))
    
print(Find_book(libros_inv, "J.K. Rowling"))