import random as rd
from turtle import position

#Two Arrays of Unequal size (256 and 300) containing randomly generated numbers between 0 and 1024
A = [rd.randrange(0,1025)for i in range(256)]
B = [rd.randrange(0,1025)for i in range(300)]
C = []

#Shell Sort Algorithm Method
def shell_Sort(array):
    length = len(array)
    gap = length//2
    
    while gap > 0:
        for i in range(gap, length):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap

            array[j] = temp
        gap //= 2

#Quick Sort Algorithm Method
def split(array, low, high):
    idx_small = (low-1)
    pivot = array[high]
 
    for i in range(low, high):
        # Current element = array[j]
        if array[i] <= pivot:
 
            # Increment index of smaller element
            idx_small = idx_small+1
            array[idx_small], array[i] = array[i], array[idx_small]
 
    array[idx_small+1], array[high] = array[high], array[idx_small+1]
    return (idx_small+1)

def quick_Sort(array, low, high):
    if len(array) == 1:
        return array
    if low < high:
 
        # Index for Split
        spin = split(array, low, high)
 
        # Sorting elements before and after splitting them up
        quick_Sort(array, low, spin-1)
        quick_Sort(array, spin+1, high)
    
#Printing Array A before and After using Shell Sort
print("\nArray A Before Shell Sort: \n " ,A) 
shell_Sort(A)
print("\nArray A After Shell Sort: \n " ,A)


#Printing Array B before and After using Quick Sort
print("\nArray B Before Quick Sort: \n " ,B) 
h = len(B) - 1
quick_Sort(B, 0 ,h)
print("\nArray B After Quick Sort: \n " ,B) 
 

def merge_Arrays(A, B, C):
    #Setting the length of Array C
    length = len(A) + len(B)
    
    pointer_A = 0
    pointer_B = 0
    d = 0
    
    while (length - 2 > d):
        d = pointer_A + pointer_B
        if (pointer_A == len(A)-1):
            C.append(B[pointer_B])    
            pointer_B += 1 
             
        elif (pointer_B == len(B)-1):
            C.append(A[pointer_A])    
            pointer_A += 1  
                
        elif (A[pointer_A] <= B[pointer_B]):
            C.append(A[pointer_A])
            pointer_A += 1
            
        else:
            C.append(B[pointer_B])    
            pointer_B += 1       
                      
                      
merge_Arrays(A, B, C)
print("\nArray C: \n" ,C)