import random

numeros = []
i = 20

while i>0:
    numeros.append(random.randrange(1,100))    
    i-=1
#Ordenamos el arreglo    
numeros.sort()

print(numeros)

def binary(arr, num):
    i = int(-(-len(arr)//2))-1
    if(i<=0):
        print(f'No se encontró el numero') 
    else:
        if(arr[i]==num):
            print(f'Numero encontrado en el indice {i}')
        elif arr[i]<num:
            #return 0
            return binary(arr[i:], num)
        else:
            #return 0
            return binary(arr[:i], num)
        
binary(numeros, 56)