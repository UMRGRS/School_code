#import random

numeros = [5,3,7,6,8,4,9,6]

#for i in range(20):
#    numeros.append(random.randrange(1,100))


def quick(arr, low, top):
    if low < top:
        pi = cut(arr,low, top)
        
        quick(arr, low, pi-1)
        quick(arr, pi+1, top)    

def cut(arr,low,top):
    piv = arr[top]
    i = low - 1
    for j in range(low, top):
        if(arr[j]<=piv):
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[top] = arr[top], arr[i+1]
    
    return i + 1 

quick(numeros,0,len(numeros)-1)

print(numeros)
