import random as rd

def Prime_Checker(num):
    denom = [2,3]

    #Only Divisible by 1 and itself 
    for i in denom:
        if ((num % i) == 0):
            #not a prime number
            prime = False 
            break  
        else: 
            prime = True
            break    

    if (prime == True):
        print(str(num) +" is Prime")
    else:
        print(str(num) +" is NOT Prime")     

num = rd.randint(1,1000)
Prime_Checker(803)                         