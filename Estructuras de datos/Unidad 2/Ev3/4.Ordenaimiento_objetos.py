class Producto():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    #Returns a printable representation of the object
    def __repr__(self):
        return (f'Nombre: {self.nombre}, Precio: {self.precio}')

inventario = []  
productos = ["Computadora", "Teléfono", "Tableta", "Televisor", "Refrigerador", "Microondas", "Lavadora", "Secadora", "Cafetera", "Licuadora"]
precios = [100.50, 55.25, 299.99, 799.00, 1499.99, 79.99, 399.50, 899.75, 29.99, 49.99]

for x, prod in enumerate(productos):
    inventario.append(Producto(prod,precios[x]))

inventario.sort(key=lambda prod: prod.precio)

print(inventario)