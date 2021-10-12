d = 1
while d < 2:
    a = int(input("Please enter the number"))
    b = int(input("please enter 2nd number"))
    c = input("please enter the operator")
    if c == "+":
        print(f"{a} {c} {b} = {a + b}")
    elif c == "-":
        print(f"{a} {c} {b} = {a - b}")
    elif c == "*":
        print(f"{a} {c} {b} = {a * b}")
    elif c == "/":
        print(f"{a} {c} {b} = {a / b}")
    else: print("!Warning invalid number") 
