
#this one works if you give it the two first numbers
def generar_fibonacci(a,x,y):
        return 0 if a == 0 else (print(x+y) or generar_fibonacci(a-1,y,x+y))
    
    
    
    
def potenciaRecursiva(x, y):
    if y == 0:
        return 1

    elif y >= 1:
        return x * potenciaRecursiva(x, y - 1)




print(5%10)