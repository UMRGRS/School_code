arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def Suma(arr):
    x=0
    for i in arr:
        x += i
    return x

print(f"La suma es {Suma(arr)}")

def Promedio(arr):
    return sum(arr)/len(arr)

print(f"El promedio es {Promedio(arr)}")

def Max_value(arr):
    arr.sort(reverse=True)
    return arr[0]

print(f"El numero mayor es {Max_value(arr)}")