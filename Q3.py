#Extreme Points = Element is bigger/smaller than both previous and following elements
A = [0, 5, 3, 6, 8, 7, 15, 9]

#Array to Store all Random Points
extreme_Points = []
size = len(A) 

#Printing the Array
print("Array: \n" ,A)

for i in range (0,size):
    if (0 < i < size-1) and ((A[i-1] < A[i] > A[i+1]) or (A[i-1] > A[i] < A[i+1])):
        extreme_Points.append(A[i])
    
if(extreme_Points == []):
    print("Sorted")
else:
    print("\nExtreme Elements:\n")
    #Printing the Extreme Elements in the Array
    print(extreme_Points)    