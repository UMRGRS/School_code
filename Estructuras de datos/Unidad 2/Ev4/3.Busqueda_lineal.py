lista = [54,26,93,17,77,31,44,55,20]

def Lineal(lista, num):
    for i in range(len(lista)-1):
        if lista[i] == num:
            return(f"Numero encontrado en el indice {i}")
    return("No se encontró el numero")
    
print(Lineal(lista,77))