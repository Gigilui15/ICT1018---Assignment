array = [1,2,3,13,5,6,51,7,30,8,12,9,10,11,1,2,3,4,6,13,7,8,9,11,50,51]
#repeated should be 1, 2, 3, 6, 7, 8, 9, 11, 13, 51 
'''
array = [1,2,3,4,5,6,7,8,9,10,11,24,67,41,72]
should have no repeated elements
'''
print("Array: \n" ,array)
repeated = set()
not_repeated = set()

for x in array:
    current_length = len(not_repeated)
    not_repeated.add(x)
    #After Adding Each element to set, I am checking if length grew to detect if set accepted element or if it is repeated
    if(len(not_repeated) != current_length + 1):
        repeated.add(x)
     
#Checking if length of non repeated elements is the same as original array      
if(len(not_repeated) == len(array)):
    print("\nThere are no repeated elements in this Array")
else:
    print("\nThe repeated values in the Array are:\n" ,list(repeated))  
      