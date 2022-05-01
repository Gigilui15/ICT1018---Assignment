stack = [] 

def Filler(data):
    operator  = data.split()

    for op in operator:

        print (stack)
        
        if op in {"+", "-", "*", "/"}:

            numB = stack.pop()
            numA = stack.pop()

            if op == "+":
                sum = numA + numB
            if op == "-":
                sum = numA - numB
            if op == "*":
                sum = numA * numB
            if op == "/":
                sum = numA / numB

            stack.append(sum)

        else:
            stack.append(int(op))

    
    return stack.pop()


#Test Data:
#print(Filler("10 5 +"))
#print(Filler("44 22 / 50 *"))
#print(Filler("100 2 + 30 b"))
print(Filler("* / 44 22 50"))