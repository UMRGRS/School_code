#Arbol binario
class TreeNode:
    def __init__(self,value):
        self.value = value
        self.rightNode = None
        self.leftNode = None
        
class Tree:
    def __init__(self, rootValue):
        self.root = TreeNode(rootValue)
        self.NodeList = [self.root]
        
        
    def createNode(self, nodeValue, parent:TreeNode):
        newNode = TreeNode(nodeValue)
        self.NodeList.append(newNode)
        if(parent.rightNode == None or parent.leftNode == None):
            if(parent.rightNode == None):
                parent.rightNode=newNode
                return
            elif(parent.rightNode.value < newNode.value):
                parent.leftNode = parent.rightNode
                parent.rightNode = newNode
                return
            else:
                parent.leftNode = newNode
                return
        print("Parent node doesn't have available space")