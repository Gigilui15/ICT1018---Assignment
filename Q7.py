'''
#Create a non balanced BST with inputs one at a time
#Needs Class, Object Node with left and right, methods for adding node to tree and possible visualisation using JSON
'''
class Node:
    def __init__(self, num):
        self.leftNode = None
        self.rightNode = None
        self.num = num
    
def addNode(root, node):
    if (root == None):
        node = root
    else:
        if (node.num < root.num):
            #place on left if not null
            if(root.leftNode == None):
                root.leftNode = node
            #Recursion to Add on Left of Left Nodes below Root
            else:
                addNode(root.leftNode, node)      
        #else if(node.num > root.num)         
        else:
            if(root.rightNode == None):
                root.rightNode = node
            #Recursion to Add on Left of Left Nodes below Root
            else:
                addNode(root.rightNode, node)      

stop_input = False 
print("Enter Root Node: ")
root = Node(int(input())) 
 
#While loop to Ask User to input Node value
while stop_input == False:
    value = input("Enter A New Node Into The BST Or Press Enter To Exit: ")
    
    #Ignore Case for Exit value
    if not value:
        print("Exiting Input Procedure...")
        stop_input = True
    else: 
        num = int(value)
        addNode(root, Node(num))  
        
'''        
For Testing Purposes  
print("Root: " ,root.num)
print("Left " ,root.leftNode.num)
print("Right" ,root.rightNode.num)     
'''   