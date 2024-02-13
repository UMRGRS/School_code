lista = [54,26,93,17,77,31,44,55,20]
def bubble(lista):
    for x in range(len(lista)-1,0,-1):
        for i in range(x):
            if lista[i]>lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                
bubble(lista)

print(lista) 