#Lista enlazada
#Clase para nodos
class Node:  
    def __init__(self,data):
        self.data = data
        self.next = None

#Declaracion del TDA
class ListaEnlazada:
    def __init__(self):
        self.start = None
        self.innerList = []
    
    #Inserta un elemento en el indice deseado, si no se pasa argumento se inserta al inicio.
    def insertNode(self,value:int,pos=0):
        newNode = Node(value)
        #Inserta un nuevo elemento al inicio y lo enlaza al segundo elemento
        if(pos==0):
            if(self.start!=None):
                newNode.next = self.start
            self.start = newNode
            self.innerList.insert(pos,newNode)

        #Verifica que el indice para insertar sea valido, inserta el elemento y corrige relaciones entre elementos
        elif(pos-1>=0 and pos+1<=len(self.innerList)):
            if(pos+1<=len(self.innerList)):
                newNode.next=self.innerList[pos]
            self.innerList[pos-1].next=newNode
            self.innerList.insert(1,newNode)
        else:
            #Mensaje de error, el indice para insertar es mayor al tamaño de la lista
            print("List index out of range")
    #Imprime todos lo elementos dentro de la lista en orden
    def PrintList(self):
        currentNode = self.start
        while True:
            print(currentNode.data)
            if(currentNode.next != None): currentNode = currentNode.next
            else: break

    #Regresa la suma total de los elementos en la lista
    def PrintSum(self, count=0):
        return 0 if count + 1 > len(self.innerList) else self.innerList[count].data + self.PrintSum(count+1)
    

li1 = ListaEnlazada()

li1.insertNode(20)

li1.insertNode(10)

li1.insertNode(15,1)

li1.PrintList()

print(li1.PrintSum())


