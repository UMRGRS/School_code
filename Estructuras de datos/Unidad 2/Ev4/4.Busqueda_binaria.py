import random

numeros = []

for i in range(20):
    numeros.append(random.randrange(1,100))    
#Ordenamos el arreglo    
numeros.sort()

def binary(arr, num):
    iz = 0
    dr = len(arr)-1
    while iz <=dr:
        md = round((iz+dr)/2)
        if(arr[md]==num):
            return (f"Numero encontrado en el indice {md}")
        elif(arr[md]>num):
            dr=md-1
        else:
            iz = md+1
    return ("Numero no encontrado")
            
print(numeros)
print(binary(numeros, 67))