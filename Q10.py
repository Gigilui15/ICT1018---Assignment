nums = [1,2,55,3,13,5,6,30,8,14]

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

#Reference:
#https://stackoverflow.com/questions/12711397/python-recursive-function-to-find-the-largest-number-in-the-list