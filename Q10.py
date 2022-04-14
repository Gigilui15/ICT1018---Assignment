nums = [1,2,3,13,5,6,30,8,14]

def find_largest(list):
    #largest element is the only element
    if len(list) == 1:
        return list[0]
    else:
        print(list[1:])
        m = find_largest(list[1:])
        print(m)
        if m > list[0]:
            return m  
        else:
            return list[0]

print("Largest Number in List: " ,find_largest(nums))