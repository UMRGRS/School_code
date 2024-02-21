numeros = list(range(1,10))

primero = numeros[0]
segundo = numeros[1]

#Obtener un elemento de la lista
primero, *otros = numeros

print(primero, otros)