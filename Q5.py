stack = [] 

def Filler(data):
    operator  = data.split()

    for op in operator:

        print (stack)
        
        if op in {"+", "-", "x", "/"}:

            num2 = stack.pop()
            num1 = stack.pop()

            if op == "+":
                ans = num1 + num2
            if op == "-":
                ans = num1 - num2
            if op == "x":
                ans = num1 * num2
            if op == "/":
                ans = num1 / num2

            stack.append(ans)

        else:
            stack.append(int(op))

    
    return stack.pop()


#Test Data:
print(Filler("1 2 +"))
print(Filler("22 11 / 33 x"))
print(Filler("3 4 + 4"))
print(Filler("100 2 + 30 z"))