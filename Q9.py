array = [1,2,3,4,5,6,7,8,9,10,11,1,2,3,4,6,7,8,9,11]
not_repeated = set()

for x in array:
    print(x)
    current_length = len(not_repeated)
    not_repeated.add(x)
    if((current_length + 1) == len(not_repeated)):
        array.remove(x)
     
if(len(not_repeated) == len(array)):
    print("There are no repeated elements in this Array")
else:
    print("The repeated values in the Array are:\n" ,array)  
    
#repeated should be [1,2,3,4,6,7,8,9,11]    