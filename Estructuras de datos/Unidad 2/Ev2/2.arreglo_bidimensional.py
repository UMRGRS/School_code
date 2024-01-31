bidi = [
    [10, 7, 8],
    [9, 9, 10],
    [10, 8, 7]
]

print(bidi[0][1])

bidi[0][1] = 10

print(bidi)
x=0
y=0
for fila in bidi:
    x+=sum(fila)
    y+=len(fila)

print(f'La suma es {x}')
print(f'El promedio es {x/y}')
