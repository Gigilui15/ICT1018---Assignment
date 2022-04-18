import random as rd

#Creating a Random Array of 30 Numbers
Temp_Set = set()
nums = [rd.randrange(1,124)for i in range(30)]
#nums = [2,5,62,46,1,42,75,24,8,35,13,11,23,9]
#nums = [2,5]
print("\nArray : \n" ,nums ,"\n") 

for a in nums:
    Temp_Set.add(a)
Array = list(Temp_Set)    
    
size = len(Array)
products = []
pairs = []

for a in range(size):
    #Populating the Array with [(Number A)(Number B)(Their Product)]
    for b in range(a + 1, size):
        product = Array[a]*Array[b]
        products.append([Array[a],Array[b],product])

length = len(products)

#Checking Each Element's Product in the Array and adding Number A and B to Array: Pairs if Equal
for x in range(0,length -1): 
    #store holds product of each element [(0:element A)(1:element B)(2:product)]      
    store = products[x][2]
    for y in range((x+1), length):
        comp = products[y][2]
        #print("A = " +str(products[x]) +" B: " +str(products[y]))
        if(store == comp):
            #print(str(store) +" is Equal to " +str(comp))
            pairA = [products[x][0]],[products[x][1]]
            pairB = [products[y][0]],[products[y][1]]
            pairs.append([[pairA],[pairB]])

#Printing All The 2-Pairs
if pairs:
    for z in range(0,(len(pairs))):
        print(str(pairs[z][0][0][0][0]) +" & " +str(pairs[z][0][0][1][0]) +" and " +str(pairs[z][1][0][0][0]) +" & " +str(pairs[z][1][0][1][0]) +" are a Two-Pair\n") 
else: print("There are no Two-Pairs in this Array")                      