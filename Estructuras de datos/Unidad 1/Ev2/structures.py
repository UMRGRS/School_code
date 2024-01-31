#Listas (Se declaran con corchetes, son mutables)
lista = ['Elemento0','Elemento1','Elemento2','Elemento3']

lista.insert(0,"Elemento0Nuevo")

print(lista)
#Tuplas (Se declaran con parentesis)
tupla = (1,2,3)
'''
Las tuplas son inmutables
tupla[0] = 0
    ~~~~~^^^
TypeError: 'tuple' object does not support item assignment
'''
#Diccionarios (Mutables)
Dictionary = {
"Nombre":"Ana",
"Edad": 22,
"Documento": "XA233"
}

Dictionary2 = dict([
    ("Nombre","Ana"),
    ("Edad", 22),
    ("Documento", "XA233")
])

Dictionary3 = dict(Nombre="Ana",
                   edad=22,
                   Documento="XA233")

print(Dictionary)
print(Dictionary2)
print(Dictionary3)
#Conjuntos (Mutables)
group_a1 = set(['Ana','Marcos','Carlos','Mario'])
group_a = {'Ana','Marcos','Carlos','Mario'}
group_b = {'Ana','Pedro','Carlos','Antonio'}
group_c = {'Ana','Antonio','Marcos','Pepe'}

all_students = group_a.union(group_b).union(group_c)

#Estructuras mixtas
grid = [
    [{"x":1,"y":1},{"x":2,"y":3},{"x":3,"y":3}],
    [{"x":1,"y":2},{"x":2,"y":2},{"x":3,"y":2}],
    [{"x":1,"y":1},{"x":2,"y":1},{"x":3,"y":1}],
]
print(grid[1][1])
#Recursividad

def calcular_mcd(a,b):
    if a%b==0 or b%a==0: return b if a>b else a
    
    if a==0: return b
    elif b==0: return a
    else: return calcular_mcd(b,a%b) if a>b else calcular_mcd(a,b%a)
    
print(calcular_mcd(270,192))

