stack = [] 

def Filler(data):
    operator  = data.split()

    for op in operator:

        print (stack)
        
        if op in {"+", "-", "*", "/"}:

            num2 = stack.pop()
            num1 = stack.pop()

            if op == "+":
                ans = num1 + num2
            if op == "-":
                ans = num1 - num2
            if op == "*":
                ans = num1 * num2
            if op == "/":
                ans = num1 / num2

            stack.append(ans)

        else:
            stack.append(int(op))

    
    return stack.pop()


#Test Data:
print(Filler("10 5 +"))
print(Filler("22 11 / 33 *"))
#print(Filler("100 2 + 30 b"))
#print(Filler("3 * / 22 11 33"))