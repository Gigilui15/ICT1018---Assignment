import math

def cosine(x, n):
    cos = 0
    for n in range(n):
        cos += ((-1)**n) * (x ** (2*n)) / (math.factorial(2 * n))
        # num ** x means num^x
    return cos

def sine(x,n):
    sin = 0
    
    for n in range(n):
        sin += ((-1)**n) / math.factorial(2*n+1)*(x**(2*n+1)) 
    return sin

print("Enter the order (n) for the expansion: ")
n = int(input())
#n = 1

print("Enter the value of x:")
x = float(input())
print("Cos(",x ,") to order",n ,"=",cosine(x,n),"\n")
print("Sin(",x ,") to order",n ,"=",sine(x,n))