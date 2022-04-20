'''
#Create a non balanced BST with inputs one at a time
#Needs Class, Object Node with left and right, methods for adding node to tree and possible visualisation using JSON

DIFFICULTY TO DISPLAY BST
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
      
def bfs(node,level=0,res=[]):
  if level<len(res):
    if node:
      res[level].append(node.num)
    else:
      res[level].append(" ")
  else:
    if node:
      res.append([node.num])
    else:
      res.append([" "])
  if not node:
    return 
  bfs(node.leftNode,level+1,res)
  bfs(node.rightNode,level+1,res)
  return res
    
def printBST(node):
  treeArray = bfs(node)
  h = len(treeArray)
  whiteSpaces = (2**h)-1
  
  def printSpaces(n):
    for i in range(n):
      print(" ",end="")

      
  for level in treeArray:
    whiteSpaces = whiteSpaces//2
    for i,x in enumerate(level):
      if i==0:
        printSpaces(whiteSpaces)
      print(x,end="")
      printSpaces(1+2*whiteSpaces)
    print()
#driver Code
printBST(root)

'''        
For Testing Purposes Part 1  
print("Root: " ,root.num)
print("Left " ,root.leftNode.num)
print("Right" ,root.rightNode.num)     
'''

'''
Part2
def display_node(node):
    if (node.leftNode and node.rightNode):
        #for every level of depth -5
        print("{:>40}".format(node.leftNode.num),"{:>20}".format(node.rightNode.num))
        display_node(node.leftNode)
        display_node(node.rightNode)
        
    elif(node.leftNode):
        print("{:>40}".format(node.leftNode.num))
        display_node(node.leftNode)
        
    elif(node.rightNode):
        print("{:>60}".format(node.rightNode.num))
        display_node(node.rightNode)


print ("{:>48}".format(root.num))  
display_node(root)
'''