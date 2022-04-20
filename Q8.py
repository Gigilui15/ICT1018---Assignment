def newtonRaphson(n, iter):

    a = float(n) # number to get square root of
    for i in range(iter):
        n =(n + a / n)/2 
    return n

#number of iterataions (effects the accuracy of the final answer)
iter = 1

"""
Testing Task 8
"""
print("With " ,iter ," iterations: \n")
print ("Approximate Square Root for 9: " ,newtonRaphson(9,iter) ,"\n")
print ("Approximate Square Root for 2: " ,newtonRaphson(2,iter) ,"\n")
print ("Approximate Square Root for 12: " ,newtonRaphson(12,iter) ,"\n")
print ("Approximate Square Root for 37: " ,newtonRaphson(37,iter) ,"\n")
print ("Approximate Square Root for 53: " ,newtonRaphson(53,iter) ,"\n")
print ("Approximate Square Root for 9: " ,newtonRaphson(25,iter) ,"\n")