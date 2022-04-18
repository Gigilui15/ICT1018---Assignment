def newtonRaphson(n, iter):

    a = float(n) # number to get square root of
    for i in range(iter):
        n =(n + a / n)/2 
    return n

#number of iterataions
iter = 10

"""
Testing Task 8
"""

print (newtonRaphson(9,iter))
print (newtonRaphson(2,iter))