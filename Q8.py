def newtonRaphson(n, iter):

    a = float(n) # number to get square root of
    for i in range(iter):
        n =(n + a / n)/2 
    return n

#number of iterataions (effects the accuracy of the final answer)
iter = 400

"""
Testing Task 8
"""

print (newtonRaphson(9,iter))
print (newtonRaphson(2,iter))
print (newtonRaphson(12,iter))
print (newtonRaphson(37,iter))
print (newtonRaphson(53,iter))
print (newtonRaphson(25,iter))