import random

numeros = []
i = 20

while i>0:
    numeros.append(random.randrange(1,10))    
    i-=1
    
for x, num in enumerate(numeros):
    if num == 5:
        numeros[x] = "No me gusta el 5 xd"
        
print(numeros)