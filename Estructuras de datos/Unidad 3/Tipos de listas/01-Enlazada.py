class Node():
    def __init__(self, numero):
        self.numero = numero
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = None
        self.length = 0
    
    def InsertStart(self, numero):
        newNode = Node(numero)
        if(self.head == None):
            self.head = newNode
            return
        
        newNode.next = self.head
        self.head = newNode
        self.SetLength(1)
        
    def InsertEnd(self, numero):
        newNode = Node(numero)
        if self.head == None:
            self.head = newNode
            return
        current = self.head
        while current.next:
            current = current.next
        
        current.next = newNode
        self.SetLength(1)
        
    def PrintList(self):
        current = self.head
        while current:
            print(current.numero, "->", end="") 
            current = current.next

    def DeleteStart(self):
        if self.head is None:
            print("No hay elementos para borrar")
            return
        self.head = self.head.next
        self.SetLength(-1)
    
    def DeleteEnd(self):
        current = self.head
        if current is None:
            print("No hay elementos para borrar")
            return
        elif current.next is None:
            self.head = None
            self.SetLength(-1)
        else:
            while current.next.next:
                current = current.next
            
            current.next=None
            self.SetLength(-1)
            
    def SearchNumber(self, number):
        current = self.head
        if(current is None):
            print("No hay elementos en la lista")
        while current:
            if(current.numero == number):
                return True
            current = current.next
        return False
    
    def GetIndex(self, i):
        if(i>self.length):
            print("Indice fuera de los limites")
            return
        current = self.head
        index = 0
        while current.next and index<i:
            current = current.next
            index+=1
        
        return current.numero
    
    def SetLength(self, n):
        self.length += n
        
        
myList = LinkedList()
myList.InsertStart(5)   
myList.InsertStart(7)
myList.InsertStart(8)
print(myList.SearchNumber(6))
myList.GetIndex(3)
#myList.DeleteEnd()
#myList.DeleteStart()
myList.PrintList()