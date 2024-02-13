import random
# ============
# Ordenamiento
# ============
#Ordenamiento de números (Selección)
numeros = [23, 44, 13, 76,100, 23, 213, 45, 71, 32, 76, 34, 204, 2]

def Selection(arr):
    for i in range(0,len(arr)):    
        sm = i
        for x in range(i+1,len(arr)) :
            if arr[x] < arr[sm] :
                sm = x
        if min is not i:
            arr[i], arr[sm]  = arr[sm], arr[i]

Selection(numeros)

print(numeros)

#Ordenamiento de objetos (Inserción)
class Producto():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __repr__(self):
        return (f'Precio: {self.precio}')
    
productos = [Producto("PC", random.randrange(1000,10000)),Producto("Laptop", random.randrange(1000,10000)),
             Producto("Audífonos", random.randrange(1000,10000)),Producto("OwO", random.randrange(1000,10000)),
             Producto("Auto", random.randrange(1000,10000)),Producto("Mouse", random.randrange(1000,10000))]

def OrderObjects(lista):
    for x in range(len(lista)-1,0,-1):
        for i in range(x):
            if lista[i].precio>lista[i+1].precio:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                
OrderObjects(productos)

print(productos) 

#Ordenamiento burbuja
lista = [8, 23, 12, 25, 65, 45, 50, 99, 90, 13, 16, 71, 32, 49, 83, 65, 67, 38, 18, 1021]
def bubble(lista):
    for x in range(len(lista)-1,0,-1):
        for i in range(x):
            print(lista)
            if lista[i]<lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                
bubble(lista)

print(lista) 
# ============
# Búsqueda
# ============

#Búsqueda lineal
letras = ["D", "E", "S", "A", "R", "R", "O", "L", "L", "O", "", "D", "E", "", "S", "O", "F", "T", "W", "A", "R", "E", "", "T", "I"]

def Lineal(arr):
    for i in range(len(arr)):
        if arr[i] == "A" or arr[i]=="E" or arr[i]=="I" or arr[i] == "O" or arr[i]=="U":
            print(f"Vocal en la posición: {i}")
            
Lineal(letras)
#Búsqueda Binaria
nums = [8, 23, 12, 25, 65, 45, 50, 99, 90, 13, 16, 71, 32, 49, 83, 65, 67, 38, 18, 1021]

nums.sort()

def binary(arr, num):
    low = 0
    high=len(arr)
    
    while low<high:
        md = int((low+high)/2)
        if(arr[md]== num):
            return (f'Numero encontrado en la posición {md}')
        elif(arr[md]>num):
            high = md
        else:
            low = md
    return ('No se encontró el numero')
print(nums)
print(binary(nums, 8))
#Aplicación practica
#Una organización requiere un método de consulta eficiente para encontrar los registros de sus trabajadores, para esto se decide almacenarlos en un arreglo por su
#numero de empleado de forma ascendente.

empleados = [1024,1025,1026,1027,1028,1029,1030,1031]

def binary(arr, num):
    low = 0
    high=len(arr)
    
    while low<high:
        md = int((low+high)/2)
        if(arr[md]== num):
            return (f'Empleado encontrado')
        elif(arr[md]>num):
            high = md
        else:
            low = md
    return ('No se encontró al empleado')
print(empleados)
print(binary(empleados, 1025))

#De esta forma se pueden acceder a los registros de cada empleado de forma rápida y eficiente.