fibonacci = [0,1] 
sum = 0  

print("Enter the value for n: ")
n = int(input())
error = "!! n cannot be equal to or less than 0 !!"
    

def Fibonacchi_Sequence(fibonacci,n,sum):
    for i in range(2,n):
        next = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next)
    print("The Fibonacci Sequence up to the first",n ,"elements is : \n" ,fibonacci ,"\n")
    
    for i in range(0,n):
        sum += fibonacci[i]

    print("The Fibonacci Sequence SUM of the first",n ,"elements is:",sum,"\n") 
     
if(n <= 0):
    print(error)
elif(n == 1):
    fibonacci.remove(1)
    Fibonacchi_Sequence(fibonacci,n,sum)
else:
    Fibonacchi_Sequence(fibonacci,n,sum)    