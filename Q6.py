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

def SieveOfEratosthenes(n):
	prime = [True for i in range(n+1)]
	p = 2
	while (p * p <= n):
		# If prime[p] is not changed, then it is a prime
		if (prime[p] == True):

			# Update all multiples of p
			for i in range(p * p, n+1, p):
				prime[i] = False
		p += 1

	# Print all prime numbers
	for p in range(2, n+1):
		if prime[p]:
			print(p)
   
# Driver code
	n = 20
	print("Following are the prime numbers smaller than or equal to", n)
	SieveOfEratosthenes(n)


num = rd.randint(1,1000)
Prime_Checker(803) 
#803 marked as bad                        