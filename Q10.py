#nums = [1,2,55,3,13,5,6,30,8,14]
#nums = [5,5,5,5,5,5]
nums = [0,-2,-3,-1,-55,-9]

print(nums ,":\n")

def find_largest(list):
    #largest element is the only element
    if len(list) == 1:
        return list[0]
    
    else:
        current_largest = find_largest(list[1:])
        if current_largest > list[0]:
            return current_largest 
         
        else:
            return list[0]

print("Largest Number in List: " ,find_largest(nums))
