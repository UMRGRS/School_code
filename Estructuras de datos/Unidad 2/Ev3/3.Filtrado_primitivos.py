import random

numeros = []
i = 20

while i>0:
    numeros.append(random.randrange(1,100))    
    i-=1

def Filter_greater(arr, value):
    for num in arr:
        if num > value:
            print(num)
            
Filter_greater(numeros, 90)